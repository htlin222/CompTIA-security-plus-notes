---
title: "Certificate pinning"
description: "application hardcodes the expected certificate or public key to prevent MITM with rogue certs"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Certificate pinning?
> It's like memorizing exactly what your best friend looks like so no stranger can dress up and trick you into thinking they are your friend. An app remembers the exact certificate it expects, so a fake one will not fool it.

## Definition

Certificate pinning is a security technique in which an application is hardcoded to accept only a specific certificate or public key when establishing TLS connections, rather than trusting any certificate signed by a recognized CA. This prevents man-in-the-middle (MITM) attacks even if an attacker has a certificate signed by a trusted CA (such as through a compromised CA or a corporate SSL inspection proxy).

## Key Details

- Pin can be the full certificate (brittle — breaks on renewal) or just the public key (more flexible)
- Mobile apps commonly use certificate pinning to prevent MITM via SSL inspection proxies
- HPKP (HTTP Public Key Pinning) was a web standard for certificate pinning, now deprecated due to risk
- Can cause legitimate outages if certificates are renewed without updating the pin
- Used in high-security apps (banking, government) where MITM risk must be eliminated

## Connections

- Parent: [[pki]] — certificate pinning is an advanced PKI trust mechanism
- See also: [[chain-of-trust]]
