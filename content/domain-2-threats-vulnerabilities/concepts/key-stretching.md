---
title: "Key stretching"
description: "Techniques (PBKDF2, bcrypt, scrypt) that make brute force against passwords computationally expensive"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Key Stretching?
> It makes guessing passwords really slow on purpose. Instead of checking a million guesses per second, the computer takes its time with each one, so attackers would need years instead of minutes.

## Definition

Key stretching is a cryptographic technique that applies a computationally expensive transformation to a password or key to make brute-force and dictionary attacks impractical. By deliberately making the hashing process slow (requiring many iterations or significant memory), key stretching ensures that even with fast hardware, an attacker can only test a relatively small number of candidates per second—dramatically increasing the time required to crack passwords.

## Key Details

- **PBKDF2 (Password-Based Key Derivation Function 2)**: Applies HMAC iteratively (typically 100,000+ rounds); widely used, NIST-approved.
- **bcrypt**: Based on the Blowfish cipher; designed to be memory-intensive and computationally slow; work factor can be increased over time.
- **scrypt**: Memory-hard key derivation—requires significant memory in addition to CPU cycles, resistant to GPU and ASIC cracking.
- **Argon2**: The winner of the Password Hashing Competition (2015); considered the modern gold standard.
- Combined with **salting** (unique random value per password) to defeat rainbow table attacks.

## Connections

- Parent: [[cryptographic-attacks]] — a defense against brute-force cryptographic attacks on passwords
- See also: [[salting]], [[rainbow-table-attack]]
