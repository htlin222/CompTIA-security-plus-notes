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

## Practice Questions

> [!qbank]- Q-Bank: Threat Intelligence (4 Questions)
>
> **Q1.** A CISO needs to brief the board of directors on emerging cyber risks targeting their financial services industry, including which nation-state actors are most active and what their motivations are. Which level of threat intelligence is MOST appropriate for this audience?
>
> A. Technical intelligence
> B. Tactical intelligence
> C. Operational intelligence
> D. Strategic intelligence
>
> > [!answer]- Show Answer
> > **D. Strategic intelligence**
> >
> > [[strategic-intelligence]] provides high-level trends and risk assessments designed for executive decision-making, covering who is attacking, why, and what industries are targeted. Option A ([[technical-intelligence]]) provides specific IoCs like IP addresses and hashes — too granular for executives. Option B ([[tactical-intelligence]]) details adversary TTPs for security teams. Option C ([[operational-intelligence]]) describes specific campaigns for operational defenders.
>
> **Q2.** A security team receives a threat feed containing IP addresses, file hashes, and domain names associated with a known malware campaign. They want to automatically block these indicators across their firewalls and EDR platforms. What standard format is this threat data MOST likely shared in?
>
> A. CSV spreadsheet
> B. STIX/TAXII
> C. PDF report
> D. Syslog format
>
> > [!answer]- Show Answer
> > **B. STIX/TAXII**
> >
> > [[stix-structured-threat-information-expression|STIX]] is the standardized language for describing threat information, and [[taxii-trusted-automated-exchange-of-intelligence-information|TAXII]] is the protocol for exchanging it — together they enable automated ingestion of threat data into security tools. Option A is a generic format without standardized threat intelligence structure. Option C is human-readable but not machine-parseable for automated blocking. Option D is for log transmission, not structured threat intelligence.
>
> **Q3.** A security analyst receives threat intelligence from multiple sources: a commercial feed, an open-source OSINT feed, and an industry ISAC. One source reports a suspicious IP as malicious while another reports it as benign. How should the analyst handle this conflicting information?
>
> A. Always trust the commercial feed since it is paid
> B. Assess the confidence level and source credibility of each report before acting
> C. Block the IP immediately since any report of malicious activity is sufficient
> D. Ignore all threat intelligence feeds and rely solely on internal detection
>
> > [!answer]- Show Answer
> > **B. Assess the confidence level and source credibility of each report before acting**
> >
> > [[confidence-levels]] and source credibility assessment are essential when consuming threat intelligence. Not all sources are equally reliable, and analysts must evaluate the quality and context of each report. Option A assumes paid equals accurate, which is not always true. Option C could lead to blocking legitimate traffic based on unreliable data. Option D abandons the value of external threat intelligence entirely.
>
> **Q4.** A healthcare organization wants to receive threat intelligence specifically about cyber threats targeting hospitals and medical devices. Which type of organization would BEST provide this industry-specific intelligence?
>
> A. A general-purpose antivirus vendor
> B. A Health-sector Information Sharing and Analysis Center (Health-ISAC)
> C. The organization's internal help desk
> D. A cloud service provider's status page
>
> > [!answer]- Show Answer
> > **B. A Health-sector Information Sharing and Analysis Center (Health-ISAC)**
> >
> > [[information-sharing-and-analysis-centers-isacs|ISACs]] are industry-specific organizations that facilitate sharing of threat intelligence among peer organizations within the same sector. Health-ISAC focuses specifically on healthcare threats. Option A provides general threat intelligence, not healthcare-specific. Option C handles internal support issues, not external threat intelligence. Option D provides service availability information, not threat intelligence.

## Scenario

> See [[case-threat-intelligence]] for a practical DevOps scenario applying these concepts.
