---
title: "Non-repudiation"
description: "Ensures actions cannot be denied after the fact; achieved through digital signatures and audit trails"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Non-Repudiation?
> It's like signing a receipt when you buy something. Later, you can't say "I never bought that!" because your signature proves you did. Non-repudiation means people can't deny what they did on a computer.

## Definition

Non-repudiation is the security property that ensures a party cannot deny having performed an action after the fact. It is the fourth pillar of information security (beyond CIA), critical for legal accountability, digital forensics, and trust in digital transactions. Non-repudiation is achieved through mechanisms that create unforgeable, auditable proof of actions—most importantly digital signatures, comprehensive logging, and timestamping.

## Key Details

- **Digital signatures**: Use the signer's private key to create a signature that only they could have produced—proof of origin and non-repudiation.
- **Logging**: Timestamped records of user actions; logs must be protected from modification to maintain evidentiary value.
- **Certificates**: Bind a digital signature to a verified identity through the PKI chain of trust.
- Critical in: **e-commerce** (proving a purchase was made), **email** (proving who sent a message), **contracts** (proving agreement was accepted).
- Relates to **accountability** in AAA: accounting logs provide non-repudiation evidence.

## Connections

- Parent: [[cia-triad]] — often considered the fourth pillar alongside CIA
- See also: [[accounting]]
