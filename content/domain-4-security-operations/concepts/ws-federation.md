---
title: "WS-Federation"
description: "web services federation standard for sharing identity across security domains using passive and active profiles"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

WS-Federation (Web Services Federation) is a federation standard that defines mechanisms for sharing identity, authentication, and authorization information across different security domains and organizations. Part of the WS-* web services family, WS-Federation supports both passive (browser-based) and active (application-to-application) federation profiles. It uses security tokens (typically SAML assertions) to convey identity claims between identity providers and service providers, enabling single sign-on across organizational boundaries.

## Key Details

- Part of the broader WS-* standards family alongside WS-Trust and WS-Security
- Passive profile: browser-redirected SSO similar to SAML; used for web application federation
- Active profile: direct token requests from client applications without browser redirection
- Uses SAML tokens to carry identity claims between federation partners
- Common in Microsoft environments: Active Directory Federation Services (AD FS) implements WS-Federation
- Being superseded by OpenID Connect in modern applications, but still prevalent in enterprise Microsoft ecosystems

## Connections

- Parent: [[federation]] — WS-Federation is one of the core standards for cross-organizational identity federation
- See also: [[saml-security-assertion-markup-language]], [[openid-connect-oidc]], [[identity-provider-idp]], [[trust-relationships]]
