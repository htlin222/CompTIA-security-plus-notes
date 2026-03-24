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

## Practice Questions

> [!qbank]- Q-Bank: Denial of Service (4 Questions)
>
> **Q1.** A web server is receiving thousands of TCP SYN packets per second from spoofed IP addresses, and its connection table is full. Legitimate users cannot establish new connections. Which BEST describes this attack?
>
> A. Slowloris attack
> B. SYN flood
> C. DNS amplification
> D. HTTP flood
>
> > [!answer]- Show Answer
> > **B. SYN flood**
> >
> > A [[syn-flood]] sends many TCP SYN packets without completing the three-way handshake, filling the target's connection state table. Slowloris (A) holds connections open with partial HTTP headers, not SYN packets. DNS amplification (C) uses DNS resolvers to reflect and amplify traffic, not direct SYN packets. HTTP flood (D) sends complete HTTP requests, not incomplete TCP handshakes.
>
> **Q2.** An attacker sends small DNS queries with a spoofed source IP (set to the victim's address) to thousands of open DNS resolvers. The resolvers send large responses to the victim. Which type of DoS attack does this BEST represent?
>
> A. Volumetric SYN flood
> B. Application-layer attack
> C. Amplification/reflection attack
> D. Smurf attack
>
> > [!answer]- Show Answer
> > **C. Amplification/reflection attack**
> >
> > This describes a [[amplificationreflection]] attack using DNS resolvers — a small query produces a large response directed at the spoofed victim IP. SYN flood (A) targets connection state tables, not bandwidth through amplification. Application-layer attack (B) targets specific services with legitimate-looking requests. Smurf attack (D) uses ICMP echo requests to broadcast addresses, not DNS queries to resolvers.
>
> **Q3.** A security team notices that a web application is becoming unresponsive. Analysis shows hundreds of HTTP connections held open with incomplete headers being sent very slowly. Which attack is MOST likely occurring?
>
> A. SYN flood
> B. UDP flood
> C. Slowloris
> D. Ping of Death
>
> > [!answer]- Show Answer
> > **C. Slowloris**
> >
> > [[slowloris]] keeps HTTP connections open by slowly sending partial headers, exhausting the web server's connection pool. SYN flood (A) targets TCP connection tables with incomplete handshakes, not HTTP-level connections. UDP flood (B) is a volumetric attack using UDP packets, not slow HTTP headers. Ping of Death (D) sends malformed ICMP packets to crash systems, not hold HTTP connections open.
>
> **Q4.** After a major DDoS attack, a security architect recommends multiple countermeasures. Which combination provides the MOST comprehensive DDoS defense strategy?
>
> A. Antivirus software and host-based firewalls
> B. CDN/DDoS mitigation service, rate limiting, and SYN cookies
> C. Full-disk encryption and VPN tunnels
> D. Intrusion detection system and vulnerability scanning
>
> > [!answer]- Show Answer
> > **B. CDN/DDoS mitigation service, rate limiting, and SYN cookies**
> >
> > This combination addresses multiple DDoS categories: CDN services absorb [[volumetric-attacks]], rate limiting mitigates [[application-layer-attacks]], and SYN cookies defend against [[syn-flood]] protocol attacks. Antivirus and host firewalls (A) are endpoint protections, not DDoS defenses. Encryption and VPNs (C) protect confidentiality, not availability. IDS and vulnerability scanning (D) detect and identify issues but do not actively mitigate DDoS traffic.

## Scenario

> See [[case-denial-of-service]] for a practical DevOps scenario applying these concepts.
