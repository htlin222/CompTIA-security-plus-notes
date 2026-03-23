---
title: "SSL/TLS interception (SSL proxy)"
description: "Using a trusted certificate to decrypt, inspect, and re-encrypt TLS traffic"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

SSL/TLS interception (also called SSL inspection or SSL proxy) is a technique used by organizations and attackers alike to decrypt, inspect, and re-encrypt TLS-encrypted traffic. An intermediary device presents its own certificate to the client (appearing as the server) while establishing a separate TLS session with the actual server. When performed by organizations using a trusted internal CA, it enables content inspection; when performed maliciously, it's a man-in-the-middle attack.

## Key Details

- **Legitimate use**: Corporate security tools decrypt TLS traffic to inspect for malware, DLP violations, or policy breaches using an enterprise CA that's trusted by managed devices.
- **Malicious use**: Attacker positions themselves as an SSL proxy, presenting a certificate that the victim's browser trusts (requires compromising a CA or installing a rogue root certificate).
- **Certificate pinning**: Applications that "pin" a specific certificate or public key will reject the proxy's certificate—prevents interception for pinned apps.
- **Transparency**: Employees should be informed when their employer performs SSL inspection—there are privacy and legal considerations.
- Detection: inspect the certificate details in the browser—the issuing CA should be the expected organization, not a suspicious interceptor.

## Connections

- Parent: [[on-path-attacks]] — SSL proxy as both a legitimate tool and attack technique
- See also: [[ssltls-stripping]], [[https-spoofing]]
