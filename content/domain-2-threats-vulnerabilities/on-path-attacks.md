---
title: "On-Path Attacks"
description: "Attacks where the adversary positions themselves between two communicating parties to intercept or alter traffic"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/medium
aliases:
  - "Man-in-the-Middle"
  - "MitM"
---

## Overview

On-path attacks (formerly called man-in-the-middle attacks) occur when an attacker secretly positions themselves between two communicating parties, intercepting and potentially altering the data in transit. The attacker can eavesdrop on sensitive communications, steal credentials, inject malicious content, or modify transactions — all while both parties believe they are communicating directly with each other.

## Key Concepts

- **[[arp-spoofingpoisoning|ARP spoofing/poisoning]]**: The most common technique on local networks — redirects traffic through the attacker's machine by poisoning ARP caches
- **[[ssltls-stripping|SSL/TLS stripping]]**: Downgrading an HTTPS connection to HTTP so the attacker can read traffic in plaintext
- **[[ssltls-interception-ssl-proxy|SSL/TLS interception (SSL proxy)]]**: Using a trusted certificate to decrypt, inspect, and re-encrypt TLS traffic (used legitimately in corporate environments)
- **[[dns-spoofing|DNS spoofing]]**: Redirecting DNS responses to send users to attacker-controlled servers
- **[[https-spoofing|HTTPS spoofing]]**: Presenting a fraudulent certificate to intercept encrypted web traffic
- **[[session-hijacking|Session hijacking]]**: Stealing session tokens from intercepted traffic to impersonate authenticated users
- **[[man-in-the-browser-mitb|Man-in-the-Browser (MitB)]]**: Malware in the browser modifies transactions in real time (e.g., changing bank account numbers)
- **[[relay-attacks|Relay attacks]]**: Forwarding authentication exchanges between a victim and a legitimate service (common with NFC/RFID)
- **[[defenses|Defenses]]**: HTTPS everywhere, HSTS (HTTP Strict Transport Security), certificate pinning, mutual TLS, encrypted protocols

## Exam Tips

> [!tip] Remember
> On-path = attacker is BETWEEN two parties. ARP poisoning = Layer 2 on-path setup. SSL stripping = HTTPS downgraded to HTTP. Defense: use encrypted protocols (HTTPS, SSH), HSTS headers, and certificate validation.

- CompTIA now uses "on-path" instead of "man-in-the-middle" — know both terms
- HSTS tells browsers to ALWAYS use HTTPS, preventing SSL stripping
- Certificate pinning prevents acceptance of fraudulent certificates

## Connections

- Uses techniques from [[network-attacks]] like ARP poisoning and DNS spoofing to position the attacker
- Can intercept credentials vulnerable to [[password-attacks]] when encryption is stripped or absent
- [[wireless-attacks]] like evil twin APs are a common setup for on-path attacks
- [[encryption]] and proper certificate validation are the primary defenses against interception

## Scenario

> See [[case-on-path-attacks]] for a practical DevOps scenario applying these concepts.
