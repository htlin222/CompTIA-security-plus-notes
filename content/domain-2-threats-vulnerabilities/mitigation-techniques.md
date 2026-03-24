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

> [!eli5] ELI5: What are Mitigation Techniques?
> When your house has problems -- maybe the lock is broken or a window won't close -- you fix them so burglars can't get in. Mitigation techniques are all the different ways we fix and protect computers from bad guys. Some fixes are like installing a better lock (patching software). Others are like adding a security camera (monitoring). Some are like teaching your family not to open the door for strangers (security training). The more layers of protection you add, the harder it is for anyone to break in.

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

## Practice Questions

> [!qbank]- Q-Bank: Mitigation Techniques (4 Questions)
>
> **Q1.** After a ransomware incident, a security architect recommends dividing the flat corporate network into separate zones for finance, engineering, and guest access. Which mitigation technique does this BEST represent?
>
> A. Application allowlisting
> B. Network segmentation
> C. Configuration management
> D. Security awareness training
>
> > [!answer]- Show Answer
> > **B. Network segmentation**
> >
> > Dividing a flat network into isolated zones is [[network-segmentation]], which limits lateral movement and reduces the blast radius of attacks like ransomware. Application allowlisting (A) restricts which software can execute, not network zones. Configuration management (C) maintains consistent system settings, not network topology. Security awareness training (D) educates users but does not address network architecture.
>
> **Q2.** A critical production server runs legacy software that cannot be patched due to vendor restrictions. The security team implements enhanced monitoring, strict firewall rules, and an IDS specifically for this server. What type of control is being applied?
>
> A. Preventive control
> B. Compensating control
> C. Deterrent control
> D. Physical control
>
> > [!answer]- Show Answer
> > **B. Compensating control**
> >
> > [[compensating-controls]] are alternative measures implemented when the primary control (patching) cannot be applied. Enhanced monitoring and strict rules compensate for the inability to patch. A preventive control (A) would be the patch itself. A deterrent control (C) discourages attackers but does not substitute for a missing primary control. A physical control (D) involves tangible barriers like locks, not logical network measures.
>
> **Q3.** An organization follows this priority when addressing a newly discovered vulnerability: first attempt to patch, then segment if patching is delayed, then document acceptance if neither is feasible. Which mitigation principle does this order BEST reflect?
>
> A. Defense in depth
> B. Risk response hierarchy: eliminate, reduce, then accept
> C. Least privilege
> D. Zero trust architecture
>
> > [!answer]- Show Answer
> > **B. Risk response hierarchy: eliminate, reduce, then accept**
> >
> > This follows the mitigation order of preference: eliminate the vulnerability through [[patching]], reduce impact through [[network-segmentation]], or accept the risk with documentation. Defense in depth (A) means layering multiple controls simultaneously, not a prioritized sequence. Least privilege (C) restricts access to the minimum necessary but does not describe a vulnerability response order. Zero trust (D) is an architectural model, not a risk response strategy.
>
> **Q4.** A company wants to ensure that only approved corporate applications can run on employee workstations, blocking any unauthorized executables. Which mitigation technique is MOST appropriate?
>
> A. Network segmentation
> B. Encryption
> C. Application allowlisting
> D. Patching
>
> > [!answer]- Show Answer
> > **C. Application allowlisting**
> >
> > [[application-allowlisting]] permits only approved software to execute, which is stronger than blocklisting because it blocks everything not explicitly allowed. Network segmentation (A) isolates network zones but does not control which applications run on endpoints. Encryption (B) protects data confidentiality, not application execution. Patching (D) fixes known vulnerabilities but does not prevent unauthorized software from running.

## Scenario

> See [[case-mitigation-techniques]] for a practical DevOps scenario applying these concepts.
