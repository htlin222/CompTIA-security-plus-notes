---
title: "Audits and Assessments"
description: "Audits and assessments evaluate the effectiveness of security controls and verify compliance with policies, standards, and regulations."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/high
aliases:
  - "Audits and Assessments"
---

> [!eli5] ELI5: What are Audits and Assessments?
> Think of a school health inspection. Someone comes in to check that the cafeteria is clean, the fire exits work, and the playground is safe. An audit is like that official inspection -- someone with a checklist making sure everything meets the rules. An assessment is more like a teacher walking around the school looking for anything that could be improved, even stuff not on the checklist. Both help make sure the school (or a company's computers and data) stays safe and follows the rules.

## Overview

Audits and assessments are systematic evaluations of an organization's security posture. Audits are formal, often conducted by third parties, and measure compliance against specific standards. Assessments are broader evaluations that identify gaps and recommend improvements. Both are essential for maintaining accountability and demonstrating due diligence to regulators and stakeholders.

## Key Concepts

- **[[internal-audit|Internal audit]]** — conducted by the organization's own audit team; provides ongoing assurance
- **[[external-audit|External audit]]** — performed by an independent third party; required for certifications and regulatory compliance
- **[[regulatory-audit|Regulatory audit]]** — mandated by a governing body (e.g., PCI QSA audit for PCI DSS compliance)
- **Assessment types:**
  - **Vulnerability assessment** — identifies known weaknesses using automated scanning tools
  - **Penetration test** — simulated attack to exploit vulnerabilities and test defenses
  - **Risk assessment** — evaluates likelihood and impact of threats
  - **Security posture assessment** — holistic review of the organization's overall security state
- **[[audit-scope|Audit scope]]** — defines what systems, processes, and controls are being examined
- **[[evidence-collection|Evidence collection]]** — logs, configurations, policies, interviews, and observations gathered during audits
- **[[findings-and-remediation|Findings and remediation]]** — audit results include findings (issues) and recommendations with timelines for remediation
- **[[soc-reports|SOC reports]]** — SOC 1 (financial controls), SOC 2 (security/availability/confidentiality), SOC 3 (public summary)
- **[[attestation|Attestation]]** — formal declaration by an auditor that controls are operating effectively

## Exam Tips

> [!tip] Remember
> External audits are more authoritative than internal audits for compliance. SOC 2 Type II covers a time period and is preferred over Type I (point-in-time). Penetration tests go further than vulnerability assessments by actually exploiting flaws.

## Connections

- Validates that [[compliance]] requirements are being met through independent verification
- Informs [[risk-management]] by identifying gaps and new risks discovered during evaluation
- See also [[regulations-and-frameworks]] for the specific standards against which audits measure
- Related to [[hardening]] as audit findings often drive remediation of system configurations

## Practice Questions

> [!qbank]- Q-Bank: Audits and Assessments (4 Questions)
>
> **Q1.** A financial services company needs to demonstrate to regulators that its security controls have been operating effectively over the past six months. Which type of report would BEST satisfy this requirement?
>
> A. SOC 2 Type I
> B. SOC 2 Type II
> C. SOC 3
> D. Internal vulnerability scan report
>
> > [!answer]- Show Answer
> > **B. SOC 2 Type II**
> >
> > [[soc-reports|SOC 2 Type II]] covers control effectiveness over a defined time period, which is exactly what regulators need to see for ongoing assurance. SOC 2 Type I (A) only evaluates controls at a single point in time and does not demonstrate sustained operation. SOC 3 (C) is a general-use public summary without the detail regulators require. An internal vulnerability scan report (D) shows technical findings but does not attest to the effectiveness of security controls as a whole.
>
> **Q2.** An organization's CISO wants to determine whether an attacker could actually exploit the weaknesses found in a recent automated scan. What should the security team perform NEXT?
>
> A. Risk assessment
> B. Security posture assessment
> C. Penetration test
> D. Another vulnerability assessment with different tools
>
> > [!answer]- Show Answer
> > **C. Penetration test**
> >
> > A [[audits-and-assessments|penetration test]] goes beyond identifying vulnerabilities by actively attempting to exploit them, confirming real-world impact. A risk assessment (A) evaluates likelihood and impact but does not prove exploitability. A security posture assessment (B) is a broad review, not focused on exploitation. Running another vulnerability assessment (D) would only find more weaknesses without confirming whether existing ones are exploitable.
>
> **Q3.** A mid-size company is preparing for its first external audit. The audit team requests documentation including system configurations, access control lists, and policy documents. Which audit concept does this activity PRIMARILY represent?
>
> A. Attestation
> B. Findings and remediation
> C. Evidence collection
> D. Audit scope definition
>
> > [!answer]- Show Answer
> > **C. Evidence collection**
> >
> > [[evidence-collection|Evidence collection]] is the process of gathering logs, configurations, policies, and other artifacts that auditors examine to evaluate controls. Attestation (A) is the formal declaration issued after the audit is complete. Findings and remediation (B) are the output of the audit, not the input. Audit scope definition (D) determines what will be examined but does not involve gathering the actual documentation.
>
> **Q4.** A healthcare organization conducts quarterly security reviews using its own compliance team but has never engaged an outside firm. A new regulation now requires independent verification of controls. Which assessment approach must the organization add?
>
> A. Increased frequency of internal audits
> B. Automated compliance monitoring
> C. External audit by an independent third party
> D. Self-assessment questionnaires
>
> > [!answer]- Show Answer
> > **C. External audit by an independent third party**
> >
> > [[external-audit|External audits]] provide independent, objective verification that cannot be achieved through internal processes alone, which is what the regulation requires. Increasing internal audit frequency (A) does not address the independence requirement. Automated compliance monitoring (B) improves efficiency but is still an internal control. Self-assessment questionnaires (D) are completed by the organization itself and lack the independent verification regulators demand.

## Scenario

> See [[case-audits-and-assessments]] for a practical DevOps scenario applying these concepts.
