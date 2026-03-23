---
title: "Health checks"
description: "load balancers monitor backend server health and remove unhealthy nodes from rotation"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What are Health checks?
> Like a coach checking if players are feeling okay before sending them into the game. If a server is not responding properly, the load balancer stops sending it work until it recovers.

## Definition

Health checks are automated tests performed by load balancers to continuously verify that backend servers are functioning correctly and can handle requests. When a health check fails, the load balancer automatically removes the failing server from the pool and stops sending traffic to it until it recovers and passes health checks again, ensuring that only healthy servers receive user traffic.

## Key Details

- Types: TCP health checks (is the port open?), HTTP health checks (does it return 200 OK?), application-level checks (does the application respond correctly?)
- Health check frequency and failure thresholds are configurable
- Failed health checks trigger automatic failover to remaining healthy servers
- Health checks enable zero-downtime deployments: new servers are only added to rotation after passing checks
- False positives in health checks can cause healthy servers to be incorrectly removed from rotation

## Connections

- Parent: [[load-balancers-and-proxies]] — health checks are an essential load balancer feature
- See also: [[failover]]
