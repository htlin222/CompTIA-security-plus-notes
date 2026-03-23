---
title: "Break-glass accounts"
description: "Emergency access accounts with heightened monitoring for use when normal access paths fail"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Break-glass accounts (also called emergency access accounts) are privileged accounts maintained for use only in emergency situations when normal administrative access pathways are unavailable — for example, when the primary admin account is locked out or identity systems are down. These accounts bypass normal access controls but are subject to heightened logging and alerting to detect unauthorized use.

## Key Details

- Used only when normal privileged access mechanisms (PAM, MFA) are unavailable
- Credentials are stored securely (sealed envelope, PAM vault with dual-control) and accessed only in genuine emergencies
- Any use automatically triggers high-priority alerts to security and management teams
- All actions taken with break-glass accounts must be thoroughly documented and reviewed post-incident
- Should be tested periodically to ensure they function when actually needed

## Connections

- Parent: [[privileged-access-management]] — break-glass accounts are a PAM control for emergency access
- See also: [[session-recording]]
