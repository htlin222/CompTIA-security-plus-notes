---
title: "Deprecated algorithms"
description: "MD5, SHA-1, DES, RC4 — algorithms that are cryptographically weak and should not be used"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Deprecated cryptographic algorithms are those that have been found to have significant weaknesses—due to short key lengths, mathematical vulnerabilities, or demonstrated attacks—and should no longer be used for security purposes. Using deprecated algorithms creates exploitable vulnerabilities even when implemented correctly, because the fundamental mathematics underlying them have been broken or weakened.

## Key Details

- **MD5**: Collision-vulnerable—two different inputs can be crafted to produce the same hash; do not use for integrity or digital signatures.
- **SHA-1**: Practical collisions demonstrated (SHAttered, 2017); being phased out by browsers and CAs.
- **DES**: 56-bit key is too short—brutable in hours with modern hardware; use AES instead.
- **RC4**: Statistical biases in keystream make it vulnerable to plaintext recovery—banned in TLS 1.3.
- **3DES**: Deprecated due to SWEET32 attack (birthday attack on 64-bit block size); replaced by AES.

## Connections

- Parent: [[cryptographic-attacks]] — deprecated algorithms are the target of cryptographic attacks
- See also: [[weak-encryption]], [[downgrade-attack]]
