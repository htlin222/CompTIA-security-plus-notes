---
title: "Log forwarding agents"
description: "Software installed on endpoints to collect and send logs to central systems"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Log Forwarding Agents?
> These are little messengers installed on each computer that grab log entries and send them to the central collection point. Like mail carriers picking up letters from every house on the block.

## Definition

Log forwarding agents are lightweight software components installed on endpoints, servers, and other devices to collect, filter, and forward log data to a centralized logging or SIEM platform. They enable collection of logs from systems that cannot natively send logs via syslog or other protocols, and can perform local filtering, enrichment, and formatting before transmission.

## Key Details

- Common agents: Splunk Universal Forwarder, Elastic Beats (Winlogbeat, Filebeat), NXLog, Fluentd
- Windows Event Log collection requires an agent (or WEF/WEC for Windows-native forwarding)
- Agents can buffer logs locally during network outages to prevent loss
- Agents should be protected from tampering — attackers may target agents to suppress log forwarding
- TLS should be used for log transmission to protect log data in transit

## Connections

- Parent: [[log-management]] — log forwarding agents are the collection infrastructure for centralized logging
- See also: [[centralized-logging]]
