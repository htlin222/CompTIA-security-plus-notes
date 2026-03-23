---
title: "Revocation"
description: "CRL or OCSP; reasons include key compromise, CA compromise, or affiliation change"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Certificate revocation is the process of permanently invalidating a digital certificate before its scheduled expiration date. When a certificate must be invalidated — due to key compromise, CA compromise, change in the certificate holder's affiliation, or other reasons — the CA publishes revocation information so that relying parties can verify whether a certificate is still valid.

## Key Details

- **CRL (Certificate Revocation List)**: periodically published list of revoked certificate serial numbers; can be large and stale
- **OCSP (Online Certificate Status Protocol)**: real-time query to check a specific certificate's status; more timely than CRL
- **OCSP Stapling**: server includes a pre-fetched, CA-signed OCSP response in the TLS handshake; improves performance
- Reasons for revocation: keyCompromise, cACompromise, affiliationChanged, superseded, cessationOfOperation
- Checking revocation status is critical — using a revoked certificate bypasses the purpose of PKI

## Connections

- Parent: [[certificates]] — revocation is a critical part of the certificate lifecycle
- See also: [[certificate-lifecycle]]
