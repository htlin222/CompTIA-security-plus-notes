---
title: "Chain of trust"
description: "each certificate is signed by the CA above it; browsers trust the root CA"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is the Chain of trust?
> Think of it like a recommendation chain: your teacher trusts the principal, and the principal trusts the school board. If the school board says "this person is a real teacher," everyone down the chain believes it. Certificates work the same way -- trust flows from the top down.

## Definition

The chain of trust (also called the certificate chain) is the hierarchical sequence of certificates from an end-entity certificate up through intermediate CAs to a root CA that is trusted by the relying party. Each certificate in the chain is digitally signed by the issuing CA above it, allowing the relying party to verify the complete trust path by tracing back to a trusted root.

## Key Details

- Trust anchors are root CA certificates stored in the OS or browser trust store
- Intermediate CAs sit between root CAs and end-entity certificates; they can be revoked without revoking the root
- Browsers verify the complete chain from server certificate → intermediate → root
- A missing intermediate certificate breaks TLS handshakes even if all certificates are valid
- Cross-certification allows two separate PKI hierarchies to establish mutual trust

## Connections

- Parent: [[pki]] — chain of trust is the core mechanism of PKI authentication
- See also: [[certificate-pinning]]
