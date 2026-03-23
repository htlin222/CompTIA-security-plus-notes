---
title: "Continuous monitoring"
description: "Agents on endpoints record process execution, file changes, registry modifications, and network connections"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Continuous Monitoring?
> It is like a baby monitor that never turns off. You are always watching your systems so the moment something weird happens, you know about it right away.

## Definition

Continuous monitoring in endpoint security refers to the persistent collection and recording of detailed telemetry from endpoints using lightweight software agents. Unlike periodic scans, continuous monitoring captures all activity in real time, including process creation and termination, file system changes, registry modifications, network connections, and user logon events, enabling both real-time detection and retrospective investigation.

## Key Details

- EDR agents run continuously on endpoints, recording all activity with minimal performance impact
- Data is sent to a central management platform for storage, analysis, and correlation
- Enables retrospective investigation: analysts can query past activity even if no alert was generated at the time
- Key telemetry types: process execution, network connections, file modifications, registry changes, user logins
- Continuous monitoring data is the foundation for threat hunting and incident investigation

## Connections

- Parent: [[edr-xdr]] — continuous monitoring is the data collection foundation of EDR platforms
- See also: [[behavioral-analysis]]
