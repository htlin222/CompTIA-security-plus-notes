---
title: "Encryption-based ransomware"
description: "Encrypts files using strong cryptographic algorithms; data is unrecoverable without the key"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Encryption-based ransomware is the dominant form of ransomware that renders victim files inaccessible by encrypting them with strong cryptographic algorithms (typically AES for file encryption, with RSA or ECC to protect the AES key). The decryption key is held by the attacker and only provided upon payment of a ransom. Without the key or unencrypted backups, recovery is generally impossible.

## Key Details

- Uses **hybrid encryption**: Fast symmetric encryption (AES-256) for files; the symmetric key is encrypted with the attacker's public RSA key.
- The attacker's **private key** is required to decrypt the AES key and thus the files—held ransom.
- Typically targets: documents, databases, backups, mapped network drives, and cloud-synced folders.
- **Shadow copies** (Windows VSS) are usually deleted by ransomware before or during encryption.
- Best defense: **offline/air-gapped backups** that cannot be reached by ransomware during its encryption phase.

## Connections

- Parent: [[ransomware]] — the primary ransomware mechanism
- See also: [[locker-ransomware]], [[lateral-movement]]
