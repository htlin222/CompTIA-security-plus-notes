---
title: "Quantum computing threat"
description: "Shor's algorithm could break RSA and ECC; post-quantum cryptography is being standardized"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Quantum computing poses an existential threat to current public-key cryptography systems. Sufficiently powerful quantum computers running Shor's algorithm could efficiently factor large integers (breaking RSA) and solve the discrete logarithm problem (breaking ECC and Diffie-Hellman). While fault-tolerant quantum computers capable of breaking current cryptography don't yet exist, the threat drives ongoing standardization of post-quantum cryptographic algorithms.

## Key Details

- **Shor's algorithm**: Polynomial-time quantum algorithm for integer factoring—would break RSA, DSA, ECC, and Diffie-Hellman.
- **Grover's algorithm**: Quadratically speeds up brute-force search—reduces effective security of symmetric keys by half (AES-256 → AES-128 effective security against quantum).
- **"Harvest now, decrypt later"**: Adversaries may be recording encrypted traffic today to decrypt when quantum computers become available.
- **Post-quantum cryptography (PQC)**: NIST standardized CRYSTALS-Kyber (key encapsulation), CRYSTALS-Dilithium, FALCON (digital signatures) in 2024.
- **Symmetric encryption** (AES-256) and hashing (SHA-256+) are largely quantum-resistant—only public-key cryptography is severely threatened.

## Connections

- Parent: [[cryptographic-attacks]] — the future threat landscape for cryptography
- See also: [[deprecated-algorithms]]
