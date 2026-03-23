---
title: "Privacy"
description: "Privacy focuses on the proper collection, use, storage, and disposal of personal information in compliance with legal requirements."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/medium
aliases:
  - "Privacy"
  - "Data Privacy"
---

## Overview

Privacy in information security refers to an individual's right to control how their personal information is collected, used, shared, and disposed of. Organizations must implement technical and administrative controls to protect personally identifiable information (PII) and comply with privacy regulations. Privacy is distinct from security: security protects data from unauthorized access, while privacy governs how authorized parties handle personal data.

## Key Concepts

- **[[pii-personally-identifiable-information|PII (Personally Identifiable Information)]]** — data that can identify an individual (name, SSN, email, biometrics)
- **[[phi-protected-health-information|PHI (Protected Health Information)]]** — health-related PII governed by HIPAA
- **Privacy principles:**
  - **Purpose limitation** — collect data only for a stated purpose
  - **Data minimization** — collect only what is necessary
  - **Consent** — obtain permission before collecting personal data
  - **Right to be forgotten (erasure)** — GDPR grants individuals the right to request data deletion
  - **Data portability** — individuals can request their data in a usable format
- **[[privacy-impact-assessment-pia|Privacy Impact Assessment (PIA)]]** — evaluates how a project or system will affect individual privacy
- **[[privacy-by-design|Privacy by design]]** — embedding privacy controls into systems from the beginning, not as an afterthought
- **[[anonymization-vs-pseudonymization|Anonymization vs. pseudonymization]]** — anonymization is irreversible; pseudonymization replaces identifiers but can be reversed with a key
- **[[data-breach-notification|Data breach notification]]** — regulations often require notifying affected individuals and authorities within a set timeframe
- **[[data-sovereignty|Data sovereignty]]** — data is subject to the laws of the country where it is stored

## Exam Tips

> [!tip] Remember
> Anonymization cannot be reversed; pseudonymization can. GDPR requires data breach notification within 72 hours. Privacy by design = build it in from the start, not bolted on later.

## Connections

- Governed by [[regulations-and-frameworks]] such as GDPR, HIPAA, and GLBA which define privacy requirements
- Closely related to [[data-classification]] which identifies and labels personal data requiring privacy protections
- See also [[compliance]] for how privacy requirements are monitored and enforced

## Scenario

> See [[case-privacy]] for a practical DevOps scenario applying these concepts.
