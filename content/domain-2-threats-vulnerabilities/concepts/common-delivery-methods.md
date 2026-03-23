---
title: "Common delivery methods"
description: "Phishing emails, exploited vulnerabilities (especially RDP), drive-by downloads, supply chain compromise"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Ransomware reaches victim systems through several primary delivery methods. Understanding these vectors is essential for implementing targeted defenses. The most common delivery methods include phishing emails with malicious attachments or links, exploitation of exposed remote services (especially RDP), drive-by downloads from compromised websites, and supply chain attacks where trusted software updates contain malicious payloads.

## Key Details

- **Phishing**: The most common initial vector—malicious attachments (Office macros, ISO files) or credential-harvesting links.
- **RDP exploitation**: Exposed RDP (port 3389) with weak credentials is actively scanned and brute-forced by ransomware operators.
- **Drive-by downloads**: Visiting a compromised website silently installs malware via browser or plugin vulnerabilities.
- **Supply chain compromise**: Attackers compromise software update mechanisms (e.g., SolarWinds, 3CX) to deliver ransomware to many victims simultaneously.
- **Vulnerable VPNs and edge devices** (Citrix, Pulse Secure, Fortinet) have been heavily exploited for initial access.

## Connections

- Parent: [[ransomware]] — describes how ransomware is initially delivered
- See also: [[phishing]]
