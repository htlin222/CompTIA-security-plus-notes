---
title: "Full disk encryption (FDE)"
description: "Encrypts the entire drive to protect data at rest (e.g., BitLocker, FileVault)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - FDE
---

## Definition

Full Disk Encryption (FDE) is a security control that encrypts all data stored on a device's storage media, including the operating system, applications, and user data. FDE ensures that if a device is lost, stolen, or physically accessed without authorization, the data remains unreadable without the correct authentication credentials or encryption key.

## Key Details

- **BitLocker** (Windows): TPM-integrated FDE; can require PIN, USB key, or TPM-only authentication
- **FileVault** (macOS): AES-XTS encryption of the startup disk
- **LUKS/dm-crypt** (Linux): standard Linux FDE implementation
- TPM integration allows BitLocker to verify boot integrity and release the key automatically if no tampering detected
- FDE protects against offline attacks — an attacker with physical access cannot read data without the key

## Connections

- Parent: [[endpoint-security]] — FDE is a critical data-at-rest protection control for endpoints
- See also: [[boot-integrity]]
