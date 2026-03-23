---
title: "OpenID Connect (OIDC)"
description: "Authentication layer built on top of OAuth 2.0, commonly used for consumer-facing SSO"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - OIDC
---

## Definition

OpenID Connect (OIDC) is an authentication protocol and identity layer built on top of OAuth 2.0 that enables applications to verify user identity and obtain basic profile information. As an SSO protocol, OIDC allows users to authenticate with an identity provider (like Google or Microsoft) and use those credentials to access multiple service provider applications without re-authenticating.

## Key Details

- OIDC adds authentication to OAuth 2.0 which handles only authorization
- The ID Token (JWT) contains user identity claims; the Access Token is used for API access
- Key endpoints: Authorization, Token, UserInfo, Discovery (OpenID Configuration)
- Widely used in B2C/consumer SSO: "Sign in with Google," "Sign in with Apple"
- PKCE (Proof Key for Code Exchange) extension should be used for public clients to prevent authorization code interception

## Connections

- Parent: [[sso]] — OIDC is a primary modern SSO protocol for web and mobile applications
- See also: [[identity-provider-idp]]
