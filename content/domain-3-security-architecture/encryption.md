---
title: "Encryption"
description: "Encryption transforms plaintext into ciphertext using algorithms and keys to protect data confidentiality."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cryptography
  - weight/high
aliases:
  - "Encryption"
---

> [!eli5] ELI5: What is Encryption?
> You know how some kids write secret notes using a code only their best friend knows? Encryption works the same way. It scrambles your message so that anyone who intercepts it just sees nonsense. Only the person with the right "key" can unscramble it and read the original message. This is one of the most important ways we keep information private on computers and the internet.

## Overview

Encryption is the process of converting readable data (plaintext) into an unreadable format (ciphertext) using a cryptographic algorithm and a key. Only parties with the correct key can decrypt the data back to its original form. Encryption protects confidentiality and is applied to data at rest, data in transit, and data in use. It is one of the most fundamental security controls.

## Key Concepts

- **Symmetric encryption:**
  - Same key for encryption and decryption
  - Fast, efficient for bulk data
  - Key distribution is the main challenge
  - Algorithms: AES (128/192/256-bit, current standard), 3DES (legacy), Blowfish, Twofish, ChaCha20
- **Asymmetric encryption:**
  - Key pair: public key encrypts, private key decrypts (or vice versa for signing)
  - Slower than symmetric; used for key exchange and digital signatures
  - Algorithms: RSA, ECC (Elliptic Curve), Diffie-Hellman (key exchange), DSA
- **[[hybrid-encryption|Hybrid encryption]]** — uses asymmetric to exchange a symmetric session key, then symmetric for bulk data (TLS uses this)
- **Block vs. stream ciphers:**
  - **Block cipher** — encrypts fixed-size blocks (AES = 128-bit blocks)
  - **Stream cipher** — encrypts one bit/byte at a time (RC4, ChaCha20)
- **[[encryption-modes|Encryption modes]]** — ECB (insecure, patterns visible), CBC, CTR, GCM (authenticated encryption)
- **Data states requiring encryption:**
  - **At rest** — full disk encryption (BitLocker, LUKS), file-level, database encryption
  - **In transit** — TLS/SSL, IPSec, SSH
  - **In use** — homomorphic encryption, secure enclaves (emerging)
- **[[key-length|Key length]]** — longer keys = stronger encryption; AES-256 is the current gold standard

## Exam Tips

> [!tip] Remember
> Symmetric = one key, fast, bulk data (AES). Asymmetric = two keys, slow, key exchange and signatures (RSA, ECC). AES-256 is the standard. TLS uses hybrid encryption. Never use ECB mode — it leaks patterns.

## Connections

- Protects the confidentiality pillar of the [[cia-triad]]
- Subject to [[cryptographic-attacks]] such as brute force, birthday attacks, and downgrade attacks
- Used by [[vpn]] protocols (IPSec, TLS) to secure data in transit
- See also [[key-management]] for the lifecycle of cryptographic keys
- Related to [[hashing]] which provides integrity rather than confidentiality

## Scenario

> See [[case-encryption]] for a practical DevOps scenario applying these concepts.
