---
title: "Change Management"
description: "Structured process for managing changes to IT systems while minimizing security risk"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/compliance
  - weight/medium
aliases:
  - "Change Control"
---

## Overview

Change management is a structured process for proposing, evaluating, approving, implementing, and reviewing changes to IT systems and infrastructure. It ensures that modifications do not introduce security vulnerabilities, cause service disruptions, or violate compliance requirements. The SY0-701 exam emphasizes change management as a critical governance control.

## Key Concepts

- **[[change-advisory-board-cab|Change Advisory Board (CAB)]]** — group of stakeholders who review and approve/deny change requests
- **Change management process**:
  1. **Request** — formal proposal documenting the change, rationale, and impact
  2. **Impact analysis** — assess risk, scope, affected systems, and rollback plan
  3. **Approval** — CAB or designated authority reviews and authorizes
  4. **Implementation** — execute the change during an approved maintenance window
  5. **Documentation** — record what was changed, when, and by whom
  6. **Verification/Testing** — confirm the change works as intended without side effects
- **Types of changes**:
  - **Standard** — pre-approved, low-risk, routine changes (e.g., password resets)
  - **Normal** — requires full CAB review and approval
  - **Emergency** — expedited process for critical issues; documented retroactively
- **[[backoutrollback-plan|Backout/Rollback plan]]** — predefined steps to reverse a change if it causes problems
- **[[maintenance-windows|Maintenance windows]]** — scheduled periods for implementing changes with minimal user impact
- **[[version-control|Version control]]** — tracking changes to configurations, code, and documentation
- **[[configuration-management|Configuration management]]** — maintaining a baseline of system configurations
- **Technical implications of changes**:
  - Allow/deny lists, firewall rules, downtime requirements
  - Service restarts, legacy application compatibility
  - Dependencies between systems

## Exam Tips

> [!tip] Remember
> Every change must have: **documentation, approval, testing, and a rollback plan**. If a scenario describes skipping any of these steps, that is the security concern. The exam loves testing "what went wrong" in a change management failure.

> [!tip] Emergency Changes
> Emergency changes bypass normal approval but still require **retroactive documentation and review**. They are not exempt from the process — just expedited.

## Connections

- Supports [[governance]] by enforcing structured oversight of system modifications
- Prevents unauthorized changes that could undermine [[security-policies]]
- Integrates with [[infrastructure-as-code]] for automated and auditable deployments
- Part of [[compliance]] requirements in frameworks like ITIL, SOC 2, and ISO 27001
- Change failures may trigger [[incident-response]] if they cause security incidents

## Scenario

> See [[case-change-management]] for a practical DevOps scenario applying these concepts.
