---
title: "Case: The Framework Explosion — Mapping Control Requirements"
description: "A cloud-native fintech must simultaneously align with NIST CSF, SOC 2, PCI DSS, and ISO 27001 for different customer segments while managing ad hoc customer questionnaires."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

FinanceCore is a Series C fintech startup that provides payment processing, invoice management, and financial reconciliation APIs to mid-market businesses. The company serves diverse customer segments: retailers (subject to PCI DSS), healthcare organizations (subject to HIPAA), regulated financial institutions (subject to SOC 2 Type II), and public companies (requiring NIST CSF alignment for cybersecurity supply chain requirements).

In September 2024, the Chief Compliance Officer, Patricia Stein, was buried under a mountain of compliance questionnaires. Each customer segment wanted different certifications:

- **Retail customers** demanded PCI DSS Level 1 compliance (because FinanceCore processes payment cards)
- **Healthcare customers** demanded HIPAA compliance (for their customers' PHI)
- **Institutional customers** demanded SOC 2 Type II reports
- **Government customers** demanded NIST SP 800-171 compliance for defense subcontractors

But there was another layer: the enterprise customers were asking individual security questionnaires. One customer demanded ISO 27001 certification. Another demanded ISO 27018 (cloud privacy). Another wanted confirmation of CIS Controls compliance. Another wanted proof that FinanceCore aligned with the Cloud Security Alliance Cloud Controls Matrix (CCM).

Patricia had the same conversation weekly:
**Customer**: "We need you to complete our compliance questionnaire before we sign the contract."
**Patricia**: "We're PCI DSS, SOC 2, and HIPAA compliant. Here are our certifications."
**Customer**: "That's great, but our procurement team won't accept that. Can you map your controls to [NIST CSF / ISO 27001 / CIS Controls / CSA CCM]?"
**Patricia**: "Sure, let me create that mapping for you." (Internal thought: "I've done this five times this month for different customers.")

Each mapping took 1-2 weeks of work because there was no central framework. The company had various policies and controls scattered across different systems:

- [[iso-27001-27002]] documentation in Google Docs
- [[pci-dss]] compliance matrix in Excel
- [[nist-sp-800-53]] control narrative scattered across security team wikis
- SOC 2 control evidence in Salesforce

When a customer asked "Show us your ISO 27001 A.12.1.1 control" or "Map your incident response process to NIST CSF," Patricia's team had to manually search through documents, reconstruct the narrative, and format it for that customer.

Patricia brought this problem to the CISO, Robert Martinez, and the CTO, Sarah Kim. The three of them mapped the situation:

**The problem**: FinanceCore had implemented solid security controls (access management, encryption, monitoring, incident response), but the company had no central [[benchmarks-vs-frameworks]] alignment system. They were answering the same questions differently for each framework because there was no "source of truth" for what controls existed and where evidence lived.

**The framework landscape**:

- [[pci-dss]]: 12 requirements, 78 controls → focused on payment card security
- [[hipaa]]: 18 requirements, 164 controls → focused on health data security
- [[nist-cybersecurity-framework-csf]]: 5 functions, 22 categories, ~200 practices → focused on overall cybersecurity governance
- [[iso-27001-27002]]: 114 controls across 14 areas → focused on information security management
- [[nist-sp-800-53]]: 180+ security controls → focused on federal information systems
- [[cis-controls]]: 18 safeguards → focused on critical security outcomes
- [[csa-cloud-controls-matrix-ccm]]: 197 controls → focused on cloud-specific security

Patricia realized that trying to maintain seven independent control frameworks was impossible. Instead, she proposed building a **Control Repository**: a single source of truth that listed every security control the company had implemented, what [[regulations-and-frameworks]] it addressed, what evidence existed, and when that evidence was last validated.

Over three months, Robert and Patricia worked with the security and compliance team to:

1. **Identify all implemented controls**: List every security control in practice:
   - [[access-control-models]] (role-based, attribute-based, least privilege)
   - Encryption (at rest, in transit, key management)
   - Authentication and MFA requirements
   - Encryption (at rest, in transit, key management)
   - Incident response procedures
   - Third-party risk management
   - Data classification and handling
   - Monitoring and logging
   - Backup and disaster recovery
   - And ~35 others

2. **Map controls to framework requirements**: For each implemented control, document which [[pci-dss]] requirement, [[hipaa]] rule, [[iso-27001-27002]] control, [[nist-cybersecurity-framework-csf]] practice, etc. it satisfied. One control often mapped to multiple frameworks.

3. **Evidence management**: For each control, identify where documentation lives (policies, procedures, audit logs, certificates, test results).

4. **Customer-specific views**: Build customizable reports that showed customers exactly which controls mapped to their required framework:
   - A retail customer got: "Here's how our controls map to PCI DSS Level 1"
   - A healthcare customer got: "Here's how our controls map to HIPAA"
   - An ISO-focused customer got: "Here's how our controls map to ISO 27001"

5. **Single certification strategy**: Instead of pursuing separate [[pci-dss]], SOC 2, and ISO 27001 certifications (which would have been expensive and redundant), FinanceCore pursued **ISO 27001 certification as the master framework**. This single certification satisfied most enterprise customers. For PCI and HIPAA, the team maintained compliance through internal audits but didn't pursue third-party certifications (the certifications weren't cost-justified).

