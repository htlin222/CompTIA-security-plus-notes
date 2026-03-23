---
title: "Single-factor authentication (SFA)"
description: "Uses one authentication factor; least secure authentication method"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
aliases:
  - SFA
---

> [!eli5] ELI5: What is Single-Factor Authentication (SFA)?
> Using just a password to log in is single-factor authentication. It's like locking your bike with only one lock -- if someone breaks that one lock, there's nothing else stopping them.

## Definition

Single-factor authentication (SFA) relies on only one authentication factor to verify identity—most commonly a password (something you know). Because a single factor can be compromised through phishing, brute force, credential stuffing, or keylogging, SFA is the least secure authentication approach. For sensitive systems and high-risk accounts, SFA alone is considered insufficient by most security standards and frameworks.

## Key Details

- The three authentication factor categories: **Something you know** (password, PIN), **Something you have** (token, smart card), **Something you are** (biometric).
- SFA alone fails when the single factor is compromised—no backup factor prevents unauthorized access.
- **MFA (Multi-Factor Authentication)**: Uses two or more factors; significantly more secure—even compromised passwords become insufficient.
- Still appropriate for **low-risk systems** where the cost of MFA implementation outweighs the risk.
- Security standards like **PCI DSS** and **NIST guidelines** require MFA for privileged access and high-risk transactions.

## Connections

- Parent: [[authentication]] — the baseline authentication approach
- See also: [[biometric-authentication]], [[passwordless-authentication]]
