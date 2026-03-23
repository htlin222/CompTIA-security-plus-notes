---
title: "Case: The Board's New Demand — Governance Maturity Awakens"
description: "After an SEC inquiry, a newly public company's board demands quarterly cybersecurity risk briefings, forcing a CISO to build governance structures from scratch."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

DataVault Inc. had gone public six months earlier at a $2.4B valuation. The company provides cloud storage and collaboration tools to enterprises. The initial public offering went smoothly, but in January 2025, the Securities and Exchange Commission issued a Wells Notice following reports that the company had experienced an undetected data exfiltration incident affecting 8,400 customers' files. The breach hadn't occurred due to any software vulnerability—a contractor's AWS credentials had been compromised and used to access customer data.

The breach notification process had been slow, reactive, and poorly coordinated with legal. Customers weren't notified for 18 days after discovery. The company's initial SEC filing was vague about the incident's scope. By the time the SEC initiated its inquiry, multiple news outlets had covered the story, and class-action lawyers were filing suits.

One week after the Wells Notice was issued, the Board of Directors held an emergency session. The new Chairman, a former financial services executive named Robert Chen, was visibly angry. He turned to the newly promoted Chief Information Security Officer, Michelle Grant, and issued a directive: "Effective immediately, I want a formal quarterly cybersecurity risk briefing to this board. I want to know our critical vulnerabilities, our incident history, our regulatory exposure, our third-party risks, and our board-level oversight structure. And I want it professionally done—not slides your engineers threw together."

Michelle's stomach dropped. DataVault had never presented formal cybersecurity metrics to the board. The company had a CISO role (Michelle had just been promoted), but there was no [[governance-committees]], no [[board-and-executive-involvement]] in cybersecurity decisions, and no formal [[roles-and-responsibilities]] defined for security oversight. The current security metrics consisted of a single Excel spreadsheet with vulnerability counts and patch compliance percentages—numbers that Michelle would be embarrassed to present to the board of a public company.

She convened the security leadership team. Over the next two weeks, they conducted an assessment:

1. **No security governance structure**: There was no [[centralized-vs-decentralized-governance]] model documented. Security decisions were made ad hoc by Michelle in consultation with whoever happened to be involved with a given incident.

2. **No [[governance-committees]]**: The board had no cybersecurity committee. Risk decisions went to the audit committee, but that body didn't have cybersecurity expertise.

3. **Metrics were not board-ready**: The vulnerability count alone wasn't strategic information. The board needed to understand [[risk-management]] priorities, [[recovery-time-objective-rto]] for critical systems, third-party risk exposure, and regulatory compliance status.

4. **No [[monitoring-and-reporting]] cadence**: There was no established process for reporting security incidents, metrics, or strategic concerns to executive leadership, let alone the board.

5. **[[Security-policies]] were incomplete**: While technical controls existed, many policies hadn't been formally documented, hadn't been through [[policy-lifecycle]] reviews, and hadn't been tied to [[regulations-and-frameworks]].

Michelle proposed a governance overhaul. Over the next eight weeks, she:

1. **Established a Security Committee of the Board**: Appointed three board members (one with cybersecurity background, one with risk management background, one with legal background) to a formal Security Committee that would meet quarterly (with ad hoc calls for serious incidents).

2. **Defined [[roles-and-responsibilities]]**: Created a security organizational structure with clear accountability. Michelle was the CISO reporting to the Chief Operating Officer, with a dedicated security team organized by function (identity and access management, application security, infrastructure, incident response, third-party risk, and compliance).

3. **Built a [[risk-management]] framework**: Implemented a risk register that tracked:
   - Critical vulnerabilities with remediation timelines
   - Third-party risk assessments for all significant vendors
   - Compliance gaps against SOC 2, ISO 27001, and relevant frameworks
   - Historical incidents with lessons learned
   - [[recovery-time-objective-rto]] and [[recovery-point-objective-rpo]] for critical systems

4. **Developed board-level metrics dashboard**: Created a quarterly briefing document that included:
   - Executive summary of security posture (qualitative assessment)
   - Heat map of critical risks with trend analysis
   - Incident summary (number, severity, response time)
   - Third-party risk overview
   - Compliance and regulatory status
   - Investment recommendations

