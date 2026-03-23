---
title: "Slowloris"
description: "Keeps many HTTP connections open by sending partial headers, exhausting the server's connection pool"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Slowloris?
> The attacker opens lots of connections to a website but talks reeeally slowly on each one, never finishing. The server politely waits for each to finish, and eventually it has no room left for real visitors.

## Definition

Slowloris is an application-layer (Layer 7) denial-of-service attack tool and technique that holds many HTTP connections open simultaneously by sending partial HTTP request headers very slowly—one header at a time with long pauses between each. The server keeps each connection open waiting for the complete request, eventually exhausting its connection pool and refusing new legitimate connections.

## Key Details

- Named after the slow loris animal—it works slowly and deliberately.
- Requires **minimal bandwidth**—a single attacker with a slow connection can take down a server with many connections.
- Works against servers with a **fixed connection pool** (Apache HTTP server is particularly vulnerable; Nginx is more resistant due to its asynchronous architecture).
- Sends a header like `X-a: b\r\n` every 15 seconds to keep the connection alive—never sending the final blank line that completes the HTTP header.
- **Mitigations**: **Connection timeouts** (close connections that take too long), **rate limiting** (limit connections per IP), **Nginx/reverse proxy** fronting Apache, **cloud WAF/CDN services**.

## Connections

- Parent: [[denial-of-service]] — an application-layer DoS attack
- See also: [[application-layer-attacks]]
