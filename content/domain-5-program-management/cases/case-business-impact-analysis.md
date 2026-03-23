---
title: "Case: The Payroll Surprise — Business Impact Analysis Uncovered"
description: "A CFO's request for downtime cost analysis reveals a critical infrastructure dependency on an aging single-server system with no redundancy and a 72-hour replacement SLA."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

Marcus Chen, the CFO of a mid-sized B2B software company with 450 employees and $120M in annual revenue, posed a seemingly straightforward question to the Chief Information Security Officer in a quarterly meeting: "What's our cost of downtime, hour by hour, for each business unit?" The question came from the audit committee, which was developing an enterprise risk framework and needed to quantify financial impact.

The CISO, Jordan Ramirez, thought it would be a simple exercise: compile uptime requirements, estimate productivity loss, and create a heat map. She assembled her team for a [[business-impact-analysis]] exercise, expecting to wrap it in two weeks. What she discovered instead was architectural fragility that had been silently embedded in the company's operations for six years.

The first shock came when mapping dependencies. The payroll system—absolutely critical for employee morale, legal compliance (direct deposit, tax withholding), and basic operations—depended on a single on-premises Windows Server 2012 R2 machine running ADP Workforce Now. That server had never been virtualized, never been replicated, and was physically located in a leased cabinet in a shared data center in New Jersey. The network diagram showed no redundancy, no clustering, no failover capability. The hardware maintenance contract had a 72-hour parts replacement SLA. Translation: a hard drive failure meant payroll would be down for three days.

Jordan pulled the historical uptime logs. The server had been up for 1,847 consecutive days. It was a ghost server that everyone had forgotten existed, kept alive by institutional memory rather than design. The [[maximum-tolerable-downtime-mtd]] for payroll was effectively zero hours—you cannot delay employee compensation without immediate legal and morale consequences. Yet the system had no [[mean-time-between-failures-mtbf]] planning, no [[mean-time-to-repair-mttr]] capability, and certainly no [[recovery-time-objective-rto]] or [[recovery-point-objective-rpo]] documented.

The second problem: dependencies weren't isolated to individual systems. The expense reporting system depended on the payroll system for employee master data and hierarchical approval chains. The financial reporting system depended on expense data. The CRM system pulled commission calculations from payroll. A cascade began to emerge: if payroll went down for 72 hours, the entire revenue recognition process for the current quarter would fail, potentially making quarterly earnings reports late to investors.

When Jordan quantified the impact, she calculated:
- **Hour 1 of payroll outage**: $8,400/hour (direct deposit processing delays, legal exposure)
- **Hour 1-8**: Additional $3,200/hour (business operations slowdown, expense reporting blockage)
- **Hour 8-72**: Additional $12,000/hour (financial close delays, commission processing backlog, CRM unable to generate proposals)

A 72-hour outage would cost approximately **$876,000 in direct costs** plus immeasurable reputational damage and potential securities law violations if a quarterly report was delayed.

The CFO's eye widened. The entire conversation shifted. Suddenly, the $90,000 annual cost of a redundant payroll server cluster, a [[recovery-point-objective-rpo]] of 4 hours, and automated failover was not a cost—it was an insurance policy against a catastrophic risk. The [[business-continuity]] team was mobilized. Engineering began virtualizing the payroll system, implementing replication to a hot standby, and testing [[recovery-time-objective-rto]] and [[mean-time-to-recover-mttr]] metrics.

Within six months, the payroll system was protected by redundancy and could be recovered in under 15 minutes. The [[business-impact-analysis]] had transformed from an audit exercise into a strategic initiative that fundamentally improved operational resilience.

## What Went Right

- **CFO asked the right question**: By demanding quantified downtime costs, leadership created the incentive for a rigorous [[business-impact-analysis]].
- **Honest vulnerability assessment**: Jordan's team didn't downplay what they found; they mapped it clearly and escalated appropriately.
- **Dependency mapping discipline**: By following the [[critical-business-functions]] chain through multiple systems, the team identified the payroll [[single-point-of-failure-spof]] that would have remained hidden in a traditional infrastructure review.
- **Financial language**: Translating technical resilience needs into dollar impact made the business case irrefutable and prioritized resources appropriately.

## What Could Go Wrong

- **No dependency analysis**: Many organizations document individual system uptime requirements but never map how systems depend on each other. This causes a failure to identify critical [[single-point-of-failure-spof]] scenarios.
- **Guessing at downtime costs**: If Jordan had assumed payroll downtime was "low impact" without quantification, the fragility would have persisted until a real failure occurred.
- **Using [[mean-time-between-failures-mtbf]] without testing**: Just because a server has run for 1,800+ days doesn't mean it's reliable. Luck is not a strategy. [[mean-time-to-repair-mttr]] is what matters in a crisis.
- **Ignoring [[recovery-point-objective-rpo]] and [[recovery-time-objective-rto]]**: Without explicit targets, different teams optimize for different goals, and critical systems end up unprotected.
- **No [[risk-management]] framework**: Without a [[business-impact-analysis]], this risk would have remained invisible until the server failed during a critical business period.

## Key Takeaways

- **[[Business-impact-analysis]] requires rigorous dependency mapping**: Don't just ask "can system X go down?" Ask "what else breaks if system X goes down?" and "what's the cost chain?"
- **[[Recovery-time-objective-rto]] and [[recovery-point-objective-rpo]] are driven by business impact, not IT preference**: If the business cannot tolerate a 72-hour outage (and payroll businesses cannot), design [[resilience-and-redundancy]] accordingly.
- **[[Critical-business-functions]] often depend on unsexy legacy systems**: A forgotten on-prem server can be more critical than your cloud-native microservices. Map everything.
- **[[Maximum-tolerable-downtime-mtd]] of zero requires redundancy**: For truly business-critical functions like payroll, payroll, HR records, or revenue recognition, zero downtime is often the actual requirement.
- **Quantify financial impact to drive investment**: IT budgets are scarce. Business impact quantification in CFO language (dollars, not minutes) wins funding battles for resilience improvements.

## Related Cases

- [[case-business-continuity]] — Understanding how [[business-impact-analysis]] drives BCP priorities
- [[case-disaster-recovery]] — Implementing the recovery procedures that BIA identifies
- [[case-risk-management]] — Using BIA to populate your risk register with prioritized scenarios
