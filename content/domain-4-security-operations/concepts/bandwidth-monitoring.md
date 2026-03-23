---
title: "Bandwidth monitoring"
description: "Detecting unusual spikes that may indicate DDoS attacks or data exfiltration"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Bandwidth monitoring is the ongoing measurement and analysis of network traffic volume across network links and interfaces. In security operations, unusual bandwidth patterns — such as sudden spikes in outbound traffic or sustained high inbound volume — can be indicators of attacks such as DDoS attempts, data exfiltration, or botnet command-and-control communications.

## Key Details

- Establishes a baseline of normal bandwidth usage for comparison with anomalies
- Outbound bandwidth spikes can indicate data exfiltration or botnet activity
- Inbound bandwidth spikes can indicate DDoS or brute-force attacks
- Tools include SNMP polling, NetFlow analysis, and network performance monitoring platforms
- Alerts should be triggered when bandwidth exceeds predefined thresholds for defined time periods

## Connections

- Parent: [[network-monitoring]] — bandwidth monitoring is a core network security monitoring technique
- See also: [[netflow-sflow-ipfix]]
