---
title: "Case: The Policy Vacuum — Building Governance from Scratch"
description: "A startup that grew from 20 to 500 employees in two years has a single password policy and no formal security policy framework, facing SOC 2 audit in four months."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

Velocity Analytics exploded from a 20-person startup to a 500-person company in 24 months. The growth was exhilarating: Series B funding at $200M valuation, expansion into EMEA and APAC, enterprise customers including three Fortune 500 companies. The engineering team had scaled from 8 developers to 85. Operations had grown from one person to 12.

But security governance had been completely neglected. The founder-CEO, Alex Kumar, knew this was a problem. The Fortune 500 customers were starting to ask about security controls, and the newest customer had requested a SOC 2 Type II audit before they would give the company enterprise-wide access.

Alex brought in a Chief Information Security Officer, James Mitchell, in January 2025. James's first task was to assess the current security posture. The findings were sobering:

**Security policies**:
- One policy document: a wiki page titled "Password Complexity Requirements" written in 2022
- Content: "Passwords must be at least 8 characters with uppercase, lowercase, numbers, and symbols"
- That was it. No other security policies existed.

**Critical missing policies**:
- No [[access-control-models]] or identity management policy
- No [[data-classification]] or data handling procedures
- No incident response procedures
- No acceptable use policy
- No [[third-party-risk]] vendor assessment requirements
- No physical security policy
- No [[business-continuity]] or [[disaster-recovery]] procedures
- No security awareness training requirements
- No [[audit-scope]] or audit procedures
- No [[exception-process]] for policy violations

James realized the audit deadline (Q2 2025, four months away) was actually helpful—it created urgency. He proposed a [[policy-lifecycle]] approach to build a complete policy framework in 16 weeks.

**Weeks 1-2: Policy framework definition**

James worked with the executive team to define what policies would be needed for SOC 2 Type II compliance:

**Core governance policies**:
1. Information Security Policy (overall governance framework)
2. Security Awareness and Training Policy
3. Access Control and Identity Management Policy
4. [[Data-classification]] and Handling Policy
5. Incident Response and Business Continuity Policy
6. [[Third-party-risk]] and Vendor Management Policy
7. Physical Security and Environmental Controls Policy
8. Acceptable Use Policy
9. Change Management and Configuration Control Policy
10. Risk Management Policy

For each policy, James defined the components that would be required:
- Scope and applicability
- Roles and responsibilities
- Procedures and controls
- [[Exception-process]] and approval authority
- Review and update schedule

**Weeks 3-6: Policy drafting and stakeholder input**

James drafted policies with input from department heads:

**Access Control Policy** (drafted with engineering and operations):
- All users must authenticate with MFA
- Privileged access requires approval from department head and security
- Access must be reviewed quarterly
- Unused accounts must be disabled within 30 days
- Contractor access must be terminated within 48 hours of offboarding
- [[Exception-process]]: Request to CISO with business justification and risk assessment

**[[Data-classification]] Policy** (drafted with product and legal):
- Public: Marketing materials, public documentation
- Internal: Employee directories, internal processes
- Confidential: Customer data, product roadmaps, contracts
- Restricted: API keys, credentials, source code repositories
- Handling procedures by classification level were defined

**Incident Response Policy** (drafted with engineering and legal):
- Any suspected security incident must be reported to security team within 1 hour
- Incident response team meets within 2 hours of critical incident report
- Customer notification required within 72 hours for breaches involving customer data
- Post-incident review completed within 10 days
- Communications restricted to "need to know" basis to avoid disclosure

**[[Third-party-risk]] Policy** (drafted with procurement and legal):
- All software vendors must complete security assessment questionnaire
- Vendors processing customer data must have SOC 2 Type II certification or equivalent
- Vendor contracts must include data processing agreements and security obligations
- Annual vendor risk review required
- Critical vendors must be assessed for [[supply-chain-risk]]

**Weeks 7-10: Testing and rollout**

Rather than distributing all policies at once and expecting compliance, James took a phased approach:

1. **Soft rollout with departments**: Pilot policies were shared with department heads for feedback and testing
2. **Refinement**: Policies were updated based on feedback
3. **Training**: Department heads received training on their roles in policy implementation
4. **Formal rollout**: Final policies were distributed company-wide with training sessions for all employees

