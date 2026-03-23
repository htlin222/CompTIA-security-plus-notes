---
title: "Role-Based Access Control (RBAC)"
description: "Assigning permissions based on job roles rather than individual users"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - RBAC
---

> [!eli5] ELI5: What is Role-Based Access Control?
> RBAC gives access based on your job title. A teacher can access grade books, a janitor can access supply closets, and neither can access the other's stuff.

## Definition

Role-Based Access Control (RBAC) is an access control model in which permissions are assigned to roles (representing job functions) rather than directly to individual users. Users are then assigned to roles based on their job responsibilities, inheriting the permissions of those roles. RBAC simplifies access management at scale and makes it easier to enforce least privilege and separate duties.

## Key Details

- Users receive permissions by virtue of their role membership — not individual permission grants
- Roles map to job functions: "Accountant," "HR Manager," "Network Engineer," "Security Analyst"
- Easier to audit and maintain than per-user permission assignment
- Role changes (promotion, transfer) require updating role assignments rather than individual permissions
- Contrasts with ABAC (attribute-based) which is more dynamic, and mandatory access control (MAC) which is policy-driven

## Connections

- Parent: [[identity-management]] — RBAC is the most widely used access control model in enterprise environments
- See also: [[attribute-based-access-control-abac]]
