---
title: "Guardrails"
description: "Safety controls in automation to prevent unintended actions (approval gates, rollback capabilities)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Guardrails are safety controls embedded into security automation workflows to prevent automated actions from causing unintended harm to the organization's systems or operations. They establish boundaries within which automation can act freely, while requiring human approval or blocking action entirely for operations that could have significant or irreversible consequences.

## Key Details

- **Approval gates**: require human authorization before high-risk automated actions (e.g., deleting user accounts)
- **Rollback capabilities**: automated actions should be reversible so mistakes can be corrected
- **Scope limitations**: automation should only be able to affect systems within a defined scope
- Rate limiting: preventing runaway automation from taking too many actions too quickly
- Testing automation in staging environments before production deployment

## Connections

- Parent: [[automation-and-scripting]] — guardrails are essential safety controls for any automation implementation
- See also: [[risks]]
