---
title: "Pass-the-hash"
description: "Using a captured NTLM hash to authenticate without knowing the actual plaintext password"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Pass-the-hash is an attack technique that exploits Windows NTLM authentication by using a captured password hash directly for authentication—without needing to crack it to obtain the plaintext password. Since NTLM authentication uses the hash itself as proof of knowledge, an attacker with access to a hash (e.g., extracted from LSASS memory) can authenticate to other systems using that hash.

## Key Details

- Exploits **NTLM authentication**: The hash IS the credential in NTLM—knowing the hash is equivalent to knowing the password for authentication purposes.
- Hashes are extracted from: **LSASS process memory** (using Mimikatz), **SAM database**, **NTDS.dit** (Active Directory database).
- Enables **lateral movement** without cracking: attacker uses the hash to authenticate to other systems the account has access to.
- **Mitigation**: **Credential Guard** (Windows 10/Server 2016+)—uses virtualization-based security to protect LSASS; **Kerberos authentication** (doesn't use NTLM hashes); **local admin account restrictions**.
- **Pass-the-ticket**: The Kerberos equivalent—uses stolen Kerberos tickets instead of NTLM hashes.

## Connections

- Parent: [[password-attacks]] — a credential re-use attack against Windows authentication
- See also: [[kerberoasting]]
