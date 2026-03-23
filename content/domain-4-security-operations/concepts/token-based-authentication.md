---
title: "Token-based authentication"
description: "SSO systems issue tokens (JWT, SAML assertions) that prove identity to relying parties"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Token-based authentication is the mechanism by which SSO and federation systems allow users to authenticate once to an Identity Provider and then access multiple Service Providers using tokens — signed digital artifacts that assert the user's identity without requiring re-authentication. Tokens carry identity claims and are cryptographically signed by the issuing authority to prevent forgery.

## Key Details

- **JWT (JSON Web Token)**: compact, self-contained token format used in OIDC; consists of header, payload, and signature
- **SAML assertion**: XML-format token used in SAML federation; signed by the IdP
- Tokens have expiration times: short-lived access tokens (15 minutes) + longer-lived refresh tokens
- Token theft (session hijacking) is a concern — stolen tokens grant access without knowing the user's password
- Token binding and continuous access evaluation can detect and invalidate stolen tokens

## Connections

- Parent: [[sso]] — token-based authentication is the technical mechanism enabling SSO
- See also: [[saml-security-assertion-markup-language]]
