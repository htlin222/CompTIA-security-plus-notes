---
title: "Case: The Vanishing Trail — Audits and Assessments in Action"
description: "A SOC 2 auditor discovers critical evidence gaps during a routine compliance audit, forcing a team to reconstruct six months of access reviews in two weeks."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

It was a Tuesday morning at TechFlow Analytics, a Series B fintech startup serving hedge funds, when the SOC 2 Type II auditor Melissa Chen walked into the conference room with a concerned expression. She'd been tasked with validating the company's control environment for the past 18 months, and she'd just discovered something alarming: there was no documented evidence of quarterly access reviews for the past six months.

The timing was brutal. The company had undergone a major GRC tool migration in September—moving from ServiceNow to a homegrown system to save costs—and during the transition, the audit logs and evidence artifacts for Q3 and Q4 had simply vanished into a black hole of incomplete backups and forgotten documentation. The [[compliance-reporting]] deadline was written in stone: 14 days until the final audit report was due to their largest customer, a $500M hedge fund that required SOC 2 Type II certification.

The Chief Information Security Officer, Marcus Webb, was in his office reviewing a CrowdStrike alert when he got the call. He immediately pulled together the access control team. They had exactly two weeks to reconstruct and document six months of access reviews—for approximately 280 employees, contractors, and service accounts spread across 47 systems. The old audit trail still existed in the decommissioned ServiceNow instance, but nobody had full admin access, and the company that managed the old system had been acquired three months earlier.

By noon, Marcus had escalated to legal. The [[evidence-collection]] team began a frantic audit of email inboxes, looking for any manager sign-offs on access reviews. What they found was a mix of informal approvals—some via Slack, some via email, many missing entirely. The real problem became clear as they dug deeper: the process documentation for what constituted a completed access review had never been formally written down. Did a Jira ticket count? A spreadsheet? An email? Three different managers had three different interpretations.

Marcus made a command decision. They would use the existing records—imperfect as they were—and create a detailed [[findings-and-remediation]] plan that would show management commitment to fixing the process going forward. The team worked through the night, rebuilding the audit trail from fragments, creating retroactive documentation, and implementing a new [[internal-audit]] schedule with automated reminders. Melissa would note in her report that controls were designed and operated effectively from Q1 forward, but that evidence management processes had been strengthened following the platform transition.

## What Went Right

- **Transparent escalation and rapid response**: Marcus immediately involved legal and communicated the gap to the auditor rather than attempting to hide the problem, demonstrating due-care and governance commitment.
- **Process documentation recovery**: The team leveraged email trails and existing system records to reconstruct a defensible audit trail, showing the practical application of [[evidence-collection]] fundamentals.
- **Remediation focus**: Rather than dwelling on past failures, the team implemented automated [[audit-scope]] controls and clear [[internal-audit]] procedures that would prevent recurrence—a key factor in the auditor's final assessment.
- **Stakeholder management**: By involving legal and being transparent with the customer, the company maintained trust and demonstrated mature [[regulatory-audit]] understanding despite the control gap.

## What Could Go Wrong

- **Cover-up approach**: If management had attempted to fabricate or backdated evidence, the auditor would likely have identified the inconsistencies and issued a management letter with significant findings, damaging customer relationships.
- **System migration without controls planning**: Failing to establish data migration and retention procedures during the GRC tool changeover created the evidence gap in the first place—a critical [[hardening]] oversight.
- **No [[attestation]] process**: Without formal sign-offs and clear procedures, there's no way to prove controls were operating. This is how audit findings become contractual breaches.
- **Inadequate [[regulations-and-frameworks]] alignment**: If the company hadn't understood SOC 2's requirements around [[evidence-collection]] and documentation, they wouldn't have known what "control operating" means, making the audit a compliance failure.

## Key Takeaways

- **Evidence is everything in audits**: [[external-audit]] credibility depends entirely on documented proof. Maintain audit trails from day one, especially across system migrations and [[compliance-monitoring]] activities.
- **Document the process, not just the outcome**: Clear procedures for what constitutes a completed access review, who must approve it, and how it's documented prevents disputes during [[attestation]].
- **Automate where possible**: Manual quarterly access reviews are human-dependent and easily forgotten. Automation ensures [[compliance]] consistency and reduces [[evidence-collection]] burden.
- **Plan for compliance during platform changes**: Any system migration should include data retention, audit log preservation, and testing of evidence export before decommissioning old tools.
- **Risk register matters**: Identifying this gap early during [[risk-management]] would have prevented the last-minute scramble. Regular [[risk-assessment]] cadences catch these issues before auditors do.

## Related Cases

- [[case-compliance]] — Understanding how compliance requirements drive audit expectations
- [[case-regulations-and-frameworks]] — Deep dive into SOC 2 and other frameworks that demand audit trails
- [[case-risk-management]] — How risk registers and [[evidence-collection]] procedures prevent audit surprises
- [[case-governance]] — Board-level understanding of audit findings and remediation priorities
