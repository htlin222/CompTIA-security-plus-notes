---
title: "Regulations and Frameworks"
description: "Key regulations and security frameworks that organizations use to structure their security programs and meet legal requirements."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/high
aliases:
  - "Regulations and Frameworks"
---

> [!eli5] ELI5: What are Regulations and Frameworks?
> Regulations are like traffic laws -- the government says you must stop at red lights, and you'll get a ticket if you don't. Frameworks are more like a coach's playbook -- a set of best plays you can choose to follow to win the game. Companies use both: they have to follow the laws (regulations), and they choose proven playbooks (frameworks) to build a strong security program. Together, these give the company a clear set of instructions to keep data safe.

## Overview

Regulations are legally binding requirements imposed by governments, while frameworks are structured best-practice guidelines that organizations adopt voluntarily or as part of contractual obligations. Together, they provide the blueprint for building and measuring a security program. The SY0-701 exam requires familiarity with major regulations and frameworks and when each applies.

## Key Concepts

- **[[nist-cybersecurity-framework-csf|NIST Cybersecurity Framework (CSF)]]** — Identify, Protect, Detect, Respond, Recover; voluntary, widely adopted in the US
- **[[nist-sp-800-53|NIST SP 800-53]]** — comprehensive catalog of security and privacy controls for federal systems
- **[[iso-27001-27002|ISO 27001 / 27002]]** — international standard for information security management systems (ISMS); 27001 is certifiable
- **[[gdpr|GDPR]]** — EU regulation protecting personal data; applies to any org processing EU residents' data; heavy fines
- **[[hipaa|HIPAA]]** — US law protecting health information (PHI); applies to covered entities and business associates
- **[[pci-dss|PCI DSS]]** — payment card industry standard; required for any organization handling cardholder data
- **[[sox-sarbanes-oxley|SOX (Sarbanes-Oxley)]]** — US law requiring financial reporting integrity and internal controls
- **[[glba|GLBA]]** — US law requiring financial institutions to protect customer information
- **[[ferpa|FERPA]]** — US law protecting student education records
- **[[cis-controls|CIS Controls]]** — prioritized list of cybersecurity best practices (formerly SANS Top 20)
- **[[csa-cloud-controls-matrix-ccm|CSA Cloud Controls Matrix (CCM)]]** — cloud-specific security control framework
- **[[benchmarks-vs-frameworks|Benchmarks vs. frameworks]]** — benchmarks are specific configuration guides; frameworks are broader programs

## Exam Tips

> [!tip] Remember
> NIST CSF = voluntary framework, broad adoption. ISO 27001 = certifiable international standard. PCI DSS = mandatory for card data. HIPAA = healthcare. GDPR = EU data + right to be forgotten. Know which applies where.

## Connections

- Provides the external requirements that [[compliance]] programs must satisfy
- Works alongside [[governance]] to shape internal security policies and standards
- See also [[audits-and-assessments]] for how adherence to frameworks is verified

## Practice Questions

> [!qbank]- Q-Bank: Regulations and Frameworks (4 Questions)
>
> **Q1.** A US federal agency is required to implement a comprehensive set of security and privacy controls for its information systems. Which framework is the agency MOST likely required to follow?
>
> A. PCI DSS
> B. NIST SP 800-53
> C. ISO 27001
> D. CIS Controls
>
> > [!answer]- Show Answer
> > **B. NIST SP 800-53**
> >
> > [[nist-sp-800-53|NIST SP 800-53]] provides a comprehensive catalog of security and privacy controls specifically designed for federal information systems. PCI DSS (A) applies to organizations handling payment card data, not federal agencies specifically. ISO 27001 (C) is an international standard for ISMS that is certifiable but not mandated for US federal systems. CIS Controls (D) are prioritized best practices but are not the authoritative control set for federal agencies.
>
> **Q2.** A hospital's compliance officer needs to ensure that all systems handling patient records meet regulatory requirements. Which regulation applies MOST directly to this scenario?
>
> A. GDPR
> B. SOX
> C. HIPAA
> D. GLBA
>
> > [!answer]- Show Answer
> > **C. HIPAA**
> >
> > [[hipaa|HIPAA]] is the US law specifically designed to protect Protected Health Information (PHI) and applies to covered entities like hospitals. GDPR (A) protects EU personal data broadly but is not specific to healthcare in the US. SOX (B) governs financial reporting integrity for publicly traded companies. GLBA (D) requires financial institutions to protect customer financial information.
>
> **Q3.** A company wants to achieve an internationally recognized certification for its information security management system to build customer trust. Which standard should it pursue?
>
> A. NIST CSF
> B. CIS Controls
> C. ISO 27001
> D. CSA Cloud Controls Matrix
>
> > [!answer]- Show Answer
> > **C. ISO 27001**
> >
> > [[iso-27001-27002|ISO 27001]] is the international standard for ISMS that is certifiable, meaning organizations can undergo an audit and receive formal certification. NIST CSF (A) is a voluntary framework widely adopted in the US but does not offer formal certification. CIS Controls (B) are prioritized best practices without a certification program. CSA CCM (D) is cloud-specific and used as a supplementary framework, not a primary certification path.
>
> **Q4.** A security analyst is asked to explain the difference between the CIS Benchmarks and the NIST Cybersecurity Framework to a new team member. Which distinction is MOST accurate?
>
> A. CIS Benchmarks are legally required; NIST CSF is voluntary
> B. CIS Benchmarks provide specific configuration guides; NIST CSF is a broader program framework
> C. NIST CSF applies only to cloud environments; CIS Benchmarks apply to on-premises systems
> D. Both are identical in scope and purpose
>
> > [!answer]- Show Answer
> > **B. CIS Benchmarks provide specific configuration guides; NIST CSF is a broader program framework**
> >
> > [[benchmarks-vs-frameworks|Benchmarks vs. frameworks]] is a key distinction: benchmarks like CIS provide prescriptive, system-specific configuration guidance, while frameworks like NIST CSF provide a broad structure for organizing an entire security program. CIS Benchmarks are not legally required (A); they are voluntary best practices. NIST CSF is not limited to cloud (C); it applies across all environments. The two are fundamentally different in scope and purpose (D).

## Scenario

> See [[case-regulations-and-frameworks]] for a practical DevOps scenario applying these concepts.
