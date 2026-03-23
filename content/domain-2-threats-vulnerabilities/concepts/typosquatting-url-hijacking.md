---
title: "Typosquatting / URL hijacking"
description: "Registering look-alike domains (e.g., googel.com) to capture users who mistype URLs"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Typosquatting / URL Hijacking?
> If you accidentally type "gogle.com" instead of "google.com," a bad guy might own that misspelled address and use it to trick you. They set up traps at addresses where people commonly make typos.

## Definition

Typosquatting and URL hijacking in the DNS context refers to registering domain names that differ from legitimate ones by common typographical errors or slight variations. Users who mistype a URL or click on a misleadingly similar link end up at an attacker-controlled server rather than the legitimate website. These domains are used for phishing, malware distribution, or traffic monetization through advertising.

## Key Details

- Exploits: **keyboard adjacency** (goofle.com), **missing/extra letters**, **transposition errors**, **wrong TLD** (.net instead of .com), **homograph attacks** (Unicode look-alikes).
- **IDN homograph attacks**: Register domains using Unicode characters that visually identical to ASCII—e.g., using Cyrillic "а" instead of Latin "a" in a domain name.
- Impact: **phishing credential theft**, **malware delivery**, **brand damage**, **traffic theft**.
- Organizations mitigate by: **registering typo variants** preemptively, **trademark monitoring services**, **UDRP (Uniform Domain-Name Dispute-Resolution Policy)** to reclaim abusive registrations.
- Browser **phishing protection** databases (Google Safe Browsing) include known typosquatting domains.

## Connections

- Parent: [[dns-attacks]] — domain-level deception using DNS
- See also: [[domain-hijacking], [[brand-impersonation]]
