---
title: "Configuration management"
description: "Maintaining a consistent, secure baseline of system configurations and detecting drift"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Configuration Management?
> Think of it like keeping a perfect photo of how your room should look. If someone moves things around without asking, you compare against the photo and fix what changed.

## Definition

Configuration management is the practice of establishing, documenting, and maintaining a known-good baseline configuration for systems, and continuously monitoring for unauthorized changes (configuration drift). It ensures that systems remain in a secure, consistent state throughout their lifecycle. Tools like SCCM, Ansible, Puppet, and Chef automate configuration enforcement and drift detection.

## Key Details

- A **configuration baseline** documents the approved secure state of a system (OS version, installed software, settings).
- **Configuration drift** occurs when systems deviate from their baseline—often through unauthorized changes or improper updates.
- Frameworks like **CIS Benchmarks** and **DISA STIGs** provide configuration baselines for common platforms.
- **Change management** processes should govern all configuration changes to prevent unauthorized drift.
- Automated tools provide **continuous compliance monitoring**—alerting when configurations deviate from the baseline.

## Connections

- Parent: [[change-management]] — configuration management is enforced through change control
- See also: [[security-baselines-and-hardening]], [[patching]]
