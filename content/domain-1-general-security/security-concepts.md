---
title: "Security Concepts"
description: "Foundational security principles and terminology for the SY0-701 exam"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/high
aliases:
  - "Security Fundamentals"
---

## Overview

Security concepts form the bedrock of the CompTIA Security+ exam, encompassing the principles, terminology, and frameworks that guide all cybersecurity practices. Understanding these foundational ideas is essential for grasping how threats are identified, risks are managed, and systems are protected across an organization.

## Key Concepts

- **Confidentiality, Integrity, Availability (CIA)** — the three pillars of information security; every control maps back to at least one of these (see [[cia-triad]])
- **[[non-repudiation|Non-repudiation]]** — ensures that a party cannot deny having performed an action; achieved through digital signatures, logging, and audit trails
- **[[least-privilege|Least privilege]]** — users and processes should only have the minimum permissions necessary to perform their function
- **[[separation-of-duties|Separation of duties]]** — no single person should control all aspects of a critical transaction, reducing fraud and error risk
- **[[need-to-know|Need to know]]** — access to information is restricted to those who require it for their role
- **[[due-diligence-vs-due-care|Due diligence vs. due care]]** — due diligence is researching and understanding risks; due care is acting responsibly to mitigate them
- **[[security-through-obscurity|Security through obscurity]]** — relying on secrecy of design rather than robust controls; considered insufficient on its own
- **[[open-design-principle|Open design principle]]** — security mechanisms should not depend on secrecy of implementation

## Exam Tips

> [!tip] Remember
> The CIA triad appears in nearly every domain. When evaluating a scenario question, ask: "Which element of CIA is being threatened?" This frames the correct answer quickly.

> [!tip] Least Privilege vs. Need to Know
> Least privilege limits _permissions_; need to know limits _information access_. Both reduce attack surface but operate at different levels.

## Connections

- Built upon [[cia-triad]] as the core framework for evaluating security posture
- Implemented through [[defense-in-depth]] to create layered security controls
- Enforced by [[access-control-models]] which define how least privilege and separation of duties are applied
- Directly informs [[risk-management]] decisions about which controls to implement

## Scenario

> See [[case-security-concepts]] for a practical DevOps scenario applying these concepts.
