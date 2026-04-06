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
- **[[attestation|Attestation]]**: Process of validating that a device or identity claim is genuine and trustworthy
- **[[radius-federation|RADIUS federation]]**: Extending RADIUS authentication across organizational boundaries (e.g., eduroam)

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

## Practice Questions

> [!qbank]- Q-Bank: Federation (4 Questions)
>
> **Q1.** A hospital system needs to allow doctors from a partner university to access its patient scheduling system without creating separate accounts for each doctor. The university will authenticate its own users and vouch for their identity. Which solution BEST enables this?
>
> A. Creating shared accounts for university doctors to use
> B. Establishing a federated trust using SAML between the two organizations
> C. Giving university doctors VPN access to the hospital network
> D. Synchronizing the university's Active Directory with the hospital's directory
>
> > [!answer]- Show Answer
> > **B. Establishing a federated trust using SAML between the two organizations**
> >
> > [[saml|SAML]]-based [[trust-relationships|federation]] allows the university (acting as the [[identity-provider-idp|Identity Provider]]) to authenticate its users, while the hospital (acting as the [[service-provider-sp|Service Provider]]) accepts those assertions without creating local accounts. Option A violates the principle of individual accountability. Option C provides network access but still requires local accounts. Option D creates tight coupling and duplicates identity data across organizations.
>
> **Q2.** In a federated identity environment, Organization A trusts Organization B, and Organization B trusts Organization C. A security architect is concerned that Organization A might implicitly trust users from Organization C. What risk is the architect identifying?
>
> A. Single point of failure
> B. Transitive trust vulnerability
> C. Credential stuffing attack
> D. Certificate revocation failure
>
> > [!answer]- Show Answer
> > **B. Transitive trust vulnerability**
> >
> > [[transitive-trust]] means that if A trusts B and B trusts C, then A may unintentionally trust C — extending access beyond what was originally intended. Option A refers to SSO availability risks, not trust chain risks. Option C is a password attack, not a federation architecture concern. Option D relates to PKI management, not trust relationship design.
>
> **Q3.** An employee clicks "Sign in with Google" to access a third-party project management application. The application never receives the user's Google password. Which federation protocol is MOST likely being used?
>
> A. NTLM
> B. LDAP
> C. OpenID Connect
> D. RADIUS
>
> > [!answer]- Show Answer
> > **C. OpenID Connect**
> >
> > [[openid-connect|OpenID Connect]] is the modern federation protocol built on OAuth 2.0 that enables consumer-facing "Sign in with..." functionality using JSON Web Tokens without sharing passwords. Option A is a legacy Windows authentication protocol, not a federation standard. Option B is a directory query protocol, not a federation protocol. Option D is an AAA protocol for network access, not web-based federation.
>
> **Q4.** Two organizations are setting up federation but use different internal attribute names — one uses "dept" while the other uses "department" for the same field. What must be configured to resolve this issue?
>
> A. Attribute mapping between the two identity schemas
> B. A new DNS SPF record for both domains
> C. Bilateral cross-certification of SSL certificates
> D. A shared LDAP directory replicated between both organizations
>
> > [!answer]- Show Answer
> > **A. Attribute mapping between the two identity schemas**
> >
> > [[attribute-mapping]] translates identity attributes between different organizational schemas, ensuring that claims like department, role, and group membership are correctly interpreted by both the IdP and SP. Option B relates to email security, not identity federation. Option C establishes PKI trust but does not resolve attribute naming differences. Option D requires data synchronization, which federation is specifically designed to avoid.

## Scenario

> See [[case-federation]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [4.6 – Identity and Access Management](https://www.youtube.com/watch?v=ZoOyyqhptik)
