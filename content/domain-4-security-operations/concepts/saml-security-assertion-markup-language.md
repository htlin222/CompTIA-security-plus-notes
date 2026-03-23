---
title: "SAML (Security Assertion Markup Language)"
description: "XML-based standard for exchanging authentication and authorization data between an IdP and SP"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - SAML
---

## Definition

SAML (Security Assertion Markup Language) is an XML-based open standard for exchanging authentication and authorization data between an Identity Provider (IdP) and a Service Provider (SP). In SSO implementations, SAML allows a user authenticated by the IdP to access the SP's resources without re-authenticating, as the SP accepts the SAML assertion from the trusted IdP as proof of the user's identity.

## Key Details

- SAML 2.0 is the current version and the dominant enterprise SSO protocol
- Assertions are XML documents signed by the IdP and passed to the SP via the user's browser
- Relying on XML signatures: the SP validates the IdP's digital signature to trust the assertion
- SAML is stateless from the SP's perspective — each request includes a self-contained assertion
- Common identity providers: ADFS (Windows), Okta, Azure AD/Entra ID, PingFederate

## Connections

- Parent: [[sso]] — SAML is the primary enterprise SSO protocol
- See also: [[identity-provider-idp]]
