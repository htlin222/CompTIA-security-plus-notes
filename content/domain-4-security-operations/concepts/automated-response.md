---
title: "Automated response"
description: "Predefined playbooks can kill processes, quarantine files, or block IPs without human intervention"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Automated response is a capability of EDR/XDR and SOAR platforms that allows predefined response actions to execute automatically when specific threat conditions are detected, without requiring human approval. These actions can include terminating malicious processes, quarantining infected files, isolating endpoints from the network, or blocking IP addresses at the firewall — all in real time to minimize attacker dwell time.

## Key Details

- Actions typically include: kill process, quarantine file, isolate endpoint, block IP, disable user account
- Reduces Mean Time to Respond (MTTR) by eliminating human-in-the-loop delays
- Must be carefully tuned to avoid false-positive actions that disrupt legitimate operations
- Playbooks define the conditions and sequence of automated actions
- High-confidence detections are automated; lower-confidence events may require analyst approval

## Connections

- Parent: [[edr-xdr]] — automated response is a key capability of EDR/XDR platforms
- See also: [[playbooksrunbooks]]
