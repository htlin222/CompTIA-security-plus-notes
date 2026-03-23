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

## Scenario

> See [[case-incident-response]] for a practical DevOps scenario applying these concepts.
