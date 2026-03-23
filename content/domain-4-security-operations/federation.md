---
title: "Federation"
description: "Trust relationship between organizations enabling cross-domain authentication and resource sharing"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/identity
  - weight/medium
aliases:
  - "Federated Identity"
---

> [!eli5] ELI5: What is Federation?
> You know how a library card from your town sometimes works at libraries in nearby towns too? That is federation. Different organizations agree to trust each other, so when you prove who you are at one place, the others accept it without making you sign up again. Each library still controls its own books and rules, but they all honor the same card. This makes life easier for everyone while each place stays in charge of its own stuff.

## Overview

Federation is a system of trust between separate organizations or security domains that allows users authenticated in one domain to access resources in another without re-authenticating. It enables seamless cross-organizational collaboration while maintaining each organization's control over its own identity management. Federation relies on standardized protocols to exchange identity assertions.

## Key Concepts

- **[[trust-relationships|Trust relationships]]**: Formal agreements between identity providers and service providers defining how identity data is shared
- **[[identity-provider-idp|Identity Provider (IdP)]]**: The organization that authenticates users and vouches for their identity
- **[[service-provider-sp|Service Provider (SP)]]**: The organization that accepts identity assertions from the IdP
- **[[saml|SAML]]**: Most common enterprise federation protocol; uses XML assertions exchanged via browser redirects
- **[[openid-connect|OpenID Connect]]**: Modern federation protocol built on OAuth 2.0; uses JSON Web Tokens (JWT)
- **[[ws-federation|WS-Federation]]**: Microsoft-centric federation standard used in ADFS environments
- **[[transitive-trust|Transitive trust]]**: If A trusts B and B trusts C, A may transitionally trust C — this can introduce risk
- **[[attribute-mapping|Attribute mapping]]**: Translating identity attributes (role, department) between different organizational schemas
- **[[cross-certification|Cross-certification]]**: Two CAs establish mutual trust by signing each other's certificates

## Exam Tips

> [!tip] Remember
> Federation = trust BETWEEN organizations. SSO = access within one organization's applications. Federation enables SSO across organizational boundaries. Think of federation as "inter-organizational SSO."

- SAML is the go-to answer for enterprise federation scenarios on the exam
- Federation does NOT require users to have accounts in the remote organization
- Common real-world example: "Sign in with Google" uses OpenID Connect federation

## Connections

- Extends [[sso]] capabilities across organizational boundaries
- Relies on [[identity-management]] infrastructure at each participating organization
- Should be protected with [[mfa]] to ensure federated assertions are backed by strong authentication
- Federation protocols use [[encryption]] to protect identity assertions in transit

## Scenario

> See [[case-federation]] for a practical DevOps scenario applying these concepts.
