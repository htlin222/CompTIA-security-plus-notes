---
title: "SSL/TLS offloading"
description: "load balancer handles encryption/decryption, reducing server workload"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is SSL/TLS offloading?
> Scrambling and unscrambling secret messages takes a lot of effort. SSL/TLS offloading lets a helper machine do all that heavy work so the main server can focus on actually answering your requests, like having someone else unwrap all your presents for you.

## Definition

SSL/TLS offloading (also called SSL termination) is a load balancer configuration in which the load balancer handles all TLS encryption and decryption on behalf of the backend servers. The load balancer decrypts incoming HTTPS traffic, optionally inspects or modifies it, then forwards the request to backend servers in plaintext (or re-encrypts it for backend SSL). This reduces the cryptographic processing burden on backend servers.

## Key Details

- Load balancer holds the TLS certificate and private key; backend servers communicate in HTTP
- Reduces CPU load on backend servers, improving throughput and response times
- Enables the load balancer to inspect request content for security (WAF functionality, load-based routing)
- Security consideration: traffic between load balancer and backend is unencrypted — must be on a trusted internal network
- Re-encryption (SSL bridging): load balancer re-encrypts traffic to the backend; inspection + end-to-end encryption

## Connections

- Parent: [[load-balancers-and-proxies]] — SSL/TLS offloading is a key load balancer performance and security feature
- See also: [[scheduling-algorithms]]
