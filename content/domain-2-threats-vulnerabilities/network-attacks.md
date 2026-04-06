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

> [!eli5] ELI5: What are Network Attacks?
> Think of computer networks like roads that connect buildings in a city. Network attacks are when bad guys mess with those roads -- they might put up fake detour signs to redirect traffic, block the road so nobody can get through, or secretly listen in on conversations happening in passing cars. Every time your computer sends information to another computer, it travels along these "roads," and attackers look for ways to intercept, redirect, or block that information before it reaches its destination.
>
> > [!eli5] ELI5: Network Attacks (繁體中文版)
> > 網路攻擊是在資料傳輸的過程中搞鬼。壞人可能在半路攔截你的訊息、假冒成別人、或是在你的網路線路裡塞滿垃圾。
> >
> > ```ascii
> > [你的電腦] <--(攔截/攻擊)--> [網路] <--> [伺服器]
> > ```

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
- **[[bluetooth-attacks|Bluejacking]]** — sending unsolicited messages via Bluetooth (nuisance, not data theft)
- **[[bluetooth-attacks|Bluesnarfing]]** — unauthorized access to data through Bluetooth connections (more serious than bluejacking)
- **Broadcast storm** — excessive broadcast traffic overwhelming a network segment

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

## Practice Questions

> [!qbank]- Q-Bank: Network Attacks (4 Questions)
>
> **Q1.** A network administrator notices that a switch has begun flooding all traffic to every port, behaving like a hub. Investigation reveals the CAM table is full of bogus MAC addresses. Which attack is MOST likely occurring?
>
> A. ARP spoofing
> B. VLAN hopping
> C. MAC flooding
> D. IP spoofing
>
> > [!answer]- Show Answer
> > **C. MAC flooding**
> >
> > [[mac-flooding]] overwhelms a switch's CAM table with fake MAC addresses, forcing it into hub mode where traffic is broadcast to all ports. ARP spoofing (A) manipulates ARP caches to redirect traffic but does not fill the CAM table. VLAN hopping (B) exploits trunk port configurations to access other VLANs, not the CAM table. IP spoofing (D) forges source IP addresses but operates at Layer 3, not Layer 2 switching.
>
> **Q2.** An attacker connects a device to the corporate network that begins responding to DHCP requests before the legitimate DHCP server, providing clients with a malicious default gateway. Which attack does this describe?
>
> A. Evil twin
> B. Rogue DHCP server
> C. DNS amplification
> D. Replay attack
>
> > [!answer]- Show Answer
> > **B. Rogue DHCP server**
> >
> > A [[rogue-dhcp-server]] provides malicious network settings (gateway, DNS) to clients, enabling traffic interception. An evil twin (A) is a fake wireless access point, not a DHCP server on a wired network. DNS amplification (C) uses DNS resolvers for DDoS attacks. A replay attack (D) retransmits captured traffic, not DHCP responses.
>
> **Q3.** An attacker crafts Ethernet frames with two 802.1Q VLAN tags to send traffic from the default native VLAN to a restricted VLAN that should be inaccessible. Which attack technique is this?
>
> A. MAC flooding
> B. ARP poisoning
> C. VLAN hopping (double tagging)
> D. IP spoofing
>
> > [!answer]- Show Answer
> > **C. VLAN hopping (double tagging)**
> >
> > [[vlan-hopping]] via double tagging uses two 802.1Q headers so the switch strips the first tag and forwards the frame to the target VLAN. MAC flooding (A) fills the CAM table but does not cross VLAN boundaries. ARP poisoning (B) manipulates ARP caches within a single broadcast domain. IP spoofing (D) forges source IP addresses at Layer 3, not VLAN tags at Layer 2.
>
> **Q4.** A security team wants to prevent ARP spoofing attacks on the corporate LAN. Which Layer 2 defense mechanism BEST addresses this threat?
>
> A. Network address translation (NAT)
> B. Dynamic ARP Inspection (DAI)
> C. Full-disk encryption
> D. Web application firewall
>
> > [!answer]- Show Answer
> > **B. Dynamic ARP Inspection (DAI)**
> >
> > Dynamic ARP Inspection validates ARP packets against the DHCP snooping binding table, preventing [[arp-spoofingpoisoning|ARP spoofing]] attacks. NAT (A) translates IP addresses for routing purposes but does not validate ARP messages. Full-disk encryption (C) protects data at rest, not Layer 2 traffic. A WAF (D) protects web applications at Layer 7, not Layer 2 network communications.

## Scenario

> See [[case-network-attacks]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [2.4 – Malicious Code](https://www.youtube.com/watch?v=xDhUBQ_lnUA)
