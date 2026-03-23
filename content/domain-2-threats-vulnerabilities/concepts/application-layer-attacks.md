---
title: "Application-layer attacks"
description: "Targeting specific services with legitimate-looking requests to exhaust application resources"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Application-layer DoS attacks (Layer 7) target specific web services or applications using seemingly legitimate HTTP, DNS, or other protocol requests to exhaust server resources such as threads, memory, or database connections. Unlike volumetric attacks, these require far less bandwidth because they exploit how the application processes requests rather than overwhelming network capacity.

## Key Details

- **HTTP flood**: Sending massive numbers of GET or POST requests to overwhelm web servers.
- **Slowloris**: Keeps connections open by sending partial HTTP headers very slowly, exhausting the server's connection pool.
- **RUDY (R-U-Dead-Yet)**: Similar to Slowloris but targets POST request bodies.
- Application-layer attacks are harder to detect because the traffic appears legitimate to the network layer.
- Mitigations include: rate limiting, CAPTCHA, WAF (Web Application Firewall), connection timeouts, and CDN-based scrubbing.

## Connections

- Parent: [[denial-of-service]] — a sub-type classified by OSI layer
- See also: [[slowloris]], [[volumetric-attacks]]
