---
title: "Ransomware"
description: "Malware that encrypts victim data and demands payment for the decryption key"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/endpoint
  - weight/high
aliases:
  - "Crypto-Malware"
---

> [!eli5] ELI5: What is Ransomware?
> Picture someone sneaking into your room, putting all your favorite toys and books into a locked safe, and then saying "Pay me $50 or you'll never see them again." That's ransomware. It's a type of bad software that scrambles all your computer files so you can't open them, then demands money to unlock them. Sometimes the attacker also threatens to show your private stuff to everyone if you don't pay. It's one of the scariest computer threats because people can lose everything important to them.

## Overview

Ransomware is a type of malware that encrypts a victim's files or locks system access, then demands a ransom payment (typically in cryptocurrency) in exchange for the decryption key. Modern ransomware operations have evolved into sophisticated criminal enterprises using double and triple extortion tactics. Ransomware is one of the most impactful and heavily tested threat types on the SY0-701 exam.

## Key Concepts

- **[[encryption-based-ransomware|Encryption-based ransomware]]**: Encrypts files using strong cryptographic algorithms; data is unrecoverable without the key
- **[[locker-ransomware|Locker ransomware]]**: Locks the user out of the system entirely without necessarily encrypting files
- **[[double-extortion|Double extortion]]**: Attackers exfiltrate data before encrypting — threaten to publish it if ransom is not paid
- **[[triple-extortion|Triple extortion]]**: Adds DDoS attacks or contacting victims' customers/partners as additional pressure
- **[[ransomware-as-a-service-raas|Ransomware-as-a-Service (RaaS)]]**: Criminal developers provide ransomware tools to affiliates in exchange for a cut of profits
- **[[common-delivery-methods|Common delivery methods]]**: Phishing emails, exploited vulnerabilities (especially RDP), drive-by downloads, supply chain compromise
- **[[lateral-movement|Lateral movement]]**: Ransomware spreads across the network before detonating to maximize impact
- **[[cryptocurrency-payment|Cryptocurrency payment]]**: Bitcoin or Monero used to make payments difficult to trace
- **[[notable-examples|Notable examples]]**: WannaCry (EternalBlue exploit), NotPetya (supply chain), LockBit, BlackCat/ALPHV

## Exam Tips

> [!tip] Remember
> Best defense against ransomware: offline/immutable backups + network segmentation + patching + user training. Never rely solely on paying the ransom — there is no guarantee of decryption, and it funds criminal operations.

- The 3-2-1 backup rule: 3 copies, 2 different media types, 1 offsite (ideally air-gapped or immutable)
- Network segmentation limits blast radius when ransomware detonates
- Know that paying ransom may violate OFAC sanctions if the threat actor is in a sanctioned country

## Connections

- Triggers [[incident-response]] procedures — ransomware events are major security incidents
- Impacts [[business-continuity]] — recovery depends on backup availability and tested restore procedures
- Uses [[encryption]] algorithms against the victim — strong crypto makes recovery without keys virtually impossible
- Delivered through phishing ([[email-security]]) and exploits of [[vulnerability-types]]

## Scenario

> See [[case-ransomware]] for a practical DevOps scenario applying these concepts.