**Weeks 11-16: Implementation and evidence gathering**

This phase included:
- Training tracking: Evidence that all employees completed security awareness training
- Access control review: Documented quarterly access review process
- Incident response testing: Tabletop exercise of incident response procedures
- Vendor assessment: Documented assessment of top 15 critical vendors
- [[Exception-process]] testing: Examples of policy exceptions requested and approved with documented risk assessment
- Policy maintenance schedule: Calendar for annual policy review and update

**Policy governance structure**:

James also established a [[policy-lifecycle]] governance model:
- **Policy Owner**: Who is accountable for each policy (e.g., CISO owns security policy, HR owns acceptable use)
- **Review Schedule**: All policies reviewed annually, with updates documented
- **Approval Authority**: Who can approve exceptions and policy updates
- **Communication**: Policies published in company wiki with version control
- **Training**: All new hires complete security awareness training within first week
- **Compliance Reporting**: Monthly tracking of policy compliance metrics

**The SOC 2 audit**:

When the SOC 2 auditor arrived in May, James presented the complete policy framework:
- 10 formal policies covering all material security areas
- Evidence of policy communication and training
- Documented [[exception-process]] for policy violations
- Incident response procedures with examples
- Vendor assessment results
- Access control review documentation

The auditor was impressed. The company had implemented a mature policy framework in four months. The final SOC 2 report included only minor findings (all in the "remediation not required" category), and the company received a clean audit opinion.

More importantly, the policy framework became the foundation for scaling security. As the company grew to 1000+ employees over the next two years, the policies provided consistent governance. New employees understood security expectations. Departments knew how to manage risk. The company could explain its security approach to customers confidently.

## What Went Right

- **Executive commitment**: Alex recognized that security policies were non-negotiable for a company managing customer data. He prioritized them appropriately.
- **Stakeholder engagement**: Policies were drafted with input from department heads, ensuring they were practical and addressed real business needs.
- **[[Policy-lifecycle]] governance**: Establishing who owns each policy, when it's reviewed, and how exceptions are managed prevented policies from becoming stale artifacts.
- **Soft rollout**: Testing policies with department heads before company-wide rollout allowed for refinement and reduced resistance.
- **Evidence gathering**: The team didn't just write policies; they gathered evidence that policies were being followed (training records, access reviews, vendor assessments).

## What Could Go Wrong

- **Compliance checkbox mentality**: If the team had written policies just to "pass SOC 2" and then ignored them, the framework would have been useless and inconsistent.
- **Top-down policies without stakeholder buy-in**: If James had written policies in isolation without department head input, they would have been impractical and resisted.
- **No [[policy-lifecycle]] maintenance**: Many companies write policies and never update them. A 2022 policy in 2025 is likely obsolete. Scheduled review prevents drift.
- **[[Exception-process]] ignored**: If policies had no clear [[exception-process]], they would have been either too strict (blocking legitimate business) or ignored entirely. Exceptions with documented risk assessment maintain policy credibility.
- **No training or communication**: Writing a policy doesn't implement it. People must know what's expected, understand why it matters, and be trained on compliance.

## Key Takeaways

- **[[Security-policies]] are foundational governance**: You can't scale security without policies. They establish expectations, define roles and responsibilities, and create accountability.
- **[[Policy-lifecycle]] requires scheduled review and updates**: Policies written once and never updated become stale and eventually ignored. Schedule annual reviews and update when business or threat landscape changes.
- **[[Exception-process]] is part of policy governance**: If people can't request exceptions with documented risk assessment, they'll either break the policy secretly or be blocked from legitimate business. Clear exception process maintains policy credibility.
- **Stakeholder engagement drives better policies**: Policies written with department head input are more practical, more likely to be followed, and reflect real business needs rather than security team assumptions.
- **Evidence of compliance matters**: Documentation that training was completed, access was reviewed, vendors were assessed, and [[exception-process]] was followed are what auditors look for. Policy implementation, not just policy writing.

## Related Cases

- [[case-governance]] — Governance structures that oversee policy frameworks
- [[case-compliance]] — How policies support regulatory compliance
- [[case-security-awareness-training]] — Training that communicates and enforces policies
