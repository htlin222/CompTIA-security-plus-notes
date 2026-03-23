---
title: "Authentication"
description: "Methods and mechanisms for verifying the identity of users, devices, and services"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/identity
  - weight/high
aliases:
  - "AuthN"
---

## Overview

Authentication is the process of verifying that an entity (user, device, or service) is who or what it claims to be. It is the first step in the AAA framework and serves as the gatekeeper for all subsequent authorization decisions. Strong authentication is critical to preventing unauthorized access and is a recurring theme across all five Security+ exam domains.

## Key Concepts

- **Authentication factors**:
  - **Something you know** — passwords, PINs, security questions
  - **Something you have** — smart cards, hardware tokens, mobile devices
  - **Something you are** — fingerprints, retinal scans, facial recognition
  - **Somewhere you are** — geolocation, IP-based restrictions
  - **Something you do** — behavioral biometrics, typing patterns
- **[[single-factor-authentication-sfa|Single-factor authentication (SFA)]]** — uses one factor; least secure
- **Multi-factor authentication (MFA)** — uses two or more _different_ factor types (see [[mfa]])
- **Password-based authentication** — most common but most vulnerable to [[password-attacks]]
- **[[certificate-based-authentication|Certificate-based authentication]]** — uses digital certificates from a PKI for mutual authentication
- **[[biometric-authentication|Biometric authentication]]** — FAR (False Acceptance Rate) vs. FRR (False Rejection Rate); CER (Crossover Error Rate) measures accuracy
- **[[passwordless-authentication|Passwordless authentication]]** — FIDO2/WebAuthn, passkeys; eliminates password-related vulnerabilities
- **[[directory-services|Directory services]]** — LDAP, Active Directory; centralized authentication stores
- **Single sign-on (SSO)** — authenticate once, access multiple systems (see [[sso]])
- **Federation** — extends authentication across organizational boundaries (see [[federation]])

## Exam Tips

> [!tip] Remember
> Two passwords is NOT multi-factor — it is two instances of the same factor (something you know). True MFA requires factors from _different categories_.

> [!tip] Biometric Rates
> **FAR** = unauthorized person accepted (security concern). **FRR** = authorized person rejected (usability concern). **CER** = where FAR and FRR meet — lower CER means better biometric system.

## Connections

- First component of the [[aaa-framework]] that gates all access decisions
- Strengthened significantly by [[mfa]] which combines multiple factor types
- Vulnerable to [[password-attacks]] and [[social-engineering]] which target credentials
- Enables [[sso]] for streamlined user access across multiple applications
- Central to [[zero-trust]] architectures which require continuous authentication verification

## Scenario

> See [[case-authentication]] for a practical DevOps scenario applying these concepts.
