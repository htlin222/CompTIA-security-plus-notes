---
title: "Advisary emulation"
description: "Simulating known threat actor behavior to test detection capabilities"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Adversary emulation is a threat-hunting and security testing technique that involves simulating the tactics, techniques, and procedures (TTPs) of known threat actors to evaluate an organization's detection and response capabilities. Unlike general penetration testing, adversary emulation is guided by threat intelligence about specific threat groups and their known attack patterns, often mapped to frameworks like MITRE ATT&CK.

## Key Details

- Uses real-world threat actor TTPs as the basis for simulation scenarios
- Mapped to MITRE ATT&CK framework for structured, repeatable assessments
- Differs from red teaming: adversary emulation focuses on specific known actors
- Goal is to validate detection rules, SIEM alerts, and SOC response procedures
- Results help identify gaps in defenses against the most likely threats to the organization

## Connections

- Parent: [[threat-hunting]] — adversary emulation is a structured hunting technique
- See also: [[mitre-attck-framework]]
