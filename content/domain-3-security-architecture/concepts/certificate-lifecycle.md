---
title: "Certificate lifecycle"
description: "request (CSR), issuance, usage, renewal, revocation"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

The certificate lifecycle describes the complete sequence of stages a digital certificate goes through from initial request to final revocation or expiration. Managing certificates across their entire lifecycle is a critical PKI administration function, as improperly managed certificates can create security vulnerabilities (expired certificates causing service outages) or weaken trust (unrevoked compromised certificates).

## Key Details

- **Request**: entity generates a key pair and submits a Certificate Signing Request (CSR) to the CA
- **Issuance**: CA verifies identity and signs the certificate, binding the public key to the identity
- **Usage**: certificate is deployed and used for its intended purpose (TLS, code signing, etc.)
- **Renewal**: certificates must be renewed before expiration; typically automated in modern PKI
- **Revocation**: invalidated before expiry via CRL or OCSP when compromised or no longer needed

## Connections

- Parent: [[certificates]] — the lifecycle defines how certificates are managed over time
- See also: [[revocation]]
