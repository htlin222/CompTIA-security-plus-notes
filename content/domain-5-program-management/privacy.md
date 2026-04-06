---
title: "Privacy"
description: "Privacy focuses on the proper collection, use, storage, and disposal of personal information in compliance with legal requirements."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/medium
aliases:
  - "Privacy"
  - "Data Privacy"
---

> [!eli5] ELI5: What is Privacy?
> You know how your diary is yours, and nobody should read it without your permission? Privacy in the computer world means people get to control who sees their personal information -- like their name, address, or health records. Companies that collect this information have to follow rules about how they use it, store it, and who they share it with. It's about respecting that your personal stuff belongs to you.
>
> > [!eli5] ELI5: Privacy (繁體中文版)
> > 隱私就是「保護個人秘密」。確保公司不會亂用你的個人資料，並且只在有需要的時候才看。
> >
> > ```ascii
> > [個人資料] --|隱私權政策|--> [安全存取]
> > ```

## Overview

Privacy in information security refers to an individual's right to control how their personal information is collected, used, shared, and disposed of. Organizations must implement technical and administrative controls to protect personally identifiable information (PII) and comply with privacy regulations. Privacy is distinct from security: security protects data from unauthorized access, while privacy governs how authorized parties handle personal data.

## Key Concepts

- **[[pii-personally-identifiable-information|PII (Personally Identifiable Information)]]** — data that can identify an individual (name, SSN, email, biometrics)
- **[[phi-protected-health-information|PHI (Protected Health Information)]]** — health-related PII governed by HIPAA
- **Privacy principles:**
  - **Purpose limitation** — collect data only for a stated purpose
  - **Data minimization** — collect only what is necessary
  - **Consent** — obtain permission before collecting personal data
  - **Right to be forgotten (erasure)** — GDPR grants individuals the right to request data deletion
  - **Data portability** — individuals can request their data in a usable format
- **[[privacy-impact-assessment-pia|Privacy Impact Assessment (PIA)]]** — evaluates how a project or system will affect individual privacy
- **[[privacy-by-design|Privacy by design]]** — embedding privacy controls into systems from the beginning, not as an afterthought
- **[[anonymization-vs-pseudonymization|Anonymization vs. pseudonymization]]** — anonymization is irreversible; pseudonymization replaces identifiers but can be reversed with a key
- **[[data-breach-notification|Data breach notification]]** — regulations often require notifying affected individuals and authorities within a set timeframe
- **[[data-sovereignty|Data sovereignty]]** — data is subject to the laws of the country where it is stored
- **Tokenization** — substituting sensitive data elements with non-sensitive tokens
- **Data masking** — obscuring specific data within a database to protect it in non-production environments

## Exam Tips

> [!tip] Remember
> Anonymization cannot be reversed; pseudonymization can. GDPR requires data breach notification within 72 hours. Privacy by design = build it in from the start, not bolted on later.

## Connections

- Governed by [[regulations-and-frameworks]] such as GDPR, HIPAA, and GLBA which define privacy requirements
- Closely related to [[data-classification]] which identifies and labels personal data requiring privacy protections
- See also [[compliance]] for how privacy requirements are monitored and enforced

## Practice Questions

> [!qbank]- Q-Bank: Privacy (4 Questions)
>
> **Q1.** A healthcare application development team replaces patient names with randomly generated tokens in their test database. The mapping between tokens and real names is stored in a separate secured system. This technique is BEST described as:
>
> A. Anonymization
> B. Pseudonymization
> C. Data minimization
> D. Data masking
>
> > [!answer]- Show Answer
> > **B. Pseudonymization**
> >
> > [[anonymization-vs-pseudonymization|Pseudonymization]] replaces identifying information with artificial identifiers while maintaining a reversible mapping. Since the token-to-name mapping is preserved, the data can be re-identified. Anonymization (A) is irreversible -- no mapping exists to reconnect data to individuals. Data minimization (C) is about collecting only necessary data, not replacing identifiers. Data masking (D) obscures data in place but typically refers to display-level obfuscation rather than a token-based replacement with a separate key.
>
> **Q2.** A European customer requests that an online retailer delete all personal data associated with their account. Under which privacy principle is the company MOST likely obligated to comply?
>
> A. Purpose limitation
> B. Data portability
> C. Right to be forgotten (erasure)
> D. Consent
>
> > [!answer]- Show Answer
> > **C. Right to be forgotten (erasure)**
> >
> > The [[privacy|right to be forgotten]] under GDPR grants individuals the right to request deletion of their personal data. Purpose limitation (A) restricts data collection to stated purposes but does not address deletion requests. Data portability (B) allows individuals to receive their data in a usable format, not delete it. Consent (C) is about obtaining permission before collecting data, not post-collection deletion.
>
> **Q3.** A software company is building a new mobile application that will collect user location data. The privacy officer recommends integrating consent mechanisms and data minimization controls into the initial design. This approach BEST represents which privacy concept?
>
> A. Privacy Impact Assessment
> B. Data breach notification
> C. Privacy by design
> D. Data sovereignty
>
> > [!answer]- Show Answer
> > **C. Privacy by design**
> >
> > [[privacy-by-design|Privacy by design]] means embedding privacy controls into systems from the beginning rather than adding them later. Building consent and minimization into the initial design is the textbook example. A Privacy Impact Assessment (A) evaluates how a project affects privacy but is an assessment, not a design approach. Data breach notification (B) is about responding to incidents, not building privacy into systems. Data sovereignty (D) concerns the laws of the country where data is stored.
>
> **Q4.** A multinational company stores EU customer data on servers located in the United States. The legal team raises concerns that US law enforcement could access this data under US jurisdiction. Which privacy concept does this concern PRIMARILY relate to?
>
> A. Data minimization
> B. Data sovereignty
> C. Anonymization
> D. Purpose limitation
>
> > [!answer]- Show Answer
> > **B. Data sovereignty**
> >
> > [[data-sovereignty|Data sovereignty]] means data is subject to the laws of the country where it is stored. Storing EU data in the US exposes it to US legal jurisdiction, creating a conflict with EU privacy expectations. Data minimization (A) addresses the volume of data collected, not its geographic location. Anonymization (C) makes data non-identifiable but does not resolve jurisdictional concerns. Purpose limitation (D) restricts how data is used, not where it is stored.

## Scenario

> See [[case-privacy]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [5.4 – Privacy](https://www.youtube.com/watch?v=KiEptGbnEBc&list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv&index=117)
