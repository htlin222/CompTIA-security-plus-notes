---
title: "Email encryption"
description: "Protects email content in transit and at rest; can be gateway-based or end-to-end"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Email Encryption?
> Email encryption scrambles your message so only the person you sent it to can read it. It is like writing a letter in a secret code that only your friend knows how to decode.

## Definition

Email encryption protects the confidentiality of email message content from unauthorized access. It can be applied at the transport level (TLS encrypts the connection between mail servers), gateway level (the mail gateway encrypts/decrypts on behalf of users), or end-to-end (only the sender and recipient can read the message using S/MIME or PGP).

## Key Details

- **TLS (opportunistic or enforced)**: encrypts the SMTP connection between mail servers; does not protect against compromised mail servers
- **Gateway-based encryption**: email security gateway handles encryption; transparent to users but vulnerable to gateway compromise
- **S/MIME**: certificate-based end-to-end encryption; requires both parties to have certificates
- **PGP (Pretty Good Privacy)**: web-of-trust-based end-to-end encryption; common in technical communities
- End-to-end encryption is the strongest but requires key management overhead

## Connections

- Parent: [[email-security]] — email encryption is a core email security control for confidentiality
- See also: [[smime]]
