---
title: "Log retention policies"
description: "Defining how long logs are stored based on regulatory and organizational requirements"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Log retention policies define the minimum and maximum periods for which different types of log data must be stored, based on legal and regulatory requirements, forensic investigation needs, and organizational policies. Retaining logs too briefly creates gaps in the audit trail needed for investigations; retaining them too long increases storage costs and privacy risk.

## Key Details

- Common regulatory requirements: PCI DSS requires 12 months (3 months immediately available); HIPAA recommends 6 years; GDPR requires limiting to what is necessary
- Security logs should be retained long enough to support investigations that may span months
- Tiered retention: recent logs stored in fast, searchable storage; older logs archived to cheaper cold storage
- Legal holds may require extending retention beyond normal policy for specific investigations
- Automated archival moves aging logs to cold storage while maintaining accessibility for compliance

## Connections

- Parent: [[log-management]] — retention policies govern the lifecycle of log data
- See also: [[log-integrity]]
