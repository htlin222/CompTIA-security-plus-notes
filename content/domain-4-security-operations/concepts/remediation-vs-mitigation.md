---
title: "Remediation vs. mitigation"
description: "Remediation fixes the vulnerability; mitigation reduces the risk without fully eliminating it"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

In vulnerability management, remediation completely eliminates a vulnerability by fixing the root cause (typically by applying a patch or reconfiguring the system), while mitigation reduces the likelihood of exploitation or the impact of a successful attack without fully eliminating the vulnerability. Organizations use mitigation when full remediation is not immediately possible.

## Key Details

- **Remediation**: applying the vendor patch, removing the vulnerable software, replacing the affected component
- **Mitigation**: disabling the affected feature, adding compensating controls (WAF rules, network restrictions), reducing exposure
- **Compensating controls**: alternative security measures that reduce risk when direct remediation is not feasible
- **Risk acceptance**: formally documenting the decision not to remediate and accepting the residual risk
- Mitigation is temporary — remediation should be planned and implemented as soon as possible

## Connections

- Parent: [[vulnerability-management]] — understanding remediation vs. mitigation options is core to vulnerability management
- See also: [[patch-management]]
