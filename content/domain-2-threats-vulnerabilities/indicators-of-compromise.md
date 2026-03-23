---
title: "Indicators of Compromise"
description: "Observable artifacts or behaviors that indicate a system or network has been breached"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/incident
  - weight/high
aliases:
  - "IoC"
---

## Overview

Indicators of Compromise (IoCs) are pieces of forensic evidence — such as file hashes, IP addresses, domain names, or behavioral patterns — that suggest a system or network has been compromised. IoCs are used by security tools and analysts to detect, investigate, and respond to security incidents. They represent the "breadcrumbs" left behind by attackers and are critical for threat detection and intelligence sharing.

## Key Concepts

- **[[file-based-indicators|File-based indicators]]**: Malicious file hashes (MD5, SHA-256), suspicious file names, unexpected file locations
- **[[network-based-indicators|Network-based indicators]]**: Known malicious IP addresses, suspicious domains, unusual outbound connections, C2 (command and control) traffic patterns
- **[[host-based-indicators|Host-based indicators]]**: Unexpected processes, registry changes, scheduled tasks, unauthorized user accounts, modified system files
- **[[behavioral-indicators|Behavioral indicators]]**: Unusual login times, impossible travel (logins from distant locations in short timeframes), lateral movement patterns
- **[[email-indicators|Email indicators]]**: Phishing sender addresses, malicious attachment hashes, suspicious URLs in email bodies
- **[[account-indicators|Account indicators]]**: Multiple failed logins, privilege escalation attempts, account lockouts, new admin accounts
- **[[indicators-of-attack-ioa|Indicators of Attack (IoA)]]**: Proactive behavioral signals suggesting an attack is in progress (more real-time than IoCs)
- **[[stixtaxii|STIX/TAXII]]**: Standards for formatting (STIX) and sharing (TAXII) IoC data between organizations
- **[[threat-feeds|Threat feeds]]**: Automated IoC data streams from commercial and open-source providers
- **[[false-positives|False positives]]**: Legitimate activity that matches IoC patterns — tuning is essential

## Exam Tips

> [!tip] Remember
> IoCs = evidence of past compromise (reactive). IoAs = signs of active attack (proactive). Common IoCs: unexpected outbound traffic, unusual process execution, beaconing (regular interval C2 communication), new accounts.

- Beaconing (regular interval outbound connections) is a classic C2 indicator
- Data exfiltration indicators: large outbound transfers, DNS tunneling, encrypted traffic to unusual destinations
- IoCs have a shelf life — sophisticated attackers change infrastructure frequently

## Connections

- Fed into [[siem]] to create correlation rules and automated detection alerts
- Drives the detection phase of [[incident-response]] by identifying potential security events
- [[threat-intelligence]] provides IoCs from external sources to enhance organizational detection
- May reveal specific [[malware-types]] through file hashes and behavioral patterns

## Scenario

> See [[case-indicators-of-compromise]] for a practical DevOps scenario applying these concepts.
