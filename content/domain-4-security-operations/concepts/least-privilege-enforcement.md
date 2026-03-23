---
title: "Least privilege enforcement"
description: "Ensuring even administrators only have access to what their role requires"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Least privilege enforcement is the ongoing operational practice of ensuring that all users, including administrators and privileged accounts, have only the minimum level of access required to perform their specific job functions — no more. PAM solutions implement and enforce least privilege for privileged accounts by controlling, monitoring, and restricting what actions privileged users can take.

## Key Details

- Even domain administrators should not have unrestricted access to all systems at all times
- Role-based segmentation: different admin tiers for workstations, servers, domain controllers
- Privileged accounts should be separate from regular user accounts (admin account ≠ daily-use account)
- Regular access reviews identify and remove accumulated excessive permissions (privilege creep)
- Zero standing privilege is the ideal: no user has persistent elevated access (combined with JIT)

## Connections

- Parent: [[privileged-access-management]] — least privilege enforcement is the core objective of PAM
- See also: [[just-in-time-jit-access]]
