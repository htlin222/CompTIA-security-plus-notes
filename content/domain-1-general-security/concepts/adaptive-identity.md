---
title: "Adaptive identity"
description: "Authentication and authorization that adjust based on real-time risk assessment"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Adaptive identity is a security approach in which authentication and authorization decisions dynamically adjust based on real-time risk signals such as device health, user location, behavior patterns, and threat intelligence. Rather than applying static, one-size-fits-all policies, adaptive identity systems continuously evaluate context and may require step-up authentication when risk is elevated. It is a core enabler of Zero Trust architecture.

## Key Details

- Risk signals include: **device compliance status**, **geolocation**, **time of access**, **IP reputation**, and **user behavioral baseline**.
- **Step-up authentication** (e.g., requiring MFA mid-session) is triggered when risk increases during a session.
- Adaptive identity supports **least-privilege** by narrowing permissions dynamically based on context.
- Closely tied to **conditional access** policies in identity platforms (e.g., Azure AD Conditional Access).
- Helps detect **account compromise** by flagging unusual behavior even after successful authentication.

## Connections

- Parent: [[zero-trust]] — a key principle enabling Zero Trust dynamic access control
- See also: [[conditional-access]]
