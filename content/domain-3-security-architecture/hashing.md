---
title: "Hashing"
description: "Hashing produces a fixed-length digest from input data to verify integrity, authenticate messages, and securely store passwords."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cryptography
  - weight/high
aliases:
  - "Hashing"
  - "Hash Functions"
---

> [!eli5] ELI5: What is Hashing?
> Think of hashing like a fingerprint for data. Just like every person has a unique fingerprint, hashing takes any piece of information and creates a unique code for it. If even one tiny thing changes in the original data, the fingerprint looks completely different. This makes it easy to check if something has been tampered with. Unlike encryption, you cannot turn the fingerprint back into the original -- it is a one-way process.

## Overview

Hashing is a one-way cryptographic function that converts input data of any size into a fixed-length output (hash, digest, or fingerprint). Unlike encryption, hashing is irreversible. Hashing is used to verify data integrity, authenticate messages (HMAC), store passwords securely, and create digital signatures. Any change to the input produces a completely different hash.

## Key Concepts

- **Properties of a good hash function:**
  - **Deterministic** — same input always produces the same output
  - **Fixed output length** — regardless of input size
  - **Avalanche effect** — small input change produces drastically different output
  - **Pre-image resistance** — cannot derive the input from the hash
  - **Collision resistance** — computationally infeasible to find two inputs with the same hash
- **Common hash algorithms:**
  - **MD5** — 128-bit; broken, vulnerable to collisions; do not use for security
  - **SHA-1** — 160-bit; deprecated due to collision vulnerabilities
  - **SHA-2 family** — SHA-256, SHA-384, SHA-512; current standard; widely used
  - **SHA-3** — newest standard; based on Keccak algorithm; alternative to SHA-2
- **[[hmac-hash-based-message-authentication-code|HMAC (Hash-based Message Authentication Code)]]** — combines a hash with a secret key to provide integrity AND authentication
- **[[password-hashing|Password hashing]]** — uses salting and key stretching to protect stored passwords
  - **Salt** — random value added to each password before hashing; prevents rainbow table attacks
  - **Key stretching** — intentionally slow hashing (bcrypt, scrypt, PBKDF2, Argon2) to resist brute force
  - **Rainbow table** — precomputed table of hashes; defeated by salting
- **[[digital-signatures|Digital signatures]]** — hash the message, then encrypt the hash with the sender's private key
- **[[file-integrity-monitoring|File integrity monitoring]]** — comparing current file hashes to known-good baselines to detect tampering

## Exam Tips

> [!tip] Remember
> MD5 and SHA-1 are deprecated. SHA-256 is the current standard. Hashing is one-way; encryption is two-way. HMAC = hash + key = integrity + authentication. Salt defeats rainbow tables. Bcrypt/Argon2 defeat brute force on passwords.

## Connections

- Provides the integrity component that [[encryption]] does not (encryption = confidentiality, hashing = integrity)
- Used within [[pki]] for digital signatures — the message hash is signed with the private key
- See also [[key-management]] for HMAC key handling and password hashing salt management

## Scenario

> See [[case-hashing]] for a practical DevOps scenario applying these concepts.
