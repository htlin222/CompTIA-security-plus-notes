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

> [!eli5] ELI5: What is SOAR?
> You know how a vending machine automatically gives you a snack when you press a button, without needing a person behind it? SOAR does that for security. When an alert comes in, SOAR follows a recipe of steps automatically -- like blocking a suspicious address, sending a message to the team, and creating a ticket. This way, the security team does not have to do every little step by hand and can respond way faster.

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

## Practice Questions

> [!qbank]- Q-Bank: SOAR (4 Questions)
>
> **Q1.** A SOC receives 200 phishing email alerts daily. For each alert, an analyst must check the sender reputation, extract URLs, query threat intelligence feeds, and block malicious domains — a process taking 15 minutes per alert. Which solution would MOST effectively reduce analyst workload for these repetitive tasks?
>
> A. Hiring additional Tier 1 analysts to handle the volume
> B. Implementing a SOAR playbook that automates the enrichment and blocking steps
> C. Disabling phishing email alerts to reduce noise
> D. Replacing the SIEM with a more advanced version
>
> > [!answer]- Show Answer
> > **B. Implementing a SOAR playbook that automates the enrichment and blocking steps**
> >
> > [[playbooksrunbooks|SOAR playbooks]] automate repetitive incident response workflows, such as [[threat-intelligence-enrichment]] and automated blocking, dramatically reducing mean time to respond. Option A adds cost without addressing the inefficiency. Option C eliminates security visibility. Option D does not address the response automation gap — SIEM detects, but [[soar]] responds.
>
> **Q2.** A security team wants to connect their SIEM, firewall, EDR, ticketing system, and threat intelligence platform so that alerts automatically trigger coordinated responses across all tools. Which SOAR capability enables this?
>
> A. Case management
> B. Orchestration through API integrations
> C. Compliance reporting
> D. Vulnerability scanning
>
> > [!answer]- Show Answer
> > **B. Orchestration through API integrations**
> >
> > [[orchestration]] connects and coordinates multiple security tools through [[integration-apis|APIs]] to enable automated, cross-platform response actions. Option A tracks incidents but does not coordinate actions across tools. Option C generates compliance documentation, not automated responses. Option D identifies weaknesses but does not orchestrate responses.
>
> **Q3.** After deploying a SOAR platform, a security manager wants to measure its effectiveness. Which metric BEST demonstrates that SOAR is improving incident response efficiency?
>
> A. The total number of security tools deployed
> B. Reduction in Mean Time to Respond (MTTR) for automated incident types
> C. The number of SOAR playbooks created
> D. The total storage capacity of the SIEM platform
>
> > [!answer]- Show Answer
> > **B. Reduction in Mean Time to Respond (MTTR) for automated incident types**
> >
> > [[metrics-and-reporting|MTTR]] directly measures how quickly incidents are resolved — a decrease demonstrates that SOAR automation is speeding up response. Option A measures tool count, not effectiveness. Option C measures activity, not outcomes — playbooks are only valuable if they improve response. Option D measures SIEM capacity, unrelated to SOAR effectiveness.
>
> **Q4.** A SOAR playbook for handling malware alerts was created two years ago. Recently, it blocked a legitimate software update by misidentifying it as malicious, causing a production outage. What should the team do to prevent this in the future?
>
> A. Disable all SOAR automation and revert to manual processes
> B. Regularly review and update playbooks to reflect current environments and threat landscapes
> C. Remove all blocking actions from SOAR playbooks
> D. Reduce the number of log sources feeding into the SOAR platform
>
> > [!answer]- Show Answer
> > **B. Regularly review and update playbooks to reflect current environments and threat landscapes**
> >
> > SOAR [[playbooksrunbooks|playbooks]] must be tested and updated regularly — outdated playbooks can cause harm as environments and applications change. Option A eliminates the efficiency benefits of automation entirely. Option C removes a critical response capability to avoid one issue. Option D reduces visibility, which could cause more incidents to be missed.

## Scenario

> See [[case-soar]] for a practical DevOps scenario applying these concepts.
