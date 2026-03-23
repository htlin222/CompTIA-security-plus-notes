---
title: "NetFlow / sFlow / IPFIX"
description: "Protocols that collect metadata about network traffic flows without capturing full packets"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

NetFlow, sFlow, and IPFIX are network flow monitoring protocols that collect statistical metadata about network traffic flows (source IP, destination IP, ports, protocol, volume, duration) without capturing full packet payloads. This flow data provides visibility into network communication patterns at scale, enabling detection of unusual traffic without the storage overhead of full packet capture.

## Key Details

- **NetFlow**: Cisco-developed protocol; routers and switches export flow records to a collector
- **sFlow**: samples packets at a configured rate; supported by many multi-vendor devices
- **IPFIX** (IP Flow Information Export): IETF-standardized version of NetFlow v9; most modern standard
- Flow data reveals: communication patterns, volume anomalies, protocol misuse, and potential C2 traffic
- Does NOT capture packet payloads — preserves privacy while providing network visibility
- Security tools (SIEM, NDR) ingest flow data for behavioral analysis and anomaly detection

## Connections

- Parent: [[network-monitoring]] — NetFlow/sFlow/IPFIX are primary tools for network traffic visibility
- See also: [[bandwidth-monitoring]]
