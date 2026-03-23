---
title: "DNS poisoning / DNS cache poisoning"
description: "Injecting false DNS records into a resolver's cache to redirect users to attacker-controlled servers"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is DNS Cache Poisoning?
> The internet has a phone book it checks often. DNS poisoning sneaks a wrong number into that phone book, so everyone who looks up a website gets sent to the wrong place.

## Definition

DNS cache poisoning is an attack in which an attacker injects fraudulent DNS records into a recursive resolver's cache, causing subsequent DNS queries for a domain to return an attacker-controlled IP address instead of the legitimate one. All users relying on that resolver are then redirected to the attacker's server, enabling credential theft, malware distribution, or traffic interception.

## Key Details

- Exploits the fact that DNS resolvers cache responses for performance—poisoned entries persist until TTL expires.
- **Kaminsky Attack (2008)**: Discovered a fundamental flaw allowing cache poisoning at scale—patched by randomizing source ports and transaction IDs.
- **DNSSEC** is the definitive defense—digitally signs DNS records so clients can verify authenticity.
- Without DNSSEC, attackers who can intercept or predict DNS transaction IDs can inject false responses.
- Affects: web browsing, email delivery (MX records), and any service that relies on DNS resolution.

## Connections

- Parent: [[dns-attacks]] — a fundamental DNS integrity attack
- See also: [[dns-spoofing]], [[dnssec-dns-security-extensions]]
