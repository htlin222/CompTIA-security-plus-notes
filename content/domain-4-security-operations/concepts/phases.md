---
title: "Phases"
description: "Planning/scoping → Reconnaissance → Scanning → Exploitation → Post-exploitation → Reporting"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Phases?
> Phases break a big process into clear steps. It is like following a recipe -- you do not frost the cake before you bake it. Each phase has to happen in the right order.

## Definition

Penetration testing follows a structured set of phases that guide the tester from initial authorization through final reporting. Each phase builds on the previous one and is designed to methodically evaluate the security of the target environment in a controlled, authorized manner that mimics the approach of real attackers.

## Key Details

- **Planning/Scoping**: define objectives, scope, rules of engagement, and obtain written authorization
- **Reconnaissance**: gather information about the target (OSINT, DNS, WHOIS, social engineering research)
- **Scanning/Enumeration**: identify live systems, open ports, running services, and potential vulnerabilities
- **Exploitation**: actively attempt to compromise identified vulnerabilities to gain unauthorized access
- **Post-exploitation**: pivot, escalate privileges, demonstrate impact, document what an attacker could achieve
- **Reporting**: document all findings, evidence, and remediation recommendations for the client

## Connections

- Parent: [[penetration-testing]] — these phases define the structured methodology of penetration testing
- See also: [[reconnaissance]]
