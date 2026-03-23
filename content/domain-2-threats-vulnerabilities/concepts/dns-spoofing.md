---
title: "DNS spoofing"
description: "Forging DNS responses to redirect queries to malicious IP addresses"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is DNS Spoofing?
> When your computer asks "Where is this website?", a bad guy answers first with a fake address. Your computer trusts the answer and goes to the wrong place without knowing it.

## Definition

DNS spoofing is the act of forging DNS responses to redirect DNS queries to attacker-controlled IP addresses. Unlike DNS cache poisoning (which targets the resolver's cache), DNS spoofing may also occur in real-time through on-path attacks where the attacker intercepts DNS queries and responds with fraudulent answers before the legitimate resolver does. The result is that victims are directed to malicious servers while believing they are visiting legitimate ones.

## Key Details

- Can occur as **cache poisoning** (persistent—affects many users) or **on-path spoofing** (real-time—affects one session).
- Used as a precursor to **phishing sites**, **malware distribution**, and **credential harvesting**.
- **DNSSEC** signs DNS records cryptographically—allows clients to verify response authenticity and detect spoofed records.
- ARP spoofing on the LAN is often combined with DNS spoofing to redirect traffic in on-path attack scenarios.
- Monitoring for unexpected DNS responses and deploying DNSSEC are key mitigations.

## Connections

- Parent: [[dns-attacks]] — a core DNS attack technique
- Parent: [[on-path-attacks]] — DNS spoofing supports on-path interception
- See also: [[dns-poisoning-dns-cache-poisoning]]
