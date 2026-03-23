---
title: "Digital signatures"
description: "hash the message, then encrypt the hash with the sender's private key"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

A digital signature is a cryptographic mechanism that provides authenticity and integrity for digital data. The process involves the sender hashing the message content and then encrypting the hash value with their private key. The recipient decrypts the encrypted hash with the sender's public key and compares it to a freshly computed hash of the received message — if they match, the message is authentic and unaltered.

## Key Details

- Provides **non-repudiation**: the sender cannot deny signing the message because only their private key could create the signature
- Provides **integrity**: any modification to the message after signing invalidates the signature
- Provides **authentication**: verifies the message came from the owner of the private key
- Does NOT provide confidentiality — the message content is still readable; use encryption for confidentiality
- Common algorithms: RSA, ECDSA, DSA; used in TLS certificates, code signing, email (S/MIME), and software distribution

## Connections

- Parent: [[hashing]] — digital signatures combine hashing with asymmetric cryptography
- See also: [[hmac-hash-based-message-authentication-code]]
