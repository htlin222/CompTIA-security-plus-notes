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

## Scenario

> See [[case-defense-in-depth]] for a practical DevOps scenario applying these concepts.
