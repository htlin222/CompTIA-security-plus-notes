---
title: "Defense in Depth"
description: "Layered security strategy using multiple controls to protect information assets"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/high
aliases:
  - "Layered Security"
  - "DiD"
---

> [!eli5] ELI5: What is Defense in Depth?
> Think of a castle. It doesn't just have one wall -- it has a moat, then an outer wall, then an inner wall, then guards, then a locked tower. If an attacker gets past one barrier, there's always another one waiting. Defense in depth means protecting computers the same way: with many layers of security stacked on top of each other. No single lock is perfect, but together they make it really, really hard for anyone to get through.

## Overview

Defense in Depth is a security strategy that employs multiple layers of controls across different domains to protect information assets. If one layer fails, subsequent layers continue to provide protection. This approach recognizes that no single security control is sufficient on its own and draws from military doctrine of creating multiple barriers an adversary must overcome.

## Key Concepts

- **[[security-layers|Security layers]]** (from outer to inner):
  - **Physical** — fences, locks, guards, surveillance cameras (see [[physical-security]])
  - **Perimeter** — firewalls, DMZ, IDS/IPS, border routers
  - **Network** — segmentation, VLANs, NAC, VPN
  - **Host** — endpoint protection, OS hardening, patch management
  - **Application** — input validation, WAF, secure coding, code review
  - **Data** — encryption, DLP, access controls, backups
  - **Policies/Procedures** — security awareness training, incident response plans, change management
- **[[administrative-controls|Administrative controls]]** — policies, procedures, training, background checks
- **[[technical-controls|Technical controls]]** — firewalls, encryption, access control systems, IDS
- **[[physical-controls|Physical controls]]** — locks, fences, mantraps, security guards
- **[[preventive-detective-corrective|Preventive, Detective, Corrective]]** — controls categorized by when they act relative to an incident
- **[[vendor-diversity|Vendor diversity]]** — using products from multiple vendors so a vulnerability in one does not compromise all layers
- **[[control-diversity|Control diversity]]** — combining different types of controls (technical + administrative + physical) at each layer

## Exam Tips

> [!tip] Remember
> Defense in Depth = **multiple layers** + **multiple control types**. If a question asks about protecting against a single point of failure in security, the answer is Defense in Depth (or redundancy for availability).

> [!tip] Control Categories
> Administrative (people/policy), Technical (technology), Physical (tangible barriers). The exam frequently asks you to categorize a given control into one of these three types.

## Connections

- Protects all elements of the [[cia-triad]] through layered controls
- Physical layer relies on [[physical-security]] controls like mantraps and surveillance
- Network layer implements [[network-segmentation]] and [[firewalls]] to isolate threats
- Aligns with [[zero-trust]] by not relying on any single trust boundary
- Informed by [[security-concepts]] like least privilege and separation of duties across all layers

## Practice Questions

> [!qbank]- Q-Bank: Defense in Depth (4 Questions)
>
> **Q1.** An organization deploys firewalls at the network perimeter, endpoint protection on all workstations, encrypts sensitive data at rest, and conducts monthly security awareness training. Which security strategy does this combination of controls BEST illustrate?
>
> A. Zero Trust architecture
> B. Defense in depth
> C. Implicit deny
> D. Network segmentation
>
> > [!answer]- Show Answer
> > **B. Defense in depth**
> >
> > [[defense-in-depth|Defense in depth]] uses multiple layers of controls (perimeter, host, data, policies) across different domains so that if one layer fails, subsequent layers continue to provide protection — exactly what is described. Zero Trust focuses on continuous verification and eliminating implicit trust, not layered controls specifically. Implicit deny is a single access control principle, not a comprehensive strategy. Network segmentation is one component within a defense-in-depth strategy, not the overarching approach.
>
> **Q2.** A security auditor categorizes an organization's controls and finds that background checks, security policies, and incident response procedures all fall into the same category. Which type of control do these represent?
>
> A. Technical controls
> B. Physical controls
> C. Administrative controls
> D. Corrective controls
>
> > [!answer]- Show Answer
> > **C. Administrative controls**
> >
> > [[administrative-controls|Administrative controls]] include policies, procedures, training, and background checks — all people-and-process-oriented measures that guide security behavior. [[technical-controls|Technical controls]] are technology-based (firewalls, encryption, IDS), which none of the listed items are. [[physical-controls|Physical controls]] are tangible barriers (locks, fences, guards), which are also not listed. Corrective controls describe when a control acts relative to an incident (after the fact), not the type of control — background checks and policies are preventive, not corrective.
>
> **Q3.** A company uses Cisco firewalls at the perimeter, Palo Alto firewalls for internal segmentation, and Fortinet for the DMZ. Which defense-in-depth principle does this approach BEST demonstrate?
>
> A. Control diversity
> B. Separation of duties
> C. Vendor diversity
> D. Least privilege
>
> > [!answer]- Show Answer
> > **C. Vendor diversity**
> >
> > [[vendor-diversity|Vendor diversity]] means using products from multiple vendors so that a vulnerability in one vendor's product does not compromise all layers — the use of Cisco, Palo Alto, and Fortinet at different network points exemplifies this. [[control-diversity|Control diversity]] means combining different types of controls (technical + administrative + physical), not using different vendors for the same control type. Separation of duties divides critical tasks among multiple people, not technology vendors. Least privilege limits access permissions and is unrelated to firewall vendor selection.
>
> **Q4.** A security architect needs to add a detective control to the application layer of their defense-in-depth strategy. Which control would BEST fulfill this requirement?
>
> A. Input validation on web forms
> B. Web application firewall (WAF) logging and alerting
> C. Code review during development
> D. Encryption of data at rest
>
> > [!answer]- Show Answer
> > **B. Web application firewall (WAF) logging and alerting**
> >
> > WAF logging and alerting is a [[preventive-detective-corrective|detective control]] at the application layer — it monitors and alerts on suspicious activity to detect attacks in progress. Input validation is a preventive control that blocks malicious input before it is processed. Code review is a preventive control applied during development, not at runtime. Encryption of data at rest is a preventive control at the data layer, not a detective control at the application layer.

## Scenario

> See [[case-defense-in-depth]] for a practical DevOps scenario applying these concepts.
