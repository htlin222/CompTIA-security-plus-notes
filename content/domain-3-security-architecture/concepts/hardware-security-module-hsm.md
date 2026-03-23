---
title: "Hardware Security Module (HSM)"
description: "tamper-resistant hardware device that manages keys and performs cryptographic operations"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
aliases:
  - HSM
---

## Definition

A Hardware Security Module (HSM) is a dedicated, tamper-resistant physical computing device that safeguards and manages cryptographic keys and performs cryptographic operations. HSMs provide a hardened, isolated environment for key storage and crypto operations, ensuring that private keys are never exposed to software or the host operating system, even for administrators.

## Key Details

- Keys stored in HSMs cannot be exported in plaintext — they stay inside the secure boundary
- HSMs are designed to be tamper-evident and tamper-resistant: physical intrusion triggers key deletion
- Used for: CA private keys, payment HSMs (PIN processing), TLS private keys, code signing keys
- Available as physical appliances (nCipher, Thales Luna) or cloud HSMs (AWS CloudHSM, Azure Dedicated HSM)
- FIPS 140-2 Level 3 validation is the common certification standard for HSMs

## Connections

- Parent: [[key-management]] — HSMs are the gold standard for protecting cryptographic keys
- See also: [[trusted-platform-module-tpm]]
