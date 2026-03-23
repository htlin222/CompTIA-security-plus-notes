---
title: "Registry and GPO hardening"
description: "Windows Group Policy Objects enforce security settings across domains"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Registry hardening involves configuring specific Windows registry keys to enforce security settings, disable dangerous features, and restrict user capabilities. Group Policy Objects (GPOs) in Active Directory environments provide a centralized, scalable mechanism to apply and enforce registry settings, security configurations, and restrictions across all managed Windows systems in a domain.

## Key Details

- GPOs are linked to Active Directory Organizational Units (OUs) and applied automatically to member computers
- Common GPO hardening: disable autorun, enforce NTLMv2, restrict SMBv1, configure Windows Firewall, enforce password policies
- CIS Benchmarks and STIGs provide specific GPO templates for baseline hardening
- Registry hardening without GPO requires manual or scripted changes on each system
- GPO settings are applied at startup/login and periodically refreshed (every 90 minutes + random offset)

## Connections

- Parent: [[hardening]] — GPO and registry hardening are the primary Windows-specific hardening mechanisms
- See also: [[cis-benchmarks]]
