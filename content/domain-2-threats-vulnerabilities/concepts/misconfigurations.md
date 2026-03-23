---
title: "Misconfigurations"
description: "Default settings, open ports, unnecessary services, overly permissive rules — the most common vulnerability type"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Misconfigurations are security vulnerabilities arising not from flawed code but from incorrectly configured systems, services, and security controls. They are the most commonly exploited vulnerability category and include leaving default credentials, enabling unnecessary services, granting excessive permissions, improper firewall rules, and exposing sensitive data through misconfigured cloud storage. Misconfigurations are typically straightforward to fix but require ongoing vigilance to prevent.

## Key Details

- **Cloud misconfigurations**: Publicly accessible S3 buckets, open security groups, overly permissive IAM policies—a leading cause of cloud data breaches.
- **Default settings**: Default admin credentials, sample applications, default SNMP community strings, unnecessary features enabled.
- **Overly permissive access rules**: Firewall rules that allow more traffic than necessary, directory browsing enabled on web servers.
- Mitigation: **security hardening baselines** (CIS Benchmarks, STIGs), **configuration management** tools, **cloud security posture management (CSPM)**.
- Security misconfiguration is consistently in the **OWASP Top 10** for web applications.

## Connections

- Parent: [[vulnerability-types]] — the most prevalent vulnerability category
- See also: [[default-credentials]], [[security-baselines-and-hardening]]
