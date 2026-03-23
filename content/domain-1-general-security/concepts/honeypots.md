---
title: "Honeypots"
description: "Decoy systems designed to attract and trap attackers for detection and analysis"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Honeypots are decoy computer systems configured to simulate production servers or services, placed within or alongside a real network to attract and observe attackers. Any interaction with a honeypot is inherently suspicious—legitimate users have no reason to access it. Honeypots serve two purposes: detection (any access triggers an alert) and intelligence gathering (capturing attacker TTPs for analysis).

## Key Details

- **Low-interaction honeypots**: Simulate only specific services (open ports); easier to deploy, lower risk, less intelligence gathered (e.g., Honeyd, Kippo).
- **High-interaction honeypots**: Full operating systems and applications; richer intelligence but higher deployment complexity and risk.
- Any connection to a honeypot is a **high-fidelity indicator**—near-zero false positive rate.
- Must be isolated carefully—a compromised high-interaction honeypot could be used as an attack pivot.
- Valuable data collected: malware samples, exploitation techniques, attacker behavior patterns, C2 infrastructure.

## Connections

- Parent: [[deception-technologies]] — the foundational deception technology
- See also: [[honeynets]], [[honeyfiles]]
