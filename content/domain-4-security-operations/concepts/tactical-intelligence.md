---
title: "Tactical intelligence"
description: "TTPs (tactics, techniques, procedures) used by adversaries — informs detection rules"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Tactical Intelligence?
> Tactical intelligence describes the specific tools and methods attackers are using right now. It is like scouting reports that tell a coach exactly what plays the other team runs.

## Definition

Tactical threat intelligence provides information about the specific tactics, techniques, and procedures (TTPs) used by threat actors to conduct attacks. This type of intelligence is consumed by security analysts, detection engineers, and threat hunters to create detection rules, tune security tools, and identify specific attacker behaviors to hunt for in the environment.

## Key Details

- Describes HOW attackers operate: specific commands used, tools deployed, evasion techniques employed
- Mapped to MITRE ATT&CK framework for structured, actionable analysis
- Used to create SIEM detection rules and EDR behavioral signatures
- More durable than technical IoCs: TTPs change less frequently than IP addresses or file hashes
- Example: "Adversary uses living-off-the-land techniques including PowerShell with encoded commands for initial execution"

## Connections

- Parent: [[threat-intelligence]] — tactical intelligence is one of the three levels of threat intelligence
- See also: [[mitre-attck-framework]]
