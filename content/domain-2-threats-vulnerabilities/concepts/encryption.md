---
title: "Encryption"
description: "Protecting data at rest and in transit to ensure confidentiality even if intercepted"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Encryption is a fundamental security control that transforms plaintext data into an unreadable ciphertext using cryptographic algorithms, ensuring that only parties with the correct key can access the original data. As a mitigation technique, encryption protects data confidentiality both when stored (data at rest) and when transmitted across networks (data in transit), rendering intercepted or stolen data useless to attackers without the decryption key.

## Key Details

- **Data at rest**: Full disk encryption (BitLocker, FileVault), database encryption (TDE), file-level encryption (EFS, VeraCrypt).
- **Data in transit**: TLS for web traffic, SSH for remote access, S/MIME or PGP for email, SFTP/FTPS for file transfers.
- **Symmetric encryption** (AES): Same key for encryption/decryption—fast, used for bulk data.
- **Asymmetric encryption** (RSA, ECC): Public/private key pair—used for key exchange and digital signatures.
- Encryption does not protect availability or integrity on its own—must be combined with other controls.

## Connections

- Parent: [[mitigation-techniques]] — encryption as a primary mitigation for data exposure
- See also: [[confidentiality]]
