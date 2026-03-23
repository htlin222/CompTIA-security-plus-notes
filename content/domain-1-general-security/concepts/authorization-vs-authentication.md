---
title: "Authorization vs. Authentication"
description: "Authentication proves identity; authorization defines permissions"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Authentication is the process of verifying that a user, device, or system is who or what it claims to be (proving identity). Authorization is the process of determining what an authenticated entity is permitted to do (defining permissions). These are distinct steps in the AAA framework: you must first authenticate before the system can evaluate what you are authorized to access.

## Key Details

- **Authentication**: "Who are you?" — verified by credentials (password, certificate, biometric).
- **Authorization**: "What can you do?" — determined by access control policies, roles, and permissions.
- A user can be **authenticated but not authorized** (valid identity, insufficient permissions).
- Authorization decisions occur after successful authentication and are enforced at the **policy enforcement point**.
- Common authorization models: **RBAC** (role-based), **ABAC** (attribute-based), **MAC** (mandatory), **DAC** (discretionary).

## Connections

- Parent: [[authorization]] — core concept within the authorization domain
- See also: [[accounting]], [[adaptive-identity]]
