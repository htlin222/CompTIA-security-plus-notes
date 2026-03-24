---
title: "Incident Response"
description: "Structured approach to preparing for, detecting, containing, and recovering from security incidents"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/incident
  - weight/high
aliases:
  - "IR"
---

> [!eli5] ELI5: What is Incident Response?
> Think about a fire drill at school. Before any fire happens, you practice what to do: who calls for help, which exit to use, where to meet outside. Incident response is a plan like that, but for cyberattacks. It spells out what the team should do step by step when something bad happens -- how to spot the problem, stop it from spreading, clean it up, and learn from it so it does not happen again.

## Overview

Incident response (IR) is the organized approach to addressing and managing the aftermath of a security breach or cyberattack. The goal is to handle the situation in a way that limits damage, reduces recovery time and costs, and preserves evidence for potential legal action. A well-defined IR plan is essential for every organization and is heavily tested on the SY0-701 exam.

## Key Concepts

- **[[nist-ir-lifecycle|NIST IR lifecycle]]**: Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity
- **[[preparation|Preparation]]**: Building the IR team, creating playbooks, deploying tools, conducting tabletop exercises
- **[[detection-and-analysis|Detection and analysis]]**: Identifying incidents through alerts, logs, user reports, and threat intelligence
- **[[containment|Containment]]**: Short-term (isolate the system) and long-term (apply temporary fixes while building permanent solutions)
- **[[eradication|Eradication]]**: Removing the threat — deleting malware, closing vulnerabilities, resetting compromised credentials
- **[[recovery|Recovery]]**: Restoring systems to normal operations, monitoring for re-infection
- **[[lessons-learned-post-incident-review|Lessons learned / Post-incident review]]**: Documenting what happened, what worked, what failed, and how to improve
- **[[chain-of-custody|Chain of custody]]**: Maintaining evidence integrity for legal proceedings
- **[[communication-plan|Communication plan]]**: Who to notify (management, legal, law enforcement, customers, regulators)
- **[[tabletop-exercises|Tabletop exercises]]**: Discussion-based simulations that walk through IR scenarios without touching systems

## Exam Tips

> [!tip] Remember
> NIST phases: Prep → Detect → Contain → Eradicate → Recover → Lessons Learned. The exam loves scenario questions asking "what do you do FIRST?" — answer: contain the threat to prevent spread.

- Containment before eradication — you must stop the bleeding before cleaning up
- Lessons learned phase is NOT optional — it drives continuous improvement
- Evidence preservation is critical — image drives before wiping them

## Connections

- Directly supports [[business-continuity]] by minimizing downtime and data loss during incidents
- Relies on [[indicators-of-compromise]] for detection and analysis of potential security events
- [[digital-forensics]] provides the evidence collection and analysis techniques used during IR
- [[soar]] automates containment and eradication steps defined in IR playbooks

## Practice Questions

> [!qbank]- Q-Bank: Incident Response (4 Questions)
>
> **Q1.** A SOC analyst detects ransomware actively encrypting files on a workstation that is connected to a shared network drive containing critical business data. What should the analyst do FIRST?
>
> A. Begin eradicating the malware from the workstation
> B. Isolate the affected workstation from the network to contain the threat
> C. Restore the encrypted files from the latest backup
> D. Conduct a lessons learned meeting with the team
>
> > [!answer]- Show Answer
> > **B. Isolate the affected workstation from the network to contain the threat**
> >
> > [[containment]] must come before eradication — the analyst must stop the ransomware from spreading to the shared drive and other network resources. Option A skips containment, allowing continued encryption of network files during eradication. Option C is a recovery step that should occur after containment and eradication. Option D is a post-incident activity, not an immediate response action.
>
> **Q2.** After successfully containing and eradicating a security breach, the incident response team restores affected systems from clean backups and monitors them for signs of reinfection. Which phase of the NIST IR lifecycle does this represent?
>
> A. Preparation
> B. Detection and Analysis
> C. Recovery
> D. Post-Incident Activity
>
> > [!answer]- Show Answer
> > **C. Recovery**
> >
> > The [[recovery]] phase involves restoring systems to normal operations and monitoring for signs of re-infection to ensure the threat has been fully eliminated. Option A occurs before any incident and involves building the IR capability. Option B involves identifying and understanding the incident. Option D ([[lessons-learned-post-incident-review|lessons learned]]) occurs after recovery and focuses on documenting improvements.
>
> **Q3.** An organization's incident response team conducts a discussion-based exercise where team members walk through a simulated phishing attack scenario, reviewing their roles and response procedures without touching any actual systems. What type of exercise is this?
>
> A. Penetration test
> B. Tabletop exercise
> C. Red team engagement
> D. Vulnerability scan
>
> > [!answer]- Show Answer
> > **B. Tabletop exercise**
> >
> > [[tabletop-exercises]] are discussion-based simulations that walk through incident response scenarios without interacting with live systems, testing team coordination and procedure familiarity. Option A actively exploits vulnerabilities on real systems. Option C simulates real adversary attacks against production infrastructure. Option D is an automated technical assessment, not a team exercise.
>
> **Q4.** During the post-incident review of a data breach, the IR team discovers that the initial containment was delayed by two hours because the on-call analyst could not reach the network team to isolate the affected VLAN. What should the organization improve PRIMARILY based on this finding?
>
> A. Deploy more advanced EDR tools
> B. Update the communication plan with clear escalation paths and emergency contacts
> C. Increase the frequency of vulnerability scans
> D. Implement full disk encryption on all servers
>
> > [!answer]- Show Answer
> > **B. Update the communication plan with clear escalation paths and emergency contacts**
> >
> > The [[communication-plan]] is critical to incident response effectiveness. The delay was caused by a communication breakdown, not a technical control gap. The [[lessons-learned-post-incident-review|lessons learned]] phase exists specifically to identify and address such process failures. Option A addresses detection capability, not communication. Option C addresses vulnerability discovery, not incident response speed. Option D protects data at rest, unrelated to the communication issue.

## Scenario

> See [[case-incident-response]] for a practical DevOps scenario applying these concepts.
