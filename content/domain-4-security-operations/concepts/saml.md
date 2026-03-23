---
title: "SAML"
description: "Most common enterprise federation protocol; uses XML assertions exchanged via browser redirects"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

SAML (Security Assertion Markup Language) is the most widely deployed enterprise federation protocol, using XML-formatted assertions exchanged between an Identity Provider (IdP) and Service Provider (SP) via browser redirects to enable single sign-on. The IdP authenticates the user and generates a SAML assertion containing the user's identity and attributes, which the browser delivers to the SP.

## Key Details

- Uses XML assertions transmitted via HTTP redirects or HTTP POST
- Three parties: user/principal, Identity Provider (IdP), and Service Provider (SP)
- Three types of assertions: Authentication (who you are), Authorization (what you can do), Attribute (your properties)
- SP-initiated vs. IdP-initiated flows: user can start at SP or IdP
- SAML is dominant in enterprise B2B federation; OIDC is more common for consumer/B2C applications

## Connections

- Parent: [[federation]] — SAML is the primary enterprise federation protocol
- See also: [[saml-security-assertion-markup-language]]
