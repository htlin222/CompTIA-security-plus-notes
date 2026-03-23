---
title: "Secure baseline images"
description: "Golden images with pre-hardened configurations for consistent deployment"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Secure baseline images (also called golden images or gold masters) are pre-configured, fully hardened operating system images that include all required security settings, software, and configurations baked in from the start. When new systems are deployed using these images, they immediately meet the organization's security baseline without requiring manual hardening steps.

## Key Details

- Golden images include: hardened OS configuration, required security agents (EDR, AV), approved applications, security tools
- Dramatically reduces deployment time and ensures consistent security posture across all deployed systems
- Images should be version-controlled and regularly updated with latest patches
- Images must be rebuilt regularly — a 6-month-old golden image already has unpatched vulnerabilities
- CIS Benchmarks and STIGs provide the hardening specifications that should be baked into the golden image

## Connections

- Parent: [[hardening]] — secure baseline images operationalize hardening at scale
- See also: [[cis-benchmarks]]
