---
title: "Network Monitoring"
description: "Continuous observation of network traffic and performance to detect anomalies and security threats"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/network
  - weight/medium
aliases:
  - "Network Traffic Analysis"
---

> [!eli5] ELI5: What is Network Monitoring?
> Picture a lifeguard sitting in a tall chair watching the whole swimming pool. They scan the water constantly, looking for anyone in trouble. Network monitoring is like that lifeguard, but for your computer network -- it watches all the data flowing back and forth, looking for anything unusual. If someone is sending way too much data or connecting from a strange place, the monitoring system spots it and raises the alarm.

## Overview

Network monitoring involves continuously observing network traffic, bandwidth utilization, and device status to ensure availability, performance, and security. From a security perspective, network monitoring identifies anomalous traffic patterns, unauthorized connections, and potential data exfiltration. It provides visibility into what is traversing the network at any given time.

## Key Concepts

- **[[snmp-simple-network-management-protocol|SNMP (Simple Network Management Protocol)]]**: Used to monitor and manage network devices; SNMPv3 adds encryption and authentication
- **[[netflow-sflow-ipfix|NetFlow / sFlow / IPFIX]]**: Protocols that collect metadata about network traffic flows (source, destination, ports, volume) without capturing full packets
- **[[packet-capture-pcap|Packet capture (PCAP)]]**: Full capture of network packets for deep analysis using tools like Wireshark or tcpdump
- **[[network-taps|Network taps]]**: Hardware devices that copy network traffic for monitoring without affecting the traffic flow
- **[[port-mirroring-span|Port mirroring (SPAN)]]**: Switch feature that copies traffic from one port to a monitoring port
- **[[bandwidth-monitoring|Bandwidth monitoring]]**: Detecting unusual spikes that may indicate DDoS attacks or data exfiltration
- **[[baseline-establishment|Baseline establishment]]**: Defining normal network behavior to identify deviations and anomalies
- **[[protocol-analysis|Protocol analysis]]**: Inspecting traffic to detect protocol misuse or tunneling (e.g., DNS tunneling for data exfiltration)
- **[[network-based-idsips|Network-based IDS/IPS]]**: Inline or passive devices that inspect network traffic for known attack signatures and anomalies

## Exam Tips

> [!tip] Remember
> Full packet capture = most detail but most storage. NetFlow = metadata only (who talked to whom, how much). Use SPAN ports or network taps to feed traffic to monitoring tools. SNMPv3 is the only secure version.

- DNS query logs are an often-overlooked but valuable source for detecting C2 communication and data exfiltration
- Encrypted traffic (TLS) limits visibility — consider TLS inspection at the network boundary
- Know the difference between SPAN (software, switch feature) and TAP (hardware, dedicated device)

## Connections

- Feeds traffic data to [[siem]] for correlation with other security event sources
- Supports detection of [[network-attacks]] including DDoS, ARP spoofing, and lateral movement
- Complements [[edr-xdr]] by providing the network perspective that endpoint agents cannot see
- Anomalies detected may trigger [[incident-response]] investigation and containment procedures

## Scenario

> See [[case-network-monitoring]] for a practical DevOps scenario applying these concepts.
