---
title: "Network Attacks"
description: "Attacks targeting network infrastructure, protocols, and communications to intercept, disrupt, or manipulate traffic"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/high
aliases:
  - "Network-Based Attacks"
---

## Overview

Network attacks target the infrastructure, protocols, and communications that connect systems and users. These attacks exploit weaknesses in network protocols, configurations, and architectures to intercept data, disrupt services, or gain unauthorized access. Understanding network attacks is critical for the Security+ exam, as they represent fundamental threat categories that security controls are designed to mitigate.

## Key Concepts

- **[[arp-spoofingpoisoning|ARP spoofing/poisoning]]**: Sending fake ARP messages to associate the attacker's MAC address with a legitimate IP, enabling traffic interception
- **[[mac-flooding|MAC flooding]]**: Overwhelming a switch's CAM table to force it into hub mode, broadcasting traffic to all ports
- **[[vlan-hopping|VLAN hopping]]**: Exploiting trunk port configurations (switch spoofing or double tagging) to access traffic on other VLANs
- **[[rogue-dhcp-server|Rogue DHCP server]]**: Unauthorized DHCP server providing malicious gateway or DNS settings to clients
- **[[evil-twin|Evil twin]]**: Setting up a fake wireless access point that mimics a legitimate one to intercept traffic
- **[[deauthentication-attack|Deauthentication attack]]**: Sending forged deauth frames to disconnect clients from a wireless network (802.11)
- **[[replay-attack|Replay attack]]**: Capturing and retransmitting valid network traffic to gain unauthorized access or duplicate transactions
- **[[amplification-attack|Amplification attack]]**: Using protocols like DNS, NTP, or memcached to amplify a small request into a massive response directed at the victim
- **[[ip-spoofing|IP spoofing]]**: Forging the source IP address of packets to impersonate another system or hide the attacker's identity
- **[[port-scanning|Port scanning]]**: Enumerating open ports and services on target systems (reconnaissance phase)

## Exam Tips

> [!tip] Remember
> ARP poisoning = Layer 2 (data link). VLAN hopping = Layer 2. IP spoofing = Layer 3 (network). Port security, DHCP snooping, dynamic ARP inspection (DAI), and 802.1X are key Layer 2 defenses.

- MAC flooding defense: port security with MAC address limits
- VLAN hopping defense: disable auto-trunking, use a dedicated native VLAN
- Replay attack defense: timestamps, nonces, and sequence numbers in protocols

## Connections

- [[denial-of-service]] attacks are a specific category of network attacks focused on disruption
- [[on-path-attacks]] leverage ARP spoofing and similar techniques for traffic interception
- [[dns-attacks]] target the name resolution infrastructure critical to network operations
- [[network-monitoring]] detects anomalous traffic patterns that indicate network attacks in progress

## Scenario

> See [[case-network-attacks]] for a practical DevOps scenario applying these concepts.
