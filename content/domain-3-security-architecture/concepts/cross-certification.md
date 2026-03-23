---
title: "Cross-certification"
description: "two CAs trust each other's certificates for interoperability"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Cross-certification?
> It's like two schools agreeing to accept each other's hall passes. If School A trusts School B's passes, and School B trusts School A's, students from either school can move freely between both buildings.

## Definition

Cross-certification is a PKI trust mechanism in which two separate Certificate Authorities (CAs) issue certificates to each other, establishing bidirectional mutual trust between their respective PKI hierarchies. This allows users in one organization to trust certificates issued by the other organization's CA, enabling interoperability between independently managed PKI systems.

## Key Details

- Both CAs sign each other's certificates, creating a mesh of trust between PKI hierarchies
- Used for inter-organizational federation and trusted communication between separate PKI systems
- Different from a bridge CA, which acts as an intermediary between multiple PKI hierarchies
- Cross-certificates must be revoked if the trust relationship is terminated
- Commonly used between government agencies or business partners that maintain separate PKIs

## Connections

- Parent: [[pki]] — cross-certification is a PKI trust model for inter-organizational interoperability
- Parent: [[federation]] — cross-certification enables certificate-based federation between organizations
- See also: [[chain-of-trust]]
