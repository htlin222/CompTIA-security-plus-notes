---
title: "Hardening"
description: "Reducing the attack surface of systems by eliminating unnecessary services, applying patches, and enforcing secure configurations"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/endpoint
  - weight/high
aliases:
  - "System Hardening"
  - "OS Hardening"
---

## Overview

Hardening is the process of securing a system by reducing its attack surface through removing unnecessary software, disabling unused services, applying patches, and configuring security settings according to established benchmarks. Every system should be hardened before deployment and maintained through ongoing configuration management. Hardening applies to operating systems, applications, network devices, and firmware.

## Key Concepts

- **[[cis-benchmarks|CIS Benchmarks]]**: Industry-standard security configuration guidelines from the Center for Internet Security
- **[[stig-security-technical-implementation-guide|STIG (Security Technical Implementation Guide)]]**: DoD-specific hardening standards for government systems
- **[[disable-unnecessary-services-and-ports|Disable unnecessary services and ports]]**: Reduce potential entry points by turning off what is not needed
- **[[remove-default-accounts-and-passwords|Remove default accounts and passwords]]**: Default credentials are publicly known and easily exploited
- **[[patch-management|Patch management]]**: Applying security updates promptly to close known vulnerabilities
- **[[least-functionality-principle|Least functionality principle]]**: Systems should only have the minimum capabilities needed for their role
- **[[application-allowlisting|Application allowlisting]]**: Only permit approved executables to run
- **[[registry-and-gpo-hardening|Registry and GPO hardening]]**: Windows Group Policy Objects enforce security settings across domains
- **[[firmware-updates|Firmware updates]]**: BIOS/UEFI and device firmware must be kept current
- **[[secure-baseline-images|Secure baseline images]]**: Golden images with pre-hardened configurations for consistent deployment
- **[[file-system-permissions|File system permissions]]**: Restricting access to sensitive files and directories

## Exam Tips

> [!tip] Remember
> Hardening = reduce attack surface. Steps: remove defaults, disable services, patch, configure securely, monitor for drift. CIS Benchmarks are the go-to reference for "how should I configure this?"

- Hardening is NOT a one-time activity — drift detection ensures systems stay in compliance
- Know that hardening applies to ALL layers: OS, apps, network devices, firmware, cloud services
- Default configurations are NEVER secure — always customize security settings

## Connections

- Implements findings from [[vulnerability-management]] by closing identified weaknesses
- Strengthens [[endpoint-security]] by establishing secure baselines before deploying systems
- Supports [[compliance]] requirements by following recognized security standards (CIS, STIG)
- [[automation-and-scripting]] ensures hardening configurations are applied consistently at scale

## Scenario

> See [[case-hardening]] for a practical DevOps scenario applying these concepts.
