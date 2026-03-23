---
title: "NTP synchronization"
description: "All systems must use the same time source — accurate timestamps are critical for event correlation"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is NTP Synchronization?
> NTP makes sure every computer's clock shows the same time. When investigating a problem, matching timestamps is like making sure all the witnesses agree on when things happened.

## Definition

NTP (Network Time Protocol) synchronization ensures that all systems across an organization use the same accurate time source, keeping their clocks synchronized. Accurate and consistent timestamps are absolutely critical for security operations — without synchronized clocks, correlating events from different systems becomes unreliable, and forensic timelines may be inaccurate.

## Key Details

- NTP synchronizes clocks to within milliseconds across an organization
- All systems should be configured to use trusted NTP servers (organization's internal NTP servers synced to internet time sources)
- Clock skew between systems complicates SIEM correlation — events may appear out of order
- Kerberos authentication requires clocks synchronized within 5 minutes — large skew breaks authentication
- Time manipulation (clock skew attacks) can be used to obfuscate forensic timelines

## Connections

- Parent: [[log-management]] — NTP synchronization is prerequisite to meaningful log correlation
- See also: [[centralized-logging]]
