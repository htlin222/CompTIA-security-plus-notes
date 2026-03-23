---
title: "Deception Technologies"
description: "Decoy systems and techniques designed to detect, deflect, and study attackers"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/medium
aliases:
  - "Honeypots"
  - "Honeynets"
---

## Overview

Deception technologies are security tools and techniques that use decoy systems, files, and credentials to detect, deflect, and analyze attacker behavior. By creating fake targets that appear legitimate, organizations can identify unauthorized activity early, slow down attackers, and gather intelligence about their tactics, techniques, and procedures (TTPs).

## Key Concepts

- **[[honeypots|Honeypots]]** — decoy systems designed to attract and trap attackers
  - **Low-interaction** — simulates limited services; easy to deploy, less intelligence gathered
  - **High-interaction** — fully functional system; riskier but captures detailed attacker behavior
- **[[honeynets|Honeynets]]** — networks of honeypots simulating an entire environment
- **[[honeyfiles|Honeyfiles]]** — fake files (e.g., "passwords.xlsx") placed on systems to trigger alerts when accessed
- **[[honeytokens|Honeytokens]]** — fake data (credentials, database records, API keys) that alert when used
- **[[dns-sinkholes|DNS sinkholes]]** — redirect malicious domain requests to a controlled server; disrupts botnet communication and detects infected hosts
- **[[fake-telemetry|Fake telemetry]]** — generating false network data to confuse attackers performing reconnaissance
- **[[deception-platforms|Deception platforms]]** — enterprise solutions that automate deployment and management of decoys across the network
- **Benefits**:
  - Early detection of lateral movement and insider threats
  - Low false-positive rate — legitimate users have no reason to access decoys
  - Intelligence gathering on attacker methods
  - Slows attackers by wasting their time on fake targets
- **Risks**:
  - Maintenance overhead; decoys must appear realistic
  - High-interaction honeypots can be co-opted if not properly isolated

## Exam Tips

> [!tip] Remember
> **Honeypot** = decoy system. **Honeynet** = network of honeypots. **Honeyfile** = decoy file. **Honeytoken** = decoy credential/data. **DNS sinkhole** = redirects malicious DNS to controlled IP. Know the distinctions — the exam tests each term specifically.

> [!tip] Key Advantage
> Deception technologies have a very low false-positive rate because legitimate users and processes should never interact with decoy resources. Any interaction is suspicious by definition.

## Connections

- Provides intelligence about [[threat-actors]] and their tactics, techniques, and procedures
- Complements [[ids-ips]] by offering an additional detection mechanism with fewer false positives
- Supports [[threat-intelligence]] and [[threat-hunting]] by gathering data on active adversaries
- Works within a [[defense-in-depth]] strategy as a detective control layer
- DNS sinkholes aid [[network-monitoring]] in identifying compromised internal hosts

## Scenario

> See [[case-deception-technologies]] for a practical DevOps scenario applying these concepts.
