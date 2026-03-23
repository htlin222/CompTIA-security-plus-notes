---
title: "Certificate formats"
description: "PEM (.pem, .crt), DER (.der), PKCS#12 (.pfx, .p12), PKCS#7 (.p7b)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Digital certificates are encoded in several standard formats depending on the use case and platform requirements. Understanding certificate formats is important for importing, exporting, and deploying certificates correctly across different systems and applications. The format determines the encoding and what data is contained in the file.

## Key Details

- **PEM** (.pem, .crt, .cer, .key): Base64-encoded text format; most common on Linux/Apache; can contain certificates and/or private keys
- **DER** (.der, .cer): Binary encoding of the same ASN.1 structure as PEM; common on Windows and Java
- **PKCS#12** (.pfx, .p12): Binary format that bundles the certificate AND private key together in one file; protected by a password; common on Windows
- **PKCS#7** (.p7b, .p7c): Contains certificates and certificate chains but NOT private keys; used for certificate distribution
- Conversion between formats uses tools like OpenSSL

## Connections

- Parent: [[certificates]] — understanding certificate formats is required for certificate management
- See also: [[certificate-lifecycle]]
