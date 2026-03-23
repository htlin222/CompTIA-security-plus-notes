---
title: "Host-based IDS/IPS (HIDS/HIPS)"
description: "Monitors system activity and file integrity on the endpoint"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - HIDS/HIPS
---

> [!eli5] ELI5: What is Host-based IDS/IPS?
> This is a guard stationed inside one specific building who watches everything happening there. If someone acts suspicious, the guard either alerts security or stops them directly.

## Definition

Host-based Intrusion Detection Systems (HIDS) and Host-based Intrusion Prevention Systems (HIPS) are security tools installed directly on endpoints that monitor system activity, log file changes, registry modifications, running processes, and network connections from the host's perspective. HIDS detects and alerts; HIPS can actively block suspicious activities.

## Key Details

- Monitors activities that network-based systems cannot see (local process execution, file changes)
- Can detect privilege escalation, rootkit installation, and file tampering
- HIDS is detection-only; HIPS can actively block suspicious activities (process termination, connection blocking)
- Modern EDR solutions subsume traditional HIDS/HIPS functionality with richer telemetry
- File integrity monitoring (FIM) is often a component of HIDS implementations

## Connections

- Parent: [[endpoint-security]] — HIDS/HIPS is a key endpoint security monitoring technology
- See also: [[file-integrity-monitoring]]
