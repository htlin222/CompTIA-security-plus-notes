---
title: "Kerberoasting"
description: "Extracting and cracking service account ticket hashes from Active Directory"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Kerberoasting is a post-exploitation attack against Active Directory environments that exploits the Kerberos authentication protocol to extract encrypted service ticket hashes for service accounts (accounts with SPNs—Service Principal Names). Any authenticated domain user can request service tickets encrypted with the service account's NTLM hash, which can then be taken offline and cracked to recover the service account's plaintext password.

## Key Details

- **Any authenticated domain user** can request service tickets—no special privileges required to perform Kerberoasting.
- Service tickets are encrypted with the **NTLM hash** of the service account's password—weak passwords are quickly cracked offline.
- **Service accounts** often have overly broad privileges and rarely changed passwords—making cracked credentials high-value.
- Detection: unusual TGS (Ticket Granting Service) requests, particularly requesting RC4 encrypted tickets for many SPNs.
- Mitigation: **strong, long, random passwords** for service accounts, **group managed service accounts (gMSA)**—auto-rotate passwords.

## Connections

- Parent: [[password-attacks]] — a Kerberos-specific password extraction technique
- See also: [[pass-the-hash]], [[kerberos]]
