---
title: "Known plaintext attack"
description: "Attacker has both plaintext and corresponding ciphertext and uses them to derive the key"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

In a known-plaintext attack (KPA), the attacker possesses pairs of plaintext messages and their corresponding ciphertexts, which they use to analyze the relationship between the two in order to deduce the encryption key or find patterns that can be exploited to decrypt other ciphertexts. This attack model is weaker than chosen-plaintext (where the attacker can select what to encrypt) but historically significant.

## Key Details

- **Historical context**: The Allied codebreakers at Bletchley Park used known-plaintext attacks against the German Enigma cipher (knowing that messages often started with "WETTER" for weather reports).
- **XOR cipher**: Trivially broken with known plaintext—XOR the plaintext with ciphertext to recover the key directly.
- Relevant when attackers have predictable portions of encrypted messages (file headers, protocol fields, email signatures).
- **Weak stream ciphers** (like WEP's RC4 implementation) were vulnerable to known-plaintext attacks.
- Modern ciphers (AES in randomized modes) are designed to resist known-plaintext attacks.

## Connections

- Parent: [[cryptographic-attacks]] — a classical cryptanalytic attack model
- See also: [[chosen-plaintextciphertext-attack]]
