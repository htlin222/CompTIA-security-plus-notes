---
title: "Risk-based prioritization"
description: "Considering exploit availability, asset criticality, and exposure when deciding remediation order"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Risk-based Prioritization?
> You cannot fix everything at once, so you fix the most dangerous things first. Like patching the hole near the gas stove before fixing the one in the guest room closet.

## Definition

Risk-based prioritization in vulnerability management moves beyond simple CVSS severity scoring to consider multiple contextual factors when determining the order in which vulnerabilities should be remediated. By factoring in exploit availability, asset criticality, internet exposure, and environmental context, organizations focus limited remediation resources on the vulnerabilities that pose the greatest actual risk.

## Key Details

- Factors: CVSS base score + exploit availability (is there a public exploit?) + asset criticality + external exposure + compensating controls
- High CVSS score + public exploit + internet-exposed critical system = immediate, emergency remediation
- High CVSS score + no public exploit + internal-only system = lower urgency
- EPSS (Exploit Prediction Scoring System) predicts the likelihood that a vulnerability will be exploited in the wild
- Vulnerability prioritization platforms (Tenable, Qualys, Rapid7) automate risk-based scoring

## Connections

- Parent: [[vulnerability-management]] — risk-based prioritization is the foundation of an effective vulnerability program
- See also: [[cvss-common-vulnerability-scoring-system]]
