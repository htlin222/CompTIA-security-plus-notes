---
title: "Compensating controls"
description: "Alternative measures when the primary control cannot be implemented"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Compensating controls are alternative security measures put in place when a primary or preferred control cannot be implemented due to technical, financial, or operational constraints. They are designed to reduce risk to an acceptable level in the absence of the ideal control. Compensating controls are recognized in frameworks like PCI DSS and are a common topic in risk management and compliance scenarios.

## Key Details

- Common when **legacy systems** cannot be patched—enhanced monitoring, network isolation, or WAF rules compensate.
- Must be **documented** and justified, especially in compliance environments (PCI DSS, HIPAA audits).
- Examples: if MFA can't be deployed on a system, **IP allowlisting** and **enhanced logging** may compensate.
- Compensating controls are **temporary** when possible—they should be replaced with the proper control when feasible.
- Risk acceptance documentation accompanies compensating controls to acknowledge residual risk.

## Connections

- Parent: [[mitigation-techniques]] — an alternative approach to risk reduction
- See also: [[patching]], [[configuration-management]]
