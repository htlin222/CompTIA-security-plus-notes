---
title: "Least privilege"
description: "Users and processes should only have the minimum permissions necessary to perform their function"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

The principle of least privilege states that every user, process, system, or service should be granted only the minimum level of access rights (permissions, capabilities) necessary to perform its intended function—and nothing more. This limits the potential damage from compromised accounts, malware, insider threats, and human error by ensuring that any breach has the smallest possible blast radius.

## Key Details

- Applies to: **users** (no admin accounts for daily tasks), **service accounts** (only the permissions the service needs), **processes** (run with minimum OS privileges), **network access** (only reach the resources they need).
- **Privilege escalation attacks** are directly countered by least privilege—there's less to escalate to.
- Implement via: **RBAC** (roles with minimum necessary permissions), **just-in-time (JIT) access** (temporary elevation when needed), **privileged access management (PAM)**.
- Regular **access reviews** are needed to prevent privilege creep (accumulation of permissions over time).
- Often implemented alongside **need-to-know** (data access restriction) and **separation of duties**.

## Connections

- Parent: [[security-concepts]] — a foundational security principle
- See also: [[separation-of-duties]], [[need-to-know]]
