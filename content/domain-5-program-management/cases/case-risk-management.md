---
title: "Case: The Insurance Ultimatum — Risk Management Program from Scratch"
description: "After a third-party breach, cyber insurance carriers demand a complete risk register and management program within 30 days, or premium rates double."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

ServiceLogix is a $150M SaaS company that manages logistics and supply chain operations for over 2,000 small and mid-sized distributors. In December 2024, the company learned that a key third-party vendor—their customer identity and access management provider—had suffered a breach affecting customer credentials. Approximately 180,000 ServiceLogix customer login credentials had been exposed on the dark web.

The company's Chief Information Security Officer, David Chen, immediately initiated their incident response procedure. They notified customers, rotated credentials, reviewed logs for unauthorized access, and engaged a forensic firm. No customer data had been accessed using the compromised credentials (the attacker had gone after higher-value targets), so the incident was contained with relatively limited damage. The breach notification process took six weeks, and within eight weeks, the incident was largely behind them.

Then came the letter from their cyber insurance carrier, Beazley Cyber Insurance.

The letter was professional but firm:

> "ServiceLogix has experienced a material security incident. To maintain your cyber liability coverage at current rates, you must provide evidence of a formal [[risk-management]] program by March 15. This must include:
>
> - A comprehensive [[risk-register]] documenting all significant risks, current control status, and remediation timelines
> - Risk-identification methodology and cadence
> - Residual-risk assessment showing how controls reduce inherent risk
> - Risk-appetite-vs-risk-tolerance statement approved by executive leadership
> - Threat-actors and [[vulnerability-management]] baseline
> - Documented [[risk-threat-x-vulnerability-x-impact]] analysis
>
> If this documentation is not provided by March 15, your renewal premium will be increased 100% (from $240K to $480K annually) and coverage limits will be reduced by 25%."

The deadline was 30 days away. David had no risk management program. The company had security controls (firewalls, encryption, monitoring), but they had never been formally assessed against a risk register. There was no risk register. Risk decisions were made ad hoc by whoever was involved in a given incident.

David called an emergency meeting with the CEO, CTO, and CFO. They decided to build a risk management program immediately. David assembled a team of six people (himself, the VP of Security Operations, the Chief Architect, a business analyst, and two security engineers) and they worked intensively.

**Week 1-2: Risk Identification**

Using a combination of [[threat-actors]] research, historical incident data, and [[vulnerability-assessment]] results, they identified 47 potential risks:

- External threat risks (zero-day exploits, advanced persistent threats, supply chain compromises)
- Internal threat risks (insider threat, privilege misuse, negligent data exposure)
- Operational risks (system failures, data loss, availability issues)
- Compliance risks (regulatory violations, audit findings, third-party breaches)

They prioritized these down to 18 risks significant enough to track on the formal [[risk-register]]:

| Risk                                           | Category        | Inherent Risk | Current Controls                                 | Residual Risk |
| ---------------------------------------------- | --------------- | ------------- | ------------------------------------------------ | ------------- |
| Zero-day RCE in customer portal                | External Threat | Critical      | WAF, IDS, patch SLA                              | High          |
| Supply chain (vendor) breach                   | External Threat | High          | Vendor assessments, [[third-party-risk]] reviews | Medium        |
| Insider data exfiltration                      | Internal Threat | High          | DLP, logging, access controls                    | Medium-High   |
| Ransomware attack                              | External Threat | High          | Backups, immutable snapshots                     | Medium        |
| Application vulnerability leading to data leak | External Threat | High          | SAST/DAST, security code review                  | Medium        |
| Credential compromise via phishing             | External Threat | Medium        | MFA, awareness training                          | Medium        |
| Cloud misconfigurations                        | Operational     | Medium        | IaC scanning, CSPM tool                          | Low           |
| Database backup failure                        | Operational     | High          | 3-2-1 backups, DR testing                        | Low           |
| Third-party SaaS provider goes out of business | Supply Chain    | Medium        | Vendor diversity, data export procedures         | Low           |

For each risk, the team documented:

- **Risk-identification**: How was the risk identified? (Threat assessment, historical incident, industry trend)
- **Threat-actors**: Who would exploit this risk and why?
- **Vulnerability-management**: What vulnerabilities enable this risk?
- **Risk-threat-x-vulnerability-x-impact**: Risk = Threat × Vulnerability × Impact. What is the probability and severity?
- **Current controls**: What's already in place?
- **Residual-risk**: What risk remains after controls?
- **Remediation plan**: What additional controls would reduce residual risk further?

**Week 2-3: Risk Appetite and Tolerance**

This was the hardest conversation. The executive team had to answer: "What level of risk can we tolerate?"

For each risk category, they documented [[risk-appetite-vs-risk-tolerance]]:

