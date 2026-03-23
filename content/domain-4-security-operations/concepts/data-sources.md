---
title: "Data sources"
description: "EDR telemetry, SIEM logs, network flow data, DNS logs, authentication logs"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Data Sources?
> Data sources are all the places that feed information into your security tools -- like cameras, door sensors, and motion detectors all reporting to the same guard station.

## Definition

Data sources in threat hunting refer to the diverse types of telemetry and log data that threat hunters query and analyze when searching for attacker activity. Having access to rich, high-fidelity data sources is essential for effective threat hunting — the more complete the visibility, the better the chance of finding attackers who have evaded automated detection.

## Key Details

- **EDR telemetry**: process execution, file changes, network connections, registry modifications from endpoints
- **SIEM logs**: aggregated, normalized logs from all security tools and systems
- **Network flow data** (NetFlow, IPFIX): metadata about all network connections without packet capture
- **DNS logs**: domain resolution requests that can reveal C2 communications and data exfiltration
- **Authentication logs**: logon/logoff events, failed attempts, privilege escalation events

## Connections

- Parent: [[threat-hunting]] — rich data sources are the foundation of effective threat hunting
- See also: [[log-sources]]
