---
title: "Compliance"
description: "Compliance ensures an organization meets the legal, regulatory, and contractual security requirements applicable to its operations."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/high
aliases:
  - "Compliance"
---

> [!eli5] ELI5: What is Compliance?
> It's like following the rules at school. There are rules about being quiet in the library, not running in the halls, and turning in homework on time. If you break them, you get in trouble. Compliance means a company follows all the rules it's supposed to -- rules from the government, rules from its own leaders, and rules it promised to follow when working with other companies. Breaking these rules can mean big fines or losing trust.
>
> > [!eli5] ELI5: Compliance (繁體中文版)
> > 合規就是「遵守法規」。不管你喜不喜歡，法律規定要怎麼保護資料，公司就得照做。
> >
> > ```ascii
> > [公司政策] ==(符合)==> [法律法規]
> > ```

## Overview

Compliance is the practice of adhering to laws, regulations, industry standards, and internal policies that govern how an organization handles data and security. Non-compliance can result in fines, legal action, loss of business, and reputational damage. A mature compliance program includes continuous monitoring, regular audits, and clear accountability.

## Key Concepts

- **[[regulatory-compliance|Regulatory compliance]]** — meeting requirements imposed by law (GDPR, HIPAA, SOX, GLBA, FERPA)
- **[[industry-standards|Industry standards]]** — voluntary or contractually required frameworks (PCI DSS, ISO 27001, NIST CSF)
- **[[contractual-compliance|Contractual compliance]]** — obligations defined in business agreements and SLAs
- **[[compliance-monitoring|Compliance monitoring]]** — ongoing checks to ensure controls remain effective and policies are followed
- **[[compliance-reporting|Compliance reporting]]** — documentation submitted to regulators or auditors demonstrating adherence
- **[[consequences-of-non-compliance|Consequences of non-compliance]]** — fines, sanctions, loss of certifications, lawsuits, reputational harm
- **[[internal-vs-external-compliance|Internal vs. external compliance]]** — internal policies may exceed regulatory minimums
- **[[compliance-automation|Compliance automation]]** — tools that continuously assess configurations against baselines and flag deviations
- **[[geographic-considerations|Geographic considerations]]** — different jurisdictions have different requirements; data sovereignty matters
- **[[gdpr|GDPR]]** — EU regulation; applies to any organization handling EU citizens' data regardless of location; fines up to 4% of annual global revenue
- **[[pci-dss|PCI DSS]]** — Payment Card Industry Data Security Standard; 12 requirements for handling cardholder data
- **[[hipaa|HIPAA]]** — US regulation protecting health information (PHI); requires administrative, physical, and technical safeguards

## Exam Tips

> [!tip] Remember
> Compliance != security. You can be compliant and still insecure. The exam tests whether you know which regulation applies to which industry: HIPAA = healthcare, PCI DSS = payment cards, GDPR = EU personal data, SOX = financial reporting.

## Connections

- Relies on [[audits-and-assessments]] to verify that controls satisfy regulatory requirements
- Enforced through [[hardening]] practices that bring systems into alignment with compliance baselines
- Driven by external [[regulations-and-frameworks]] that define the specific requirements organizations must meet
- See also [[governance]] for the organizational structure that enables compliance

## Practice Questions

> [!qbank]- Q-Bank: Compliance (4 Questions)
>
> **Q1.** A US-based online retailer begins accepting payments from customers in the European Union. Which regulation MOST likely introduces new compliance obligations for this company?
>
> A. HIPAA
> B. SOX
> C. GDPR
> D. FERPA
>
> > [!answer]- Show Answer
> > **C. GDPR**
> >
> > [[gdpr|GDPR]] applies to any organization that processes personal data of EU residents, regardless of where the company is headquartered. HIPAA (A) covers healthcare information, not retail. SOX (B) governs financial reporting integrity for publicly traded companies. FERPA (D) protects student education records.
>
> **Q2.** A company passes its annual security audit and achieves full compliance with PCI DSS. Three months later, it suffers a data breach due to an unpatched server. This scenario BEST illustrates which concept?
>
> A. Compliance automation eliminates all risk
> B. Compliance does not equal security
> C. External audits are unreliable
> D. PCI DSS standards are insufficient
>
> > [!answer]- Show Answer
> > **B. Compliance does not equal security**
> >
> > [[compliance|Compliance]] means meeting a defined set of requirements at a point in time, but it does not guarantee security against all threats. An organization can be compliant and still have vulnerabilities. Compliance automation (A) helps but cannot eliminate all risk. External audits (C) are valid assessments but only capture a snapshot. PCI DSS (D) is a robust standard; the issue is that compliance is a minimum bar, not a security guarantee.
>
> **Q3.** A multinational corporation stores customer data in data centers across three countries. The legal team warns that data handling requirements differ by location. Which compliance consideration is this an example of?
>
> A. Contractual compliance
> B. Compliance monitoring
> C. Geographic considerations
> D. Industry standards
>
> > [!answer]- Show Answer
> > **C. Geographic considerations**
> >
> > [[geographic-considerations|Geographic considerations]] address the fact that different jurisdictions impose different regulatory requirements, including data sovereignty laws. Contractual compliance (A) covers obligations in business agreements, not jurisdictional differences. Compliance monitoring (B) is the process of checking controls, not a type of requirement. Industry standards (D) apply across geographies and are not specific to jurisdictional variations.
>
> **Q4.** An organization's security team deploys a tool that continuously scans system configurations against CIS benchmarks and sends alerts when deviations are detected. This approach BEST represents which compliance concept?
>
> A. Compliance reporting
> B. Compliance automation
> C. Regulatory compliance
> D. Internal vs. external compliance
>
> > [!answer]- Show Answer
> > **B. Compliance automation**
> >
> > [[compliance-automation|Compliance automation]] uses tools to continuously assess configurations against baselines and flag deviations without manual intervention. Compliance reporting (A) is the documentation submitted to auditors, not the continuous scanning itself. Regulatory compliance (C) refers to meeting legal requirements, which this tool supports but does not specifically describe. Internal vs. external compliance (D) distinguishes between internal policies and regulatory requirements, which is unrelated to the automated scanning approach.

## Scenario

> See [[case-compliance]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [5.4 – Compliance](https://www.youtube.com/watch?v=KiEptGbnEBc&list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv&index=116)
