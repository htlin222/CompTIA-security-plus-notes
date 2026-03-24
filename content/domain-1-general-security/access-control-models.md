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

> [!eli5] ELI5: What are Access Control Models?
> You know how some classrooms let the teacher decide who can borrow supplies (the teacher picks), while other classrooms have strict rules posted on the wall that nobody can change? Access control models are like different sets of rules for deciding who gets to use what. Some let the owner choose, some follow strict labels, and some give access based on your job or role. Each set of rules works better in different situations.

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

## Practice Questions

> [!qbank]- Q-Bank: Access Control Models (4 Questions)
>
> **Q1.** A defense contractor requires that all employees can only access documents at or below their assigned clearance level, and no user can override these restrictions regardless of their role. Which access control model BEST meets this requirement?
>
> A. Discretionary Access Control (DAC)
> B. Role-Based Access Control (RBAC)
> C. Mandatory Access Control (MAC)
> D. Attribute-Based Access Control (ABAC)
>
> > [!answer]- Show Answer
> > **C. Mandatory Access Control (MAC)**
> >
> > [[access-control-models|MAC]] uses system-enforced labels and clearance levels where users cannot change access permissions, making it the most restrictive model and ideal for military/government environments. DAC allows the resource owner to decide access, which violates the requirement that no user can override restrictions. RBAC assigns permissions based on roles but does not enforce classification labels. ABAC evaluates multiple attributes but does not inherently enforce hierarchical clearance levels.
>
> **Q2.** A hospital IT team needs an access control policy that grants doctors access to patient records only during business hours, from on-premises workstations, and only for patients in their assigned department. Which model provides the MOST granular enforcement of these conditions?
>
> A. Role-Based Access Control (RBAC)
> B. Rule-Based Access Control
> C. Mandatory Access Control (MAC)
> D. Attribute-Based Access Control (ABAC)
>
> > [!answer]- Show Answer
> > **D. Attribute-Based Access Control (ABAC)**
> >
> > [[access-control-models|ABAC]] evaluates multiple attributes simultaneously — user attributes (department), resource attributes (patient department), environment attributes (time and location) — making it the most granular and flexible model for complex conditional policies. RBAC assigns permissions based on roles but cannot natively enforce time-of-day or location conditions. Rule-based access can enforce simple conditions like time but lacks the multi-attribute evaluation ABAC provides. MAC uses classification labels, not contextual attributes like time and location.
>
> **Q3.** A security analyst discovers that a Trojan horse program inherited the file permissions of the user who executed it and exfiltrated sensitive documents the user owned. Which access control model weakness does this exploit PRIMARILY demonstrate?
>
> A. RBAC role explosion
> B. DAC permission inheritance vulnerability
> C. MAC label downgrade attack
> D. ABAC attribute spoofing
>
> > [!answer]- Show Answer
> > **B. DAC permission inheritance vulnerability**
> >
> > Under [[access-control-models|DAC]], programs run with the permissions of the executing user, so a Trojan horse inherits all the user's access rights — this is a well-known DAC weakness. RBAC role explosion refers to the problem of having too many roles to manage, not malware inheritance. MAC explicitly prevents this scenario because access is determined by system-enforced labels, not user ownership. ABAC attribute spoofing is a theoretical concern about falsifying attributes, not about program inheritance.
>
> **Q4.** A security architect needs to explain why the Bell-LaPadula model prevents a user with "Secret" clearance from writing data to an "Unclassified" document. Which principle does this restriction BEST enforce?
>
> A. Integrity through "no read down"
> B. Confidentiality through "no write down"
> C. Availability through access restrictions
> D. Non-repudiation through audit logging
>
> > [!answer]- Show Answer
> > **B. Confidentiality through "no write down"**
> >
> > The [[bell-lapadula-model|Bell-LaPadula model]] enforces confidentiality with "no read up, no write down." Preventing a Secret-cleared user from writing to an Unclassified document stops classified information from leaking to lower classification levels. "No read down" is a [[biba-model|Biba model]] integrity principle, not Bell-LaPadula. Availability is not the focus of either Bell-LaPadula or Biba. Non-repudiation involves proving who performed an action and is unrelated to classification-based access controls.

## Scenario

> See [[case-access-control-models]] for a practical DevOps scenario applying these concepts.
