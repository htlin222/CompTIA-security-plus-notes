---
title: "Weak encryption"
description: "Using deprecated algorithms (DES, MD5, SHA-1, RC4) or insufficient key lengths"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Weak encryption refers to the use of cryptographic algorithms that are known to be vulnerable due to mathematical flaws, computational feasibility of breaking them, or insufficient key lengths given modern computing power. Using weak encryption provides a false sense of security—data appears protected but can be decrypted by a determined attacker with the right tools.

## Key Details

- **DES (56-bit)**: Brutable in hours with modern hardware; replaced by **3DES** (temporarily) then **AES**.
- **RC4**: Statistical biases in the keystream make it vulnerable to various attacks; banned in TLS 1.3.
- **MD5/SHA-1**: Collision attacks demonstrated; unsuitable for digital signatures and integrity verification.
- **RSA with small keys** (< 2048-bit): No longer secure against well-resourced adversaries; use RSA-2048+ or ECC.
- **Insufficient IV reuse**: Using the same initialization vector with a stream cipher reveals XOR patterns between messages.

## Connections

- Parent: [[vulnerability-types]] — cryptographic weakness as a vulnerability category
- See also: [[deprecated-algorithms]], [[downgrade-attack]]
