---
title: "Provisioning and deprovisioning"
description: "Creating, modifying, and removing user accounts throughout the identity lifecycle"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Provisioning is the process of creating user accounts and granting appropriate access rights when a user joins an organization or changes roles. Deprovisioning is the reverse — revoking all access and disabling or deleting accounts when a user leaves the organization or changes roles. Both processes must be timely, accurate, and auditable.

## Key Details

- Automated provisioning (triggered by HR system events) is faster and more reliable than manual processes
- **SCIM** (System for Cross-domain Identity Management): protocol for automating provisioning/deprovisioning across multiple systems
- Deprovisioning timeliness is critical: ex-employee accounts are a significant security risk
- All systems and applications must be included — not just Active Directory (cloud SaaS, VPN, etc.)
- Orphaned accounts (accounts without active owners) should be detected and reviewed regularly

## Connections

- Parent: [[identity-management]] — provisioning and deprovisioning are core IAM operational processes
- See also: [[identity-lifecycle-management]]
