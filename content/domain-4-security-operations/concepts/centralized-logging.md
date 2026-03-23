---
title: "Centralized logging"
description: "Aggregating logs from all sources into a single repository for unified analysis"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Centralized logging is the practice of collecting log data from all systems, applications, network devices, and security tools across an organization and storing them in a single, unified repository. This centralization enables comprehensive security monitoring, correlation analysis, and forensic investigation across the entire environment from a single interface.

## Key Details

- Enables correlation of events across different systems that would be missed when logs are siloed
- SIEM platforms are the primary tool for implementing centralized logging in security operations
- Log sources include firewalls, servers, endpoints, applications, cloud services, and network devices
- Requires standardized time synchronization (NTP) across all log sources for accurate correlation
- Protects logs from tampering — centralized logs are harder for attackers to modify than local logs

## Connections

- Parent: [[log-management]] — centralized logging is the foundational log management architecture
- See also: [[log-aggregation]]
