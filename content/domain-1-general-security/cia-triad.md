---
title: "CIA Triad"
description: "The three pillars of information security: Confidentiality, Integrity, and Availability"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/high
aliases:
  - "CIA Triad"
  - "Confidentiality Integrity Availability"
---

> [!eli5] ELI5: What is the CIA Triad?
> The CIA Triad is the three big promises of keeping information safe. Confidentiality means only the right people can see your secret diary. Integrity means nobody can sneak in and change what you wrote. Availability means you can always open your diary when you need it. Every security rule and tool exists to protect at least one of these three things. If any one of them breaks, your information is in trouble.

## Overview

The CIA Triad is the foundational model in information security that defines three core objectives: Confidentiality (preventing unauthorized disclosure), Integrity (preventing unauthorized modification), and Availability (ensuring authorized access when needed). Every security control, policy, and architecture decision can be mapped back to protecting one or more of these three properties.

## Key Concepts

- **[[confidentiality|Confidentiality]]** — protecting data from unauthorized access or disclosure
  - Controls: encryption, access controls, data masking, DLP
  - Threats: eavesdropping, data breaches, shoulder surfing, social engineering
- **[[integrity|Integrity]]** — ensuring data is accurate, complete, and unaltered by unauthorized parties
  - Controls: hashing, digital signatures, checksums, version control
  - Threats: man-in-the-middle attacks, malware, unauthorized modification
- **[[availability|Availability]]** — ensuring systems and data are accessible to authorized users when needed
  - Controls: redundancy, backups, load balancing, failover clusters
  - Threats: DDoS attacks, hardware failure, ransomware, natural disasters
- **[[dad-triad|DAD Triad]]** (opposite) — Disclosure, Alteration, Destruction; represents what attackers aim to achieve
- **[[non-repudiation|Non-repudiation]]** — often considered the fourth pillar; ensures actions cannot be denied after the fact

## Exam Tips

> [!tip] Remember
> **CIA vs. DAD**: Confidentiality opposes Disclosure, Integrity opposes Alteration, Availability opposes Destruction. Scenario questions often describe an attack — identify which CIA element is compromised.

> [!tip] Ransomware and CIA
> Ransomware primarily attacks **Availability** (locks you out of data) and **Confidentiality** (threatens to leak data in double-extortion schemes).

## Connections

- Core framework for all [[security-concepts]] and foundational to every exam domain
- Encryption technologies protect confidentiality (see [[encryption]])
- Hashing algorithms verify integrity (see [[hashing]])
- Redundancy and disaster recovery ensure availability (see [[resilience-and-redundancy]], [[disaster-recovery]])
- [[defense-in-depth]] layers controls to protect all three CIA properties simultaneously

## Scenario

> See [[case-cia-triad]] for a practical DevOps scenario applying these concepts.
