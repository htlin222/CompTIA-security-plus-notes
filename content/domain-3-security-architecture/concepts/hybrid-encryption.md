---
title: "Hybrid encryption"
description: "uses asymmetric to exchange a symmetric session key, then symmetric for bulk data (TLS uses this)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Hybrid encryption combines asymmetric and symmetric encryption to leverage the advantages of both: asymmetric encryption's ability to securely exchange keys without prior shared secrets, and symmetric encryption's speed for encrypting large volumes of data. A symmetric session key is generated, encrypted with the recipient's public key (asymmetric), and transmitted; the bulk data is then encrypted with the faster symmetric session key.

## Key Details

- Solves the key distribution problem: no pre-shared secret needed between communicating parties
- Asymmetric encryption (RSA, ECDH) is used only for the short key exchange phase
- Symmetric encryption (AES) handles all bulk data encryption because it's much faster
- TLS uses hybrid encryption: ECDHE or RSA for key exchange, AES for data encryption
- PGP and S/MIME email encryption also use hybrid encryption

## Connections

- Parent: [[encryption]] — hybrid encryption is the dominant practical encryption approach
- See also: [[ephemeral-keys]]
