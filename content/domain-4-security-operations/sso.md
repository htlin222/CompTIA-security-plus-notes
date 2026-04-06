---
title: "Single Sign-On"
description: "Authentication mechanism allowing users to access multiple systems with one set of credentials"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/identity
  - weight/high
aliases:
  - "SSO"
  - "Single Sign-On"
---

> [!eli5] ELI5: What is Single Sign-On?
> Remember how annoying it would be if you had to show your ID at every single classroom door in school? Single sign-on is like showing your ID once at the front entrance and then being allowed into every room for the rest of the day. You log in one time, and all your apps and websites recognize you without asking for your password again. It saves time and means you only need to remember one password.

## Overview

Single Sign-On (SSO) allows users to authenticate once and gain access to multiple independent applications or systems without re-entering credentials. SSO improves user experience and reduces password fatigue while centralizing authentication control. It is a key component of modern identity and access management strategies.

## Key Concepts

- **[[saml-security-assertion-markup-language|SAML (Security Assertion Markup Language)]]**: XML-based standard for exchanging authentication and authorization data between an identity provider (IdP) and a service provider (SP)
- **[[oauth-20|OAuth 2.0]]**: Authorization framework that grants third-party applications limited access to resources without sharing credentials
- **[[openid-connect-oidc|OpenID Connect (OIDC)]]**: Authentication layer built on top of OAuth 2.0, commonly used for consumer-facing SSO
- **[[kerberos|Kerberos]]**: Ticket-based authentication protocol used in Active Directory environments; uses a Key Distribution Center (KDC)
- **[[identity-provider-idp|Identity Provider (IdP)]]**: The trusted authority that authenticates users and issues tokens or assertions
- **[[service-provider-sp|Service Provider (SP)]]**: The application or resource that relies on the IdP for authentication
- **[[token-based-authentication|Token-based authentication]]**: SSO systems issue tokens (JWT, SAML assertions) that prove identity to relying parties
- **[[single-point-of-failure-risk|Single point of failure risk]]**: If SSO is compromised, all linked applications are at risk

## Exam Tips

> [!tip] Remember
> SAML = enterprise/web SSO (XML-based), OAuth = authorization (not authentication), OIDC = authentication on top of OAuth. Kerberos = on-premises AD environments using tickets and a KDC.

- SSO reduces the attack surface for password-based attacks but creates a high-value target
- Know the difference between SSO (one login, many apps) and federated identity (across organizations)
- LDAP is a directory protocol, not an SSO protocol — but it supports SSO implementations

## Connections

- Core component of [[identity-management]] for streamlining user access
- Should always be paired with [[mfa]] to mitigate the risk of credential compromise
- Extends across organizations through [[federation]] using protocols like SAML
- Reduces exposure to [[password-attacks]] by minimizing the number of credentials users manage

## Practice Questions

> [!qbank]- Q-Bank: Single Sign-On (4 Questions)
>
> **Q1.** An organization implements SSO so employees can access email, CRM, and HR systems with a single login. A security architect raises a concern about this configuration. What is the PRIMARY security risk of SSO?
>
> A. SSO increases the number of passwords users must remember
> B. If the SSO credentials are compromised, an attacker gains access to all linked applications
> C. SSO prevents the use of multi-factor authentication
> D. SSO requires each application to maintain its own user database
>
> > [!answer]- Show Answer
> > **B. If the SSO credentials are compromised, an attacker gains access to all linked applications**
> >
> > [[single-point-of-failure-risk]] is the primary security concern with SSO — a single compromised credential unlocks all connected applications. This is why SSO should always be paired with [[mfa]]. Option A is the opposite — SSO reduces passwords. Option C is incorrect — SSO works well with MFA. Option D is incorrect — SSO centralizes authentication, eliminating separate user databases.
>
> **Q2.** A company uses Active Directory on-premises and wants to implement SSO for internal applications. Users authenticate at their Windows workstation and receive access to internal web apps and file shares without re-entering credentials. Which protocol is MOST likely handling this authentication?
>
> A. SAML
> B. OAuth 2.0
> C. Kerberos
> D. RADIUS
>
> > [!answer]- Show Answer
> > **C. Kerberos**
> >
> > [[kerberos]] is the ticket-based authentication protocol used in Active Directory environments for on-premises SSO. The Key Distribution Center (KDC) issues tickets that grant access to domain resources. Option A is used for web-based enterprise federation, not on-premises AD environments. Option B is an authorization framework, not an authentication protocol. Option D is used for network access authentication (VPN, Wi-Fi), not domain SSO.
>
> **Q3.** A web application allows users to log in using their Google account. When the user clicks "Sign in with Google," they are redirected to Google to authenticate, then returned to the application with a token. Which protocol combination is MOST likely in use?
>
> A. Kerberos and LDAP
> B. OpenID Connect (built on OAuth 2.0)
> C. NTLM and Active Directory
> D. RADIUS and TACACS+
>
> > [!answer]- Show Answer
> > **B. OpenID Connect (built on OAuth 2.0)**
> >
> > [[openid-connect-oidc|OpenID Connect (OIDC)]] is the authentication layer built on [[oauth-20|OAuth 2.0]] commonly used for consumer-facing SSO and "Sign in with..." functionality. It returns identity information via JSON Web Tokens. Option A is for on-premises Windows domain environments. Option C is a legacy Windows authentication protocol. Option D handles network device authentication, not web application SSO.
>
> **Q4.** An enterprise uses SAML-based SSO for its cloud applications. The identity provider (IdP) authenticates users and sends SAML assertions to service providers (SPs). What does the SAML assertion contain?
>
> A. The user's plaintext password for the service provider to verify
> B. Authentication and authorization data about the user in XML format
> C. A copy of the user's biometric template
> D. The service provider's private encryption key
>
> > [!answer]- Show Answer
> > **B. Authentication and authorization data about the user in XML format**
> >
> > [[saml-security-assertion-markup-language|SAML]] assertions are XML-based documents exchanged between the [[identity-provider-idp|IdP]] and [[service-provider-sp|SP]] containing authentication status, user attributes, and authorization decisions. Passwords are never sent to the SP. Option A violates SSO principles — the SP never receives the user's password. Option C is biometric data, not part of SAML assertions. Option D would be a critical security violation — private keys are never shared.

## Scenario

> See [[case-sso]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [4.6 – Identity and Access Management](https://www.youtube.com/watch?v=ZoOyyqhptik)
