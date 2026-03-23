---
title: "DNS over HTTPS (DoH) / DNS over TLS (DoT)"
description: "Encrypts DNS queries to prevent eavesdropping and manipulation"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - DoH
  - DOH
  - DoT
  - DOT
---

> [!eli5] ELI5: What is DNS over HTTPS / DNS over TLS?
> Normally when your computer looks up a website address, everyone nearby can see what you're looking up. DoH and DoT put that lookup inside a sealed envelope so nobody can peek.

## Definition

DNS over HTTPS (DoH) and DNS over TLS (DoT) are protocols that encrypt DNS queries, protecting them from eavesdropping, manipulation, and surveillance. Traditional DNS transmits queries in plaintext over UDP port 53, allowing anyone on the network path to see what domains a user is resolving. DoH (port 443) and DoT (port 853) tunnel DNS through encrypted connections, preventing interception.

## Key Details

- **DoH**: Sends DNS queries inside HTTPS (port 443)—looks like normal web traffic, making it harder to block.
- **DoT**: Dedicated TLS-encrypted DNS on port 853—easier to monitor/allow/block by IT departments.
- Protects against: **DNS poisoning**, **eavesdropping**, **ISP DNS logging**, and **on-path manipulation**.
- Security consideration: encrypted DNS can bypass organizational DNS filtering controls—relevant for enterprise security policy.
- Supported by major resolvers: Cloudflare (1.1.1.1), Google (8.8.8.8), and built into Firefox, Chrome, and modern OS resolvers.

## Connections

- Parent: [[dns-attacks]] — a defense against DNS-based attacks
- See also: [[dnssec-dns-security-extensions]]
