---
title: "Retention and archival"
description: "Storing log data for compliance requirements and forensic investigations"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Retention and Archival?
> Retention is deciding how long to keep data, and archival is moving old data to long-term storage. Like keeping this year's schoolwork in your desk and last year's in the attic.

## Definition

Retention and archival in the context of SIEM and log management refers to the policies and technical implementations for storing security log data for the required duration based on regulatory requirements, forensic investigation needs, and organizational policy. A tiered storage approach keeps recent logs in fast, searchable storage while moving older logs to cheaper archival storage.

## Key Details

- **Hot storage**: recent logs (30-90 days) in fast, indexed storage for immediate querying
- **Warm storage**: older logs (90 days - 1 year) in lower-cost storage with acceptable query performance
- **Cold/archival storage**: older logs compressed and stored cheaply; slow retrieval (used only when needed for investigations)
- Regulatory requirements drive minimum retention periods (PCI DSS: 12 months, HIPAA: 6 years)
- Archived logs must be cryptographically verified for integrity when retrieved for forensic use

## Connections

- Parent: [[siem]] — retention and archival is a critical operational consideration for SIEM implementations
- See also: [[log-retention-policies]]
