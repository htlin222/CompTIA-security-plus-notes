---
title: "Network-based IDS/IPS"
description: "Inline or passive devices that inspect network traffic for known attack signatures and anomalies"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Network-based IDS/IPS?
> This is a security guard watching the main highway into your network. An IDS spots trouble and calls for help; an IPS spots trouble and blocks it right there on the spot.

## Definition

Network-based Intrusion Detection Systems (NIDS) and Network-based Intrusion Prevention Systems (NIPS) monitor network traffic flowing through the network to detect or block attack patterns, malware communications, and policy violations. They provide centralized network-level visibility that complements host-based endpoint security tools.

## Key Details

- **Signature-based detection**: matches traffic against known attack patterns (Snort rules, Suricata rules)
- **Anomaly-based detection**: identifies deviations from baseline normal traffic patterns
- **Protocol analysis**: detects protocol violations and evasion techniques
- NIDS is passive (port mirror/TAP) and alerts only; NIPS is inline and can block traffic
- Modern NGFWs incorporate NIPS functionality alongside firewall and application control

## Connections

- Parent: [[network-monitoring]] — network IDS/IPS is a core network security monitoring technology
- See also: [[inline-vs-passive-deployment]]
