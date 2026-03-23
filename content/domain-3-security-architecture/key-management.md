---
title: "Key Management"
description: "Key management encompasses the generation, distribution, storage, rotation, and destruction of cryptographic keys throughout their lifecycle."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cryptography
  - weight/medium
aliases:
  - "Key Management"
---

> [!eli5] ELI5: What is Key Management?
> If encryption is like using a lock to keep your secrets safe, then key management is about taking care of the keys themselves. Where do you keep the key? Who gets a copy? When do you change the locks? If you lose the key or someone copies it, the lock becomes useless. Key management is all the rules for creating, sharing, storing, and eventually throwing away those keys so your secrets stay protected.

## Overview

Key management is the set of policies and procedures governing the entire lifecycle of cryptographic keys. Poor key management can undermine even the strongest encryption algorithms. Keys must be generated securely, distributed safely, stored with strong protections, rotated regularly, and destroyed completely when no longer needed.

## Key Concepts

- **Key lifecycle stages:**
  1. **Generation** — use cryptographically secure random number generators; adequate key length
  2. **Distribution** — secure key exchange (Diffie-Hellman, out-of-band delivery, key wrapping)
  3. **Storage** — protect keys in hardware security modules (HSMs), TPMs, or key vaults; never store in plaintext
  4. **Usage** — enforce least privilege; separate keys for different purposes (signing vs. encryption)
  5. **Rotation** — regularly replace keys to limit exposure if a key is compromised
  6. **Revocation** — invalidate compromised or expired keys (CRL, OCSP for certificates)
  7. **Destruction** — securely erase keys using cryptographic erasure or zeroization
- **[[hardware-security-module-hsm|Hardware Security Module (HSM)]]** — tamper-resistant hardware device that manages keys and performs cryptographic operations
- **[[trusted-platform-module-tpm|Trusted Platform Module (TPM)]]** — chip on the motherboard that stores keys and supports measured boot
- **[[key-escrow|Key escrow]]** — third party holds a copy of the key for recovery; controversial due to trust implications
- **[[key-splitting-secret-sharing|Key splitting / secret sharing]]** — divide a key among multiple custodians; requires a threshold to reconstruct (Shamir's Secret Sharing)
- **[[ephemeral-keys|Ephemeral keys]]** — temporary keys used for a single session; provide perfect forward secrecy
- **[[perfect-forward-secrecy-pfs|Perfect forward secrecy (PFS)]]** — compromising long-term keys does not compromise past session keys

## Exam Tips

> [!tip] Remember
> HSM = hardware key storage, tamper-resistant. TPM = motherboard chip for keys and secure boot. PFS = session keys are ephemeral, so past traffic cannot be decrypted even if the private key is later compromised. Never store keys in plaintext.

## Connections

- Supports the security of [[encryption]] by ensuring keys are handled properly throughout their lifecycle
- Critical to [[pki]] operations where CA private keys must be protected in HSMs
- See also [[certificates]] for how key management applies to certificate private keys and renewal

## Scenario

> See [[case-key-management]] for a practical DevOps scenario applying these concepts.
