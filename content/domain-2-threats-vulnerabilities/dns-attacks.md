---
title: "DNS Attacks"
description: "Attacks targeting the Domain Name System to redirect traffic, intercept communications, or disrupt name resolution"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/medium
aliases:
  - "DNS Attacks"
---

## Overview

DNS attacks exploit the Domain Name System — the internet's directory service that translates domain names to IP addresses. Because nearly all internet communication begins with a DNS query, compromising DNS allows attackers to redirect users to malicious sites, intercept sensitive data, or disrupt internet access entirely. DNS was designed without security in mind, making it inherently vulnerable without additional protections.

## Key Concepts

- **[[dns-poisoning-dns-cache-poisoning|DNS poisoning / DNS cache poisoning]]**: Injecting false DNS records into a resolver's cache so users are directed to attacker-controlled servers
- **[[dns-spoofing|DNS spoofing]]**: Forging DNS responses to redirect queries to malicious IP addresses
- **[[dns-hijacking|DNS hijacking]]**: Compromising a domain's DNS settings (at the registrar or DNS server) to redirect all traffic
- **[[dns-tunneling|DNS tunneling]]**: Encoding data within DNS queries and responses to exfiltrate data or establish command-and-control channels
- **[[dns-amplification|DNS amplification]]**: Using open DNS resolvers to amplify DDoS attacks by sending small queries that generate large responses
- **[[domain-hijacking|Domain hijacking]]**: Taking control of a domain name through social engineering the registrar or exploiting weak account security
- **[[typosquatting-url-hijacking|Typosquatting / URL hijacking]]**: Registering domains similar to legitimate ones (e.g., googel.com) to capture mistyped URLs
- **[[dnssec-dns-security-extensions|DNSSEC (DNS Security Extensions)]]**: Adds digital signatures to DNS records to verify authenticity and integrity
- **[[dns-over-https-doh-dns-over-tls-dot|DNS over HTTPS (DoH) / DNS over TLS (DoT)]]**: Encrypts DNS queries to prevent eavesdropping and manipulation

## Exam Tips

> [!tip] Remember
> DNS poisoning = fake records in cache. DNS tunneling = data exfiltration via DNS queries. DNSSEC = integrity (digital signatures, NOT encryption). DoH/DoT = confidentiality (encrypts DNS traffic).

- DNS tunneling is hard to detect because DNS traffic is almost always allowed through firewalls
- DNSSEC prevents poisoning but does NOT encrypt DNS traffic — that is DoH/DoT
- Monitor for unusually large or frequent DNS queries as indicators of DNS tunneling

## Connections

- Specific category of [[network-attacks]] targeting critical internet infrastructure
- DNS amplification is used in [[denial-of-service]] attacks to multiply attack traffic
- DNS tunneling can be detected through [[network-monitoring]] and DNS query log analysis
- [[on-path-attacks]] can intercept and modify DNS responses to redirect victims

## Scenario

> See [[case-dns-attacks]] for a practical DevOps scenario applying these concepts.
