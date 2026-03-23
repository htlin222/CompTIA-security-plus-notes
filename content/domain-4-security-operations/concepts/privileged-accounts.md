---
title: "Privileged accounts"
description: "Service accounts, admin accounts, and root accounts require additional controls"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Privileged Accounts?
> These are the super-user accounts with the most power. They are like master keys that open every lock in the building, which makes them very valuable targets for attackers.

## Definition

Privileged accounts are user accounts with elevated permissions that allow them to perform administrative or sensitive operations beyond those available to standard users. These accounts — including domain administrators, local admins, root accounts, and service accounts — represent the highest-value targets for attackers because compromising them often provides full control over systems or entire environments.

## Key Details

- **Service accounts**: used by applications and automated processes; should have minimal permissions for their specific function
- **Admin accounts**: separate from regular user accounts; used only for administrative tasks (never for email/web browsing)
- **Root/Domain admin**: highest-privilege accounts; should be used only through PAM controls with full session recording
- Privileged accounts should require MFA and be subject to PAM controls (vaulting, JIT access, session recording)
- All privileged account activity should be logged and reviewed for anomalous behavior

## Connections

- Parent: [[identity-management]] — privileged accounts require special management controls
- See also: [[privileged-access-management]]
