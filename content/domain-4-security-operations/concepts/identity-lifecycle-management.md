---
title: "Identity lifecycle management"
description: "Joiner-mover-leaver processes that track an identity from onboarding to offboarding"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Identity Lifecycle Management?
> From the day someone joins a company to the day they leave, their account follows a journey. This manages every step -- creating the account, updating it, and shutting it down when they go.

## Definition

Identity lifecycle management is the set of processes that govern a digital identity from creation (joining the organization) through modifications (role changes, departmental moves) to termination (leaving the organization). Proper lifecycle management ensures that identities and their access rights are always current, appropriate, and promptly revoked when no longer needed.

## Key Details

- **Joiner**: new employee onboarding — provisioning accounts, email, and role-appropriate access
- **Mover**: role/department change — modifying access rights to match new role, removing old access
- **Leaver**: offboarding — immediate deprovisioning of all accounts upon separation (especially critical)
- Delayed deprovisioning of ex-employee accounts is a significant security risk
- Automated provisioning/deprovisioning via SCIM protocol or HR system integration reduces human error

## Connections

- Parent: [[identity-management]] — identity lifecycle management is a core IAM process
- See also: [[provisioning-and-deprovisioning]]
