---
title: "Behavioral indicators"
description: "Unusual login times, impossible travel, lateral movement patterns suggesting compromise"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Behavioral indicators of compromise are anomalies in user or system behavior that suggest account compromise or insider threat activity. Unlike file-based or network IoCs, behavioral indicators focus on what a user or system is doing rather than what artifacts they leave. They are a key component of User and Entity Behavior Analytics (UEBA) and are particularly useful for detecting credential-based attacks where the attacker uses legitimate credentials.

## Key Details

- **Impossible travel**: Login from New York at 8 AM and London at 9 AM—physically impossible without credential sharing.
- **Unusual login times**: An employee logging in at 3 AM when they normally work 9–5.
- **Lateral movement patterns**: A user account accessing systems it has never touched before.
- **Data hoarding**: Bulk downloading or copying files to external destinations—a pre-exfiltration indicator.
- SIEM/UEBA platforms establish **behavioral baselines** and alert when deviations exceed a threshold.

## Connections

- Parent: [[indicators-of-compromise]] — a category of IoC based on behavior patterns
- See also: [[account-indicators]]
