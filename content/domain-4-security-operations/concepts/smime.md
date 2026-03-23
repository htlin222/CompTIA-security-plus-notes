---
title: "S/MIME"
description: "Certificate-based encryption and digital signing of email content"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

S/MIME (Secure/Multipurpose Internet Mail Extensions) is a standard for public-key encryption and digital signing of email messages using X.509 certificates. It provides end-to-end security for email: the sender digitally signs the message with their private key (proving authenticity and integrity), and can encrypt the message body with the recipient's public key (providing confidentiality).

## Key Details

- **Digital signing**: sender signs with private key; recipient verifies with sender's public key (authenticity + integrity)
- **Encryption**: sender encrypts with recipient's public key; only recipient's private key can decrypt (confidentiality)
- Requires both parties to have X.509 certificates from a mutually trusted CA
- Certificates can be obtained from public CAs or issued by an organization's internal PKI
- S/MIME is widely supported in enterprise email clients (Outlook, Apple Mail) but requires more PKI infrastructure than PGP

## Connections

- Parent: [[email-security]] — S/MIME provides end-to-end email security using PKI
- See also: [[email-encryption]]
