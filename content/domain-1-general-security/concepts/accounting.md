---
title: "Accounting"
description: "Logging and tracking user activities for audit and forensic purposes"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Accounting is the third component of the AAA (Authentication, Authorization, Accounting) framework. It involves recording what authenticated and authorized users do on systems and networks, creating an audit trail that supports forensic investigations, compliance reporting, and anomaly detection. Accounting data typically includes login times, commands executed, resources accessed, and session durations.

## Key Details

- Accounting provides **non-repudiation**—users cannot deny actions that are logged.
- Implemented via protocols like **RADIUS** or **TACACS+**, which log authentication events and session details.
- Syslog, Windows Event Logs, and SIEM platforms are common accounting infrastructure.
- Must capture: who (user), what (action), when (timestamp), where (source IP/device).
- Logs must be protected from tampering—write-once storage and centralized log management are best practices.

## Connections

- Parent: [[aaa-framework]] — the "A" for Accounting in AAA
- See also: [[radius]], [[tacacs]]
