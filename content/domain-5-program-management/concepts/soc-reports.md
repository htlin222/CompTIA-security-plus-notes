---
title: "SOC reports"
description: "SOC 1 (financial controls), SOC 2 (security/availability/confidentiality), SOC 3 (public summary)"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What are SOC Reports?
> A SOC report is like a report card for a company's security, written by an outside expert. SOC 1 is about money controls, SOC 2 is about keeping data safe and systems running, and SOC 3 is a short public summary anyone can read.

## Definition

SOC (System and Organization Controls) reports are independent audit reports issued by CPA firms under SSAE 18 standards, providing assurance about a service organization's controls. **SOC 1** covers controls relevant to financial reporting (for financial statement audits). **SOC 2** covers the Trust Services Criteria (security, availability, processing integrity, confidentiality, privacy) and is the primary tool for evaluating cloud and SaaS providers. **SOC 3** is a simplified, public-facing summary of a SOC 2 report.

## Key Details

- **SOC 2 Type I**: assesses design of controls at a *point in time* — are the controls designed appropriately?
- **SOC 2 Type II**: assesses design *and* operating effectiveness of controls over a *period of time* (typically 6–12 months) — stronger assurance
- SOC 2 reports are confidential and shared under NDA with customers; SOC 3 reports can be published publicly
- Organizations request SOC 2 Type II reports from cloud providers and SaaS vendors as part of vendor due diligence
- Exam tip: Type I = design (point in time); Type II = design + effectiveness (over time); Type II provides more assurance

## Connections

- Parent: [[audits-and-assessments]] — SOC reports are the primary audit assurance mechanism for service organizations
- Parent: [[third-party-risk]] — SOC 2 reports are used to evaluate vendor security without direct audits
- See also: [[external-audit]]
- See also: [[vendor-assessment]]
