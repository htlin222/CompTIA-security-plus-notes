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

## Scenario

> See [[case-threat-hunting]] for a practical DevOps scenario applying these concepts.
