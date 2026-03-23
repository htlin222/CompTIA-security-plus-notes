---
title: "Unpatched software"
description: "Known vulnerabilities with available fixes that have not been applied — one of the most exploited vulnerability types"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Unpatched software contains known security vulnerabilities for which the vendor has already released fixes (patches), but the organization has not applied them. This is one of the most commonly exploited vulnerability types in cyberattacks because the vulnerability is publicly known, exploit code is often available, and attackers can scan the internet for vulnerable systems at scale. Timely patching is the most fundamental vulnerability management practice.

## Key Details

- Most successful attacks exploit **known vulnerabilities** with available patches—not zero-days.
- Attackers scan for specific CVEs (Common Vulnerabilities and Exposures) using tools like **Shodan**, **Censys**, and **Masscan**.
- **Time-to-exploit**: The window between patch release and widespread exploitation has shortened dramatically—sometimes measured in hours.
- **CISA KEV (Known Exploited Vulnerabilities) catalog**: A US government list of actively exploited CVEs—organizations should prioritize patching these immediately.
- Challenges: **legacy systems** that cannot be patched, **testing requirements** before deployment, **operational availability** constraints.

## Connections

- Parent: [[vulnerability-types]] — the most commonly exploited vulnerability class
- See also: [[patching]], [[zero-day-vulnerabilities]]
