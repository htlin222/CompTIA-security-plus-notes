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
- **Key stretching** — techniques that make weak keys stronger by applying hash functions multiple times (bcrypt, PBKDF2)
- **Lightweight cryptography** — algorithms designed for resource-constrained IoT and embedded devices
- **[[perfect-forward-secrecy-pfs|Perfect Forward Secrecy (PFS)]]** — ensures session keys are not compromised even if the server's private key is later exposed; uses [[ephemeral-keys|ephemeral Diffie-Hellman]]
- **NTRU** — post-quantum lattice-based cryptographic algorithm resistant to quantum computing attacks

## Exam Tips

> [!tip] Remember
> Symmetric = one key, fast, bulk data (AES). Asymmetric = two keys, slow, key exchange and signatures (RSA, ECC). AES-256 is the standard. TLS uses hybrid encryption. Never use ECB mode — it leaks patterns.

## Connections

- Protects the confidentiality pillar of the [[cia-triad]]
- Subject to [[cryptographic-attacks]] such as brute force, birthday attacks, and downgrade attacks
- Used by [[vpn]] protocols (IPSec, TLS) to secure data in transit
- See also [[key-management]] for the lifecycle of cryptographic keys
- Related to [[hashing]] which provides integrity rather than confidentiality

## Practice Questions

> [!qbank]- Q-Bank: Encryption (4 Questions)
>
> **Q1.** A security architect needs to encrypt a large database backup file as quickly as possible. Which encryption approach is BEST for this task?
>
> A. RSA with a 4096-bit key
> B. AES-256 symmetric encryption
> C. Diffie-Hellman key exchange
> D. ECC digital signature
>
> > [!answer]- Show Answer
> > **B. AES-256 symmetric encryption**
> >
> > [[encryption|Symmetric encryption]] with AES-256 is fast and efficient for bulk data encryption, making it ideal for large files. RSA (A) is asymmetric and far too slow for encrypting large data directly. Diffie-Hellman (C) is a key exchange protocol, not an encryption algorithm. ECC digital signature (D) provides authentication and integrity, not confidentiality for bulk data.
>
> **Q2.** During a TLS handshake, the client and server use asymmetric encryption to establish a session. Once the session is established, they switch to symmetric encryption for data transfer. Which term BEST describes this approach?
>
> A. Stream cipher encryption
> B. Block cipher encryption
> C. Hybrid encryption
> D. Homomorphic encryption
>
> > [!answer]- Show Answer
> > **C. Hybrid encryption**
> >
> > [[hybrid-encryption|Hybrid encryption]] uses asymmetric cryptography to securely exchange a symmetric session key, then switches to symmetric encryption for the actual data transfer, combining the strengths of both. Stream cipher (A) and block cipher (B) are types of symmetric ciphers, not the overall approach. Homomorphic encryption (D) allows computation on encrypted data, which is unrelated to TLS session establishment.
>
> **Q3.** A developer encrypts sensitive images using ECB (Electronic Codebook) mode and a security auditor flags this as a vulnerability. What is the PRIMARY concern with ECB mode?
>
> A. ECB mode does not use any encryption key
> B. ECB mode produces identical ciphertext blocks for identical plaintext blocks, revealing patterns
> C. ECB mode is too slow for image encryption
> D. ECB mode only works with asymmetric algorithms
>
> > [!answer]- Show Answer
> > **B. ECB mode produces identical ciphertext blocks for identical plaintext blocks, revealing patterns**
> >
> > [[encryption-modes|ECB mode]] encrypts each block independently, so identical plaintext blocks produce identical ciphertext blocks, which leaks data patterns. This is especially visible with images. ECB does use a key (A). ECB is actually fast since blocks can be processed in parallel (C). ECB is a mode for symmetric block ciphers, not limited to asymmetric (D), but the issue is its pattern-leaking behavior.
>
> **Q4.** An organization needs to implement encryption for data in transit between its web servers and client browsers. Which protocol should be used?
>
> A. BitLocker
> B. TLS
> C. LUKS
> D. FileVault
>
> > [!answer]- Show Answer
> > **B. TLS**
> >
> > [[encryption|TLS (Transport Layer Security)]] is the standard protocol for encrypting data in transit between web servers and browsers (HTTPS). BitLocker (A) is a Windows full-disk encryption tool for data at rest. LUKS (C) is a Linux disk encryption standard for data at rest. FileVault (D) is macOS full-disk encryption for data at rest. All three incorrect options protect data at rest, not in transit.

## Scenario

> See [[case-encryption]] for a practical DevOps scenario applying these concepts.
