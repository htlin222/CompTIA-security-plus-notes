---
title: "Rainbow table attack"
description: "Using precomputed hash-to-password lookup tables to crack hashed passwords quickly"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Rainbow Table Attack?
> Instead of guessing passwords one by one, the attacker has a giant cheat sheet that already has millions of passwords matched to their scrambled versions. They just look yours up.

## Definition

A rainbow table attack uses precomputed lookup tables that map plaintext passwords to their hash values, allowing an attacker to quickly reverse a hash to its plaintext password by looking it up in the table—instead of computing hashes on the fly. Rainbow tables trade storage space for speed, enabling extremely fast password cracking of unsalted hashes.

## Key Details

- **Precomputed lookup**: Instead of computing hashes during the attack, the attacker simply looks up the hash in a pre-built table—orders of magnitude faster than brute-force.
- **Space-time tradeoff**: Rainbow tables use clever chain compression to store more combinations in less space than simple hash tables.
- Effective against: **unsalted MD5**, **SHA-1**, and other unsalted common hash functions—tables for these are freely available online.
- **Completely defeated by salting**: A unique random salt added to each password before hashing makes precomputed tables useless—must build a unique table for each salt.
- Sites like CrackStation.net serve as online rainbow table lookups for common hashes.

## Connections

- Parent: [[password-attacks]] — a precomputed attack against hashed passwords
- See also: [[salting]], [[key-stretching]]
