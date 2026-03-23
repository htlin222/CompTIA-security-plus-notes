---
title: "Order of volatility"
description: "Collect the most volatile evidence first — CPU registers → RAM → swap → disk → logs → network → archival media"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Order of Volatility?
> Some clues disappear faster than others. Order of volatility says grab the ones that vanish quickest first -- like catching a snowflake before it melts, then picking up the rock later.

## Definition

The order of volatility is a forensic principle that dictates evidence should be collected starting from the most volatile (easily lost) data and progressing to the least volatile. This ensures that transient evidence that would be lost upon system shutdown or power loss is captured first, while more stable evidence is collected later.

## Key Details

- Most volatile to least volatile: CPU registers/cache → RAM → swap space/page file → disk (NVRAM/SSD/HDD) → remote logging data → archival media
- RAM contains running processes, decrypted data, encryption keys, and network connections — lost on shutdown
- Network connections visible via netstat show current attacker communication — lost quickly
- Disk data is preserved through shutdown; archival media is the most persistent
- Always document the order in which evidence was collected for chain of custody purposes

## Connections

- Parent: [[digital-forensics]] — order of volatility is a fundamental forensic evidence collection principle
- See also: [[live-forensics-vs-dead-forensics]]
