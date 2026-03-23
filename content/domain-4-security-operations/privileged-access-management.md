---
title: "Privileged Access Management"
description: "Controls and monitoring for accounts with elevated permissions to critical systems"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/identity
  - weight/high
aliases:
  - "PAM"
---

> [!eli5] ELI5: What is Privileged Access Management?
> In a school, the principal has a master key that opens every room. If that key gets lost, someone could go anywhere -- the office, the supply room, everywhere. Privileged access management is about keeping those master keys in a locked safe, only handing them out when absolutely needed, watching what people do with them, and taking them back as soon as possible. The fewer people holding master keys, the safer the building.

## Overview

Privileged Access Management (PAM) is a set of strategies and technologies for controlling, monitoring, and auditing elevated access to critical systems and data. Privileged accounts (admin, root, service accounts) are prime targets for attackers because they provide broad access. PAM solutions enforce least privilege and provide accountability for privileged actions.

## Key Concepts

- **[[password-vaulting|Password vaulting]]**: Storing privileged credentials in an encrypted vault; users check out passwords for time-limited sessions
- **[[just-in-time-jit-access|Just-in-time (JIT) access]]**: Granting privileged access only when needed and automatically revoking it after a set period
- **[[session-recording|Session recording]]**: Recording all actions taken during privileged sessions for audit and forensic purposes
- **[[credential-rotation|Credential rotation]]**: Automatically changing privileged passwords on a schedule or after each use
- **[[break-glass-accounts|Break-glass accounts]]**: Emergency access accounts with heightened monitoring for use when normal access paths fail
- **[[service-account-management|Service account management]]**: Tracking and securing non-human accounts used by applications and scripts
- **[[least-privilege-enforcement|Least privilege enforcement]]**: Ensuring even administrators only have access to what their role requires
- **[[separation-of-duties|Separation of duties]]**: Requiring multiple privileged users to complete sensitive operations

## Exam Tips

> [!tip] Remember
> PAM focuses on the "keys to the kingdom" — admin and root accounts. Key controls: vault credentials, limit time, record sessions, rotate passwords. If a scenario mentions admin access, think PAM.

- Service accounts are frequently overlooked — they often have excessive permissions and rarely rotate passwords
- Know the difference between PAM (managing privileged accounts) and general IAM (managing all accounts)
- Break-glass procedures should be documented and heavily monitored

## Connections

- Critical extension of [[identity-management]] for high-risk accounts
- Must be protected with [[mfa]] — privileged accounts should always require multi-factor authentication
- Helps detect compromises through [[log-management]] by recording privileged session activity
- [[hardening]] includes restricting and monitoring privileged access as a key security baseline

## Scenario

> See [[case-privileged-access-management]] for a practical DevOps scenario applying these concepts.
