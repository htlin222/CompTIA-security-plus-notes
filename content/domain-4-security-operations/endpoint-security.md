---
title: "Endpoint Security"
description: "Protection of end-user devices such as workstations, laptops, and mobile devices from threats"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/endpoint
  - weight/high
aliases:
  - "Endpoint Protection"
---

## Overview

Endpoint security encompasses the tools, policies, and practices used to protect individual devices — laptops, desktops, mobile phones, servers, and IoT devices — from cyber threats. As endpoints are the primary interface between users and networks, they represent a critical attack surface. Modern endpoint security has evolved beyond traditional antivirus to include behavioral analysis and automated response.

## Key Concepts

- **[[antivirus-anti-malware|Antivirus / Anti-malware]]**: Signature-based and heuristic detection of known and unknown malware
- **[[host-based-firewall|Host-based firewall]]**: Controls inbound and outbound traffic at the individual device level
- **[[host-based-idsips-hidships|Host-based IDS/IPS (HIDS/HIPS)]]**: Monitors system activity and file integrity on the endpoint
- **[[data-loss-prevention-dlp|Data Loss Prevention (DLP)]]**: Prevents sensitive data from being copied, emailed, or transferred from endpoints
- **[[full-disk-encryption-fde|Full disk encryption (FDE)]]**: Encrypts the entire drive to protect data at rest (e.g., BitLocker, FileVault)
- **[[application-whitelistingallowlisting|Application whitelisting/allowlisting]]**: Only approved applications can execute on the endpoint
- **[[patch-management|Patch management]]**: Keeping OS and applications up to date to close known vulnerabilities
- **[[mobile-device-management-mdm|Mobile Device Management (MDM)]]**: Centralized control of mobile endpoints — remote wipe, enforce policies, manage apps
- **[[boot-integrity|Boot integrity]]**: Secure Boot, Measured Boot, and TPM ensure the system hasn't been tampered with at startup

## Exam Tips

> [!tip] Remember
> Endpoint security is defense-in-depth at the device level. Layer: FDE + host firewall + AV + EDR + patching + allowlisting. Know that BYOD requires MDM and containerization.

- Application allowlisting is more secure than blocklisting but harder to manage
- TPM (Trusted Platform Module) stores encryption keys and supports Secure Boot attestation
- Mobile security: remote wipe, screen lock, containerization, geofencing

## Connections

- Advanced detection capabilities provided by [[edr-xdr]] extend traditional endpoint security
- [[hardening]] procedures (disable services, remove bloatware) are fundamental to endpoint security
- Protects against [[malware-types]] including viruses, trojans, rootkits, and fileless malware
- [[vulnerability-management]] identifies missing patches and misconfigurations on endpoints

## Scenario

> See [[case-endpoint-security]] for a practical DevOps scenario applying these concepts.
