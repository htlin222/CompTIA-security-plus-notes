---
title: "Real-time alerting"
description: "Immediate notification when correlation rules or thresholds are triggered"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Real-time Alerting?
> Real-time alerting sends a warning the instant something happens. It is like a doorbell that rings the second someone steps on your porch, not an hour later.

## Definition

Real-time alerting is the SIEM capability that generates immediate notifications to security analysts when correlation rules, threshold conditions, or pattern matches are triggered by incoming log data. Real-time alerts minimize the time between attack activity and analyst awareness, reducing attacker dwell time and limiting the damage from incidents.

## Key Details

- Alerts fire in near-real-time as log data arrives and matches defined conditions
- Alert delivery channels: email, SMS, SIEM dashboard, SOAR platform, ticketing system
- Alert severity tiers (Critical, High, Medium, Low) help analysts prioritize their response queue
- Alert tuning is essential: poorly tuned rules generate excessive false positives, causing alert fatigue
- SOAR platforms can receive SIEM alerts and automatically execute response playbooks without analyst involvement

## Connections

- Parent: [[siem]] — real-time alerting is a core SIEM output capability
- See also: [[correlation-rules]]
