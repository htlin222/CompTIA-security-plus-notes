---
title: "Attribute mapping"
description: "Translating identity attributes (role, department) between different organizational schemas"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Attribute Mapping?
> When two schools merge, they need to match up "Grade 5" at one school with "Year 5" at the other. Attribute mapping translates identity details between different systems so they understand each other.

## Definition

Attribute mapping is the process of translating identity attributes such as roles, department names, and group memberships between the schemas used by different organizations participating in a federation. Since organizations may use different naming conventions and structures for their identity systems, attribute mapping ensures that the service provider receives the identity information in the format it expects.

## Key Details

- Required when IdP and SP use different attribute naming conventions or data formats
- Common in SAML and OpenID Connect federations between different enterprises
- Example: mapping an IdP's "employee_department=Finance" to SP's "group=FinanceUsers"
- Misconfigured attribute mapping can result in privilege escalation or access denial
- Often configured in the identity provider or in a federation broker/hub

## Connections

- Parent: [[federation]] — attribute mapping is a technical requirement for federation to work
- See also: [[identity-provider-idp]]
