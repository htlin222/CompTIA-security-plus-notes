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

> [!eli5] ELI5: What are DNS Attacks?
> The internet has a phone book that turns website names (like "google.com") into the actual addresses computers use. DNS attacks mess with that phone book. It's like if someone secretly changed the phone number next to your friend's name so that when you call them, you actually reach a stranger pretending to be your friend. The stranger could trick you into sharing secrets. DNS attacks redirect people to fake websites without them ever knowing the address was swapped.

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

## Practice Questions

> [!qbank]- Q-Bank: DNS Attacks (4 Questions)
>
> **Q1.** A security analyst discovers unusually large TXT record queries at regular intervals from an internal workstation to an unfamiliar external domain. Which DNS attack technique is MOST likely being used?
>
> A. DNS cache poisoning
> B. DNS tunneling
> C. DNS amplification
> D. Typosquatting
>
> > [!answer]- Show Answer
> > **B. DNS tunneling**
> >
> > Regular, large DNS queries (especially TXT records) to an external domain are classic indicators of [[dns-tunneling]], which encodes data within DNS queries to exfiltrate data or establish C2 channels. DNS cache poisoning (A) injects false records into a resolver's cache, not unusual query patterns. DNS amplification (C) uses open resolvers to flood a victim with large responses, not internal-to-external exfiltration. Typosquatting (D) involves registering look-alike domains, not unusual DNS query patterns.
>
> **Q2.** An organization deploys DNSSEC across its domains. Which type of DNS attack does DNSSEC PRIMARILY protect against?
>
> A. DNS tunneling
> B. DNS cache poisoning
> C. DNS amplification
> D. Domain hijacking via social engineering
>
> > [!answer]- Show Answer
> > **B. DNS cache poisoning**
> >
> > [[dnssec-dns-security-extensions|DNSSEC]] adds digital signatures to DNS records, allowing resolvers to verify authenticity and integrity — directly preventing [[dns-poisoning-dns-cache-poisoning|DNS cache poisoning]]. DNSSEC does not prevent DNS tunneling (A), which uses valid DNS queries for data exfiltration. DNS amplification (C) is a DDoS technique that DNSSEC does not address. Domain hijacking via social engineering (D) targets registrar accounts, not DNS record integrity.
>
> **Q3.** Users at a company report being redirected to a phishing site when visiting their bank's website. Investigation reveals the company's DNS resolver has incorrect A records for the bank's domain. No changes were made to the resolver configuration. What attack has MOST likely occurred?
>
> A. DNS tunneling
> B. Typosquatting
> C. DNS cache poisoning
> D. DNS amplification
>
> > [!answer]- Show Answer
> > **C. DNS cache poisoning**
> >
> > Incorrect records appearing in a resolver's cache without configuration changes indicates [[dns-poisoning-dns-cache-poisoning|DNS cache poisoning]], where an attacker injected false DNS records. DNS tunneling (A) involves data exfiltration, not record manipulation. Typosquatting (B) requires users to mistype a URL, but users are typing the correct domain. DNS amplification (D) is a DDoS technique, not a redirection attack.
>
> **Q4.** A security team wants to prevent eavesdropping on DNS queries between clients and the organization's DNS resolver. Which solution BEST addresses this requirement?
>
> A. DNSSEC
> B. DNS over HTTPS (DoH)
> C. Longer DNS TTL values
> D. Split-horizon DNS
>
> > [!answer]- Show Answer
> > **B. DNS over HTTPS (DoH)**
> >
> > [[dns-over-https-doh-dns-over-tls-dot|DoH]] encrypts DNS queries to prevent eavesdropping, providing confidentiality for DNS traffic. DNSSEC (A) provides integrity and authenticity through digital signatures but does NOT encrypt DNS queries. Longer TTL values (C) reduce query frequency but do not encrypt traffic. Split-horizon DNS (D) provides different responses to internal vs. external clients but does not encrypt queries.

## Scenario

> See [[case-dns-attacks]] for a practical DevOps scenario applying these concepts.
