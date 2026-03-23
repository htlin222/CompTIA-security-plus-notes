---
title: "Something you know"
description: "Passwords, PINs, security questions"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is "Something You Know"?
> This is information only you should know, like a password or a PIN. It is the most common type of proof, but it is also the easiest one for a bad guy to steal or guess.

## Definition

"Something you know" is one of the three primary MFA authentication factors, referring to knowledge-based secrets that only the legitimate user should know. This includes passwords, PINs, and security questions. It is the most common authentication factor but also the most frequently compromised — phishing, credential stuffing, and brute force attacks all target this factor.

## Key Details

- **Passwords**: most common authentication mechanism; should be long, complex, and unique per site
- **PINs**: shorter numeric or alphanumeric codes; common for local device authentication (paired with biometrics or smart card)
- **Security questions**: weak factor — answers are often guessable or findable through social media; should be avoided or treated as backup codes
- Passwords alone (single-factor) are insufficient for sensitive systems — always combine with another factor
- Password managers help users maintain unique, strong passwords across many sites

## Connections

- Parent: [[mfa]] — knowledge factors are the most widely deployed but least secure MFA component
- See also: [[something-you-have]]
