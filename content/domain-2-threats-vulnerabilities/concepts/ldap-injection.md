---
title: "LDAP injection"
description: "Manipulating LDAP queries to bypass authentication or enumerate directory information"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is LDAP Injection?
> A company has a digital address book for all its employees. LDAP injection is like tricking the search box into showing you everyone's information, even the stuff you're not supposed to see.

## Definition

LDAP injection is an injection attack targeting applications that use LDAP (Lightweight Directory Access Protocol) queries to authenticate users or look up directory information. When user input is incorporated into LDAP queries without proper sanitization, attackers can modify the query structure to bypass authentication, enumerate user accounts, or access unauthorized directory information.

## Key Details

- Works similarly to SQL injection—unsanitized input modifies the query structure.
- **Authentication bypass**: Classic payload `*)(uid=*))(|(uid=*` can cause an LDAP query to always return true, bypassing password checks.
- **Information disclosure**: Modified queries can enumerate all users, groups, or attributes in the directory.
- Common in **web applications** that use LDAP for authentication (corporate intranets, web portals backed by Active Directory).
- Mitigation: **input validation** and **escaping** LDAP special characters (`(`, `)`, `*`, `\`, `NUL`), use parameterized LDAP queries.

## Connections

- Parent: [[injection-attacks]] — LDAP-specific injection attack
- See also: [[sql-injection-sqli]], [[input-validation]]
