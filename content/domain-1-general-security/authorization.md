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

## Scenario

> See [[case-authorization]] for a practical DevOps scenario applying these concepts.
