---
title: "AAA Framework"
description: "Authentication, Authorization, and Accounting — the three pillars of access management"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/identity
  - weight/high
aliases:
  - "AAA"
---

## Overview

The AAA (Authentication, Authorization, and Accounting) framework defines how users are identified, what they are permitted to do, and how their actions are tracked. AAA is implemented through protocols like RADIUS, TACACS+, and Kerberos and underpins identity and access management across enterprise environments.

## Key Concepts

- **Authentication** — verifying the identity of a user, device, or service (see [[authentication]])
  - Something you know (password), something you have (token), something you are (biometric)
- **Authorization** — determining what an authenticated entity is allowed to do (see [[authorization]])
  - Enforced through access control models (RBAC, ABAC, MAC, DAC)
- **[[accounting|Accounting]]** — logging and tracking user activities for audit and forensic purposes
  - Includes session duration, commands executed, data accessed, and resource usage
- **[[radius|RADIUS]]** (Remote Authentication Dial-In User Service) — UDP-based, encrypts only the password, commonly used for network access (Wi-Fi, VPN)
  - Combines authentication and authorization in a single step
- **[[tacacs|TACACS+]]** (Terminal Access Controller Access-Control System Plus) — TCP-based, encrypts the entire payload, separates AAA functions independently
  - Preferred for device administration (switches, routers, firewalls)
- **[[kerberos|Kerberos]]** — ticket-based authentication protocol used in Active Directory environments; uses port 88

## Exam Tips

> [!tip] RADIUS vs. TACACS+
> | Feature | RADIUS | TACACS+ |
> |---|---|---|
> | Protocol | UDP (1812/1813) | TCP (49) |
> | Encryption | Password only | Full packet |
> | AAA Separation | Combined auth/authz | Separate |
> | Best for | Network access | Device admin |

> [!tip] Remember
> "RADIUS for Remote users, TACACS+ for Terminal/device administration." The exam loves comparing these two.

## Connections

- Authentication component detailed in [[authentication]] with methods like [[mfa]] and [[sso]]
- Authorization component detailed in [[authorization]] and implemented via [[access-control-models]]
- Accounting feeds into [[log-management]] and [[siem]] for monitoring and incident detection
- Essential for [[identity-management]] in security operations

## Scenario

> See [[case-aaa-framework]] for a practical DevOps scenario applying these concepts.
