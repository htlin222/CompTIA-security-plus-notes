---
title: "Something you have"
description: "Smart cards, hardware tokens (YubiKey), mobile authenticator apps, OTP devices"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

"Something you have" is one of the three primary MFA factors referring to a physical or digital possession that proves identity. This includes hardware devices, smart cards, and software tokens on registered devices. This factor assumes that an attacker cannot authenticate without physical possession of the device, even if they know the user's password.

## Key Details

- **Hardware tokens**: physical devices (RSA SecurID, YubiKey) that generate OTPs or perform challenge-response
- **Smart cards**: contain embedded certificates used for authentication; require PIN to activate (two-factor in one card)
- **Mobile authenticator apps**: software on a registered phone that generates TOTP codes (Google Authenticator, Microsoft Authenticator)
- **FIDO2/WebAuthn hardware keys** (YubiKey): phishing-resistant; cryptographic proof of possession
- FIDO2 keys are the strongest "something you have" factor because they are phishing-resistant and bound to specific sites

## Connections

- Parent: [[mfa]] — physical possession factors are a key component of MFA implementations
- See also: [[totp-time-based-one-time-password]]
