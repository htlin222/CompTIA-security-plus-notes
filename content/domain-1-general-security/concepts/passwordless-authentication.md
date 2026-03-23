---
title: "Passwordless authentication"
description: "FIDO2/WebAuthn, passkeys — eliminates password-related vulnerabilities entirely"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Passwordless Authentication?
> Instead of remembering a password that someone could guess or steal, you log in with your fingerprint, your face, or a special key you carry. There's no password to steal because there is no password at all.

## Definition

Passwordless authentication eliminates the use of shared secrets (passwords) for user authentication, replacing them with cryptographic methods that are phishing-resistant and not vulnerable to credential theft, brute-force, or password reuse attacks. The primary standards are FIDO2 and WebAuthn, which use public-key cryptography with hardware authenticators or device biometrics ("passkeys").

## Key Details

- **FIDO2/WebAuthn**: The authenticator generates a public/private key pair for each service; the private key never leaves the device; authentication proves possession of the private key.
- **Passkeys**: Device-bound or synced FIDO2 credentials—can be backed up across devices via iCloud/Google Password Manager while maintaining phishing resistance.
- Inherently **phishing-resistant**: The credential is bound to the specific website's origin—cannot be used on a lookalike phishing site.
- Eliminates: **password brute-force**, **credential stuffing**, **password spraying**, **password reuse**, **phishing for passwords**.
- Being adopted by major platforms: Windows Hello, Apple Face ID/Touch ID, Google passkeys, hardware security keys (YubiKey).

## Connections

- Parent: [[authentication]] — the future of authentication
- See also: [[certificate-based-authentication]]
