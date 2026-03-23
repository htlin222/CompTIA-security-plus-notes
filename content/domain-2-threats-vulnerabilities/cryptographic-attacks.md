---
title: "Cryptographic Attacks"
description: "Attacks targeting cryptographic implementations to break encryption, forge signatures, or bypass protections"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/cryptography
  - weight/medium
aliases:
  - "Crypto Attacks"
---

## Overview

Cryptographic attacks target weaknesses in cryptographic algorithms, implementations, or key management practices to decrypt protected data, forge digital signatures, or bypass security controls. While modern algorithms are generally secure when properly implemented, flaws in implementation, key management, or the use of deprecated algorithms create exploitable vulnerabilities. The exam focuses on understanding attack types and knowing which algorithms are considered secure.

## Key Concepts

- **[[brute-force|Brute force]]**: Trying all possible keys until the correct one is found — feasibility depends on key length
- **[[birthday-attack|Birthday attack]]**: Exploits the mathematics of hash collisions; finding two inputs that produce the same hash output
- **[[collision-attack|Collision attack]]**: Specifically crafting two different inputs that produce an identical hash — compromises integrity verification
- **[[downgrade-attack|Downgrade attack]]**: Forcing a system to use a weaker, vulnerable cryptographic protocol or cipher (e.g., POODLE forcing SSL 3.0)
- **[[known-plaintext-attack|Known plaintext attack]]**: Attacker has both plaintext and corresponding ciphertext and uses them to derive the key
- **[[chosen-plaintextciphertext-attack|Chosen plaintext/ciphertext attack]]**: Attacker can encrypt or decrypt chosen data to extract information about the key
- **[[side-channel-attacks|Side-channel attacks]]**: Exploiting physical characteristics (timing, power consumption, electromagnetic emissions) rather than algorithmic weaknesses
- **[[key-stretching|Key stretching]]**: Techniques (PBKDF2, bcrypt, scrypt) that make brute force against passwords computationally expensive
- **[[deprecated-algorithms|Deprecated algorithms]]**: MD5 and SHA-1 (collision-vulnerable), DES (56-bit key too short), RC4 (biases in keystream)
- **[[quantum-computing-threat|Quantum computing threat]]**: Shor's algorithm could break RSA and ECC; post-quantum cryptography is being standardized

## Exam Tips

> [!tip] Remember
> MD5 and SHA-1 = broken (collisions found). DES = too short (56-bit). Use SHA-256+ for hashing, AES-256 for symmetric encryption. Downgrade attacks force weaker crypto — disable legacy protocols to prevent them.

- Birthday attack effectiveness: a 128-bit hash only provides 64 bits of collision resistance
- Key stretching (bcrypt, PBKDF2) is the defense for password hashing — NOT plain SHA-256
- Know that quantum computing threatens asymmetric crypto (RSA, ECC) more than symmetric (AES)

## Connections

- Targets [[encryption]] implementations and protocols — understanding these attacks informs proper crypto choices
- [[password-attacks]] overlap with brute-force attacks on cryptographic keys and hashed passwords
- Downgrade attacks can undermine [[vpn]] and TLS connections by forcing weak cipher suites
- Understanding these attacks is essential for [[vulnerability-types]] assessment in cryptographic systems

## Scenario

> See [[case-cryptographic-attacks]] for a practical DevOps scenario applying these concepts.
