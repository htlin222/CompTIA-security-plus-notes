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

## Practice Questions

> [!qbank]- Q-Bank: Key Management (4 Questions)
>
> **Q1.** A financial institution needs to store its most sensitive cryptographic keys in a tamper-resistant device that also performs cryptographic operations. Which solution BEST meets this requirement?
>
> A. Trusted Platform Module (TPM)
> B. Hardware Security Module (HSM)
> C. Software key vault on a hardened server
> D. Encrypted USB drive in a safe
>
> > [!answer]- Show Answer
> > **B. Hardware Security Module (HSM)**
> >
> > An [[hardware-security-module-hsm|HSM]] is a dedicated, tamper-resistant hardware device specifically designed to manage cryptographic keys and perform cryptographic operations at scale. A TPM (A) is a chip on the motherboard useful for individual device keys and secure boot, but not designed for enterprise-scale key management. A software key vault (C) lacks the hardware tamper resistance. An encrypted USB drive (D) provides physical storage but no cryptographic processing capability.
>
> **Q2.** A security team implements a TLS configuration that generates unique session keys for every connection, ensuring that compromising the server's long-term private key cannot decrypt past sessions. Which concept does this describe?
>
> A. Key escrow
> B. Key splitting
> C. Perfect forward secrecy (PFS)
> D. Key wrapping
>
> > [!answer]- Show Answer
> > **C. Perfect forward secrecy (PFS)**
> >
> > [[perfect-forward-secrecy-pfs|Perfect forward secrecy]] uses [[ephemeral-keys|ephemeral keys]] for each session, so past session keys cannot be derived from a compromised long-term key. Key escrow (A) involves a third party holding key copies for recovery. Key splitting (B) divides a key among multiple custodians. Key wrapping encrypts keys for secure transport but does not address session key independence.
>
> **Q3.** An organization's key management policy requires that no single administrator can access the master encryption key alone. Which technique enforces this requirement?
>
> A. Key rotation on a monthly schedule
> B. Storing the key in a TPM chip
> C. Key splitting using Shamir's Secret Sharing
> D. Using ephemeral keys for each transaction
>
> > [!answer]- Show Answer
> > **C. Key splitting using Shamir's Secret Sharing**
> >
> > [[key-splitting-secret-sharing|Key splitting (Shamir's Secret Sharing)]] divides a key among multiple custodians so that a threshold number must collaborate to reconstruct it, preventing any single person from accessing it alone. Key rotation (A) replaces keys periodically but does not address single-person access. TPM storage (B) ties the key to hardware but does not enforce multi-person access. Ephemeral keys (D) are temporary session keys, not related to access control.
>
> **Q4.** During a security review, an auditor finds that encryption keys are stored in a plaintext configuration file on the application server. Which key management principle is being violated?
>
> A. Key rotation
> B. Secure key storage
> C. Key generation
> D. Key distribution
>
> > [!answer]- Show Answer
> > **B. Secure key storage**
> >
> > [[key-management|Secure key storage]] requires that keys never be stored in plaintext — they should be protected in HSMs, TPMs, or encrypted key vaults. Key rotation (A) addresses how often keys are replaced, not how they are stored. Key generation (C) concerns how keys are created using secure random number generators. Key distribution (D) addresses how keys are securely transmitted between parties.

## Scenario

> See [[case-key-management]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [1.4 – Key Exchange](https://www.youtube.com/watch?v=U6BWn81P5Ec)
