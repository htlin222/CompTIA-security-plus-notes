---
title: "Scan scheduling"
description: "Regular scans (weekly, monthly) plus ad-hoc scans after major changes"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Scan Scheduling?
> Scan scheduling decides when and how often to check systems for weaknesses. Like scheduling regular dentist checkups instead of only going when your tooth hurts.

## Definition

Scan scheduling in vulnerability management defines the frequency and timing of automated vulnerability scans across the organization's systems. A well-designed scanning schedule ensures continuous visibility into the vulnerability posture while managing the performance impact of scanning on production systems.

## Key Details

- **Regular scheduled scans**: weekly or monthly scans of all systems provide baseline vulnerability tracking
- **Ad-hoc scans**: triggered after major changes (new system deployment, patch rollout, architecture changes)
- **Emergency scans**: triggered in response to newly disclosed critical vulnerabilities (zero-days)
- Scan timing should minimize impact on production: schedule during low-traffic periods
- Credentialed scans should be run regularly for depth; external-view scans for perimeter visibility
- Compliance frameworks often specify minimum scan frequencies (PCI DSS: quarterly external scans)

## Connections

- Parent: [[vulnerability-management]] — scan scheduling ensures continuous and timely vulnerability assessment
- See also: [[vulnerability-scanning]]
