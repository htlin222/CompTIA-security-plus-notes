---
title: "Load Balancers and Proxies"
description: "Load balancers distribute traffic across servers for availability, while proxies act as intermediaries for security and performance."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/medium
aliases:
  - "Load Balancers"
  - "Proxies"
---

> [!eli5] ELI5: What are Load Balancers and Proxies?
> Picture a really popular ice cream shop with five windows. A load balancer is like a helper out front who sends each customer to the window with the shortest line, so nobody waits too long. A proxy is more like a middle-man -- you tell the proxy what ice cream you want, and the proxy goes and gets it for you, so the shop never knows who you are. Both help things run smoothly and safely.

## Overview

Load balancers distribute incoming network traffic across multiple servers to ensure availability, performance, and reliability. Proxies act as intermediaries between clients and servers, providing security, caching, and anonymity. Both are important components of a secure network architecture that supports high availability and controlled access.

## Key Concepts

- **Load balancer types:**
  - **Layer 4 (transport)** — distributes based on IP and port; fast, no content inspection
  - **Layer 7 (application)** — inspects content and routes based on URLs, headers, cookies; supports SSL offloading
- **[[scheduling-algorithms|Scheduling algorithms]]** — round-robin, least connections, weighted, IP hash, health-based
- **[[active-active-vs-active-passive|Active-active vs. active-passive]]** — active-active uses all nodes; active-passive has standby nodes for failover
- **[[ssltls-offloading|SSL/TLS offloading]]** — load balancer handles encryption/decryption, reducing server workload
- **[[health-checks|Health checks]]** — load balancers monitor backend server health and remove unhealthy nodes from rotation
- **Proxy types:**
  - **Forward proxy** — sits in front of clients; controls outbound access, caches content, hides client IPs
  - **Reverse proxy** — sits in front of servers; protects backend servers, handles SSL, provides load balancing
  - **Transparent proxy** — intercepts traffic without client configuration
  - **Open proxy** — accessible to any user; security risk if unintended
- **[[content-filtering|Content filtering]]** — proxies can inspect and block traffic based on URLs, categories, or content types
- **[[caching|Caching]]** — proxies store frequently accessed content to reduce bandwidth and improve response times

## Exam Tips

> [!tip] Remember
> Forward proxy = protects clients (outbound). Reverse proxy = protects servers (inbound). Load balancers improve availability and are part of high-availability design. SSL offloading reduces backend server load.

## Connections

- Supports [[resilience-and-redundancy]] by distributing traffic and providing failover capabilities
- Works within [[network-security-architecture]] as a layer of defense and performance optimization
- See also [[cloud-security]] where load balancing is a core managed service

## Practice Questions

> [!qbank]- Q-Bank: Load Balancers and Proxies (4 Questions)
>
> **Q1.** A company wants to reduce the TLS encryption workload on its web servers while maintaining HTTPS for all client connections. Which solution BEST addresses this need?
>
> A. Deploying a forward proxy with content filtering
> B. Configuring SSL/TLS offloading on a Layer 7 load balancer
> C. Adding a Layer 4 load balancer with round-robin scheduling
> D. Installing additional CPU resources on each web server
>
> > [!answer]- Show Answer
> > **B. Configuring SSL/TLS offloading on a Layer 7 load balancer**
> >
> > [[ssltls-offloading|SSL/TLS offloading]] on a Layer 7 load balancer handles the encryption and decryption on the load balancer itself, freeing backend servers from this processing overhead. A forward proxy (A) controls outbound client traffic, not inbound server TLS. A Layer 4 load balancer (C) routes based on IP/port and does not inspect or offload TLS. Adding CPU (D) addresses the symptom but not the root cause efficiently.
>
> **Q2.** An organization wants to control and monitor employee web browsing by routing all outbound HTTP/HTTPS traffic through an intermediary. Which solution is MOST appropriate?
>
> A. Reverse proxy
> B. Forward proxy
> C. Layer 4 load balancer
> D. VPN concentrator
>
> > [!answer]- Show Answer
> > **B. Forward proxy**
> >
> > A [[load-balancers-and-proxies|forward proxy]] sits in front of clients and controls outbound access, enabling [[content-filtering|content filtering]], caching, and monitoring of employee web traffic. A reverse proxy (A) protects backend servers from inbound traffic, not outbound browsing. A Layer 4 load balancer (C) distributes traffic but does not filter content. A VPN concentrator (D) terminates VPN tunnels for remote access, not outbound web monitoring.
>
> **Q3.** A web application receives traffic from a load balancer, and the security team notices that all source IP addresses in the application logs show the load balancer's IP instead of the actual client IPs. Which load balancer type is MOST likely causing this?
>
> A. Layer 4 load balancer in DSR (Direct Server Return) mode
> B. Layer 7 load balancer acting as a reverse proxy
> C. DNS-based load balancer
> D. Layer 4 load balancer in transparent mode
>
> > [!answer]- Show Answer
> > **B. Layer 7 load balancer acting as a reverse proxy**
> >
> > A [[load-balancers-and-proxies|Layer 7 load balancer]] acting as a reverse proxy terminates the client connection and opens a new connection to the backend, replacing the source IP with its own. DSR mode (A) preserves the client IP since return traffic bypasses the load balancer. DNS-based load balancing (C) resolves to different server IPs and does not proxy connections. Transparent mode (D) passes traffic without IP modification.
>
> **Q4.** A load balancer is configured with health checks that periodically verify backend server availability. One server fails a health check. What action does the load balancer MOST likely take?
>
> A. Shut down all backend servers to prevent data corruption
> B. Remove the unhealthy server from the rotation and direct traffic to healthy servers
> C. Continue sending traffic to the unhealthy server until manually removed
> D. Restart the unhealthy server automatically
>
> > [!answer]- Show Answer
> > **B. Remove the unhealthy server from the rotation and direct traffic to healthy servers**
> >
> > [[health-checks|Health checks]] allow load balancers to detect unhealthy nodes and automatically remove them from the pool, directing traffic only to healthy servers. Shutting down all servers (A) would cause a complete outage. Continuing to send traffic to a failed server (C) defeats the purpose of health checks. Automatically restarting the server (D) is beyond the scope of a load balancer's typical function.

## Scenario

> See [[case-load-balancers-and-proxies]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [3.2 – Network Appliances](https://www.youtube.com/watch?v=WlOslEy3ztg)
