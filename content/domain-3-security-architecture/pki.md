---
title: "PKI"
description: "Public Key Infrastructure provides the framework of policies, hardware, and software for managing digital certificates and public-key encryption."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cryptography
  - weight/high
aliases:
  - "PKI"
---

## Overview

Public Key Infrastructure (PKI) is a comprehensive system for creating, distributing, managing, storing, and revoking digital certificates. PKI binds public keys to identities through a trusted Certificate Authority (CA), enabling secure communications, authentication, and digital signatures. PKI underpins HTTPS, email encryption, code signing, VPNs, and many other security services.

## Key Concepts

- **PKI components:**
  - **Certificate Authority (CA)** — trusted entity that issues and signs certificates
  - **Registration Authority (RA)** — verifies the identity of certificate requestors before the CA issues
  - **Certificate Revocation List (CRL)** — list of revoked certificates published by the CA
  - **Online Certificate Status Protocol (OCSP)** — real-time certificate validity checking; more efficient than CRL
  - **OCSP stapling** — server periodically checks its own certificate status and includes it in the TLS handshake
- **Certificate hierarchy:**
  - **Root CA** — top of the trust chain; self-signed; kept offline for security
  - **Intermediate / subordinate CA** — issues certificates on behalf of the root CA; if compromised, only its branch is affected
  - **Leaf certificate** — end-entity certificate issued to a server, user, or device
- **[[chain-of-trust|Chain of trust]]** — each certificate is signed by the CA above it; browsers trust the root CA
- **[[certificate-pinning|Certificate pinning]]** — application hardcodes the expected certificate or public key to prevent MITM with rogue certs
- **[[key-escrow|Key escrow]]** — a third party holds a copy of the private key for recovery purposes
- **[[cross-certification|Cross-certification]]** — two CAs trust each other's certificates for interoperability

## Exam Tips

> [!tip] Remember
> Root CA should be offline. OCSP is real-time; CRL is a list. Chain of trust: root signs intermediate, intermediate signs leaf. If the root is compromised, the entire PKI is compromised. OCSP stapling reduces latency.

## Connections

- Issues and manages [[certificates]] that bind identities to public keys
- Relies on [[encryption]] (asymmetric cryptography) as its underlying technology
- See also [[key-management]] for the lifecycle of the keys within a PKI ecosystem

## Scenario

> See [[case-pki]] for a practical DevOps scenario applying these concepts.
