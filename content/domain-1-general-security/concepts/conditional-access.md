---
title: "Conditional access"
description: "Dynamic authorization based on risk signals (device compliance, location, behavior)"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Conditional Access?
> It's like a parent saying "you can watch TV if your homework is done and it's before 9 PM." Access depends on conditions being met -- where you are, what device you're using, and whether anything looks risky.

## Definition

Conditional access is an authorization approach that evaluates real-time risk signals before granting or denying access to resources. Rather than making static allow/deny decisions based solely on identity, conditional access policies consider factors like device compliance state, user location, IP reputation, time of day, and behavioral risk to dynamically adjust access permissions—including requiring step-up authentication for high-risk scenarios.

## Key Details

- Key risk signals: **device compliance** (MDM enrollment, patch level), **location** (trusted vs. untrusted network), **user risk score**, **sign-in risk** (impossible travel, unfamiliar location).
- Can enforce **MFA as a condition** only when risk is elevated, reducing friction for low-risk access.
- Implemented in platforms like **Azure Active Directory Conditional Access**, **Okta Adaptive MFA**, and **Google BeyondCorp**.
- Supports **Zero Trust** principles by continuously evaluating context rather than trusting network location.
- Can block access from **non-compliant devices** even if credentials are valid.

## Connections

- Parent: [[authorization]] — a dynamic authorization mechanism
- See also: [[adaptive-identity]]
