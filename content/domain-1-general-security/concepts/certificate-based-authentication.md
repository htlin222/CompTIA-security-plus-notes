---
title: "Certificate-based authentication"
description: "Uses digital certificates from a PKI for mutual authentication"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Certificate-based authentication uses X.509 digital certificates issued by a trusted Certificate Authority (CA) within a Public Key Infrastructure (PKI) to verify identity. The authenticating party presents their certificate, and the relying party validates it against the CA's trust chain. This can be used for mutual authentication (both sides verify each other), such as in smart card logon, TLS client certificates, or VPN authentication.

## Key Details

- Certificates contain the subject's **public key**, identity information, validity period, and the CA's digital signature.
- **Mutual TLS (mTLS)**: Both client and server present certificates—provides strong two-way authentication.
- Smart card logon (CAC/PIV cards) in government environments uses certificate-based authentication.
- Certificates must be validated for: **revocation status** (CRL or OCSP), **expiration**, and **chain of trust**.
- Certificate-based auth eliminates password-related attacks (brute force, spraying, stuffing) entirely.

## Connections

- Parent: [[authentication]] — a strong authentication method using PKI
- See also: [[passwordless-authentication]]
