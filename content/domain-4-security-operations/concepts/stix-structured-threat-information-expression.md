---
title: "STIX (Structured Threat Information eXpression)"
description: "Standardized language for describing cyber threat information"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - STIX
---

## Definition

STIX (Structured Threat Information eXpression) is a standardized, machine-readable language for describing cybersecurity threat information. Developed by MITRE and now maintained by OASIS, STIX provides a common format for expressing threat intelligence including threat actors, attack campaigns, indicators of compromise (IoCs), malware details, and vulnerability information.

## Key Details

- Current version is STIX 2.1; uses JSON format (earlier versions used XML)
- STIX objects: threat actors, campaigns, indicators, malware, attack patterns, courses of action, vulnerabilities
- Relationships between objects create a graph of threat intelligence (e.g., threat actor "uses" malware, malware "indicates" campaign)
- STIX is used with TAXII for automated, standardized sharing of threat intelligence between organizations
- Security tools that consume STIX can automatically import and act on shared threat intelligence

## Connections

- Parent: [[threat-intelligence]] — STIX is the standard format for machine-readable threat intelligence sharing
- See also: [[taxii-trusted-automated-exchange-of-intelligence-information]]
