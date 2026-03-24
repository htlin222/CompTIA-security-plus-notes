---
title: "DLP"
description: "Data Loss Prevention systems detect and prevent unauthorized transmission or exfiltration of sensitive data."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/data
  - weight/medium
aliases:
  - "DLP"
  - "Data Loss Prevention"
---

> [!eli5] ELI5: What is DLP?
> Picture a guard standing at every exit of a building, checking bags to make sure nobody takes anything valuable out. DLP (Data Loss Prevention) works like that guard for your computer network. It watches emails, file transfers, and other ways data moves around, and if someone tries to send secret information outside the company -- whether on purpose or by accident -- it steps in and stops it.

## Overview

Data Loss Prevention (DLP) is a set of tools and policies designed to detect and prevent the unauthorized transfer of sensitive data outside the organization. DLP systems inspect data at rest, in motion, and in use to identify sensitive content based on patterns, keywords, classification labels, and policies. When a policy violation is detected, DLP can alert, block, encrypt, or quarantine the data.

## Key Concepts

- **DLP deployment types:**
  - **Network DLP** — monitors data in transit on the network; inspects email, web, file transfers
  - **Endpoint DLP** — installed on workstations and servers; monitors copy/paste, USB transfers, printing, screen captures
  - **Cloud DLP** — monitors data in cloud applications and storage; often integrated with CASB
- **Detection methods:**
  - **Pattern matching / regex** — detects credit card numbers, SSNs, and other structured data formats
  - **Keyword matching** — flags content containing specific words or phrases
  - **Document fingerprinting** — creates a hash of sensitive documents and detects copies or derivatives
  - **Classification-based** — enforces policies based on data classification labels and metadata
  - **Machine learning** — identifies sensitive content based on trained models
- **[[policy-actions|Policy actions:]]** alert, block, encrypt, quarantine, log, notify manager
- **Common use cases:**
  - Preventing email of unencrypted PII or PHI
  - Blocking USB transfers of classified documents
  - Detecting credit card numbers in cloud storage
  - Preventing source code from being uploaded to unauthorized repositories
- **[[false-positives|False positives]]** — DLP can generate many false positives; tuning is essential for operational effectiveness

## Exam Tips

> [!tip] Remember
> DLP monitors data in all three states: at rest, in transit, in use. Network DLP catches email and web exfiltration. Endpoint DLP catches USB and print. Cloud DLP integrates with CASB. Tuning is critical to reduce false positives.

## Connections

- Enforces the handling rules defined by [[data-classification]] and [[data-protection]] policies
- Often integrated with [[cloud-security]] tools like CASB for cloud data monitoring
- See also [[privacy]] for the regulatory drivers that make DLP necessary for protecting PII and PHI

## Practice Questions

> [!qbank]- Q-Bank: DLP (4 Questions)
>
> **Q1.** An employee accidentally attaches a spreadsheet containing customer Social Security numbers to an outbound email. Which DLP deployment type would MOST likely detect and block this before it leaves the organization?
>
> A. Endpoint DLP
> B. Network DLP
> C. Cloud DLP
> D. Database DLP
>
> > [!answer]- Show Answer
> > **B. Network DLP**
> >
> > [[dlp|Network DLP]] monitors data in transit on the network, including email traffic, and can detect and block outbound emails containing sensitive patterns like SSNs. Endpoint DLP (A) monitors actions on the workstation (USB, printing) but email inspection is primarily handled at the network level. Cloud DLP (C) monitors cloud applications, not on-premises email. Database DLP (D) is not a standard DLP deployment type.
>
> **Q2.** A security team implements DLP and immediately receives hundreds of alerts per day, most of which are not actual policy violations. Which action should the team take FIRST to address this?
>
> A. Disable the DLP system until a replacement is found
> B. Tune the DLP policies to reduce false positives
> C. Switch from pattern matching to keyword matching only
> D. Set all DLP policies to monitor-only mode permanently
>
> > [!answer]- Show Answer
> > **B. Tune the DLP policies to reduce false positives**
> >
> > [[false-positives|False positive]] tuning is essential for DLP operational effectiveness. Excessive alerts cause alert fatigue and reduce the value of the system. Disabling DLP (A) removes all protection. Switching to keyword-only detection (C) would reduce detection capability. Setting permanent monitor-only mode (D) never blocks actual violations, which defeats the purpose of DLP.
>
> **Q3.** A company discovers that employees are uploading proprietary source code to personal cloud storage accounts. Which combination of DLP controls would BEST prevent this?
>
> A. Network DLP with document fingerprinting
> B. Endpoint DLP with keyword matching only
> C. Cloud DLP integrated with CASB
> D. Network DLP with data classification labels only
>
> > [!answer]- Show Answer
> > **C. Cloud DLP integrated with CASB**
> >
> > [[dlp|Cloud DLP]] integrated with a [[cloud-security|CASB]] is BEST because CASB enforces policies between users and cloud services, and Cloud DLP monitors data in cloud applications. Network DLP with fingerprinting (A) could help but may not inspect encrypted uploads to cloud services. Endpoint DLP with keyword matching (B) is limited since source code may not contain specific keywords. Network DLP with classification labels only (D) assumes all source code is properly classified, which is often not the case.
>
> **Q4.** A DLP system uses a technique that creates a unique representation of sensitive documents and can detect when copies or modified versions are transmitted. Which detection method does this describe?
>
> A. Regular expression pattern matching
> B. Machine learning classification
> C. Document fingerprinting
> D. Keyword matching
>
> > [!answer]- Show Answer
> > **C. Document fingerprinting**
> >
> > [[dlp|Document fingerprinting]] creates a hash-based representation of sensitive documents and can detect copies or derivative versions. Regex pattern matching (A) detects structured data formats like credit card numbers, not document derivatives. Machine learning (B) classifies content based on trained models but is not specifically designed to detect document copies. Keyword matching (D) flags content containing specific terms but cannot detect modified copies of documents.

## Scenario

> See [[case-dlp]] for a practical DevOps scenario applying these concepts.
