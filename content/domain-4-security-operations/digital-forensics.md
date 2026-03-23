---
title: "Digital Forensics"
description: "Collection, preservation, and analysis of digital evidence following security incidents or legal matters"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/incident
  - weight/medium
aliases:
  - "Computer Forensics"
---

## Overview

Digital forensics is the process of identifying, preserving, collecting, analyzing, and presenting digital evidence in a manner that is legally admissible. It plays a critical role during and after security incidents to determine what happened, how it happened, and who was responsible. Forensic principles ensure evidence integrity so findings can support legal proceedings or internal investigations.

## Key Concepts

- **[[order-of-volatility|Order of volatility]]**: Collect the most volatile evidence first — CPU registers → RAM → swap → disk → logs → network → archival media
- **[[chain-of-custody|Chain of custody]]**: Documented record of who handled the evidence, when, and what was done — breaks invalidate evidence
- **[[disk-imaging|Disk imaging]]**: Creating a bit-for-bit copy of storage media for analysis without altering the original
- **[[write-blockers|Write blockers]]**: Hardware or software tools that prevent accidental modification of evidence during acquisition
- **[[hash-verification|Hash verification]]**: Using MD5/SHA-256 hashes to prove the forensic copy is identical to the original
- **[[legal-hold|Legal hold]]**: Directive to preserve all relevant data when litigation is anticipated
- **[[timeline-analysis|Timeline analysis]]**: Reconstructing the sequence of events using file timestamps, logs, and artifacts
- **[[live-forensics-vs-dead-forensics|Live forensics vs. dead forensics]]**: Live = analyzing a running system (captures volatile data); dead = analyzing powered-off media
- **[[e-discovery|E-discovery]]**: Legal process of identifying and collecting electronically stored information (ESI) for litigation
- **[[anti-forensics|Anti-forensics]]**: Techniques attackers use to hinder forensic analysis (encryption, log wiping, timestomping)

## Exam Tips

> [!tip] Remember
> Order of volatility (most to least): Registers → Cache → RAM → Disk → Remote logs → Archive. ALWAYS image first, analyze the copy. Never work on original evidence.

- If a system is ON, capture RAM before powering off — you lose volatile data otherwise
- Chain of custody must be maintained at ALL times; one gap can invalidate all evidence
- Know the difference between legal hold (preserve data) and e-discovery (produce data)

## Connections

- Core skill used during [[incident-response]] to determine scope and attribution of attacks
- [[log-management]] provides crucial evidence sources for forensic timeline reconstruction
- Evidence may reveal [[indicators-of-compromise]] that inform broader organizational defense
- Findings feed into [[threat-intelligence]] to improve detection of similar future attacks

## Scenario

> See [[case-digital-forensics]] for a practical DevOps scenario applying these concepts.
