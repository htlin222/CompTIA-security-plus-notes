---
title: "Tuning"
description: "adjusting sensitivity and rules to reduce false positives without increasing false negatives"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Tuning?
> It's like adjusting the volume on a smoke detector. Too sensitive, and it goes off every time you make toast. Not sensitive enough, and it might miss a real fire. Tuning means finding the right balance so your security alerts catch real threats without crying wolf.

## Definition

IDS/IPS tuning is the ongoing process of adjusting detection sensitivity, rule thresholds, and exception lists to optimize the balance between false positives (legitimate traffic incorrectly flagged as malicious) and false negatives (actual attacks that are missed). A poorly tuned IDS/IPS will either overwhelm analysts with false alerts or miss real attacks.

## Key Details

- High sensitivity: low threshold for alerting → fewer false negatives, more false positives (alert fatigue)
- Low sensitivity: high threshold → fewer false positives, more false negatives (missed attacks)
- Tuning process: review false positives, add exceptions for known-good traffic, adjust rule thresholds
- Baselines of normal traffic patterns guide tuning decisions
- Signature updates from the vendor may introduce new false positives — tuning is an ongoing process, not a one-time activity

## Connections

- Parent: [[ids-ips]] — tuning is essential for effective IDS/IPS operation
- See also: [[inline-vs-passive-deployment]]
