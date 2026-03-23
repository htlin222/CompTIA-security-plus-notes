---
title: "Case: The Health Check Cascade — Load Balancer Misconfiguration During Surge Traffic"
description: "A reverse proxy misconfigures health checks to return 200 OK even when application servers are overloaded and rejecting new connections. During a product launch with 10x expected traffic, all requests route to unavailable servers, causing cascading failures and platform downtime."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

StreamSense is a social media analytics platform with 2.4 million users. In March 2024, they prepared for a major product launch: a new AI-powered sentiment analysis feature that required running a heavy machine learning pipeline on every user post. The marketing team predicted the launch would drive 10x normal traffic volume (from 40,000 requests/second to 400,000 requests/second).

The platform's infrastructure is built on a load-balanced architecture:

1. **HAProxy reverse proxy** (2 instances in active-active mode) accept all incoming HTTP requests
2. **Apache application servers** (24 instances) process requests and call the sentiment analysis API
3. **AWS Elastic Load Balancer** maintains a pool of healthy application servers and distributes traffic

The platform engineering team, led by VP of Engineering David Wu, designed a surge capacity plan:

- Pre-stage additional Apache instances to handle 10x traffic
- Configure aggressive horizontal scaling so new instances are added within 60 seconds of load increase
- Ensure [[health-checks]] are accurate so the load balancer routes traffic only to healthy servers

The day of the launch, everything was ready. Marketing sent out the announcement at 2 PM. Traffic began climbing at 2:05 PM. By 2:12 PM, traffic had reached 400,000 requests/second—10x the baseline. The horizontal scaling kicked in, and new application servers began spinning up.

But something was wrong.

The monitoring dashboard showed 24 application servers, but the actual request throughput was only 80,000 requests/second—a 5x increase instead of the expected 10x. Latency was climbing: 200ms, 500ms, 1000ms, 1500ms. Customer dashboards showed "loading..." indefinitely.

The engineers checked application server metrics. Each server was processing 3,300 requests/second—at full capacity. They were reporting CPU utilization of 95%, database query wait times of 2+ seconds, and memory pressure was causing garbage collection pauses. The servers were struggling, but according to HAProxy's [[health-checks]], they were all healthy.

David dove into the HAProxy configuration. The [[health-checks]] were configured like this:

```
backend app_servers
  http-check expect status 200
  server app01 10.0.1.1:8080 check inter 5000
  server app02 10.0.1.2:8080 check inter 5000
  server app03 10.0.1.3:8080 check inter 5000
  # ... 21 more servers
```

The health check was simple: every 5 seconds, send an HTTP GET request to the application server. If the server responds with HTTP 200, consider it healthy. If it doesn't respond or returns an error, mark it unhealthy.

The problem was that the application server's health check endpoint was trivial. It didn't actually verify that the server could process requests—it just checked if the application process was running. A server that was completely overloaded, unable to accept new connections, and with 300 pending requests in the queue would still return HTTP 200 to a [[health-checks|health check request]] because the health check endpoint was a lightweight no-op.

So HAProxy kept routing new requests to servers that were already overloaded. Each request would queue behind 300 other requests, waiting 10+ seconds for processing.

At 2:18 PM, the first cascade failure occurred. An application server stopped responding to [[health-checks]] entirely because the server process was completely blocked by garbage collection. HAProxy correctly marked it as unhealthy and stopped routing traffic to it. But now the remaining 23 servers had to absorb that traffic. The overload intensified, and another server started GC thrashing.

By 2:25 PM, 8 application servers were marked as unhealthy due to unresponsiveness. The remaining 16 servers were completely saturated. New application servers were being launched automatically, but they would never become healthy—by the time they finished boot and registered with HAProxy, they were immediately overwhelmed.

The customer experience was a disaster. Requests that should have taken 200ms were taking 30+ seconds. Many requests timed out entirely. Some customers saw "503 Service Unavailable" errors. The team received support tickets at a rate of 100 per minute.

David made an emergency decision: reduce the [[health-checks|health check interval]] from 5 seconds to 1 second, making the system more responsive to overload. But that didn't help—the overloaded servers were still reporting as healthy.

The real fix was to improve the [[health-checks|health check]] endpoint. David quickly deployed a new version of the application server with an enhanced health check:

```java
@GetMapping("/health")
public ResponseEntity<HealthStatus> health() {
  HealthStatus status = new HealthStatus();
  status.healthy = applicationQueue.size() < MAX_QUEUE_SIZE &&
                   connectionPoolAvailable > MIN_CONNECTIONS &&
                   gcPauseTimeMs < MAX_GC_PAUSE;

  if (!status.healthy) {
    return ResponseEntity.status(503).body(status);
  }
  return ResponseEntity.ok(status);
}
```

