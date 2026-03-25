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

> [!eli5] ELI5: What is Endpoint Security?
> Every laptop, phone, and tablet in a company is like a door into a building. Endpoint security means putting a strong lock, an alarm, and a guard at each of those doors. If someone tries to sneak in through any single device, the protection catches them. It is not enough to just guard the front gate when there are hundreds of doors -- you need protection on every single one.

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
- **[[tpm|TPM (Trusted Platform Module)]]**: Hardware chip storing cryptographic keys; enables secure boot and disk encryption
- **[[secure-boot|Secure boot]]**: UEFI firmware verifies that boot software is signed by a trusted authority
- **[[measured-boot|Measured boot]]**: Records each boot component's hash in the TPM for later verification (does not block, just logs)
- **[[trusted-boot|Trusted boot]]**: Kernel verifies the integrity of drivers and startup files during the boot process
- **[[sed|SED (Self-Encrypting Drive)]]**: Drive with built-in hardware encryption; data is always encrypted at rest

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

## Practice Questions

> [!qbank]- Q-Bank: Endpoint Security (4 Questions)
>
> **Q1.** A company issues laptops to remote employees who frequently travel. If a laptop is lost or stolen, the organization needs to ensure that data on the device cannot be accessed by unauthorized individuals. Which control BEST addresses this risk?
>
> A. Installing a host-based IDS on the laptop
> B. Enabling full disk encryption with BitLocker
> C. Deploying application allowlisting
> D. Configuring a host-based firewall
>
> > [!answer]- Show Answer
> > **B. Enabling full disk encryption with BitLocker**
> >
> > [[full-disk-encryption-fde|Full disk encryption (FDE)]] protects all data at rest on the device, making it unreadable without the decryption key even if the physical device is stolen. Option A detects suspicious activity but does not protect data at rest. Option C controls which applications can run but does not protect data if the drive is removed. Option D controls network traffic but does not protect stored data.
>
> **Q2.** A healthcare organization wants to prevent employees from installing unauthorized software on company workstations. Some employees have attempted to install personal applications that could introduce malware. Which endpoint control is MOST effective?
>
> A. Full disk encryption
> B. Host-based firewall rules
> C. Application allowlisting
> D. Disabling USB ports
>
> > [!answer]- Show Answer
> > **C. Application allowlisting**
> >
> > [[application-whitelistingallowlisting|Application allowlisting]] ensures only pre-approved applications can execute on the endpoint, preventing all unauthorized software installation. Option A protects data at rest but does not restrict application execution. Option B controls network traffic but does not prevent local software installation. Option D blocks one installation vector but users could still download software from the internet.
>
> **Q3.** An organization discovers that several workstations are running outdated versions of a web browser with known critical vulnerabilities. The security team wants to address this across all 500 endpoints efficiently. What is the BEST approach?
>
> A. Send an email asking users to update their browsers manually
> B. Deploy the update through a centralized patch management system
> C. Block all web browsing until users update their own machines
> D. Replace the affected workstations with new hardware
>
> > [!answer]- Show Answer
> > **B. Deploy the update through a centralized patch management system**
> >
> > [[patch-management]] through a centralized system ensures consistent and timely deployment of updates across all endpoints without relying on user action. Option A depends on user compliance and is unreliable at scale. Option C disrupts business operations unnecessarily. Option D is disproportionate and wasteful when software updates resolve the issue.
>
> **Q4.** A company allows employees to use personal smartphones for work email and accessing internal applications. The security team needs to enforce screen locks, enable remote wipe, and separate personal and corporate data. Which solution BEST meets these requirements?
>
> A. Installing antivirus software on each personal device
> B. Deploying a Mobile Device Management solution with containerization
> C. Requiring employees to use only the corporate VPN
> D. Implementing network access control on the wireless network
>
> > [!answer]- Show Answer
> > **B. Deploying a Mobile Device Management solution with containerization**
> >
> > [[mobile-device-management-mdm|MDM]] provides centralized control over mobile endpoints including policy enforcement (screen locks), remote wipe capability, and containerization to separate corporate and personal data in BYOD scenarios. Option A addresses malware but cannot enforce device policies or enable remote wipe. Option C secures network traffic but does not manage the device itself. Option D controls network access but cannot enforce device-level security policies.

## Scenario

> See [[case-endpoint-security]] for a practical DevOps scenario applying these concepts.
