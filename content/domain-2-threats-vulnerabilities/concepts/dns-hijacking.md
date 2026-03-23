---
title: "DNS hijacking"
description: "Compromising a domain's DNS settings to redirect all traffic to attacker-controlled servers"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

DNS hijacking is an attack in which an attacker gains control over a domain's DNS configuration—either by compromising the domain registrar account, the authoritative DNS server, or ISP-level DNS infrastructure—and changes DNS records to redirect traffic for legitimate domains to attacker-controlled servers. This enables mass interception of traffic, credential harvesting, and malware distribution.

## Key Details

- **Registrar-level hijacking**: Attacker gains access to the domain registrar account (via credential theft) and changes nameserver records.
- **Authoritative server compromise**: Attacker compromises the DNS server that holds authoritative records for a domain.
- **Router/ISP hijacking**: Malware changes DNS settings on home routers or ISPs redirect queries to rogue resolvers.
- **DNSChanger** malware is a famous example—changed DNS settings on millions of routers worldwide.
- Prevention: **registrar lock** (prevents unauthorized transfers), **DNSSEC**, **MFA on registrar accounts**, **monitoring DNS records for changes**.

## Connections

- Parent: [[dns-attacks]] — a DNS infrastructure attack
- See also: [[dns-poisoning-dns-cache-poisoning]]
