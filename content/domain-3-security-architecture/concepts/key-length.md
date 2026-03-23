---
title: "Key length"
description: "longer keys = stronger encryption; AES-256 is the current gold standard"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Key length refers to the number of bits in a cryptographic key, which directly determines the theoretical strength of the encryption — longer keys increase the computational work required for a brute-force attack exponentially. The appropriate minimum key length depends on the algorithm type (symmetric vs. asymmetric) and the security requirements of the data being protected.

## Key Details

- **Symmetric (AES)**: 128-bit is currently secure; AES-256 is the recommended standard (quantum-resistant planning)
- **Asymmetric (RSA)**: 2048-bit minimum for current use; 3072+ recommended for data with long-term sensitivity
- **Elliptic Curve (ECC)**: 256-bit ECC provides roughly equivalent security to 3072-bit RSA
- NIST recommends AES-256 and SHA-256+ for algorithms expected to protect data beyond 2030
- Key length alone is not sufficient — algorithm selection and implementation quality also matter

## Connections

- Parent: [[encryption]] — key length is a fundamental parameter determining encryption strength
- See also: [[encryption-modes]]
