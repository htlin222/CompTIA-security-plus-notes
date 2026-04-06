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

> [!eli5] ELI5: What is Identity Management?
> It is like the front office at a school that keeps track of every student, teacher, and visitor. They decide who gets a badge, what rooms each person can enter, and when someone leaves, they take the badge back. Identity management does the same thing for computers -- it controls who gets an account, what they are allowed to access, and makes sure old accounts get shut off when people leave. Without it, anyone could wander in and go anywhere.

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
- **[[identity-provider-idp|IdP (Identity Provider)]]**: Trusted service that creates and manages user identities and provides authentication tokens

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

## Practice Questions

> [!qbank]- Q-Bank: Identity Management (4 Questions)
>
> **Q1.** An employee transfers from the finance department to the marketing department. Two months later, an audit reveals the employee still has access to the finance billing system. What identity management process failed?
>
> A. Initial provisioning
> B. The mover process within identity lifecycle management
> C. Multi-factor authentication enrollment
> D. Directory service replication
>
> > [!answer]- Show Answer
> > **B. The mover process within identity lifecycle management**
> >
> > The [[identity-lifecycle-management|joiner-mover-leaver]] process requires that when an employee changes roles, their access is updated to reflect their new position — removing old permissions and granting new ones. Option A applies to new employees, not transfers. Option C relates to authentication strength, not access rights management. Option D is a technical directory function, not an access governance process.
>
> **Q2.** A large organization has 10,000 employees across multiple departments. The security team wants to simplify permission management by assigning access based on job function rather than configuring each user individually. Which access control model BEST fits this need?
>
> A. Discretionary Access Control (DAC)
> B. Mandatory Access Control (MAC)
> C. Role-Based Access Control (RBAC)
> D. Rule-Based Access Control
>
> > [!answer]- Show Answer
> > **C. Role-Based Access Control (RBAC)**
> >
> > [[role-based-access-control-rbac|RBAC]] assigns permissions to roles based on job functions, and users are assigned to roles — making it efficient to manage access at scale. Option A allows resource owners to set permissions, which is decentralized and hard to manage at scale. Option B uses classification labels and clearance levels, typically for government/military contexts. Option D uses conditional rules rather than job-based roles.
>
> **Q3.** A security administrator discovers several active user accounts belonging to employees who left the organization months ago. These orphaned accounts have not been accessed but still have valid permissions. What is the PRIMARY risk of this situation?
>
> A. The accounts consume unnecessary storage space
> B. Former employees or attackers could use these accounts to gain unauthorized access
> C. The accounts will generate false positive alerts in the SIEM
> D. The directory service performance will degrade
>
> > [!answer]- Show Answer
> > **B. Former employees or attackers could use these accounts to gain unauthorized access**
> >
> > Failure to [[provisioning-and-deprovisioning|deprovision]] accounts is a major security vulnerability. Orphaned accounts with valid credentials and permissions can be exploited by former employees with grudges or by attackers who compromise the unused credentials. Option A is a minor operational concern, not a security risk. Option C is unlikely since inactive accounts rarely generate alerts. Option D is negligible for most directory implementations.
>
> **Q4.** An organization needs to implement access control that considers the user's department, time of day, device type, and geographic location when making authorization decisions. Which model BEST supports this level of granularity?
>
> A. Role-Based Access Control (RBAC)
> B. Attribute-Based Access Control (ABAC)
> C. Mandatory Access Control (MAC)
> D. Discretionary Access Control (DAC)
>
> > [!answer]- Show Answer
> > **B. Attribute-Based Access Control (ABAC)**
> >
> > [[attribute-based-access-control-abac|ABAC]] makes access decisions based on multiple attributes such as department, time, location, and device type, providing the most granular and context-aware authorization. Option A groups users by role but does not natively consider contextual factors like time or location. Option C uses static classification labels, not dynamic attributes. Option D relies on resource owner discretion without attribute evaluation.

## Scenario

> See [[case-identity-management]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [4.6 – Identity and Access Management](https://www.youtube.com/watch?v=ZoOyyqhptik)
