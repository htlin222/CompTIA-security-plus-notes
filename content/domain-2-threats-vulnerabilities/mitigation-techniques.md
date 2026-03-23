---
title: "Mitigation Techniques"
description: "Strategies and controls used to reduce or eliminate the impact of threats and vulnerabilities"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/risk
  - weight/high
aliases:
  - "Threat Mitigation"
  - "Security Controls"
---

## Overview

Mitigation techniques are the security controls and strategies applied to reduce or eliminate the impact of identified threats and vulnerabilities. Effective mitigation follows a defense-in-depth approach, layering multiple controls so that the failure of one does not result in compromise. The Security+ exam tests knowledge of specific mitigations and the ability to select appropriate controls for given scenarios.

## Key Concepts

- **[[patching|Patching]]**: Applying vendor-supplied fixes to close known vulnerabilities — the most fundamental mitigation
- **[[network-segmentation|Network segmentation]]**: Dividing the network into isolated zones to limit lateral movement and blast radius
- **[[least-privilege|Least privilege]]**: Granting only the minimum access necessary to perform a job function
- **[[input-validation|Input validation]]**: Sanitizing and validating all user input to prevent injection and other application attacks
- **[[encryption|Encryption]]**: Protecting data at rest and in transit to ensure confidentiality even if intercepted
- **[[access-control-lists-acls|Access control lists (ACLs)]]**: Defining explicit allow/deny rules for network traffic and resource access
- **[[security-baselines-and-hardening|Security baselines and hardening]]**: Configuring systems according to CIS Benchmarks or STIGs before deployment
- **[[application-allowlisting|Application allowlisting]]**: Only permitting approved software to execute — stronger than blocklisting
- **[[configuration-management|Configuration management]]**: Maintaining consistent, secure configurations and detecting drift
- **[[decommissioning|Decommissioning]]**: Properly retiring end-of-life systems that can no longer be patched
- **[[compensating-controls|Compensating controls]]**: Alternative measures when the primary control cannot be implemented (e.g., enhanced monitoring when patching is not feasible)
- **[[security-awareness-training|Security awareness training]]**: Educating users to recognize and respond to social engineering and phishing

## Exam Tips

> [!tip] Remember
> Mitigation order of preference: Eliminate the vulnerability (patch/remove) > Reduce the impact (segment/encrypt) > Transfer the risk (insurance/contract) > Accept the risk (documented decision). Compensating controls are NOT equal to primary controls.

- Network segmentation is a key mitigation for limiting ransomware spread
- Compensating controls require documentation and approval — they are temporary measures
- Defense in depth = multiple layers — no single control is sufficient

## Connections

- Applied to address [[vulnerability-types]] identified through scanning and assessment
- Includes many controls implemented via [[hardening]] processes
- [[penetration-testing]] validates whether mitigation techniques are effective
- Feeds into [[risk-management]] as the "treat" option in risk response strategies

## Scenario

> See [[case-mitigation-techniques]] for a practical DevOps scenario applying these concepts.
