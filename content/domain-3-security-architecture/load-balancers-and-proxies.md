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

## Scenario

> See [[case-load-balancers-and-proxies]] for a practical DevOps scenario applying these concepts.