The new endpoint would return HTTP 503 (Service Unavailable) if the application server was overloaded, the connection pool was exhausted, or GC pauses were exceeding thresholds.

The deployment took 8 minutes. Within 30 seconds of the new health check being active on the first few servers, those servers were marked as unhealthy. HAProxy immediately stopped routing traffic to them. New application servers that came online were now correctly categorized: healthy servers received traffic, overloaded servers didn't.

New instance launches continued, but now they were effective. By 2:40 PM (25 minutes into the incident), traffic was stabilizing. Latency dropped from 30+ seconds back to 500ms. By 2:50 PM, the surge had been absorbed by 67 application servers, latency was back to 200-300ms, and the product launch was proceeding (albeit with a rough start).

The [[active-active-vs-active-passive|active-active]] HAProxy pair had performed well—neither instance bottlenecked. The [[resilience-and-redundancy|scaling mechanisms]] had worked. The problem was entirely the [[health-checks]] logic.

### Post-Incident Review

In the aftermath, the team realized several design failures:

**1. Health-checks Weren't Representative of Real Work**:
- The original [[health-checks]] endpoint didn't exercise the application's actual code paths
- It didn't check resource availability (connection pools, thread pools, queue depth)
- It didn't measure response time or queue wait time

**2. No [[caching]] for Health Check Responses**:
- If a server was under heavy load, HAProxy was sending health check requests every 1-5 seconds, adding to the load
- With 67 servers and 4 HAProxy instances checking every second, that's 268 requests/second dedicated to health checks (0.7% of total traffic)

**3. No [[scheduling-algorithms|advanced scheduling]]** beyond round-robin:
- HAProxy was using simple round-robin distribution without considering server load
- A [[scheduling-algorithms|weighted least-connections]] algorithm would have better distributed traffic to less-loaded servers

**4. No Circuit Breaker Pattern**:
- When a server became unhealthy, all remaining servers had to absorb its traffic immediately
- A [[resilience-and-redundancy|circuit breaker]] would have gradually reduced traffic to overloaded servers before marking them unavailable

## What Went Right

- **Monitoring was comprehensive enough to detect the issue**: Response time metrics clearly showed degradation within 5 minutes.
- **The [[active-active-vs-active-passive|active-active]] load balancer pair provided failover**: If one HAProxy instance failed, the other continued serving traffic.
- **Automatic horizontal scaling was functional**: New instances launched and became available (though not optimally due to health check issues).
- **The fix was deployable in under 10 minutes**: The enhanced health check was developed, tested, and deployed without requiring a HAProxy restart.
- **Root cause was identified clearly**: The team quickly isolated the problem to health check logic, not infrastructure failures.

## What Could Go Wrong

- **If no monitoring existed**: The team would have been blind to the overload. They would have continued launching instances ineffectively.
- **If the health check fix had taken longer to develop**: Each additional minute of degradation would have driven more customers away from the product launch.
- **If HAProxy itself had failed**: With both instances in active-active mode, a single failure would still result in 50% load balancing. If both had failed, the entire platform would have been unreachable.
- **If [[resilience-and-redundancy|failback]] was broken**: After the surge subsided, if the extra instances didn't scale down properly, operational costs would have remained inflated.

## Key Takeaways

- **Health-checks must verify real application health, not just process availability**: A good health check measures queue depth, connection pool availability, recent error rates, and GC pressure—not just "is the process running?"
- **Health check latency adds to overall system load**: If you have 100 servers and check each one every second, that's 100 requests/second dedicated to health checks. Consider [[caching]] or reducing check frequency under load.
- **Weighted load distribution is better than round-robin**: When servers have different capacities or are under different load, round-robin causes imbalance. Use [[scheduling-algorithms|least-connections]] or adaptive weighting.
- **Graceful degradation requires circuit breaker patterns**: When a server becomes overloaded, gradually reducing traffic to it (circuit breaker) is better than dropping it cold and causing a cascade on remaining servers.
- **Active-active is better than passive failover**: With active-active load balancers, no single point of failure can take down the entire system. Both instances actively serve traffic.
- **Surge testing should use realistic traffic patterns**: A 10x surge is unusual. Test with expected load patterns, then with 2x, 5x, and 10x to understand where the system breaks and to validate health checks and scaling behavior.

## Related Cases

- [[case-resilience-and-redundancy]] — The broader architecture patterns that make systems resilient to surge traffic
- [[case-network-security-architecture]] — Load balancer placement and network design that supports high availability
- [[case-denial-of-service]] — How attackers use similar surge patterns to cause DoS

