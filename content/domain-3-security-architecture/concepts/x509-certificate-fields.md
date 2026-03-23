---
title: "X.509 certificate fields"
description: "subject, issuer, serial number, validity period, public key, signature algorithm, and extensions"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

X.509 is the ITU-T standard defining the format of public key certificates used in PKI. An X.509 certificate contains structured fields that identify the certificate subject, bind the subject's identity to a public key, specify the certificate's validity period, and include the CA's digital signature authenticating all of these fields. Understanding X.509 fields is essential for interpreting certificates in TLS, S/MIME, code signing, and other PKI applications.

## Key Details

- **Subject**: the entity the certificate identifies (CN, O, OU, C fields; for TLS, the domain name)
- **Issuer**: the CA that signed and issued the certificate
- **Serial number**: unique identifier assigned by the CA; used in CRL and OCSP revocation lookups
- **Validity period**: NotBefore and NotAfter timestamps defining when the certificate is valid
- **Public key**: the subject's public key and algorithm (RSA, ECDSA, etc.)
- **Extensions**: Subject Alternative Names (SANs), Key Usage, Extended Key Usage, CRL Distribution Points, Authority Information Access (OCSP)
- **Signature**: the CA's digital signature over all fields, verifiable with the CA's public key

## Connections

- Parent: [[certificates]] — X.509 certificate fields define the standard structure for all PKI certificates
- See also: [[chain-of-trust]], [[revocation]], [[certificate-formats]], [[digital-signatures]]
