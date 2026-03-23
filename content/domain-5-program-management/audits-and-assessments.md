---
title: "Audits and Assessments"
description: "Audits and assessments evaluate the effectiveness of security controls and verify compliance with policies, standards, and regulations."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/high
aliases:
  - "Audits and Assessments"
---

## Overview

Audits and assessments are systematic evaluations of an organization's security posture. Audits are formal, often conducted by third parties, and measure compliance against specific standards. Assessments are broader evaluations that identify gaps and recommend improvements. Both are essential for maintaining accountability and demonstrating due diligence to regulators and stakeholders.

## Key Concepts

- **[[internal-audit|Internal audit]]** — conducted by the organization's own audit team; provides ongoing assurance
- **[[external-audit|External audit]]** — performed by an independent third party; required for certifications and regulatory compliance
- **[[regulatory-audit|Regulatory audit]]** — mandated by a governing body (e.g., PCI QSA audit for PCI DSS compliance)
- **Assessment types:**
  - **Vulnerability assessment** — identifies known weaknesses using automated scanning tools
  - **Penetration test** — simulated attack to exploit vulnerabilities and test defenses
  - **Risk assessment** — evaluates likelihood and impact of threats
  - **Security posture assessment** — holistic review of the organization's overall security state
- **[[audit-scope|Audit scope]]** — defines what systems, processes, and controls are being examined
- **[[evidence-collection|Evidence collection]]** — logs, configurations, policies, interviews, and observations gathered during audits
- **[[findings-and-remediation|Findings and remediation]]** — audit results include findings (issues) and recommendations with timelines for remediation
- **[[soc-reports|SOC reports]]** — SOC 1 (financial controls), SOC 2 (security/availability/confidentiality), SOC 3 (public summary)
- **[[attestation|Attestation]]** — formal declaration by an auditor that controls are operating effectively

## Exam Tips

> [!tip] Remember
> External audits are more authoritative than internal audits for compliance. SOC 2 Type II covers a time period and is preferred over Type I (point-in-time). Penetration tests go further than vulnerability assessments by actually exploiting flaws.

## Connections

- Validates that [[compliance]] requirements are being met through independent verification
- Informs [[risk-management]] by identifying gaps and new risks discovered during evaluation
- See also [[regulations-and-frameworks]] for the specific standards against which audits measure
- Related to [[hardening]] as audit findings often drive remediation of system configurations

## Scenario

> See [[case-audits-and-assessments]] for a practical DevOps scenario applying these concepts.
