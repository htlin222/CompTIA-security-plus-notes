---
title: "Transitive trust"
description: "If A trusts B and B trusts C, A may transitionally trust C — this can introduce risk"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Transitive Trust?
> If School A trusts School B, and School B trusts School C, then School A automatically trusts School C too. That chain can be useful but also risky if one link is weak.

## Definition

Transitive trust is a property of trust relationships where trust flows through intermediaries: if organization A trusts organization B, and organization B trusts organization C, then organization A may implicitly trust organization C. In federated identity and PKI, transitive trust must be carefully understood and managed because it can unintentionally extend trust to third parties the organization did not directly vet.

## Key Details

- Active Directory domain trusts can be transitive or non-transitive — transitive trusts extend across the trust chain
- In PKI, chain of trust is inherently transitive: root CA trusts intermediate CA, which trusts end-entity certificates
- In SAML federation chains, transitive trust can allow unexpected access if not carefully scoped
- Security risk: compromise of an intermediary in a transitive trust chain can potentially impact all trusting parties
- Organizations should audit trust relationships regularly and minimize transitive trust where possible

## Connections

- Parent: [[federation]] — transitive trust is an important concept in federated identity architectures
- See also: [[trust-relationships]]
