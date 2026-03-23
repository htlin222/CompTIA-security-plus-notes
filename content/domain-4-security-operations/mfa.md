---
title: "Multi-Factor Authentication"
description: "Authentication requiring two or more distinct factors to verify user identity"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/identity
  - weight/high
aliases:
  - "MFA"
  - "Multi-Factor Authentication"
---

## Overview

Multi-Factor Authentication (MFA) requires users to present two or more verification factors from different categories to gain access. MFA significantly reduces the risk of unauthorized access even when one factor (such as a password) is compromised. It is one of the most frequently tested topics on the Security+ exam.

## Key Concepts

- **[[something-you-know|Something you know]]**: Passwords, PINs, security questions
- **[[something-you-have|Something you have]]**: Smart cards, hardware tokens (YubiKey), mobile authenticator apps, OTP devices
- **[[something-you-are|Something you are]]**: Biometrics — fingerprint, facial recognition, iris scan, voice recognition
- **[[something-you-do|Something you do]]**: Behavioral biometrics such as typing patterns or gait analysis (less common on exam)
- **[[somewhere-you-are|Somewhere you are]]**: Geolocation or IP-based restrictions (sometimes considered a factor)
- **[[totp-time-based-one-time-password|TOTP (Time-based One-Time Password)]]**: Algorithm that generates codes valid for a short time window (e.g., Google Authenticator)
- **[[hotp-hmac-based-one-time-password|HOTP (HMAC-based One-Time Password)]]**: Counter-based OTP that remains valid until used
- **[[push-notifications|Push notifications]]**: Authentication apps send approve/deny prompts to registered devices
- **[[passwordless-authentication|Passwordless authentication]]**: FIDO2/WebAuthn uses public key cryptography to eliminate passwords entirely
- **[[mfa-fatigue-attacks|MFA fatigue attacks]]**: Attackers bombard users with push notifications hoping they approve one

## Exam Tips

> [!tip] Remember
> Two passwords = NOT MFA (same factor category). MFA requires factors from DIFFERENT categories. A password + PIN = single factor (both "something you know"). A password + fingerprint = true MFA.

- Know the difference between MFA and two-factor authentication (2FA is a subset of MFA)
- Biometric errors: FAR (False Acceptance Rate) vs. FRR (False Rejection Rate) — CER (Crossover Error Rate) is the balance point
- SMS-based OTP is considered weaker due to SIM swapping and SS7 vulnerabilities

## Connections

- Strengthens [[identity-management]] by adding layers beyond password-only authentication
- Essential component of [[sso]] to protect the single point of authentication
- Mitigates [[password-attacks]] — even if credentials are stolen, a second factor is needed
- Key control in [[privileged-access-management]] for protecting high-risk accounts

## Scenario

> See [[case-mfa]] for a practical DevOps scenario applying these concepts.
