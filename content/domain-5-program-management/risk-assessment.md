---
title: "Risk Assessment"
description: "Risk assessment evaluates identified risks using qualitative or quantitative methods to prioritize security responses."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/risk
  - weight/high
aliases:
  - "Risk Assessment"
---

## Overview

A risk assessment is the evaluation phase of risk management where identified threats and vulnerabilities are analyzed to determine their likelihood and potential impact. Organizations use qualitative, quantitative, or hybrid approaches to rank risks and decide which ones require immediate attention. Regular risk assessments ensure that the security posture adapts to evolving threats.

## Key Concepts

- **[[qualitative-risk-assessment|Qualitative risk assessment]]** — uses subjective ratings (high, medium, low) based on expert judgment; faster but less precise
- **[[quantitative-risk-assessment|Quantitative risk assessment]]** — uses numerical values and formulas; more precise but requires reliable data
  - **Asset Value (AV)** — dollar value of the asset
  - **Exposure Factor (EF)** — percentage of asset lost in an incident
  - **Single Loss Expectancy (SLE)** — AV x EF
  - **Annualized Rate of Occurrence (ARO)** — how often the threat is expected per year
  - **Annualized Loss Expectancy (ALE)** — SLE x ARO
- **[[risk-matrix-heat-map|Risk matrix / heat map]]** — visual tool plotting likelihood vs. impact
- **[[threat-assessment|Threat assessment]]** — evaluating threat sources and their capabilities
- **[[vulnerability-assessment|Vulnerability assessment]]** — identifying weaknesses that could be exploited
- **[[ad-hoc-vs-recurring-vs-continuous|Ad hoc vs. recurring vs. continuous]]** — assessments may be triggered by events, scheduled, or ongoing
- **[[environmental-factors|Environmental factors]]** — internal (staffing, technology) and external (regulatory, geopolitical)

## Exam Tips

> [!tip] Remember
> Quantitative = numbers and dollar values. Qualitative = categories and expert opinion. The exam loves SLE/ALE/ARO calculations. If ALE > cost of control, implement the control.

## Connections

- A core step within the broader [[risk-management]] lifecycle
- Assessment results drive priorities in [[vulnerability-management]] — high-risk findings get patched first
- See also [[audits-and-assessments]] for how risk assessments fit into the broader audit and review process

## Scenario

> See [[case-risk-assessment]] for a practical DevOps scenario applying these concepts.
