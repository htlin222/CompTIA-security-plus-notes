---
title: "Trusted Platform Module (TPM)"
description: "chip on the motherboard that stores keys and supports measured boot"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
aliases:
  - TPM
---

## Definition

A Trusted Platform Module (TPM) is a secure cryptographic processor that is integrated into a computer's motherboard to provide hardware-based security functions. The TPM stores cryptographic keys, certificates, and measurements in tamper-protected storage and performs cryptographic operations in an isolated environment separate from the main CPU, providing a root of trust for the system.

## Key Details

- Provides a hardware root of trust that software alone cannot provide
- **Platform Certification Keys (EK)**: factory-burned, unique identifier for the TPM
- **Storage Root Key (SRK)**: protects all other keys stored in the TPM
- Supports **Measured Boot**: takes cryptographic measurements (hashes) of each boot component and stores them in PCR (Platform Configuration Register) registers
- Used by BitLocker for key sealing: the drive encryption key is sealed to the current boot state; any tampering with boot components breaks the seal and prevents decryption

## Connections

- Parent: [[key-management]] — TPM provides hardware-backed key storage and management
- See also: [[boot-integrity]]
