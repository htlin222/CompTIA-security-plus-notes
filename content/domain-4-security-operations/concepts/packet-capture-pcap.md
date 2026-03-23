---
title: "Packet capture (PCAP)"
description: "Full capture of network packets for deep analysis using tools like Wireshark or tcpdump"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Packet capture (PCAP) is the process of intercepting and recording all network packets traversing a network interface for analysis. Unlike flow data which captures metadata only, PCAP captures complete packet content including headers and payload, enabling deep inspection of network communications, malware traffic, and attacker command-and-control channels.

## Key Details

- Tools: Wireshark (GUI analysis), tcpdump (command-line capture), tshark (command-line Wireshark)
- PCAP files store complete packet data that can be replayed and analyzed offline
- Requires significant storage capacity — gigabits per second of traffic generate terabytes of PCAP data quickly
- Can decrypt TLS traffic if private keys or session keys are available
- Used in incident response for deep analysis of suspicious network activity, malware C2 traffic, and data exfiltration

## Connections

- Parent: [[network-monitoring]] — packet capture provides the deepest level of network traffic visibility
- See also: [[network-taps]]
