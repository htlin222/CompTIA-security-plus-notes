---
title: "Attribute-Based Access Control (ABAC)"
description: "Access decisions based on attributes such as department, location, or time of day"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - ABAC
---

> [!eli5] ELI5: What is Attribute-Based Access Control?
> Instead of just checking your name badge, ABAC checks lots of details -- like what department you are in, what time it is, and where you are -- before deciding if you can come in.

## Definition

Attribute-Based Access Control (ABAC) is an access control model where access decisions are made based on attributes associated with users, resources, and the environment. Unlike RBAC which uses static roles, ABAC evaluates dynamic conditions such as a user's department, their location, the time of day, device compliance status, and resource classification to grant or deny access.

## Key Details

- More granular and flexible than Role-Based Access Control (RBAC)
- Attributes can include user attributes (department, clearance), resource attributes (classification), and environmental attributes (time, location)
- Enables context-aware access control: same user may get different access from different locations
- Used in zero trust architectures for continuous authorization decisions
- Common implementation: XACML (eXtensible Access Control Markup Language) policy language

## Connections

- Parent: [[identity-management]] — ABAC is an advanced access control model
- See also: [[role-based-access-control-rbac]]
