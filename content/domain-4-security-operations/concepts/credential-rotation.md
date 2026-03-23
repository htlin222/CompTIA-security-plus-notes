---
title: "Credential rotation"
description: "Automatically changing privileged passwords on a schedule or after each use"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Credential Rotation?
> Changing your passwords on a schedule is like changing the locks on your doors every few months. Even if someone copied a key, it stops working once you swap the lock.

## Definition

Credential rotation is the practice of automatically changing privileged account passwords and secrets on a predefined schedule or immediately after each use. PAM solutions implement automatic credential rotation to ensure that even if a privileged credential is compromised, its window of validity is limited and it cannot be reused by an attacker.

## Key Details

- Passwords are changed automatically by the PAM vault — users never know the actual password
- Check-out/check-in model: user requests access, vault provides a temporary credential, rotates it after the session ends
- Service account passwords can also be rotated automatically if applications are integrated with the PAM vault
- Rotation frequency is typically daily for highly sensitive accounts, or after every use
- Eliminates the risk of stale, shared, or known passwords for privileged accounts

## Connections

- Parent: [[privileged-access-management]] — credential rotation is a core PAM control
- See also: [[password-vaulting]]
