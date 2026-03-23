---
title: "Perfect forward secrecy (PFS)"
description: "compromising long-term keys does not compromise past session keys"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Perfect Forward Secrecy (PFS) is a cryptographic property that ensures the compromise of a long-term private key does not expose the session keys used for past encrypted communications. PFS is achieved by using ephemeral key exchange (DHE or ECDHE) to generate unique, short-lived session keys for each session that are discarded after use and cannot be derived from the long-term key.

## Key Details

- Without PFS: an attacker who records encrypted traffic today and later obtains the server's private key can decrypt all past sessions
- With PFS: even with the private key, past sessions remain protected because session keys were discarded
- Implemented using DHE (Diffie-Hellman Ephemeral) or ECDHE (Elliptic Curve DHE) key exchange
- TLS 1.3 mandates PFS — all TLS 1.3 cipher suites use ECDHE
- Forward secrecy does NOT protect against a compromise where the attacker has the session key itself

## Connections

- Parent: [[key-management]] — PFS is a key management property achieved through ephemeral keys
- See also: [[ephemeral-keys]]
