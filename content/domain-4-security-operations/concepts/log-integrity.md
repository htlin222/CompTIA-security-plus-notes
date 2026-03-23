---
title: "Log integrity"
description: "Protecting logs from tampering using write-once storage, hashing, or digital signatures"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Log integrity refers to the assurance that log records have not been altered, deleted, or fabricated after their creation. Attackers routinely attempt to modify or delete logs to conceal their activities — protecting log integrity is essential for forensic investigations and compliance auditing. Multiple technical controls can protect logs from tampering.

## Key Details

- **Write-once/append-only storage**: logs can only be added, never modified or deleted
- **Cryptographic hashing**: hashing log files enables detection of any post-creation modification
- **Digital signatures**: signing logs with a trusted key provides non-repudiation
- **Remote logging**: sending logs to a remote server immediately upon generation limits attacker ability to delete them
- Centralized logging is inherently more tamper-resistant than local logs on potentially compromised systems

## Connections

- Parent: [[log-management]] — log integrity is critical for maintaining the evidentiary value of logs
- See also: [[centralized-logging]]
