---
title: "Downgrade attack"
description: "Forcing a system to use a weaker, vulnerable cryptographic protocol or cipher"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A downgrade attack forces a system to abandon a secure, modern protocol in favor of an older, weaker version that the attacker can exploit. By manipulating protocol negotiation mechanisms, the attacker tricks both parties into "downgrading" to a version with known vulnerabilities. Famous examples include POODLE (forcing SSLv3), DROWN (forcing SSLv2), and FREAK/Logjam (forcing export-grade cryptography).

## Key Details

- **POODLE (2014)**: Forces SSL 3.0 (vulnerable to padding oracle attacks)—fixed by disabling SSL 3.0.
- **DROWN (2016)**: Servers supporting SSLv2 could be used to attack modern TLS connections—fixed by disabling SSLv2.
- **FREAK**: Forces export-grade RSA (512-bit)—easily factorable; fixed by disabling export cipher suites.
- **Logjam**: Forces weak Diffie-Hellman (512-bit export groups)—fixed by removing DHE_EXPORT.
- Mitigation: **disable all legacy protocol versions** (SSLv2, SSLv3, TLS 1.0, TLS 1.1), only allow TLS 1.2+ with strong cipher suites.

## Connections

- Parent: [[cryptographic-attacks]] — an attack on protocol negotiation mechanisms
- See also: [[deprecated-algorithms]], [[ssltls-stripping]]
