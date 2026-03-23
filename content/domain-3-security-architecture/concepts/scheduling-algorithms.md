---
title: "Scheduling algorithms"
description: "round-robin, least connections, weighted, IP hash, health-based"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What are Scheduling algorithms?
> These are the different methods for deciding who goes next, like taking turns (round-robin) or going to the shortest line at the grocery store (least connections). Load balancers use these rules to decide which server handles each request.

## Definition

Load balancer scheduling algorithms (also called distribution methods) determine how the load balancer selects which backend server should handle each incoming request. The choice of algorithm affects performance, session persistence, and how evenly load is distributed across the server pool.

## Key Details

- **Round-robin**: requests distributed sequentially to each server in turn; simple, no state tracking
- **Least connections**: new requests go to the server with fewest active connections; better for unequal session lengths
- **Weighted**: servers assigned weights proportional to their capacity; higher-weight servers receive more requests
- **IP hash**: client IP address determines which server handles the request; ensures session persistence without cookies
- **Health-based**: combines health check status with the other algorithms to avoid sending traffic to degraded servers

## Connections

- Parent: [[load-balancers-and-proxies]] — scheduling algorithms are a fundamental load balancer configuration choice
- See also: [[health-checks]]
