---
title: "Credentialed vs. non-credentialed scans"
description: "Credentialed scans log into systems for deeper analysis; non-credentialed scans show the external attacker's view"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Vulnerability scanners can operate in two modes: credentialed (authenticated) scans log into target systems using provided credentials to perform deep internal analysis, while non-credentialed (unauthenticated) scans test systems from the outside without credentials, simulating what an external attacker would see. Each mode provides different value to the vulnerability management program.

## Key Details

- **Credentialed scans**: provide deeper results including installed software versions, registry settings, file permissions, and patch status
- **Non-credentialed scans**: identify open ports, exposed services, and externally visible vulnerabilities from an attacker's perspective
- Credentialed scans find significantly more vulnerabilities than non-credentialed scans
- Non-credentialed scans are useful for external perimeter assessments and prioritizing externally exploitable risks
- Both scan types should be used together for comprehensive vulnerability assessment

## Connections

- Parent: [[vulnerability-management]] — scan type selection is a key vulnerability management decision
- See also: [[vulnerability-scanning]]
