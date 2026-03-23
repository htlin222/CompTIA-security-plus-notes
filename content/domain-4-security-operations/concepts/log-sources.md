---
title: "Log sources"
description: "OS event logs, firewall logs, IDS/IPS alerts, authentication logs, application logs, DNS query logs, proxy logs"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Log Sources?
> Log sources are all the different places that create records -- servers, firewalls, apps, and more. Each one is like a witness who saw a different part of what happened.

## Definition

Log sources are the diverse categories of systems, devices, and applications that generate log data relevant to security monitoring and incident investigation. Understanding what log sources are available and what security-relevant events they capture is essential for building an effective security monitoring program.

## Key Details

- **OS event logs**: Windows Security log (4624, 4625, 4648, 4672), Linux auth/syslog
- **Firewall logs**: allowed and denied connections, NAT translations
- **IDS/IPS alerts**: signature matches, anomaly detections
- **Authentication logs**: VPN, Active Directory, cloud identity provider logon events
- **Application logs**: web server access logs, database audit logs, application errors
- **DNS query logs**: domain resolution requests — critical for detecting C2 and DNS tunneling
- **Proxy logs**: web traffic with URL, user, and content type information

## Connections

- Parent: [[log-management]] — identifying and collecting the right log sources is foundational to log management
- See also: [[centralized-logging]]
