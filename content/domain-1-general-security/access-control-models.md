---
title: "Access Control Models"
description: "Formal models that define how subjects access objects in information systems"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/identity
  - weight/high
aliases:
  - "ACL"
  - "RBAC"
  - "MAC"
  - "DAC"
  - "ABAC"
---

## Overview

Access control models are formal frameworks that dictate how access decisions are made within a system. They define the relationship between subjects (users, processes) and objects (files, resources) and establish rules for granting or denying access. Choosing the correct model depends on organizational needs, regulatory requirements, and the sensitivity of data being protected.

## Key Concepts

- **Discretionary Access Control (DAC)**
  - Resource owner decides who gets access
  - Flexible but less secure; common in Windows NTFS permissions
  - Vulnerable to Trojan horse attacks (inherited permissions)
- **Mandatory Access Control (MAC)**
  - System-enforced labels (classifications) and clearance levels
  - Used in military/government environments (Top Secret, Secret, Confidential, Unclassified)
  - Users cannot change access permissions; most restrictive model
  - Based on Bell-LaPadula (confidentiality) and Biba (integrity) models
- **Role-Based Access Control (RBAC)**
  - Permissions assigned to roles; users assigned to one or more roles
  - Most commonly implemented in enterprises; simplifies administration
  - Follows principle of least privilege by scoping roles tightly
- **Attribute-Based Access Control (ABAC)**
  - Access decisions based on attributes of user, resource, action, and environment
  - Most granular and flexible; supports complex policies
  - Example: "Allow if user.department=finance AND resource.classification=internal AND time=business_hours"
- **Rule-Based Access Control**
  - Predefined rules applied uniformly (e.g., firewall ACLs, time-of-day restrictions)
  - Not based on identity but on conditions
- **[[bell-lapadula-model|Bell-LaPadula Model]]** — "no read up, no write down" — protects confidentiality
- **[[biba-model|Biba Model]]** — "no read down, no write up" — protects integrity

## Exam Tips

> [!tip] Remember
> **Bell-LaPadula** = **BLP** = "**B**e **L**oyal to **P**rivacy" = Confidentiality (no read up, no write down)
> **Biba** = "**B**e **I**ntegrity" = Integrity (no read down, no write up)

> [!tip] RBAC vs. ABAC
> RBAC is simpler (role = permissions). ABAC is more granular (multiple attributes evaluated). If the question involves complex conditional access, think ABAC.

## Connections

- Enforces [[authorization]] decisions defined by organizational policy
- Central to [[security-concepts]] like least privilege and separation of duties
- Role-based models integrate with [[identity-management]] and directory services
- MAC aligns with [[data-classification]] requirements in government and regulated industries
- Attribute-based models support [[zero-trust]] by evaluating contextual signals for every access request

## Scenario

> See [[case-access-control-models]] for a practical DevOps scenario applying these concepts.
