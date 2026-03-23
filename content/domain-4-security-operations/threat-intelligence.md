---
title: "Threat Intelligence"
description: "Evidence-based knowledge about existing or emerging threats used to inform security decisions"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/incident
  - weight/medium
aliases:
  - "CTI"
  - "Cyber Threat Intelligence"
---

> [!eli5] ELI5: What is Threat Intelligence?
> It is like getting a heads-up from your neighbor that someone has been trying doorknobs on your street. Threat intelligence is information about what bad guys are doing, what tools they use, and who they are targeting. When security teams get this information early, they can lock the right doors before the bad guys even show up. The better your information, the better you can prepare.

## Overview

Threat intelligence is the collection, processing, and analysis of data about current and potential cyber threats to help organizations make informed security decisions. It transforms raw data into actionable intelligence that can be used to prevent, detect, and respond to attacks. Threat intelligence operates at strategic, operational, tactical, and technical levels.

## Key Concepts

- **[[strategic-intelligence|Strategic intelligence]]**: High-level trends and risks for executive decision-making (e.g., nation-state targeting your industry)
- **[[operational-intelligence|Operational intelligence]]**: Details about specific campaigns or threat actor groups to inform security teams
- **[[tactical-intelligence|Tactical intelligence]]**: TTPs (tactics, techniques, procedures) used by adversaries — informs detection rules
- **[[technical-intelligence|Technical intelligence]]**: Specific IoCs — IP addresses, file hashes, domain names — fed into security tools
- **[[threat-feeds|Threat feeds]]**: Automated streams of IoCs from commercial, open-source, or government sources (STIX/TAXII format)
- **[[stix-structured-threat-information-expression|STIX (Structured Threat Information eXpression)]]**: Standardized language for describing cyber threat information
- **[[taxii-trusted-automated-exchange-of-intelligence-information|TAXII (Trusted Automated eXchange of Intelligence Information)]]**: Protocol for exchanging STIX data
- **[[information-sharing-and-analysis-centers-isacs|Information Sharing and Analysis Centers (ISACs)]]**: Industry-specific organizations for sharing threat intelligence
- **[[threat-actor-profiling|Threat actor profiling]]**: Understanding adversary motivation, capability, and intent
- **[[confidence-levels|Confidence levels]]**: Rating how reliable and accurate a piece of intelligence is

## Exam Tips

> [!tip] Remember
> Intelligence levels: Strategic (WHY/WHO - executives) → Operational (WHAT campaigns) → Tactical (HOW - TTPs) → Technical (specific IoCs - machines). STIX = format, TAXII = transport.

- Not all threat intel is equally reliable — always assess source credibility and confidence
- Open-source threat intelligence (OSINT) is free but requires more validation
- ISACs enable industry peers to share threat data — know they exist and their purpose

## Connections

- Provides context that enriches [[siem]] alerts and correlation rules
- Supplies [[indicators-of-compromise]] used by security tools for automated detection
- Informs [[threat-hunting]] hypotheses about where and how to look for adversaries
- Intelligence about threat actors overlaps with understanding [[threat-actors]] motivations and capabilities

## Scenario

> See [[case-threat-intelligence]] for a practical DevOps scenario applying these concepts.
