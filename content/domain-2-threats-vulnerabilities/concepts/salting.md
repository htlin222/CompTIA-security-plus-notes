---
title: "Salting"
description: "Adding random data to passwords before hashing to defeat rainbow table attacks"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Salting?
> Before scrambling your password, the computer mixes in a random handful of extra characters. Even if two people use the same password, the scrambled results look completely different, which stops cheat-sheet attacks.

## Definition

Salting is a cryptographic technique that adds a unique random value (the "salt") to each password before hashing it. Because each password gets a different salt, identical passwords produce different hash outputs, and precomputed rainbow tables (which assume unsalted hashing) become completely useless. Salts are typically stored alongside the password hash in the database and are not secret—their value comes from their uniqueness.

## Key Details

- **Salt must be unique per password**: A single global salt defeats the purpose—unique salts ensure each hash is distinct.
- **Salt size**: Should be at least 128 bits (16 bytes) to ensure sufficient randomness.
- **Stored with the hash**: The salt is not secret—it's stored alongside the hash in the database. Salts thwart precomputed attacks, not targeted brute-force against a specific account.
- **Combined with key stretching**: bcrypt, scrypt, and Argon2 automatically include salting and stretching—the best practice for password storage.
- Does not protect against per-hash brute-force cracking—that's why key stretching is also needed.

## Connections

- Parent: [[password-attacks]] — the primary defense against rainbow table attacks
- See also: [[key-stretching]], [[rainbow-table-attack]]
