---
title: "Windows Event Log"
description: "built-in Windows logging system capturing security, system, and application events; critical for SIEM ingestion"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Windows Event Log is the built-in logging infrastructure in Windows operating systems that records security, system, application, and operational events. Security-relevant logs capture authentication events, privilege use, policy changes, and object access. Windows Event Logs are a primary data source for SIEMs in Windows-based environments, and specific Event IDs are critical indicators for detecting attacks, authentication failures, and suspicious activity.

## Key Details

- Key security log locations: Security, System, Application, and custom logs (e.g., PowerShell, Sysmon)
- Critical Event IDs: 4624 (successful logon), 4625 (failed logon), 4648 (explicit credential use), 4672 (special privileges assigned), 4698 (scheduled task created), 4720 (user account created)
- Windows Event Forwarding (WEF) and WinRM can forward events to a central collector without an agent
- Sysmon (System Monitor) greatly enhances Windows logging with process creation, network connections, and file hash events
- Log integrity: event logs can be cleared by attackers (Event ID 1102); monitoring for log clearing is important

## Connections

- Parent: [[log-management]] — Windows Event Log is the primary native log source on Windows systems
- See also: [[syslog]], [[log-aggregation]], [[centralized-logging]], [[siem]]
