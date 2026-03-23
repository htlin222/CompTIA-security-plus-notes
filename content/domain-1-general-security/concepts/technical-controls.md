---
title: "Technical controls"
description: "Firewalls, encryption, access control systems, IDS — technology-based security mechanisms"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What are Technical Controls?
> These are the security tools built right into the technology itself -- like a password on your phone, a firewall blocking bad websites, or software that scrambles your messages so only the right person can read them.

## Definition

Technical controls (also called logical controls) are security measures implemented through technology—hardware, software, or firmware—to protect information systems and data. They are the most directly verifiable and automatable control category, and they form the middle layer of a defense-in-depth strategy between administrative (policy) controls and physical controls.

## Key Details

- Examples: **firewalls**, **encryption**, **access control systems** (RBAC, ABAC), **IDS/IPS**, **antivirus/EDR**, **MFA systems**, **VPNs**, **SIEM**.
- Technical controls can be: **preventive** (firewalls blocking traffic), **detective** (IDS alerting on attacks), or **corrective** (antivirus quarantining malware).
- Provide **consistent enforcement** without human intervention—rules are applied automatically.
- Must be configured correctly to be effective—misconfigurations turn technical controls into vulnerabilities themselves.
- Should be supported by **administrative controls** (policies) that define what the technical controls should enforce.

## Connections

- Parent: [[defense-in-depth]] — one of three control types in layered security
- See also: [[administrative-controls]], [[physical-controls]]
