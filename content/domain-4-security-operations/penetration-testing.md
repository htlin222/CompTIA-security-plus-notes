---
title: "Penetration Testing"
description: "Authorized simulated attack against systems to evaluate security controls and identify exploitable weaknesses"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/risk
  - weight/high
aliases:
  - "Pen Test"
  - "Pentest"
---

## Overview

Penetration testing is an authorized, simulated cyberattack performed to evaluate the security of systems, networks, and applications by attempting to exploit vulnerabilities. Unlike vulnerability scanning, pen testing actively exploits weaknesses to demonstrate real-world impact. Results inform remediation priorities and validate the effectiveness of existing security controls.

## Key Concepts

- **[[testing-types|Testing types]]**: Black box (no prior knowledge), white box (full knowledge), gray box (partial knowledge)
- **[[phases|Phases]]**: Planning/scoping → Reconnaissance → Scanning → Exploitation → Post-exploitation → Reporting
- **[[rules-of-engagement-roe|Rules of engagement (ROE)]]**: Legal document defining scope, timing, allowed techniques, and emergency contacts
- **[[reconnaissance|Reconnaissance]]**: Passive (OSINT, DNS lookups) and active (port scanning, service enumeration) information gathering
- **[[exploitation|Exploitation]]**: Attempting to gain unauthorized access using discovered vulnerabilities
- **[[lateral-movement|Lateral movement]]**: Moving from a compromised system to other systems within the network
- **[[privilege-escalation|Privilege escalation]]**: Elevating access from a normal user to administrator or root
- **[[pivoting|Pivoting]]**: Using a compromised system as a launchpad to attack internal networks
- **[[bug-bounty-programs|Bug bounty programs]]**: Crowdsourced testing where external researchers report vulnerabilities for rewards
- **[[red-team-vs-pen-test|Red team vs. pen test]]**: Red teams simulate real adversaries over extended periods; pen tests are time-boxed technical assessments

## Exam Tips

> [!tip] Remember
> Black box = attacker view (unknown environment). White box = full transparency (known environment). Gray box = partial info (partially known). Always get written authorization before testing.

- Pen testing without authorization = illegal, regardless of intent
- Know the difference: vulnerability scan (find weaknesses) vs. pen test (exploit weaknesses)
- Red team = offensive, Blue team = defensive, Purple team = collaborative improvement

## Connections

- Validates findings from [[vulnerability-management]] by proving exploitability
- Findings feed into [[incident-response]] planning by revealing likely attack paths
- May uncover [[application-attacks]] such as SQL injection and XSS in web applications
- Results inform [[hardening]] priorities for systems and network infrastructure

## Scenario

> See [[case-penetration-testing]] for a practical DevOps scenario applying these concepts.