6. **Vendor questionnaire automation**: Patricia built a tool that would accept a customer questionnaire, match questions to controls in the repository, and auto-generate responses with links to evidence. For the 20% of custom questions that didn't fit the template, the team answered manually.

By January 2025, the system was operational:

- **PCI DSS**: Internally maintained (12-week audit cycle)
- **HIPAA**: Internally maintained with annual independent audit
- **ISO 27001**: Third-party certified, maintained through annual surveillance audits
- **SOC 2 Type II**: Performed by independent auditor annually
- **NIST CSF**: Mapped within the control repository, used for government customer responses
- **CIS Controls**: Mapped within the control repository
- **CSA CCM**: Mapped within the control repository

When a customer asked "Can you map your controls to XYZ framework?" Patricia could now respond: "Yes, here's the mapping from our Control Repository, with links to relevant policies and audit evidence."

Customer onboarding time dropped from 2-3 weeks to 3-5 days. Patricia's team went from spending 60% of their time answering questionnaires to 20%.

## What Went Right

- **Recognition of the core problem**: Patricia didn't try to get better at maintaining seven separate frameworks. She identified that the real problem was lack of central control mapping.
- **Master framework strategy**: Pursuing ISO 27001 as the primary certification and mapping other frameworks to it eliminated certification redundancy.
- **[[benchmarks-vs-frameworks]] discipline**: The team understood that benchmarks like [[cis-controls]] describe what good looks like, while frameworks like ISO describe how to achieve it. Different audiences need different perspectives.
- **Evidence-driven approach**: Building the system around where evidence actually lives (policies, logs, audit reports) made maintenance feasible.
- **Automation where possible**: The questionnaire matching tool reduced manual work significantly.

## What Could Go Wrong

- **Attempting to maintain all frameworks equally**: Many companies try to be equally compliant with PCI, HIPAA, ISO 27001, NIST, CIS, and CSA CCM. This is expensive, error-prone, and creates inconsistencies.
- **Outdated control mappings**: If the Control Repository isn't maintained when controls change or frameworks update, the mappings become incorrect, creating audit findings.
- **Confusion of [[benchmarks-vs-frameworks]]**: Some teams treat [[cis-controls]] as a framework (it's not—it's a benchmark of critical safeguards). Others treat [[nist-sp-800-53]] as suitable for all organizations (it's designed for federal systems, not startups). Clarity on each framework's intent is essential.
- **Customer-by-customer customization**: Without a central repository, every customer request for "map to our framework" becomes a manual project, creating inconsistency and risk.
- **Missing [[compliance-automation]]**: If mappings and evidence links are manual, they drift. The system must automate what can be automated (evidence links, framework requirement tracking).

## Key Takeaways

- **Master framework approach reduces complexity**: Instead of maintaining seven separate compliance programs, identify the one framework that best fits your business (ISO 27001 for enterprises, PCI DSS for payment processors, HIPAA for healthcare) and make it master, then map other requirements to it.
- **Benchmarks-vs-frameworks serve different purposes**: Benchmarks like [[cis-controls]] describe "what good looks like." Frameworks like ISO describe "how to manage it." Use benchmarks to inform your control design; use frameworks for certification.
- **Control repositories are essential infrastructure**: A central system mapping security controls to [[regulations-and-frameworks]] requirements, with evidence links, enables efficient compliance reporting and reduces manual work.
- **Compliance-automation reduces questionnaire burden**: Tools that match customer questionnaires to your control repository and auto-generate responses save enormous time on customer onboarding.
- **Certification strategy matters**: Not every framework requires third-party certification. Strategic selection of which frameworks to certify (ISO, SOC 2) versus maintain internally (NIST CSF, CIS) optimizes cost.

## Related Cases

- [[case-compliance]] — Understanding individual framework requirements
- [[case-governance]] — Building governance structures that manage multiple frameworks
- [[case-audits-and-assessments]] — How frameworks define audit scope and evidence requirements
