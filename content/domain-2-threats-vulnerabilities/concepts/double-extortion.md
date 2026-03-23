---
title: "Double extortion"
description: "Attackers exfiltrate data before encrypting — threaten to publish if ransom is not paid"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Double Extortion?
> Not only does the attacker lock up your files, they also copy your private stuff first and threaten to share it with everyone. Even if you have backups, they can still embarrass you.

## Definition

Double extortion is a ransomware strategy where attackers first exfiltrate sensitive data from the victim's network before encrypting files. They then threaten to publicly release or sell the stolen data on dark web leak sites if the ransom is not paid—in addition to the traditional encryption ransom demand. This eliminates the option of recovering from backups alone, since data has already been stolen.

## Key Details

- Pioneered by the **Maze ransomware group** in 2019—now standard practice for most ransomware operations.
- Victim organizations cannot simply restore from backups to avoid paying—the **data leakage threat** remains.
- Ransomware groups operate **public "shame" or "leak" sites** on the dark web where they post victim names and stolen data.
- Industries with highly sensitive data (healthcare, legal, finance) are prime targets—HIPAA/regulatory violations add pressure.
- Defenses: **DLP** to detect exfiltration, **network segmentation** to limit blast radius, **EDR** to detect data staging.

## Connections

- Parent: [[ransomware]] — an evolution of traditional ransomware tactics
- See also: [[triple-extortion]], [[lateral-movement]]
