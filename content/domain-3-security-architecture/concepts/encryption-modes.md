---
title: "Encryption modes"
description: "ECB (insecure, patterns visible), CBC, CTR, GCM (authenticated encryption)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What are Encryption modes?
> Encryption modes are different recipes for scrambling data. Some recipes are simple but leave patterns visible (like a bad disguise), while others mix things up so well that nothing recognizable remains. Choosing the right mode matters for keeping secrets truly secret.

## Definition

Block cipher encryption modes define how a block cipher algorithm (such as AES) processes data that is longer than a single block. The choice of mode significantly impacts the security properties of the encryption — some modes are considered insecure for general use, while others provide additional properties such as authentication (AEAD modes) in addition to confidentiality.

## Key Details

- **ECB (Electronic Codebook)**: each block encrypted independently; identical plaintext blocks produce identical ciphertext blocks — reveals patterns; considered insecure
- **CBC (Cipher Block Chaining)**: each block XORed with the previous ciphertext before encryption; requires an IV; vulnerable to padding oracle attacks
- **CTR (Counter)**: converts block cipher into stream cipher using a counter; parallelizable; no padding required
- **GCM (Galois/Counter Mode)**: AEAD mode providing both encryption and authentication (integrity); the preferred modern choice (used in TLS 1.3)
- AES-GCM is the recommended mode for new implementations

## Connections

- Parent: [[encryption]] — encryption modes determine how block ciphers are applied to data
- See also: [[hybrid-encryption]]
