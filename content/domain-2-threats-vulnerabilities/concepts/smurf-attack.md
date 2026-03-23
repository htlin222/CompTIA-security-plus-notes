---
title: "Smurf attack"
description: "Sending ICMP echo requests with spoofed source (victim's IP) to a broadcast address"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A Smurf attack is a distributed denial-of-service attack that exploits ICMP (ping) and IP broadcast addresses. The attacker sends ICMP echo request (ping) packets to a network's broadcast address with the source IP spoofed to be the victim's IP address. Every host on that network responds to the ping—sending their ICMP echo replies to the victim—flooding the victim with traffic from many sources.

## Key Details

- **Amplification factor**: Each ping to a broadcast address generates responses from all hosts on that network segment—potentially hundreds of replies per packet.
- Named after the "Smurf" exploit tool released in 1997—historically significant DDoS attack type.
- Largely **mitigated in modern networks**: routers now typically block directed broadcasts (`no ip directed-broadcast` on Cisco IOS); hosts may not respond to broadcast pings.
- Relies on **IP spoofing** to direct replies to the victim—mitigated by **BCP38 ingress filtering**.
- Related to the **amplification/reflection** attack category.

## Connections

- Parent: [[denial-of-service]] — a protocol amplification DDoS attack
- See also: [[amplification-attack]], [[ip-spoofing]]
