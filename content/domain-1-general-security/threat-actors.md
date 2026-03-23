---
title: "Threat Actors"
description: "Categories of adversaries and their motivations, capabilities, and attack methods"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/high
aliases:
  - "Threat Agents"
---

> [!eli5] ELI5: What are Threat Actors?
> Threat actors are the different kinds of "bad guys" in the computer world. Some are like professional burglars backed by a whole country's government. Some are criminals looking to steal money. Some are angry employees who already have the keys. Others are just bored kids trying to show off. Knowing which type you're dealing with helps you figure out what they're after and how to defend against them, because each group has different skills and goals.

## Overview

Threat actors are individuals or groups that pose a risk to an organization's security. Understanding their motivations, capabilities, sophistication levels, and resources is essential for effective risk assessment and building appropriate defenses. The SY0-701 exam tests the ability to distinguish between different actor types and predict their likely tactics.

## Key Concepts

- **[[nation-state-actors|Nation-state actors]]** (APT — Advanced Persistent Threat)
  - Highest sophistication and resources; government-sponsored
  - Motivations: espionage, sabotage, political influence
  - Long dwell times; use zero-day exploits and custom malware
- **Organized crime**
  - Financially motivated; well-funded and structured
  - Ransomware, banking trojans, identity theft, fraud
- **Hacktivists**
  - Ideologically or politically motivated
  - Website defacement, DDoS, data leaks to embarrass targets
- **Insider threats**
  - Current or former employees, contractors, partners
  - May be malicious (intentional) or negligent (unintentional)
  - Hardest to detect; already have legitimate access
- **Script kiddies / unskilled attackers**
  - Low sophistication; use pre-built tools and exploit kits
  - Opportunistic rather than targeted
- **Shadow IT**
  - Employees using unauthorized technology; creates unmanaged risk
- **Attributes of threat actors**:
  - **Internal vs. External** — insider or outsider to the organization
  - **Level of sophistication** — ranges from script kiddie to APT
  - **Resources/Funding** — determines tools, persistence, and capabilities
  - **Intent/Motivation** — financial gain, espionage, disruption, ideology, revenge
- **Attack surface** — the totality of points where an attacker can try to enter (see [[attack-vectors]])

## Exam Tips

> [!tip] Remember
> **Motivation mapping**: Nation-state = espionage/sabotage, Organized crime = money, Hacktivists = ideology, Insiders = revenge/negligence, Script kiddies = curiosity/notoriety.

> [!tip] Insider Threat
> Insider threats are the most dangerous because they bypass perimeter defenses. The exam often presents scenarios where an employee is the threat — look for signs of excessive access or unusual behavior.

## Connections

- Threat actors exploit [[attack-vectors]] to reach their targets
- Social engineering by threat actors is detailed in [[social-engineering]]
- Risk from threat actors is assessed and managed through [[risk-management]] and [[risk-assessment]]
- Defending against threat actors requires understanding their TTPs via [[threat-intelligence]]
- Insider threats are mitigated through [[security-awareness-training]] and [[privileged-access-management]]

## Scenario

> See [[case-threat-actors]] for a practical DevOps scenario applying these concepts.
