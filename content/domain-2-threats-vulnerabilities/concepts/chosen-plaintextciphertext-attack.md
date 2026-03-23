---
title: "Chosen plaintext/ciphertext attack"
description: "Attacker can encrypt or decrypt chosen data to extract information about the key"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

In a chosen-plaintext attack (CPA), the attacker can choose arbitrary plaintexts to encrypt and observe the resulting ciphertexts, using the patterns to deduce the encryption key. In a chosen-ciphertext attack (CCA), the attacker can choose arbitrary ciphertexts to decrypt and observe the plaintexts. These are among the strongest cryptanalytic attack models and are used to test the security of cryptographic algorithms.

## Key Details

- **CPA security** is the minimum bar for modern symmetric ciphers—secure algorithms resist this attack model.
- **CCA2 (adaptive chosen-ciphertext attack)**: The attacker can query the decryption oracle even after seeing the challenge ciphertext—the strongest practical model.
- **RSA without padding** (textbook RSA) is vulnerable to chosen-plaintext attacks—always use OAEP padding.
- Relevant to **oracle attacks** in web applications where error messages or timing reveal decryption results.
- Modern secure ciphers (AES-GCM, ChaCha20-Poly1305) are designed to be CCA-secure.

## Connections

- Parent: [[cryptographic-attacks]] — an advanced cryptanalytic attack model
- See also: [[known-plaintext-attack]]
