---
title: "Log aggregation"
description: "Collecting logs from firewalls, servers, endpoints, applications, and cloud services into one platform"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Log Aggregation?
> Log aggregation gathers diary entries from every computer, server, and device into one giant notebook so security teams can search through everything in one spot.

## Definition

Log aggregation is the process of collecting log data from multiple, diverse sources across an organization's infrastructure and consolidating it into a single centralized platform for storage, analysis, and correlation. Without aggregation, logs remain siloed in individual systems, making it impossible to correlate events across different infrastructure components to detect sophisticated attacks.

## Key Details

- Sources: network devices, servers, endpoints, applications, authentication systems, cloud services
- Log forwarding agents or syslog forwarders send logs to the central SIEM or log management platform
- Normalization converts diverse log formats into a common schema for consistent querying
- Volume can be very high: enterprise environments generate terabytes of log data daily
- Log aggregation is the foundation of SIEM functionality — without it, correlation is impossible

## Connections

- Parent: [[siem]] — log aggregation is the fundamental data collection function of SIEM platforms
- See also: [[centralized-logging]]
