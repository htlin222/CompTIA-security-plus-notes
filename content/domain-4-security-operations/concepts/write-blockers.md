---
title: "Write blockers"
description: "hardware or software devices that prevent any writes to digital evidence media, preserving forensic integrity"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Write blockers are hardware devices or software tools used in digital forensics to prevent any write operations to storage media being examined, ensuring that the original evidence is not modified during acquisition or analysis. Hardware write blockers sit between the evidence drive and the forensic workstation, intercepting and blocking all write commands at the hardware level. Maintaining write protection is essential for evidence admissibility and chain of custody.

## Key Details

- Hardware write blockers are preferred over software blockers for forensic validity and court admissibility
- Prevents accidental modification of evidence during disk imaging or live examination
- Without a write blocker, mounting a drive can alter timestamps, modify metadata, or trigger OS auto-run behavior
- After acquisition with a write blocker, hash verification (MD5/SHA-256) confirms image integrity
- Common hardware write blockers: Tableau (Guidance Software), UltraBlock, CRU WiebeTech

## Connections

- Parent: [[digital-forensics]] — write blockers are a fundamental tool ensuring the integrity of forensic evidence
- See also: [[disk-imaging]], [[hash-verification]], [[chain-of-custody]], [[order-of-volatility]]
