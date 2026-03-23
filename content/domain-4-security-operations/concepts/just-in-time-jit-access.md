---
title: "Just-in-time (JIT) access"
description: "Granting privileged access only when needed and automatically revoking it after a set period"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - JIT
---

## Definition

Just-in-time (JIT) access is a privileged access management principle that eliminates standing privileged access by granting elevated permissions only when explicitly requested and needed, for a defined time period, after which access is automatically revoked. This significantly reduces the risk of compromised accounts being used for privilege escalation because no user maintains persistent elevated access.

## Key Details

- Users have no standing privileged access — they must request and justify access for each use
- Access is granted only for the duration needed (e.g., 4 hours for a maintenance window)
- Automatic revocation eliminates the risk of forgotten or orphaned privileged accounts
- All JIT access requests, approvals, and sessions should be logged and audited
- Implemented via PAM platforms (CyberArk, BeyondTrust, Microsoft PIM for Azure)

## Connections

- Parent: [[privileged-access-management]] — JIT access is a key PAM technique to minimize standing privilege
- See also: [[least-privilege-enforcement]]
