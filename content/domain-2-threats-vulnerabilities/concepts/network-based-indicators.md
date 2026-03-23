---
title: "Network-based indicators"
description: "Known malicious IPs, suspicious domains, unusual outbound connections, C2 traffic patterns"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Network-based indicators of compromise are artifacts and anomalies observed in network traffic that suggest malicious activity. These include connections to known-malicious IP addresses or domains, unusual outbound traffic patterns (beaconing to C2 servers), unexpected data transfers, and protocol anomalies. Network security tools such as IDS/IPS, SIEM, and DNS security platforms collect and analyze these indicators.

## Key Details

- **Known malicious IPs/domains**: Threat intelligence feeds provide continuously updated lists of attacker infrastructure.
- **C2 beaconing patterns**: Regular, periodic outbound connections—often at fixed intervals—indicating malware checking in with its C2 server.
- **Unusual outbound ports**: Malware often uses non-standard ports or tunnels traffic through allowed protocols (HTTP, DNS) to evade filtering.
- **Large data transfers**: Unexpected bulk uploads to external destinations—potential exfiltration indicator.
- **SIEM correlation**: Combining network indicators with host-based indicators increases confidence in compromise detection.

## Connections

- Parent: [[indicators-of-compromise]] — the network-traffic IoC category
- See also: [[dns-tunneling]]
