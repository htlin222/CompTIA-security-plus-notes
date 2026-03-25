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

> [!eli5] ELI5: What is Penetration Testing?
> Have you ever asked a friend to try to sneak into your blanket fort to see if they could find a way in? Penetration testing is exactly that, but for computer systems. A company hires friendly hackers and gives them permission to try to break in. When they find a weak spot, they write a report so the company can fix it before a real bad guy finds the same hole.

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
- **[[wardriving|Wardriving]]**: Scanning for wireless networks from a moving vehicle using a laptop and antenna
- **[[warflying|Warflying]]**: Scanning for wireless networks using a drone for broader coverage

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

## Practice Questions

> [!qbank]- Q-Bank: Penetration Testing (4 Questions)
>
> **Q1.** A company hires an external security firm to test its defenses. The testers are given employee-level network credentials and a network diagram but no source code access. Which type of penetration test is this?
>
> A. Black box
> B. White box
> C. Gray box
> D. Red team engagement
>
> > [!answer]- Show Answer
> > **C. Gray box**
> >
> > [[testing-types|Gray box]] testing provides the tester with partial knowledge — some credentials and documentation but not full transparency into all systems and code. Option A (black box) provides no prior knowledge at all. Option B (white box) provides full access including source code, architecture diagrams, and credentials. Option D is an extended adversary simulation, not a defined knowledge-level test type.
>
> **Q2.** Before beginning a penetration test, the testing team and the client sign a document specifying which systems can be tested, the testing window, prohibited techniques, and emergency contact procedures. What is this document called?
>
> A. Service Level Agreement (SLA)
> B. Non-Disclosure Agreement (NDA)
> C. Rules of Engagement (ROE)
> D. Acceptable Use Policy (AUP)
>
> > [!answer]- Show Answer
> > **C. Rules of Engagement (ROE)**
> >
> > The [[rules-of-engagement-roe|Rules of Engagement]] is the legal document that defines the scope, boundaries, timing, allowed techniques, and escalation procedures for a penetration test. Option A defines service delivery expectations, not testing parameters. Option B protects confidential information but does not define testing scope. Option D governs general user behavior on systems, not penetration testing activities.
>
> **Q3.** During a penetration test, an ethical hacker compromises a low-privilege user workstation and then uses that machine's network access to reach and exploit an internal database server that was not directly accessible from outside the network. What technique does this describe?
>
> A. Social engineering
> B. Pivoting
> C. Vulnerability scanning
> D. Port mirroring
>
> > [!answer]- Show Answer
> > **B. Pivoting**
> >
> > [[pivoting]] is the technique of using a compromised system as a launchpad to access and attack other systems in the internal network that are not directly reachable from the attacker's initial position. Option A manipulates people, not network paths. Option C identifies vulnerabilities but does not involve using one system to reach another. Option D copies network traffic for monitoring, unrelated to attack progression.
>
> **Q4.** An organization runs both quarterly penetration tests and a year-round bug bounty program. What is the PRIMARY advantage of the bug bounty program over traditional penetration testing?
>
> A. Bug bounties are always less expensive than penetration tests
> B. Bug bounties provide continuous testing by a diverse pool of researchers with varied skill sets
> C. Bug bounty researchers have better tools than professional penetration testers
> D. Bug bounties eliminate the need for rules of engagement
>
> > [!answer]- Show Answer
> > **B. Bug bounties provide continuous testing by a diverse pool of researchers with varied skill sets**
> >
> > [[bug-bounty-programs]] leverage crowdsourced, ongoing testing from researchers with diverse backgrounds and techniques, providing broader coverage than time-boxed pen tests. Option A is not always true — bounty payouts can exceed pen test costs. Option C is incorrect — tools are generally similar. Option D is wrong — bug bounty programs still require scope definitions and legal agreements.

## Scenario

> See [[case-penetration-testing]] for a practical DevOps scenario applying these concepts.
