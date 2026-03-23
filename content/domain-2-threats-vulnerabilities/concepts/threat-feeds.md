---
title: "Threat feeds"
description: "Automated IoC data streams from commercial and open-source providers for security monitoring"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Threat Feeds?
> They're like a constantly updating "wanted poster" list for bad websites, files, and addresses. Security tools check this list automatically so they can block known threats the moment they show up.

## Definition

Threat feeds are automated, continuously updated streams of threat intelligence—including indicators of compromise (IoCs) such as malicious IP addresses, domains, file hashes, and URLs—provided by commercial vendors, open-source projects, government agencies, and industry sharing organizations. They are consumed by security tools (SIEM, IDS/IPS, firewalls, EDR) to enable automated detection of known threats.

## Key Details

- **Commercial feeds**: AlienVault OTX, Recorded Future, CrowdStrike, Mandiant—paid, high-quality, vendor-curated.
- **Open-source feeds**: CIRCL (MISP), Abuse.ch, Emerging Threats, PhishTank—free, community-curated.
- **Government feeds**: US-CERT/CISA, FBI InfraGard, ISACs (Information Sharing and Analysis Centers)—sector-specific.
- **STIX/TAXII format**: The standard way threat feeds are structured and transported—enables machine-readable consumption.
- Feed quality matters: high false-positive rates from low-quality feeds cause alert fatigue—validation and tuning are essential.

## Connections

- Parent: [[indicators-of-compromise]] — threat feeds provide IoC data for monitoring systems
- See also: [[stixtaxii]]
