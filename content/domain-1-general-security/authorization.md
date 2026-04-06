---
title: "Authorization"
description: "Mechanisms that determine what authenticated users are permitted to access and do"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/identity
  - weight/high
aliases:
  - "AuthZ"
---

> [!eli5] ELI5: What is Authorization?
> Once the school knows who you are, authorization is about what you're allowed to do. A regular student can go to class but can't walk into the principal's office and read private files. A teacher can go places students can't. Authorization is the set of rules that says "you're allowed to do this, but not that." On computers, it works the same way -- after you log in, the system checks what you're actually permitted to see and change.
>
> > [!eli5] ELI5: Authorization (繁體中文版)
> > 授權是在你進門後，決定你能去哪些房間。你可能有大門鑰匙，但不能進去財務室。這就是權限管理。
> >
> > ```ascii
> > [已登入者] --> [權限清單] --> [允許存取?]
> >                  |
> >                  |-- 檔案 A (V)
> >                  |-- 檔案 B (X)
> > ```

## Overview

Authorization is the process of determining what an authenticated entity is allowed to do within a system. It occurs after authentication and defines the scope of access — which resources can be read, modified, created, or deleted. Authorization is enforced through access control models, policies, and permission structures that align with organizational security requirements.

## Key Concepts

- **[[authorization-vs-authentication|Authorization vs. Authentication]]** — authentication proves identity; authorization defines permissions
- **[[principle-of-least-privilege|Principle of least privilege]]** — grant only the minimum access necessary for a role or task
- **[[separation-of-duties|Separation of duties]]** — divide critical tasks among multiple people to prevent fraud
- **Access control models** — formal frameworks for authorization decisions (see [[access-control-models]])
  - **DAC** (Discretionary) — resource owner controls access
  - **MAC** (Mandatory) — system-enforced labels and clearances
  - **RBAC** (Role-Based) — permissions assigned to roles, users assigned to roles
  - **ABAC** (Attribute-Based) — policies based on user/resource/environment attributes
  - **Rule-Based** — access determined by predefined rules (e.g., time-of-day restrictions)
- **[[permission-inheritance|Permission inheritance]]** — child objects inherit permissions from parent containers
- **[[implicit-deny|Implicit deny]]** — if no rule explicitly grants access, access is denied by default
- **[[oauth-20|OAuth 2.0]]** — authorization framework for delegated access; issues access tokens (not authentication)
- **[[conditional-access|Conditional access]]** — dynamic authorization based on risk signals (device compliance, location, behavior)

## Exam Tips

> [!tip] Remember
> **OAuth is for Authorization, NOT Authentication.** OAuth grants access tokens for resource access. OpenID Connect (OIDC) adds authentication on top of OAuth. The exam tests this distinction.

> [!tip] Implicit Deny
> If a question describes a firewall or ACL scenario where no rule matches, the answer is always **deny**. This is a core security principle.

## Connections

- Second component of the [[aaa-framework]] following authentication
- Implemented through [[access-control-models]] which define the formal authorization structure
- Works with [[authentication]] to form complete identity verification and access control
- Critical to [[zero-trust]] where authorization is continuously evaluated based on context
- Managed at scale through [[privileged-access-management]] and [[identity-management]]

## Practice Questions

> [!qbank]- Q-Bank: Authorization (4 Questions)
>
> **Q1.** A developer implements a third-party application that allows users to grant it read-only access to their cloud storage files without sharing their password. Which protocol is MOST likely being used?
>
> A. SAML
> B. OpenID Connect
> C. OAuth 2.0
> D. Kerberos
>
> > [!answer]- Show Answer
> > **C. OAuth 2.0**
> >
> > [[oauth-20|OAuth 2.0]] is an authorization framework designed for delegated access — it issues access tokens that allow a third-party application to access resources on behalf of a user without exposing their credentials. SAML is primarily used for federated authentication and single sign-on, not delegated resource access. OpenID Connect adds an authentication layer on top of OAuth but the scenario describes authorization (granting access), not authentication (proving identity). Kerberos is a ticket-based authentication protocol used in Active Directory, not for third-party delegated access.
>
> **Q2.** A firewall administrator reviews a rule set and notices that a packet does not match any configured rule. What action will the firewall MOST likely take?
>
> A. Allow the traffic and log the event
> B. Forward the traffic to a honeypot for analysis
> C. Deny the traffic based on implicit deny
> D. Queue the traffic for manual administrator review
>
> > [!answer]- Show Answer
> > **C. Deny the traffic based on implicit deny**
> >
> > [[implicit-deny|Implicit deny]] is a core security principle stating that if no rule explicitly grants access, access is denied by default. This applies to firewalls, ACLs, and access control systems. Allowing unmatched traffic would violate the principle of least privilege and create a security hole. Forwarding to a honeypot requires an explicit rule and is not default firewall behavior. Queuing for manual review is impractical for real-time network traffic processing and is not standard behavior.
>
> **Q3.** A compliance officer discovers that a single database administrator can create user accounts, assign permissions, and approve their own access changes without any oversight. Which authorization principle is MOST directly violated?
>
> A. Principle of least privilege
> B. Separation of duties
> C. Implicit deny
> D. Permission inheritance
>
> > [!answer]- Show Answer
> > **B. Separation of duties**
> >
> > [[separation-of-duties|Separation of duties]] requires that critical tasks be divided among multiple people to prevent fraud and errors — one person controlling account creation, permission assignment, and self-approval violates this principle. While least privilege may also be partially violated (the DBA may have more access than needed), the core issue is that a single person controls all aspects of a critical process. Implicit deny relates to default access denial, not role separation. Permission inheritance concerns how child objects receive parent permissions, which is unrelated.
>
> **Q4.** An organization implements a system where access to financial applications is automatically restricted when a user connects from an unrecognized device or an unusual geographic location. Which authorization concept does this BEST illustrate?
>
> A. Role-Based Access Control
> B. Implicit deny
> C. Conditional access
> D. OAuth 2.0 token scoping
>
> > [!answer]- Show Answer
> > **C. Conditional access**
> >
> > [[conditional-access|Conditional access]] dynamically adjusts authorization decisions based on real-time risk signals such as device compliance, location, and user behavior — exactly what is described. RBAC assigns permissions based on static role membership, not real-time contextual signals. Implicit deny blocks all traffic not explicitly allowed, but does not evaluate dynamic conditions like location or device posture. OAuth 2.0 token scoping limits what a third-party application can do, not user access based on contextual risk.

## Scenario

> See [[case-authorization]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [1.2 – Authentication, Authorization, and Accounting](https://www.youtube.com/watch?v=AhaZtj5P2a8)
