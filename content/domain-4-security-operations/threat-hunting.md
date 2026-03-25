---
title: "Threat Hunting"
description: "Proactive searching through networks and datasets to detect threats that evade existing security controls"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/incident
  - weight/medium
aliases:
  - "Cyber Threat Hunting"
---

> [!eli5] ELI5: What is Threat Hunting?
> Most alarms wait for a burglar to trip them. But a threat hunter is more like a detective who goes looking for trouble before the alarm even rings. They walk through the building checking closets, looking behind doors, and following suspicious footprints -- not because an alarm went off, but because they have a hunch something might be wrong. If they find anything, they can stop the bad guy before real damage is done.

## Overview

Threat hunting is the proactive, human-driven process of searching through networks, endpoints, and datasets to identify threats that have evaded automated detection systems. Unlike reactive alerting, threat hunting assumes the network may already be compromised and seeks to find evidence of adversary activity. It requires skilled analysts who form hypotheses and test them against available telemetry.

## Key Concepts

- **[[hypothesis-driven-hunting|Hypothesis-driven hunting]]**: Starting with an educated guess about attacker behavior and searching for evidence to confirm or deny it
- **[[intelligence-driven-hunting|Intelligence-driven hunting]]**: Using threat intelligence reports, IoCs, or known TTPs as starting points
- **[[baseline-driven-hunting|Baseline-driven hunting]]**: Identifying deviations from known-good baselines in network traffic, process execution, or user behavior
- **[[mitre-attck-framework|MITRE ATT&CK framework]]**: Knowledge base of adversary tactics, techniques, and procedures (TTPs) used to structure hunts
- **[[data-sources|Data sources]]**: EDR telemetry, SIEM logs, network flow data, DNS logs, authentication logs
- **[[indicators-of-attack-ioa|Indicators of Attack (IoA)]]**: Behavioral indicators that suggest an active attack in progress (more proactive than IoCs)
- **[[advisary-emulation|Advisary emulation]]**: Simulating known threat actor behavior to test detection capabilities
- **[[hunt-maturity-model|Hunt maturity model]]**: Levels from HM0 (initial, relies on automated alerts) to HM4 (leading, creates new detection content)
- **[[theharvester|theHarvester]]**: OSINT tool for gathering emails, subdomains, hosts, and names from public sources
- **[[dnsenum|dnsenum]]**: DNS enumeration tool for discovering DNS records and subdomains
- **[[nessus|Nessus]]**: Commercial vulnerability scanner for identifying security weaknesses
- **[[cuckoo-sandbox|Cuckoo Sandbox]]**: Open-source automated malware analysis system that runs suspicious files in isolated environments

## Exam Tips

> [!tip] Remember
> Threat hunting is PROACTIVE (you go looking), not reactive (waiting for alerts). It requires skilled humans — you cannot fully automate hunting. Think of it as "assume breach and go find it."

- Threat hunting often results in new detection rules being added to the SIEM
- Know the difference: threat hunting (proactive search) vs. incident response (reactive to alerts)
- MITRE ATT&CK is the most common framework referenced for structuring threat hunts

## Connections

- Uses telemetry from [[edr-xdr]] and [[siem]] as primary data sources for investigation
- Discoveries feed into [[threat-intelligence]] to improve organizational knowledge of adversary behavior
- Findings may escalate into [[incident-response]] when active threats are confirmed
- Leverages [[indicators-of-compromise]] as starting points for intelligence-driven hunts

## Practice Questions

> [!qbank]- Q-Bank: Threat Hunting (4 Questions)
>
> **Q1.** A security analyst reads a threat intelligence report about a new APT group targeting organizations in their industry using a specific PowerShell-based attack technique. The analyst decides to search EDR telemetry for evidence of this technique across the environment. What type of threat hunting is this?
>
> A. Baseline-driven hunting
> B. Intelligence-driven hunting
> C. Automated vulnerability scanning
> D. Compliance-driven auditing
>
> > [!answer]- Show Answer
> > **B. Intelligence-driven hunting**
> >
> > [[intelligence-driven-hunting]] uses threat intelligence reports, IoCs, or known TTPs as starting points for proactive searches. The analyst is using a specific threat report to guide their hunt. Option A ([[baseline-driven-hunting]]) looks for deviations from normal behavior without a specific threat in mind. Option C is automated and reactive, not proactive and human-driven. Option D verifies compliance controls, not adversary presence.
>
> **Q2.** A threat hunter notices that a domain controller is making outbound HTTPS connections to an IP address in a country where the organization has no business presence. The SIEM never alerted on this activity because no rule existed for it. This scenario BEST demonstrates why threat hunting is important because:
>
> A. It replaces the need for SIEM correlation rules
> B. It proactively discovers threats that evade automated detection systems
> C. It eliminates false positives from security tools
> D. It automates incident response workflows
>
> > [!answer]- Show Answer
> > **B. It proactively discovers threats that evade automated detection systems**
> >
> > Threat hunting assumes the network may already be compromised and seeks evidence of adversary activity that automated systems missed. This is a core principle of proactive hunting. Option A is incorrect — hunting complements SIEM, it does not replace it. Successful hunts often result in new SIEM rules. Option C relates to tuning, not hunting. Option D describes [[soar]] capabilities, not threat hunting.
>
> **Q3.** A threat hunting team wants to structure their hunts around known adversary behaviors, mapping techniques like "credential dumping" and "lateral movement via SMB" to specific detection opportunities. Which framework is MOST appropriate for organizing these hunts?
>
> A. NIST Cybersecurity Framework
> B. MITRE ATT&CK framework
> C. ISO 27001
> D. PCI-DSS
>
> > [!answer]- Show Answer
> > **B. MITRE ATT&CK framework**
> >
> > The [[mitre-attck-framework|MITRE ATT&CK framework]] is a knowledge base of adversary tactics, techniques, and procedures (TTPs) specifically designed to structure threat detection and hunting activities. Option A provides high-level cybersecurity guidance, not granular adversary technique mapping. Option C is an information security management standard. Option D is a payment card industry compliance standard.
>
> **Q4.** After completing a successful threat hunt that uncovered a compromised service account, the hunting team documents their findings and creates new SIEM detection rules to automatically alert on similar activity in the future. At which level of the hunt maturity model does creating new detection content from hunt results place the organization?
>
> A. HM0 — Initial, relying entirely on automated alerts
> B. HM1 — Minimal, using basic threat intelligence searches
> C. HM4 — Leading, creating new detection content from hunt findings
> D. HM2 — Procedural, following documented hunting procedures
>
> > [!answer]- Show Answer
> > **C. HM4 — Leading, creating new detection content from hunt findings**
> >
> > The [[hunt-maturity-model]] places organizations that create new automated detection content based on hunt results at the highest maturity level (HM4). This closes the loop between proactive hunting and automated detection. Option A describes organizations that only rely on existing automated alerts. Option B involves basic searches using external intelligence. Option D follows documented procedures but does not necessarily create new detection capabilities.

## Scenario

> See [[case-threat-hunting]] for a practical DevOps scenario applying these concepts.
