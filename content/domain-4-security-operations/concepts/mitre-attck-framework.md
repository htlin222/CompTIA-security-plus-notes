---
title: "MITRE ATT&CK framework"
description: "Knowledge base of adversary tactics, techniques, and procedures (TTPs) used to structure hunts"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a globally accessible knowledge base of adversary tactics, techniques, and sub-techniques based on real-world observations of cyberattacks. It provides a structured taxonomy of attacker behavior organized by tactics (the "why") and techniques (the "how"), enabling security teams to understand, detect, and defend against specific attacker behaviors.

## Key Details

- Organized into matrices: Enterprise ATT&CK, Mobile ATT&CK, ICS ATT&CK
- 14 tactic categories: Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact
- Each technique includes detection guidance, mitigation recommendations, and known threat actor usage
- Used for threat hunting, detection engineering, red team planning, and security gap assessment
- ATT&CK Navigator allows organizations to map their defensive coverage visually

## Connections

- Parent: [[threat-hunting]] — ATT&CK provides the TTP framework for structured threat hunting
- See also: [[advisary-emulation]]
