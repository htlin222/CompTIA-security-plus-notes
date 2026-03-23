---
title: "STIX/TAXII"
description: "Standards for formatting (STIX) and sharing (TAXII) IoC data between organizations"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

STIX (Structured Threat Information eXpression) and TAXII (Trusted Automated eXchange of Intelligence Information) are complementary standards for sharing threat intelligence. STIX defines a common language and format for describing cyber threat information—including IoCs, TTPs, threat actors, campaigns, and courses of action. TAXII defines the transport protocol and services for sharing STIX content between organizations, tools, and platforms.

## Key Details

- **STIX**: A JSON-based format for describing threat intel objects (Indicators, Observables, Attack Patterns, Threat Actors, Campaigns, etc.) in a machine-readable way.
- **TAXII**: Defines a RESTful API for exchanging STIX content—supports **push** and **pull** sharing models.
- Together they enable **automated threat intelligence sharing** between SIEMs, threat platforms, ISACs, and government agencies.
- **MISP** (Malware Information Sharing Platform) and **OpenCTI** are common open-source platforms that support STIX/TAXII.
- Enables **machine-speed IoC sharing**: A new malicious hash discovered by one organization can be pushed to all subscribers within seconds.

## Connections

- Parent: [[indicators-of-compromise]] — the standard format for sharing IoC data
- See also: [[threat-feeds]]
