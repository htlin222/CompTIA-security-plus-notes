---
title: "Tokenization"
description: "replaces sensitive data with non-sensitive tokens; original data stored in a secure vault"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Tokenization is a data protection method that substitutes sensitive data values with algorithmically generated, non-sensitive substitute values called tokens. The original data is stored in a secure, isolated token vault, while applications work with the tokens. Unlike encryption, tokens are not mathematically derived from the original data — there is no algorithm to reverse them without access to the vault.

## Key Details

- The token has no mathematical relationship to the original value — it cannot be reversed without the vault lookup
- Original sensitive data is stored in a separate, highly secured token vault
- Widely used in payment processing: credit card numbers replaced with tokens throughout the payment chain
- Reduces PCI DSS scope: systems using tokens rather than card numbers have significantly reduced compliance burden
- Differs from encryption: encryption is reversible by anyone with the key; tokens require access to the vault

## Connections

- Parent: [[data-protection]] — tokenization is a key data protection technique for sensitive data in systems
- See also: [[data-masking]]
