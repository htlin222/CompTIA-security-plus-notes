---
title: "Password hashing"
description: "uses salting and key stretching to protect stored passwords"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Password hashing is the practice of storing a one-way cryptographic hash of a password rather than the password itself, so that even if the password database is compromised, the attacker cannot directly retrieve the plaintext passwords. Modern password hashing uses salting (adding unique random data before hashing) and key stretching (deliberately slow algorithms) to resist brute-force and rainbow table attacks.

## Key Details

- **Salt**: unique random value added to each password before hashing; prevents rainbow table attacks and ensures identical passwords produce different hashes
- **Key stretching**: designed-to-be-slow algorithms (bcrypt, Argon2, PBKDF2) resist brute-force by making each guess computationally expensive
- MD5 and SHA-1 are NOT appropriate for password hashing — too fast; use bcrypt, Argon2, or PBKDF2
- Password hashing is one-way — there is no decryption; authentication works by hashing the attempt and comparing
- PBKDF2 is NIST-approved and commonly used in FIPS-compliant systems

## Connections

- Parent: [[hashing]] — password hashing is the primary application of hashing in authentication systems
- See also: [[digital-signatures]]
