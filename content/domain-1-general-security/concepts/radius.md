---
title: "RADIUS"
description: "UDP-based AAA protocol that encrypts only the password; commonly used for Wi-Fi and VPN authentication"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is RADIUS?
> When you connect to Wi-Fi at school, a central computer checks if your username and password are correct. RADIUS is the system that handles that check -- it's like a bouncer for network connections.

## Definition

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for network access services including Wi-Fi, VPN, and dial-up connections. It operates over UDP (ports 1812 for authentication/authorization and 1813 for accounting) and encrypts only the password field in authentication packets—not the entire payload.

## Key Details

- **Protocol**: UDP-based (ports 1812/1813); unreliable transport but fast and simple.
- **Encryption**: Only the password is encrypted (using MD5 and a shared secret)—other attributes transmitted in cleartext.
- **Use cases**: Authenticating users for **Wi-Fi** (802.1X), **VPN**, **dial-up**, and **network device management**.
- **802.1X**: A network access control standard that uses RADIUS as the backend authentication server; often combined with EAP (Extensible Authentication Protocol).
- **Compare to TACACS+**: TACACS+ uses TCP, encrypts the entire payload, and separates AAA functions independently—preferred for device administration.

## Connections

- Parent: [[aaa-framework]] — RADIUS implements the AAA framework for network access
- See also: [[tacacs]], [[accounting]]
