---
title: "Denial of Service"
description: "Attacks designed to make systems, services, or networks unavailable to legitimate users"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/high
aliases:
  - "DoS"
  - "DDoS"
---

> [!eli5] ELI5: What is Denial of Service?
> Picture a school water fountain. Normally, everyone takes turns getting a drink. But what if a hundred kids all crowded around the fountain at once, blocking everyone else? Nobody who actually needs a drink can get one. That's what a denial-of-service attack does to websites and computers -- it floods them with so much fake traffic that real people can't use them anymore. Sometimes attackers even get thousands of hijacked computers to join in at once, making it way harder to stop.

## Overview

Denial of Service (DoS) attacks aim to make a system, service, or network unavailable to its intended users by overwhelming it with traffic or exploiting vulnerabilities that cause crashes. Distributed Denial of Service (DDoS) attacks use multiple compromised systems (a botnet) to amplify the attack volume. DoS/DDoS attacks target availability — one of the three pillars of the CIA triad.

## Key Concepts

- **[[volumetric-attacks|Volumetric attacks]]**: Flooding the target with massive amounts of traffic to saturate bandwidth (UDP floods, ICMP floods)
- **[[protocol-attacks|Protocol attacks]]**: Exploiting protocol weaknesses to consume server resources (SYN flood, Ping of Death, Smurf attack)
- **[[application-layer-attacks|Application-layer attacks]]**: Targeting specific services with legitimate-looking requests to exhaust application resources (HTTP flood, Slowloris)
- **[[syn-flood|SYN flood]]**: Sending many TCP SYN packets without completing the handshake, filling the target's connection table
- **[[amplificationreflection|Amplification/Reflection]]**: Using third-party servers (DNS, NTP, memcached) to amplify and reflect traffic at the victim
- **[[botnet|Botnet]]**: Network of compromised devices (including IoT) controlled by an attacker to generate DDoS traffic
- **[[smurf-attack|Smurf attack]]**: Sending ICMP echo requests with a spoofed source (victim's IP) to a broadcast address
- **[[slowloris|Slowloris]]**: Keeps many HTTP connections open by sending partial headers, exhausting the server's connection pool

## Exam Tips

> [!tip] Remember
> DoS = single source. DDoS = multiple sources (botnet). Three categories: Volumetric (bandwidth), Protocol (connection state), Application (resource exhaustion). SYN cookies are the defense against SYN floods.

- Defense-in-depth: rate limiting, CDN/DDoS mitigation services (Cloudflare, AWS Shield), blackhole routing, SYN cookies
- Know that IoT botnets (like Mirai) created some of the largest DDoS attacks in history
- Application-layer DDoS is harder to detect because traffic looks legitimate

## Connections

- Specific category of [[network-attacks]] targeting the availability component of the CIA triad
- Often used as part of [[ransomware]] triple extortion strategies
- Detection relies on [[network-monitoring]] to identify abnormal traffic patterns
- [[mitigation-techniques]] include rate limiting, CDN protection, and traffic scrubbing

## Scenario

> See [[case-denial-of-service]] for a practical DevOps scenario applying these concepts.
