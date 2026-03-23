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

## Scenario

> See [[case-sso]] for a practical DevOps scenario applying these concepts.
