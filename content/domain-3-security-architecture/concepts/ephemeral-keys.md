---
title: "Ephemeral keys"
description: "temporary keys used for a single session; provide perfect forward secrecy"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Ephemeral keys are cryptographic keys generated for a single session or transaction and discarded afterward. Unlike long-term static keys, ephemeral keys are never stored persistently, which means that even if a long-term private key is later compromised, past session keys cannot be derived from it. This property is called Perfect Forward Secrecy (PFS).

## Key Details

- Generated fresh for each session using Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman (ECDHE)
- Provide Perfect Forward Secrecy: compromise of the server's long-term private key does not expose past sessions
- Used in TLS 1.3 (which mandates PFS cipher suites) and modern VPN configurations
- Performance overhead is minimal with modern hardware
- TLS cipher suites using DHE or ECDHE provide PFS; those using static RSA key exchange do not

## Connections

- Parent: [[key-management]] — ephemeral key management is critical for implementing PFS
- See also: [[perfect-forward-secrecy-pfs]]
