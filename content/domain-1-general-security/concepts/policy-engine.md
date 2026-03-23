---
title: "Policy engine"
description: "Evaluates access requests against policies, risk signals, and threat intelligence in Zero Trust"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

The Policy Engine is the core decision-making component of a Zero Trust Architecture. It evaluates each access request against enterprise security policies, identity information, device health data, threat intelligence, and real-time risk signals to produce an access decision: allow, deny, or allow with conditions (e.g., require MFA). It operates at the control plane level, with its decisions enforced by the policy enforcement point.

## Key Details

- Evaluates: **user identity and authentication strength**, **device compliance** (MDM enrollment, patch status), **request context** (time, location, IP reputation), **resource sensitivity**, **threat intelligence**.
- Makes **real-time, dynamic decisions** for each access request—not static, one-time decisions.
- Can require **step-up authentication** as a condition rather than a binary allow/deny.
- Works with the **policy administrator** to translate decisions into enforcement actions at the PEP.
- Implemented via: **SIEM correlation**, **UEBA analytics**, **IAM platforms** with risk scoring, **SOAR orchestration**.

## Connections

- Parent: [[zero-trust]] — the decision-making brain of Zero Trust Architecture
- See also: [[policy-administrator]], [[adaptive-identity]]
