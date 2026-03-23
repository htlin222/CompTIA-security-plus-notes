---
title: "False positives"
description: "Legitimate activity that matches IoC patterns — tuning is essential to reduce alert fatigue"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are False Positives?
> It's like a smoke alarm going off because you burned toast, not because there's an actual fire. False positives are when security tools cry wolf over something that's perfectly fine.

## Definition

False positives occur when a security control—such as an IDS, SIEM, or DLP system—incorrectly flags legitimate activity as malicious. In the context of Indicators of Compromise, false positives arise when normal user or system behavior happens to match the pattern of a known IoC. High false positive rates lead to alert fatigue, causing analysts to miss real threats buried in noise.

## Key Details

- **Alert fatigue**: Analysts who see hundreds of false positives daily begin ignoring or quickly closing alerts—a serious operational risk.
- **Tuning**: Adjusting detection rules, thresholds, and whitelists to reduce false positives while maintaining detection capability.
- **False positive rate vs. false negative rate**: Lowering sensitivity reduces false positives but increases false negatives (missed real attacks).
- For DLP systems specifically: tuning is critical because overly broad rules flag normal business processes (sharing sensitive data with authorized third parties).
- Regular review and refinement of detection rules is an ongoing security operations responsibility.

## Connections

- Parent: [[indicators-of-compromise]] — a challenge in operationalizing IoC-based detection
- See also: [[threat-feeds]]
