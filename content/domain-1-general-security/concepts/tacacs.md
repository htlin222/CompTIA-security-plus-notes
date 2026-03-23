---
title: "TACACS+"
description: "TCP-based AAA protocol that encrypts the entire payload; separates AAA functions independently"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is TACACS+?
> TACACS+ is like a stricter version of the Wi-Fi bouncer. It checks who you are, what you're allowed to do, and keeps a record -- all as separate steps. Plus, it scrambles the entire conversation so nobody can eavesdrop.

## Definition

TACACS+ (Terminal Access Controller Access-Control System Plus) is a Cisco-developed network AAA protocol that uses TCP (port 49) and encrypts the entire communication payload—not just the password. Unlike RADIUS, TACACS+ separates Authentication, Authorization, and Accounting into independent functions, allowing each to be handled by different servers or processes. It is primarily used for device administration (managing routers, switches, firewalls).

## Key Details

- **Protocol**: TCP port 49; connection-oriented and reliable.
- **Encryption**: Encrypts the **entire packet payload** (not just the password)—more secure than RADIUS for sensitive communications.
- **Separation of AAA**: Authentication, Authorization, and Accounting can be handled independently—greater flexibility.
- **Primary use**: Network device administration (router/switch management); RADIUS is preferred for network access (Wi-Fi, VPN).
- **Cisco proprietary**: TACACS+ is Cisco's extension of the open TACACS protocol—not fully standardized but widely supported.

## Connections

- Parent: [[aaa-framework]] — TACACS+ implements the full AAA framework for device administration
- See also: [[radius]], [[accounting]]
