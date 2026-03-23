---
title: "OpenID Connect"
description: "Modern federation protocol built on OAuth 2.0; uses JSON Web Tokens (JWT)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

OpenID Connect (OIDC) is a modern identity federation and authentication protocol that adds an identity layer on top of the OAuth 2.0 authorization framework. It enables service providers to verify the identity of users authenticated by an identity provider, using JSON Web Tokens (JWT) as the format for identity assertions. OIDC is widely used for web and mobile SSO, particularly for consumer-facing applications.

## Key Details

- Built on top of OAuth 2.0 — extends authorization with authentication claims
- Uses JSON Web Tokens (JWT) as the format for ID tokens — lightweight and widely supported
- Supports multiple authentication flows: Authorization Code, Implicit (deprecated), PKCE
- ID Token contains claims about the authenticated user (name, email, groups, custom claims)
- Widely adopted: Google Sign-In, Sign in with Apple, Microsoft identity platform all use OIDC

## Connections

- Parent: [[federation]] — OpenID Connect is a primary modern federation protocol
- See also: [[openid-connect-oidc]]
