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

## Scenario

> See [[case-dlp]] for a practical DevOps scenario applying these concepts.
