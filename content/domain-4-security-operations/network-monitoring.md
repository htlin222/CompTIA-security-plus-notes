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
- **[[tcpdump|tcpdump]]**: Command-line packet capture tool (`tcpdump -i eth0 -w capture.pcap`)
- **[[tcpreplay|tcpreplay]]**: Replays captured network traffic for testing IDS/IPS rules
- **[[wireshark|Wireshark]]**: GUI-based protocol analyzer for deep packet inspection
- **[[pathping|pathping]]**: Windows command combining ping and traceroute with statistics at each hop
- **[[hping|hping]]**: Packet crafting tool for TCP/IP auditing and firewall testing

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

## Practice Questions

> [!qbank]- Q-Bank: Network Monitoring (4 Questions)
>
> **Q1.** A security analyst wants to determine which internal hosts are communicating with external IP addresses and how much data they are transferring, without capturing full packet contents. Which technology is BEST suited for this requirement?
>
> A. Full packet capture with Wireshark
> B. NetFlow analysis
> C. Host-based IDS
> D. SNMP polling
>
> > [!answer]- Show Answer
> > **B. NetFlow analysis**
> >
> > [[netflow-sflow-ipfix|NetFlow]] collects metadata about network traffic flows — source, destination, ports, and volume — without capturing full packet contents, making it ideal for traffic analysis at scale. Option A captures full packets, which provides more detail than needed and requires massive storage. Option C monitors individual endpoints, not network-wide traffic patterns. Option D monitors device status and performance metrics, not traffic flow details.
>
> **Q2.** A network engineer needs to send a copy of all traffic passing through a core switch to a network-based IDS for analysis. The engineer does not want to affect the switch's performance or the original traffic flow. Which method is MOST appropriate?
>
> A. Installing a network tap on the switch uplink
> B. Configuring a host-based firewall on the switch
> C. Enabling SNMP traps on the switch
> D. Deploying full disk encryption on the IDS server
>
> > [!answer]- Show Answer
> > **A. Installing a network tap on the switch uplink**
> >
> > [[network-taps]] are hardware devices that copy network traffic for monitoring without affecting the original traffic flow or switch performance. Option B is a device-level control, not a traffic copying mechanism. Option C sends alerts about device events, not copies of traffic. Option D protects data at rest on the IDS, unrelated to traffic copying.
>
> **Q3.** A security team establishes a normal traffic baseline for the corporate network. Two weeks later, monitoring tools detect a 300% increase in DNS query volume from a single workstation during non-business hours. What does this anomaly MOST likely suggest?
>
> A. The workstation is performing a scheduled software update
> B. The workstation may be compromised and using DNS tunneling for data exfiltration
> C. The DNS server is experiencing a hardware failure
> D. The workstation's NTP configuration is incorrect
>
> > [!answer]- Show Answer
> > **B. The workstation may be compromised and using DNS tunneling for data exfiltration**
> >
> > Excessive DNS queries from a single host during off-hours is a strong indicator of [[protocol-analysis|DNS tunneling]], where attackers encode data within DNS queries for command-and-control communication or data exfiltration. [[baseline-establishment|Baseline deviation]] detection makes this anomaly visible. Option A would generate HTTP/HTTPS traffic, not excessive DNS queries. Option C would affect all workstations, not just one. Option D would cause time drift, not DNS query spikes.
>
> **Q4.** An organization uses SNMPv2c to monitor all network devices. A security auditor flags this as a vulnerability. What is the PRIMARY security concern?
>
> A. SNMPv2c uses too much network bandwidth
> B. SNMPv2c transmits community strings in cleartext without encryption or strong authentication
> C. SNMPv2c cannot monitor network device performance
> D. SNMPv2c is incompatible with modern network switches
>
> > [!answer]- Show Answer
> > **B. SNMPv2c transmits community strings in cleartext without encryption or strong authentication**
> >
> > [[snmp-simple-network-management-protocol|SNMPv2c]] sends community strings (essentially passwords) in plaintext, allowing attackers to intercept them and gain read or write access to network devices. Only SNMPv3 adds encryption and proper authentication. Option A is not a significant concern with SNMP. Option C is incorrect — SNMPv2c is fully capable of performance monitoring. Option D is incorrect — SNMPv2c is widely supported.

## Scenario

> See [[case-network-monitoring]] for a practical DevOps scenario applying these concepts.
