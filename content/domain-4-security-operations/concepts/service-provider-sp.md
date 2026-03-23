---
title: "Service Provider (SP)"
description: "The organization that accepts identity assertions from the IdP"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

A Service Provider (SP) in federated identity and SSO architectures is the application or organization that provides a service to users and relies on an Identity Provider (IdP) to authenticate those users. Rather than managing its own user credentials, the SP accepts identity assertions from the trusted IdP, granting access based on the claims in the assertion.

## Key Details

- The SP trusts assertions from the IdP without independently verifying user credentials
- SP configures which IdP it trusts and what claims it requires from that IdP
- In SAML, the SP receives a SAML assertion from the IdP via the user's browser
- In OIDC, the SP receives an ID Token from the authorization server (IdP)
- A single application can be both an SP (accepting identity from an IdP) and a resource server (accepting access tokens)

## Connections

- Parent: [[federation]] — the SP is a fundamental role in federated identity architectures
- Parent: [[sso]] — the SP is the application that grants access based on IdP-provided authentication
- See also: [[identity-provider-idp]]
