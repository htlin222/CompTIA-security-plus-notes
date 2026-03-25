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
- **RTO (Recovery Time Objective)** — maximum acceptable time to restore a system after failure
- **RPO (Recovery Point Objective)** — maximum acceptable data loss measured in time (how far back you can afford to lose)
- **MTTR (Mean Time to Repair)** — average time to fix a failed component
- **MTBF (Mean Time Between Failures)** — average time between system failures; higher is better
- **Mission-essential functions** — operations that must be performed during and after a disruption

## Exam Tips

> [!tip] Remember
> Know the formulas: SLE = AV x EF, ALE = SLE x ARO. The exam will test whether you can pick the right risk response strategy for a given scenario. "Accept" is valid when the cost of mitigation exceeds the potential loss.

## Connections

- Feeds directly into [[vulnerability-management]] as the process that prioritizes which vulnerabilities to remediate
- Threat identification draws on [[threat-actors]] to understand who may attack and why
- Quantitative risk values inform [[business-impact-analysis]] by calculating potential financial losses
- See also [[risk-assessment]] for the detailed evaluation step within the risk management lifecycle

## Practice Questions

> [!qbank]- Q-Bank: Risk Management (4 Questions)
>
> **Q1.** After conducting a risk assessment, a company determines that the cost to mitigate a low-probability server room flooding risk exceeds the potential loss. Management documents the risk and decides to take no further action. Which risk response strategy is this?
>
> A. Avoid
> B. Mitigate
> C. Transfer
> D. Accept
>
> > [!answer]- Show Answer
> > **D. Accept**
> >
> > [[risk-management|Risk acceptance]] means acknowledging the risk and proceeding without additional controls, which is valid when mitigation costs exceed potential losses. Avoidance (A) would mean eliminating the activity entirely. Mitigation (B) would involve implementing controls to reduce the risk. Transfer (C) would shift the risk to a third party such as an insurance provider.
>
> **Q2.** A company purchases a cyber insurance policy to cover potential losses from a data breach. This is an example of which risk response strategy?
>
> A. Avoid
> B. Mitigate
> C. Transfer
> D. Accept
>
> > [!answer]- Show Answer
> > **C. Transfer**
> >
> > [[risk-management|Risk transfer]] shifts the financial burden of a risk to a third party, such as an insurance company. Avoidance (A) would mean not performing the activity that creates the risk. Mitigation (B) would mean implementing controls to reduce likelihood or impact. Acceptance (D) would mean acknowledging the risk without any additional action or financial protection.
>
> **Q3.** An organization implements a new firewall, deploys endpoint detection software, and trains employees on phishing awareness. After these controls are in place, some risk still remains. What is this remaining risk called?
>
> A. Inherent risk
> B. Residual risk
> C. Risk appetite
> D. Risk tolerance
>
> > [!answer]- Show Answer
> > **B. Residual risk**
> >
> > [[residual-risk|Residual risk]] is the risk that remains after controls have been applied. [[inherent-risk|Inherent risk]] (A) is the risk level before any controls are implemented. Risk appetite (C) is the organization's overall willingness to accept risk, not a measure of remaining risk. Risk tolerance (D) is the acceptable deviation from risk appetite, not the risk itself.
>
> **Q4.** A CISO presents a color-coded chart to the board that plots identified risks by likelihood on one axis and impact on the other. Several risks appear in the red zone. This chart is BEST described as a:
>
> A. Risk register
> B. Risk matrix (heat map)
> C. Business impact analysis
> D. Quantitative risk assessment
>
> > [!answer]- Show Answer
> > **B. Risk matrix (heat map)**
> >
> > A [[risk-matrix-heat-map|risk matrix or heat map]] is a visual tool that plots likelihood versus impact using color coding to prioritize risks. A risk register (A) is a document tracking risks, owners, and responses but is typically a table or spreadsheet, not a color-coded chart. A business impact analysis (C) quantifies the effect of disruptions on business functions. A quantitative risk assessment (D) uses dollar values and formulas, not color-coded visual plots.

## Scenario

> See [[case-risk-management]] for a practical DevOps scenario applying these concepts.
