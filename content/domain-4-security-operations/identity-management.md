---
title: "Identity Management"
description: "Centralized management of user identities, credentials, and access rights across systems"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/identity
  - weight/high
aliases:
  - "IdM"
---

## Overview

Identity management (IdM) is the framework of policies, processes, and technologies used to manage digital identities and control access to organizational resources. It ensures the right individuals have the right access to the right resources at the right times for the right reasons. IdM is foundational to security operations and is heavily tested on the SY0-701 exam.

## Key Concepts

- **[[provisioning-and-deprovisioning|Provisioning and deprovisioning]]**: Creating, modifying, and removing user accounts throughout the identity lifecycle
- **[[identity-lifecycle-management|Identity lifecycle management]]**: Joiner-mover-leaver processes that track an identity from onboarding to offboarding
- **[[directory-services|Directory services]]**: Centralized stores (e.g., LDAP, Active Directory) that maintain identity attributes and group memberships
- **[[role-based-access-control-rbac|Role-Based Access Control (RBAC)]]**: Assigning permissions based on job roles rather than individual users
- **[[attribute-based-access-control-abac|Attribute-Based Access Control (ABAC)]]**: Access decisions based on attributes such as department, location, or time of day
- **[[identity-governance|Identity governance]]**: Periodic access reviews and certification to ensure least privilege is maintained
- **[[self-service-capabilities|Self-service capabilities]]**: Password resets and profile updates reduce helpdesk burden while maintaining security
- **[[privileged-accounts|Privileged accounts]]**: Service accounts, admin accounts, and root accounts require additional controls

## Exam Tips

> [!tip] Remember
> Identity management is the "who" — authentication verifies the identity, authorization determines access. Know the difference between identification, authentication, authorization, and accounting (IAAA).

- Deprovisioning is just as critical as provisioning — orphaned accounts are a major vulnerability
- Separation of duties and least privilege are key principles tied to identity management
- Expect scenario questions about what happens when an employee transfers departments (mover process)

## Connections

- Enables [[sso]] for streamlined authentication across multiple applications
- Works with [[mfa]] to strengthen the authentication phase of identity verification
- [[privileged-access-management]] provides additional controls for high-risk identities
- Related to [[federation]] for extending identity across organizational boundaries

## Scenario

> See [[case-identity-management]] for a practical DevOps scenario applying these concepts.
