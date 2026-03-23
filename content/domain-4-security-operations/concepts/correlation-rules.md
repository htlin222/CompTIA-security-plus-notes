---
title: "Correlation rules"
description: "Logic that identifies patterns across multiple events that indicate an attack"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Correlation rules are logic-based detection rules in SIEM platforms that analyze multiple events across time, systems, and users to identify patterns that indicate a potential attack. Rather than alerting on individual events (which may be benign), correlation rules connect sequences of related events that together suggest malicious activity, significantly reducing false positives compared to single-event alerts.

## Key Details

- Example: 5 failed logins + 1 successful login from a new IP within 1 minute = brute force alert
- Rules can correlate across multiple data sources: authentication logs, network logs, endpoint logs
- Require careful tuning to balance detection rate against false positive rate
- SIEM vendors provide default rule sets; organizations customize for their environment
- Correlation rules are often mapped to MITRE ATT&CK techniques for threat-informed defense

## Connections

- Parent: [[siem]] — correlation rules are the core detection mechanism of SIEM platforms
- See also: [[real-time-alerting]]
