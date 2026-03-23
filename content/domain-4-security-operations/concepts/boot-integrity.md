---
title: "Boot integrity"
description: "Secure Boot, Measured Boot, and TPM ensure the system hasn't been tampered with at startup"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Boot Integrity?
> When your computer starts up, boot integrity checks that nobody messed with the startup instructions. It is like checking that nobody swapped your cereal box with a look-alike before you pour a bowl.

## Definition

Boot integrity encompasses security mechanisms that verify the integrity of the boot process from firmware through operating system load, ensuring that a system has not been tampered with before handing control to the OS. These controls protect against rootkits and bootkits that attempt to compromise a system before security software loads.

## Key Details

- **Secure Boot**: UEFI feature that only loads bootloaders signed by trusted keys; prevents unsigned OS loading
- **Measured Boot**: records cryptographic measurements of each boot component into TPM; allows remote attestation
- **TPM (Trusted Platform Module)**: hardware chip that stores boot measurements and keys securely
- Protects against rootkits, bootkits, and firmware-level malware
- Remote attestation allows network policies to verify boot integrity before granting access

## Connections

- Parent: [[endpoint-security]] — boot integrity is a critical endpoint security control
- See also: [[trusted-platform-module-tpm]]