- **External threats**: Willing to tolerate "Medium" residual risk for controlled risks with strong detective controls (logging, IDS). Not willing to tolerate "High" residual risk without aggressive response procedures.
- **Supply chain**: Willing to tolerate "Medium" residual risk for critical vendors with strong oversight. Not willing to tolerate "High" without alternatives.
- **Data loss**: Not willing to tolerate "High" residual risk. All critical data must have verified backups and recovery procedures.
- **Compliance**: Not willing to tolerate any residual risk. All regulatory requirements must be fully met.

**Week 3-4: Remediation Roadmap**

For risks with residual risk higher than tolerance, the team developed remediation plans:

- "Insider exfiltration (Medium-High residual)" → Implementation of UEBA tool ($80K) + privileged access management ($120K). Target: Reduce to "Low-Medium" by Q3 2025.
- "Zero-day RCE (High residual)" → Enhanced threat detection (SOAR platform, $150K) + incident response tabletop exercises. Target: Reduce to "Medium" by Q2 2025.
- "Ransomware (Medium residual)" → Immutable backups validation + air-gapped recovery environment ($200K). Target: Reduce to "Low" by Q2 2025.

Each remediation plan included owner, budget, timeline, and success metrics.

**Week 4: Presentation to Board and Insurance Carrier**

David presented the completed [[risk-register]] to both the board and the insurance carrier. The presentation showed:

1. Systematic [[risk-identification]] process based on threat intelligence and vulnerability assessment
2. Clear [[risk-threat-x-vulnerability-x-impact]] scoring for each risk
3. Documented [[risk-appetite-vs-risk-tolerance]] approved by executive leadership
4. Current [[residual-risk]] assessment showing where the company was overleveraged
5. Concrete remediation roadmap with budgets and timelines

The insurance carrier reviewed the documentation and approved the renewal at current rates with a condition: submit quarterly updates to the [[risk-register]] and provide evidence of remediation progress.

## What Went Right

- **Crisis forced structure**: The insurance ultimatum made [[risk-management]] a business priority, not a security nice-to-have.
- **Stakeholder engagement**: Including the CEO, CTO, and CFO in the process ensured [[risk-appetite-vs-risk-tolerance]] reflected true business priorities, not just security preferences.
- **Threat-based approach**: Using actual [[threat-actors]] research and vulnerability data made the [[risk-identification]] credible rather than purely theoretical.
- **Clear [[risk-threat-x-vulnerability-x-impact]] model**: The team used a structured approach (Threat × Vulnerability × Impact) that was understandable and defensible.
- **Remediation is about tolerance, not perfection**: The team didn't try to eliminate all risk (impossible). Instead, they focused on bringing [[residual-risk]] in line with [[risk-appetite-vs-risk-tolerance]].

## What Could Go Wrong

- **No [[risk-identification]] methodology**: If the team had relied on assumption rather than systematic threat assessment and vulnerability review, the register would have been incomplete.
- **Risk-appetite-vs-risk-tolerance determined by IT, not business**: If David had written risk appetite alone, the executive team would have disagreed with priorities. Business approval is essential.
- **No remediation roadmap**: A [[risk-register]] without remediation plans is documentation for compliance, not management. Plans with owners and budgets make it actionable.
- **Set and forget**: The [[risk-register]] must be reviewed and updated quarterly at minimum. New vulnerabilities emerge, threat landscape changes, controls need validation.
- \*\*Missing [[third-party-risk]]: Supply chain risks often aren't included in risk registers, leaving organizations vulnerable to incidents like the one that triggered this case.

## Key Takeaways

- **Risk-management program requires three components**: [[risk-identification]] (what are the risks?), [[residual-risk]] assessment (how much risk remains?), and remediation planning (what will we do about unacceptable risks?).
- **Risk-appetite-vs-risk-tolerance must be business-approved**: Security teams can't unilaterally decide what risks the company is willing to accept. This must be executive-level decision with documented approval.
- **Risk-threat-x-vulnerability-x-impact provides structure**: Don't just list risks. Score them systematically: What threat actors target you? What vulnerabilities exist? What would impact be? This enables prioritization.
- **Residual-risk is what matters**: Inherent risk (what you'd face with no controls) is theoretical. Residual risk (what remains after controls) is what you're actually managing. Focus on [[residual-risk]].
- **Risk-register is a living document**: Update it quarterly. As vulnerabilities are patched, threats change, and controls are implemented, risks evolve. Treat it as active management, not compliance artifact.

## Related Cases

- [[case-risk-assessment]] — Conducting quantitative risk assessments that feed the risk register
- [[case-business-impact-analysis]] — Understanding impact that drives residual risk assessment
- [[case-governance]] — Board-level governance of risk management
- [[case-third-party-risk]] — Supply chain risk management as part of overall program
