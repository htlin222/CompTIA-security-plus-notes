---
title: "Account indicators"
description: "Multiple failed logins, privilege escalation attempts, account lockouts, new admin accounts"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Account Indicators?
> If someone tried your locker combination wrong five times in a row, that would be a clue something fishy is going on. Account indicators are those kinds of warning signs for computer accounts.

## Definition

Account indicators are signs of compromise or malicious activity observed in user account behavior and configuration. They include anomalous authentication patterns (repeated failed logins), unexpected privilege changes, account lockouts, and the appearance of new unauthorized administrator accounts. Monitoring these indicators is essential for detecting credential attacks, insider threats, and post-exploitation activity.

## Key Details

- **Multiple failed logins** may indicate a brute-force or password spraying attack in progress.
- **Privilege escalation attempts** signal that an attacker or insider is trying to gain higher access.
- **Account lockouts** triggered across many accounts simultaneously suggest a spraying campaign.
- **New admin accounts** created without a ticket or approval process are a major red flag for compromised systems.
- SIEM correlation rules should alert on combinations of these indicators to detect attacks early.

## Connections

- Parent: [[indicators-of-compromise]] — a category of IoC focused on account behavior
- See also: [[behavioral-indicators]]
