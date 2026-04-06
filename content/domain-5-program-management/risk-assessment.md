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

> [!eli5] ELI5: What is Risk Assessment?
> It's like looking at all the things that could go wrong on a field trip and figuring out which ones to worry about most. Crossing a busy road? That's high risk. Getting a mosquito bite? Not great, but not a big deal. A risk assessment helps a company look at each danger, decide how likely it is to happen and how bad it would be, and then focus on fixing the scariest ones first.

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

## Practice Questions

> [!qbank]- Q-Bank: Risk Assessment (4 Questions)
>
> **Q1.** A web server valued at $200,000 faces a threat with an exposure factor of 25% and an annualized rate of occurrence of 2. What is the Annualized Loss Expectancy (ALE)?
>
> A. $50,000
> B. $100,000
> C. $200,000
> D. $400,000
>
> > [!answer]- Show Answer
> > **B. $100,000**
> >
> > Using the [[quantitative-risk-assessment|quantitative formulas]]: SLE = AV x EF = $200,000 x 0.25 = $50,000. ALE = SLE x ARO = $50,000 x 2 = $100,000. Answer A ($50,000) is the SLE, not the ALE. Answer C ($200,000) is the asset value. Answer D ($400,000) incorrectly doubles the asset value.
>
> **Q2.** A security team gathers department heads to rate threats as high, medium, or low based on their experience and judgment. No financial data is used. This approach BEST describes which type of risk assessment?
>
> A. Quantitative risk assessment
> B. Qualitative risk assessment
> C. Vulnerability assessment
> D. Threat assessment
>
> > [!answer]- Show Answer
> > **B. Qualitative risk assessment**
> >
> > A [[qualitative-risk-assessment|qualitative risk assessment]] uses subjective ratings based on expert judgment rather than numerical values. Quantitative (A) would require dollar values and formulas like SLE and ALE. A vulnerability assessment (C) identifies specific technical weaknesses, not broad risk ratings. A threat assessment (D) evaluates threat sources and capabilities but is narrower in scope than a full risk assessment.
>
> **Q3.** An organization's risk assessment reveals that the ALE for a ransomware attack is $500,000, while a proposed email filtering solution costs $75,000 annually. Based on this analysis, what is the BEST recommendation?
>
> A. Accept the risk because ransomware is unlikely
> B. Implement the control because the ALE exceeds the control cost
> C. Transfer the risk to a cyber insurance provider instead
> D. Avoid the risk by disconnecting from the internet
>
> > [!answer]- Show Answer
> > **B. Implement the control because the ALE exceeds the control cost**
> >
> > When [[quantitative-risk-assessment|ALE exceeds the cost of a control]], implementing the control is financially justified. Accepting the risk (A) is inappropriate when a cost-effective mitigation exists. Transferring to insurance (C) could be part of a strategy but does not address the root cause when a preventive control is available and affordable. Avoiding risk by disconnecting (D) is impractical and would halt business operations.
>
> **Q4.** A company performs risk assessments only when a major incident occurs. The security team recommends changing to a scheduled quarterly approach. Which assessment frequency model is the team moving FROM and TO?
>
> A. From continuous to recurring
> B. From recurring to ad hoc
> C. From ad hoc to recurring
> D. From continuous to ad hoc
>
> > [!answer]- Show Answer
> > **C. From ad hoc to recurring**
> >
> > [[ad-hoc-vs-recurring-vs-continuous|Ad hoc assessments]] are triggered by events (like incidents), while recurring assessments are performed on a fixed schedule (quarterly). The company is moving from event-triggered to scheduled. Moving from continuous to recurring (A) would be a downgrade, not an upgrade. From recurring to ad hoc (B) is the reverse of what is described. From continuous to ad hoc (D) is also the opposite direction.

## Scenario

> See [[case-risk-assessment]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [5.2 – Risk Analysis](https://www.youtube.com/watch?v=KiEptGbnEBc&list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv&index=111)
