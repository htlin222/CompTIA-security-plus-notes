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

> [!eli5] ELI5: What is Authentication?
> It's like when your school asks you to show your student ID before letting you into the building. They need to prove you are who you say you are. You might show your face, type a password, scan your fingerprint, or tap a special card. Sometimes you need more than one of these -- like both a password and a fingerprint -- to make it really hard for someone to pretend to be you.

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

## Practice Questions

> [!qbank]- Q-Bank: Authentication (4 Questions)
>
> **Q1.** A company requires employees to enter a password and then approve a push notification on their registered mobile device before accessing the corporate VPN. Which authentication approach does this BEST represent?
>
> A. Two-step verification using the same factor
> B. Multi-factor authentication using two different factors
> C. Single-factor authentication with two credentials
> D. Certificate-based authentication
>
> > [!answer]- Show Answer
> > **B. Multi-factor authentication using two different factors**
> >
> > This combines something you know (password) with something you have (registered mobile device receiving the push notification), which are two different [[authentication]] factor categories — the definition of [[mfa|MFA]]. Two-step verification using the same factor would be two passwords or two PINs, both "something you know." Single-factor authentication uses only one factor type regardless of the number of credentials. Certificate-based authentication uses digital certificates from a PKI, which is not described here.
>
> **Q2.** A biometric access system at a secure facility is rejecting authorized employees at an unacceptably high rate, causing long entry delays. Which metric BEST describes this problem?
>
> A. False Acceptance Rate (FAR)
> B. False Rejection Rate (FRR)
> C. Crossover Error Rate (CER)
> D. Equal Error Rate (EER)
>
> > [!answer]- Show Answer
> > **B. False Rejection Rate (FRR)**
> >
> > [[biometric-authentication|FRR]] measures how often a biometric system incorrectly rejects authorized users — a usability concern that causes the delays described. FAR measures how often unauthorized users are incorrectly accepted, which is a security concern rather than a usability concern. CER (also called EER/Equal Error Rate) is the point where FAR and FRR are equal and measures overall biometric system accuracy, not a specific operational problem. EER is another name for CER and describes the same crossover metric.
>
> **Q3.** An organization wants to eliminate password-related vulnerabilities entirely. They plan to deploy hardware security keys that support the FIDO2 standard for all employee logins. Which authentication category does this BEST fall under?
>
> A. Single-factor authentication
> B. Certificate-based authentication
> C. Passwordless authentication
> D. Knowledge-based authentication
>
> > [!answer]- Show Answer
> > **C. Passwordless authentication**
> >
> > FIDO2/WebAuthn with hardware security keys is a [[passwordless-authentication|passwordless authentication]] method that eliminates password-related vulnerabilities by using cryptographic key pairs. While FIDO2 does use certificates/key pairs internally, the primary classification for this approach is passwordless authentication, which is the broader security initiative described. Single-factor authentication could apply if only the key is used, but the question focuses on the passwordless category. Knowledge-based authentication involves passwords and security questions — the opposite of what is being implemented.
>
> **Q4.** A security architect is designing an authentication system that allows employees to log in once and access email, the HR portal, and the project management tool without re-entering credentials. Which technology BEST achieves this goal?
>
> A. Multi-factor authentication
> B. Single sign-on (SSO)
> C. Federation
> D. RADIUS
>
> > [!answer]- Show Answer
> > **B. Single sign-on (SSO)**
> >
> > [[sso|SSO]] allows users to authenticate once and gain access to multiple systems and applications without re-entering credentials — exactly the scenario described. MFA strengthens the authentication process but does not inherently provide access to multiple applications with a single login. [[federation|Federation]] extends authentication across organizational boundaries, which is not described since all systems are internal. RADIUS is a network access protocol for Wi-Fi/VPN authentication, not a single sign-on solution for web applications.

## Scenario

> See [[case-authentication]] for a practical DevOps scenario applying these concepts.