5. **Documented [[security-policies]] and [[policy-lifecycle]]**: Created or formalized policies covering:
   - Access control and [[identity-management]]
   - Incident response and [[business-continuity]]
   - Third-party risk management and [[vendor-assessment]]
   - Data protection and [[data-classification]]
   - Vulnerability management

6. **Clarified [[due-diligence-vs-due-care]] expectations**: Documented what the company was doing to maintain security (due care) and what it would do if things went wrong (due diligence).

At the first quarterly Security Committee meeting in April, Michelle presented her governance structure, the risk register, and the metrics dashboard. The board was impressed. Robert Chen asked tough questions about third-party risk (after the contractor incident), about the company's ability to detect similar attacks in the future, and about the [[recovery-time-objective-rto]] for the main customer data systems.

By the third quarterly briefing, the board had elevated cybersecurity from "IT problem" to "business risk" in board discussions. The Audit Committee began connecting cybersecurity metrics to financial control effectiveness. Cybersecurity investments started being approved as strategic rather than operational.

The SEC inquiry eventually settled with an undertaking to implement enhanced cybersecurity governance—which DataVault had already done. The newfound governance structure became a competitive differentiator, and the company could now credibly demonstrate board-level oversight to customers and regulators.

## What Went Right

- **Board mandate drove urgency**: When the board demanded governance structure, it became a business priority, not a security team wish list.
- **Expertise-based committee structure**: The Security Committee included board members with cybersecurity, risk, and legal backgrounds, ensuring informed oversight.
- **Risk register as central artifact**: A formalized [[risk-management]] register that tracked both strategic and tactical issues became the source of truth for board discussions.
- **[[Due-diligence-vs-due-care]] clarity**: By documenting what the company was doing proactively (due care) and what would happen in response to incidents (due diligence), Michelle established accountability.
- **Metrics aligned to business impact**: Board-level dashboards focused on what matters to executives (incident trends, third-party risk, regulatory exposure, investment ROI), not technical details.

## What Could Go Wrong

- **No [[board-and-executive-involvement]]**: Many companies try to manage cybersecurity entirely through technical teams without board oversight. When breaches happen, the lack of documented governance becomes regulatory liability.
- **[[Centralized-vs-decentralized-governance]] drift**: If security decisions aren't formally assigned to specific people or committees, authority becomes unclear and decisions become political rather than risk-driven.
- **Metrics without [[monitoring-and-reporting]]**: Building metrics is only half the battle. They must be reported on a defined schedule (quarterly for boards) with clear ownership for discussing trends.
- **[[Policy-lifecycle]] neglect**: Policies created once and never updated become stale and unenforceable. Governance should include a policy review schedule (usually annual).
- **Third-party risk ignored at board level**: This was DataVault's specific failure. The contractor credential compromise was a third-party risk that should have been a board-level discussion topic. [[governance-committees]] must include third-party risk oversight.

## Key Takeaways

- **[[Board-and-executive-involvement]] in cybersecurity is now non-negotiable**: Public companies, regulated entities, and large enterprises must have board-level cybersecurity oversight. This is becoming standard governance expectation.
- **[[Governance-committees]] focused on security accelerate decision-making**: A dedicated Security Committee removes cybersecurity from the audit committee's overloaded agenda and ensures expert oversight.
- **[[Risk-management]] registers must be board-facing**: The board doesn't need to know vulnerability counts; they need to know risk trajectory, strategic threats, and third-party exposure.
- **[[Roles-and-responsibilities]] must be explicit in writing**: "Someone should handle that" never works. Governance requires written clarity about who is accountable for what security decisions.
- **[[Security-policies]] and [[policy-lifecycle]] are controls**: Policies aren't administrative overhead. They establish accountability, consistency, and the foundation for [[due-diligence-vs-due-care]] defense.

## Related Cases

- [[case-compliance]] — How governance structures support compliance requirements
- [[case-risk-management]] — Building risk registers and governance cadences
- [[case-security-policies]] — Implementing the policies that governance structures oversee
