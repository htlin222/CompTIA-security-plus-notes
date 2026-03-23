---
title: "False positives/negatives"
description: "Validating scan results to avoid wasting resources or missing real vulnerabilities"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are False Positives and Negatives?
> A false positive is like your smoke detector going off when you burn toast -- no real fire. A false negative is when the detector stays quiet during an actual fire. Both are problems.

## Definition

In vulnerability management and security monitoring, false positives are alerts or findings that indicate a vulnerability or threat that does not actually exist, while false negatives are real vulnerabilities or threats that are missed and not detected. Managing the balance between false positives and false negatives is a fundamental challenge in security operations.

## Key Details

- **False positive**: scanner reports a vulnerability that doesn't actually exist; wastes analyst time and resources
- **False negative**: real vulnerability is present but not detected; creates hidden risk
- Reducing false positives requires tuning scanner configurations and validating findings manually
- Credentialed scans have fewer false positives because they can verify vulnerability details internally
- All scan findings should be validated before remediation to avoid wasting effort on false positives

## Connections

- Parent: [[vulnerability-management]] — managing false positives/negatives is core to an effective vuln program
- See also: [[credentialed-vs-non-credentialed-scans]]
