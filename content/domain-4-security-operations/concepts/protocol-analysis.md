---
title: "Protocol analysis"
description: "Inspecting traffic to detect protocol misuse or tunneling (e.g., DNS tunneling for data exfiltration)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Protocol analysis in network security monitoring involves deep inspection of network protocols to detect misuse, protocol violations, and covert channel techniques that attackers use to evade detection. Attackers frequently abuse legitimate protocols (DNS, HTTP, ICMP) to tunnel malicious traffic or exfiltrate data while blending in with normal network traffic.

## Key Details

- **DNS tunneling**: encoding data within DNS queries/responses to establish covert C2 channel or exfiltrate data
- **HTTP/HTTPS tunneling**: encapsulating non-HTTP traffic within HTTP to traverse firewalls
- **ICMP tunneling**: hiding data in ICMP ping packets
- Protocol analysis detects anomalies: unusually large DNS records, unexpected DNS query rates, malformed protocol headers
- IDS/IPS rules and network detection/response (NDR) tools identify protocol misuse patterns

## Connections

- Parent: [[network-monitoring]] — protocol analysis is an advanced network monitoring capability
- See also: [[packet-capture-pcap]]
