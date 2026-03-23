---
title: "HMAC (Hash-based Message Authentication Code)"
description: "combines a hash with a secret key to provide integrity AND authentication"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
aliases:
  - HMAC
---

## Definition

HMAC (Hash-based Message Authentication Code) is a cryptographic mechanism that combines a hash function with a shared secret key to produce a message authentication code. It provides both data integrity (the message has not been altered) and authentication (the message came from someone with knowledge of the secret key). Unlike simple hashing, HMAC cannot be forged without knowing the secret key.

## Key Details

- Combines the message with a secret key using a defined algorithm (HMAC-SHA256 is common)
- Provides integrity + authentication but NOT non-repudiation (both parties know the key)
- Used in IPsec, TLS 1.2 MAC verification, API authentication, and JWT signing (HS256)
- Differs from digital signatures: HMAC uses a shared symmetric key; digital signatures use asymmetric keys
- TOTP (authenticator apps) uses HMAC internally to generate time-based codes

## Connections

- Parent: [[hashing]] — HMAC extends basic hashing with authentication using a shared key
- See also: [[digital-signatures]]
