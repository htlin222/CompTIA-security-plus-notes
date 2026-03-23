---
title: "DAD Triad"
description: "Disclosure, Alteration, Destruction — the attacker's counterpart to the CIA Triad"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

The DAD Triad (Disclosure, Alteration, Destruction) represents the three ways an attacker can undermine information security, directly opposing the CIA Triad (Confidentiality, Integrity, Availability). Disclosure attacks compromise confidentiality; Alteration attacks compromise integrity; Destruction attacks compromise availability. Understanding DAD helps frame attacker goals and the controls needed to counter them.

## Key Details

- **Disclosure** ↔ attacks on **Confidentiality**: Eavesdropping, data breaches, unauthorized access to sensitive data.
- **Alteration** ↔ attacks on **Integrity**: Data tampering, unauthorized modification, SQL injection modifying records.
- **Destruction** ↔ attacks on **Availability**: DoS/DDoS attacks, ransomware, hardware destruction, data deletion.
- Framing threats as DAD helps with risk analysis: identify which CIA pillar a threat impacts, then apply appropriate controls.
- A single attack can affect multiple DAD elements (e.g., ransomware = Destruction; double extortion also = Disclosure).

## Connections

- Parent: [[cia-triad]] — the inverse of the CIA Triad
- See also: [[confidentiality]], [[integrity]], [[availability]]
