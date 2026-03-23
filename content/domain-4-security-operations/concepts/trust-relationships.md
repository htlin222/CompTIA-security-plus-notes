---
title: "Trust relationships"
description: "Formal agreements between identity providers and service providers defining how identity data is shared"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Trust relationships in federated identity are formal, configured agreements between Identity Providers and Service Providers that define the terms under which identity assertions will be accepted. These relationships include technical configuration (exchange of certificates/metadata) and policy agreements (which user attributes will be shared, what the SP will accept) that enable federated authentication to function.

## Key Details

- Established by exchanging SAML metadata documents or OIDC client registration information
- Both parties must configure the other's signing certificates to validate assertions/tokens
- Trust is unidirectional or bidirectional depending on the federation model
- Attribute release policies define which user attributes the IdP will share with each SP
- Federation metadata must be kept current — expired certificates in metadata break federation

## Connections

- Parent: [[federation]] — trust relationships are the foundation that makes federation possible
- See also: [[transitive-trust]]
