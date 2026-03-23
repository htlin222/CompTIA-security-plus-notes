---
title: "Indicators of Attack (IoA)"
description: "Proactive behavioral signals suggesting an attack is in progress (more real-time than IoCs)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - IoA
  - IOA
---

## Definition

Indicators of Attack (IoAs) are behavioral signals that suggest an attack is actively occurring, distinct from Indicators of Compromise (IoCs) which typically indicate an attack has already occurred. IoAs focus on attacker behaviors and techniques (TTPs) rather than specific artifacts—enabling detection even when attackers use novel malware or previously unseen tools. IoAs are central to behavioral-based threat detection.

## Key Details

- **IoC vs. IoA**: IoCs are retrospective (evidence of past compromise); IoAs are proactive (signs of ongoing attack).
- Examples of IoAs: **lateral movement** between systems, **privilege escalation attempts**, **unusual process spawning chains**, **credential dumping behavior**.
- IoAs are associated with the **MITRE ATT&CK framework**—a knowledge base of adversary TTPs.
- Detection relies on **behavioral analytics** rather than static signature matching.
- IoAs remain valid even when attackers change their malware—the behavior (e.g., dumping LSASS) stays the same.

## Connections

- Parent: [[indicators-of-compromise]] — IoAs are a proactive extension of IoC-based detection
- See also: [[behavioral-indicators]]
