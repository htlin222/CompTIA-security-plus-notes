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

> [!eli5] ELI5: What is PKI?
> Imagine a post office that hands out special ID badges. Before two people can send each other secret letters, they go to the post office and get an official badge that proves who they are. The post office keeps track of all the badges and can cancel one if it gets stolen. PKI (Public Key Infrastructure) is the whole system -- the post office, the badges, and the rules -- that lets computers prove their identity and communicate securely.

> [!eli5] ELI5: PKI (繁體中文版)
> PKI 就像是發行身分證的一整套系統。它決定了誰能發證、怎麼驗證、以及如果證件弄丟了要怎麼作廢。
>
> ```ascii
> [CA] --(核發)--> [數位證書] --(加密/簽章)--> [通訊]
> ```

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
- **DV (Domain Validation) certificate** — verifies domain ownership only; quickest and cheapest
- **EV (Extended Validation) certificate** — thorough identity verification; displays organization name in browser
- **SAN (Subject Alternative Name)** — certificate field allowing multiple domain names on a single certificate
- **[[certificate-formats|Certificate formats]]** — DER (binary), PEM (Base64-encoded), PKCS#12/PFX (includes private key), PKCS#7 (certificate chain)

## Exam Tips

> [!tip] Remember
> Root CA should be offline. OCSP is real-time; CRL is a list. Chain of trust: root signs intermediate, intermediate signs leaf. If the root is compromised, the entire PKI is compromised. OCSP stapling reduces latency.

## Connections

- Issues and manages [[certificates]] that bind identities to public keys
- Relies on [[encryption]] (asymmetric cryptography) as its underlying technology
- See also [[key-management]] for the lifecycle of the keys within a PKI ecosystem

## Practice Questions

> [!qbank]- Q-Bank: PKI (4 Questions)
>
> **Q1.** A security architect is designing a PKI and wants to protect the root CA from compromise. Which practice is MOST critical?
>
> A. Keep the root CA online for real-time certificate issuance
> B. Take the root CA offline and use intermediate CAs for day-to-day issuance
> C. Use a self-signed certificate for the root CA and share its private key with all administrators
> D. Deploy the root CA on a cloud-hosted virtual machine for redundancy
>
> > [!answer]- Show Answer
> > **B. Take the root CA offline and use intermediate CAs for day-to-day issuance**
> >
> > The [[pki|root CA]] should be kept offline to minimize its exposure to attacks. Intermediate CAs handle daily certificate issuance; if compromised, only their branch of the hierarchy is affected. Keeping the root CA online (A) unnecessarily exposes the most critical component. Sharing the root private key (C) violates fundamental key security principles. Deploying on a cloud VM (D) increases the attack surface for the most sensitive PKI component.
>
> **Q2.** A user's browser displays a certificate warning when visiting a website. The browser reports that the certificate has been revoked. Which PKI mechanism MOST likely provided this real-time revocation status?
>
> A. Certificate Revocation List (CRL)
> B. Online Certificate Status Protocol (OCSP)
> C. Certificate Signing Request (CSR)
> D. Key escrow
>
> > [!answer]- Show Answer
> > **B. Online Certificate Status Protocol (OCSP)**
> >
> > [[pki|OCSP]] provides real-time certificate validity checking, which is more efficient and current than CRL. CRL (A) is a periodically published list rather than a real-time check. A CSR (C) is used to request a certificate, not to check revocation status. Key escrow (D) relates to key recovery by a third party, not certificate revocation.
>
> **Q3.** A browser trusts a website's certificate because the certificate was signed by an intermediate CA, which was signed by a root CA that the browser already trusts. Which PKI concept does this demonstrate?
>
> A. Certificate pinning
> B. Cross-certification
> C. Chain of trust
> D. OCSP stapling
>
> > [!answer]- Show Answer
> > **C. Chain of trust**
> >
> > The [[chain-of-trust|chain of trust]] is the hierarchy where each certificate is signed by the CA above it — the leaf certificate is signed by an intermediate CA, which is signed by the root CA that the browser trusts. Certificate pinning (A) hardcodes expected certificates to prevent MITM. Cross-certification (B) enables two separate CAs to trust each other. OCSP stapling (D) is a method for servers to provide revocation status during the TLS handshake.
>
> **Q4.** An organization wants to reduce the latency of certificate revocation checks during TLS handshakes. The web server should periodically retrieve its own revocation status and present it to clients. Which technique achieves this?
>
> A. Downloading the full CRL to each client browser
> B. OCSP stapling
> C. Certificate pinning
> D. Cross-certification between CAs
>
> > [!answer]- Show Answer
> > **B. OCSP stapling**
> >
> > [[pki|OCSP stapling]] allows the web server to periodically check its own certificate status and include (staple) the OCSP response in the TLS handshake, reducing client-side latency. Downloading full CRLs (A) is bandwidth-intensive and adds latency. Certificate pinning (C) restricts which certificates are accepted but does not address revocation check latency. Cross-certification (D) enables inter-CA trust but is unrelated to revocation performance.

## Scenario

> See [[case-pki]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [1.4 – Public Key Infrastructure](https://www.youtube.com/watch?v=xHAMEF7-inQ)
