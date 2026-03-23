---
title: "Security Orchestration, Automation, and Response"
description: "Platform that automates security operations workflows and coordinates incident response across tools"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/incident
  - weight/medium
aliases:
  - "SOAR"
---

## Overview

Security Orchestration, Automation, and Response (SOAR) platforms integrate with security tools to automate repetitive tasks, orchestrate workflows across multiple systems, and streamline incident response. SOAR reduces mean time to respond (MTTR) by executing predefined playbooks that would otherwise require manual analyst intervention. It complements SIEM by adding the response layer.

## Key Concepts

- **[[orchestration|Orchestration]]**: Connecting and coordinating multiple security tools (SIEM, firewalls, EDR, ticketing) through APIs
- **[[automation|Automation]]**: Executing repetitive tasks without human intervention — enriching alerts, blocking IPs, disabling accounts
- **[[playbooksrunbooks|Playbooks/Runbooks]]**: Predefined workflows that codify incident response procedures into automated steps
- **[[case-management|Case management]]**: Tracking incidents from detection through resolution with full documentation
- **[[threat-intelligence-enrichment|Threat intelligence enrichment]]**: Automatically querying threat feeds to add context to alerts before analysts review them
- **[[integration-apis|Integration APIs]]**: SOAR platforms connect to dozens of security tools to take coordinated action
- **[[metrics-and-reporting|Metrics and reporting]]**: Tracking MTTR, MTTD, analyst workload, and automation effectiveness

## Exam Tips

> [!tip] Remember
> SIEM = detect and alert. SOAR = respond and automate. They work together: SIEM triggers the alert, SOAR executes the playbook. Think "SIEM watches, SOAR acts."

- SOAR reduces alert fatigue by handling low-level incidents automatically
- Playbooks should be tested and updated regularly — outdated playbooks can cause harm
- SOAR is not a replacement for analysts — it handles Tier 1 tasks so analysts focus on complex threats

## Connections

- Extends [[siem]] by adding automated response to detection capabilities
- Automates steps in the [[incident-response]] lifecycle, particularly containment and eradication
- Can trigger [[automation-and-scripting]] workflows for custom response actions
- Integrates with [[edr-xdr]] to isolate endpoints or kill malicious processes automatically

## Scenario

> See [[case-soar]] for a practical DevOps scenario applying these concepts.
