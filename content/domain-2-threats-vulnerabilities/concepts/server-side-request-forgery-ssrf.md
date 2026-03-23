---
title: "Server-Side Request Forgery (SSRF)"
description: "Tricking the server into making requests to internal resources on behalf of the attacker"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - SSRF
---

## Definition

Server-Side Request Forgery (SSRF) is an attack where the attacker tricks a server into making HTTP requests to an unintended location—typically internal resources that aren't accessible from the internet. By supplying attacker-controlled URLs to server-side functionality (like URL fetchers, webhooks, PDF generators, or image importers), attackers can probe and access internal network services, cloud metadata endpoints, and other resources normally protected by network controls.

## Key Details

- **Cloud metadata services**: SSRF is used to access `http://169.254.169.254/` (AWS, Azure, GCP metadata endpoint) to steal IAM credentials.
- **Internal network scanning**: Attacker uses the server as a proxy to probe internal services (Redis, Elasticsearch, internal APIs) not exposed to the internet.
- In the **OWASP Top 10** since 2021—a significant and growing threat, especially in cloud environments.
- **Mitigation**: Block requests to private IP ranges (RFC 1918), cloud metadata addresses; validate and allowlist permitted URLs; use network segmentation to prevent server-to-internal access.
- Can bypass firewall protections because the request originates from a trusted internal server.

## Connections

- Parent: [[application-attacks]] — a web application vulnerability enabling internal access
- See also: [[directory-traversal]]
