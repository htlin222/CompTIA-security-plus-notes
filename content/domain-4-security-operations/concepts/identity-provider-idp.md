---
title: "Identity Provider (IdP)"
description: "The organization that authenticates users and vouches for their identity"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - IdP
  - IDP
---

> [!eli5] ELI5: What is an Identity Provider?
> An identity provider is the trusted front desk that checks your ID. Once they confirm who you are, they tell all the other services, "Yes, this person is legit."

## Definition

An Identity Provider (IdP) is a trusted system or organization that creates, maintains, and manages digital identities and is responsible for authenticating users and asserting their identity to other systems (Service Providers). In federated identity architectures, the IdP is the authoritative source of identity information, issuing assertions or tokens that Service Providers trust to grant access.

## Key Details

- The IdP holds user credentials and performs authentication (verifies the user is who they claim to be)
- Issues identity assertions via SAML, OpenID Connect tokens (JWT), or Kerberos tickets
- Examples: Microsoft Azure AD/Entra ID, Okta, Ping Identity, on-premises Active Directory
- Users authenticate to the IdP once and receive tokens they present to Service Providers (SSO)
- IdPs can be chained: an IdP can trust another IdP's assertions in federated scenarios

## Connections

- Parent: [[federation]] — the IdP is a fundamental role in federated identity architectures
- Parent: [[sso]] — the IdP is the authentication authority in SSO systems
- See also: [[service-provider-sp]]
