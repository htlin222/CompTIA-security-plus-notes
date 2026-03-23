---
title: "Decommissioning"
description: "Properly retiring end-of-life systems that can no longer be patched"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Decommissioning?
> When a car is too old to fix safely, you scrap it properly instead of leaving it on the street. Decommissioning is safely getting rid of old computers so their leftover data doesn't fall into the wrong hands.

## Definition

Decommissioning is the process of securely retiring systems, applications, or hardware that have reached end-of-life and can no longer receive security patches or vendor support. Proper decommissioning includes data sanitization (wiping or destroying storage media), revoking associated accounts and certificates, updating network documentation, and ensuring no sensitive data remains on the retired system.

## Key Details

- End-of-life systems are **high-risk** because known vulnerabilities will never be patched—they become permanent attack targets.
- **Data sanitization** methods: overwriting (DoD 5220.22-M), degaussing, physical destruction—must match the data sensitivity level.
- All **certificates**, **service accounts**, and **firewall rules** associated with the system must be revoked/removed.
- If decommissioning isn't immediately possible, apply **compensating controls**: network isolation, enhanced monitoring, strict access controls.
- Document the decommission in the **asset inventory** and **CMDB** (Configuration Management Database).

## Connections

- Parent: [[mitigation-techniques]] — decommissioning as a vulnerability mitigation strategy
- See also: [[compensating-controls]], [[patching]]
