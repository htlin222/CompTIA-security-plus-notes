---
title: "Risk Management"
description: "Risk management is the ongoing process of identifying, assessing, and responding to threats that could impact an organization's assets."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/risk
  - weight/high
aliases:
  - "Risk Management"
---

> [!eli5] ELI5: What is Risk Management?
> When you ride your bike, you wear a helmet, check the brakes, and avoid busy roads. You can't prevent every possible accident, but you take steps to lower the chances. Risk management is a company doing the same thing with its computers and data -- finding dangers, deciding which ones matter most, and choosing the best way to handle each one. The goal isn't zero risk (that's impossible) but bringing risk down to a level everyone is comfortable with.

## Overview

Risk management is the continuous cycle of identifying threats and vulnerabilities, analyzing the potential impact and likelihood of exploitation, and selecting appropriate responses. It enables organizations to make informed decisions about where to invest security resources. The goal is not to eliminate all risk but to reduce it to an acceptable level defined by leadership.

## Key Concepts

- **[[risk-threat-x-vulnerability-x-impact|Risk = Threat x Vulnerability x Impact]]** — all three factors must be present for risk to exist
- **[[risk-identification|Risk identification]]** — asset inventory, threat modeling, vulnerability scanning
- **Risk response strategies:**
  - **Avoid** — eliminate the activity that introduces risk
  - **Mitigate (reduce)** — implement controls to lower likelihood or impact
  - **Transfer** — shift risk to a third party (insurance, outsourcing)
  - **Accept** — acknowledge the risk and proceed without additional controls
- **[[risk-appetite-vs-risk-tolerance|Risk appetite vs. risk tolerance]]** — appetite is the overall willingness to take risk; tolerance is the acceptable deviation from appetite
- **[[residual-risk|Residual risk]]** — risk remaining after controls are applied
- **[[inherent-risk|Inherent risk]]** — risk present before any controls
- **[[risk-register|Risk register]]** — a living document tracking identified risks, owners, responses, and status
- **[[risk-matrix-heat-map|Risk matrix (heat map)]]** — plots likelihood vs. impact to prioritize risks visually
- **[[qualitative-vs-quantitative-analysis|Qualitative vs. quantitative analysis]]** — qualitative uses categories (high/medium/low); quantitative uses dollar values (SLE, ALE, ARO)

## Exam Tips

> [!tip] Remember
> Know the formulas: SLE = AV x EF, ALE = SLE x ARO. The exam will test whether you can pick the right risk response strategy for a given scenario. "Accept" is valid when the cost of mitigation exceeds the potential loss.

## Connections

- Feeds directly into [[vulnerability-management]] as the process that prioritizes which vulnerabilities to remediate
- Threat identification draws on [[threat-actors]] to understand who may attack and why
- Quantitative risk values inform [[business-impact-analysis]] by calculating potential financial losses
- See also [[risk-assessment]] for the detailed evaluation step within the risk management lifecycle

## Scenario

> See [[case-risk-management]] for a practical DevOps scenario applying these concepts.
