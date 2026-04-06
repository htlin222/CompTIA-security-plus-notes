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

> [!eli5] ELI5: What is Multi-Factor Authentication?
> A password is like a house key -- if someone copies it, they can walk right in. Multi-factor authentication adds extra checks, like also needing your fingerprint or a special code sent to your phone. So even if a bad guy steals your password, they still cannot get in because they do not have the other pieces. It is like needing both a key and a secret handshake to open the door.

> [!eli5] ELI5: 多因素驗證 (繁體中文版)
> 多因素驗證就是「雙重保險」。除了密碼 (你知道的東西)，還要用手機簡訊 (你有的東西) 或指紋 (你就是的東西) 才能進門。
>
> ```ascii
> [密碼] + [手機驗證碼] --> [進入系統]
> ```

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
- **[[biometric-types|Biometric types]]**: Retinal scan (blood vessel pattern), iris scan (colored ring pattern), facial recognition, voice recognition, gait analysis (walking pattern), vein/vascular pattern
- **[[far|FAR (False Acceptance Rate)]]**: Probability of incorrectly accepting an unauthorized user (Type II error)
- **[[frr|FRR (False Rejection Rate)]]**: Probability of incorrectly rejecting an authorized user (Type I error)
- **[[cer|CER (Crossover Error Rate)]]**: Point where FAR equals FRR; lower CER indicates more accurate biometric system

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

## Practice Questions

> [!qbank]- Q-Bank: Multi-Factor Authentication (4 Questions)
>
> **Q1.** An organization requires employees to enter a password and a four-digit PIN to access the corporate VPN. A security consultant reviews this setup and identifies a weakness. What is the PRIMARY issue?
>
> A. The PIN should be at least eight digits long
> B. Both factors are "something you know," so this is not true multi-factor authentication
> C. The VPN should use biometric authentication exclusively
> D. Passwords and PINs should never be used together
>
> > [!answer]- Show Answer
> > **B. Both factors are "something you know," so this is not true multi-factor authentication**
> >
> > True MFA requires factors from DIFFERENT categories. A password and a PIN are both [[something-you-know]] factors, making this single-factor authentication with two instances. Option A addresses PIN strength but does not fix the single-factor problem. Option C is impractical for VPN access and eliminates other valid factor types. Option D is incorrect — passwords and PINs can be used together if combined with a factor from a different category.
>
> **Q2.** An employee reports receiving dozens of push notification authentication requests on their phone at 2 AM, even though they are not trying to log in. An attacker has obtained the employee's password and is attempting to gain access. What type of attack is this?
>
> A. SIM swapping
> B. MFA fatigue attack
> C. Credential stuffing
> D. Keylogging
>
> > [!answer]- Show Answer
> > **B. MFA fatigue attack**
> >
> > [[mfa-fatigue-attacks]] involve attackers repeatedly triggering push notifications, hoping the user will accidentally or frustratedly approve one to stop the notifications. Option A involves convincing a carrier to transfer a phone number, not bombarding with push requests. Option C is testing stolen credentials across multiple sites, not targeting push notifications. Option D captures keystrokes, which is how the password was likely obtained initially but is not the current attack.
>
> **Q3.** A bank is evaluating biometric authentication for its high-security vault access. The security team is concerned about unauthorized individuals being falsely accepted. Which metric should they prioritize minimizing?
>
> A. False Rejection Rate (FRR)
> B. Crossover Error Rate (CER)
> C. False Acceptance Rate (FAR)
> D. Token expiration time
>
> > [!answer]- Show Answer
> > **C. False Acceptance Rate (FAR)**
> >
> > For high-security environments, minimizing the [[something-you-are|FAR (False Acceptance Rate)]] is critical because it measures how often unauthorized users are incorrectly granted access. Option A (FRR) measures how often legitimate users are rejected — annoying but not a security breach. Option B (CER) is the balance point between FAR and FRR, not a tuning target for maximum security. Option D relates to token-based authentication, not biometrics.
>
> **Q4.** An organization is deploying FIDO2/WebAuthn security keys to replace passwords for employee authentication. Which category BEST describes this approach?
>
> A. Single-factor biometric authentication
> B. Passwordless authentication using public key cryptography
> C. Knowledge-based authentication
> D. Time-based one-time password authentication
>
> > [!answer]- Show Answer
> > **B. Passwordless authentication using public key cryptography**
> >
> > [[passwordless-authentication|FIDO2/WebAuthn]] uses public key cryptography to eliminate passwords entirely — the private key stays on the device while only the public key is shared with the service. Option A describes biometrics alone, which may be a component but not the full description. Option C describes passwords, PINs, and security questions — the opposite of passwordless. Option D describes [[totp-time-based-one-time-password|TOTP]], which is a different mechanism.

## Scenario

> See [[case-mfa]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [4.6 – Multi-factor Authentication](https://www.youtube.com/watch?v=MpIzA4fNWew)
