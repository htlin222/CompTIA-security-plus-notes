---
title: "Security baselines and hardening"
description: "Configuring systems according to CIS Benchmarks or STIGs before deployment"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Security baselines and hardening involve configuring systems according to established security standards to reduce their attack surface before and during deployment. Hardening removes or disables unnecessary features, services, and accounts while enabling security-relevant settings. Security baselines—such as CIS Benchmarks or DISA STIGs—provide specific, prescriptive configuration guidance for common operating systems, applications, and network devices.

## Key Details

- **CIS Benchmarks**: Consensus-based security configuration guides for Windows, Linux, macOS, cloud platforms, network devices—free to download.
- **DISA STIGs (Security Technical Implementation Guides)**: DoD configuration standards—more stringent than CIS, mandatory for government systems.
- **Hardening activities**: Disable unused services, close unused ports, remove default accounts, enable logging, configure password policies, apply security patches.
- **Configuration management tools** (Ansible, Puppet, Chef) automate baseline application and drift detection.
- Regular **scanning** against baselines using tools like OpenSCAP verifies compliance over time.

## Connections

- Parent: [[mitigation-techniques]] — hardening as a proactive vulnerability reduction technique
- See also: [[configuration-management]], [[patching]]
