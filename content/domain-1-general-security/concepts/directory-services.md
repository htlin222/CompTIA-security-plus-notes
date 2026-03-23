---
title: "Directory services"
description: "LDAP, Active Directory — centralized authentication and identity stores"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Directory services are centralized repositories that store and manage identity information—user accounts, group memberships, computer objects, and policy settings—and provide authentication and authorization services to the network. The most common implementations are Microsoft Active Directory (AD) and LDAP (Lightweight Directory Access Protocol) directories. They are the backbone of enterprise identity management.

## Key Details

- **Active Directory (AD)**: Microsoft's directory service; uses **Kerberos** for authentication and **LDAP** for querying; organized into domains, trees, and forests.
- **LDAP** (port 389, or 636 for LDAPS): Protocol used to query and modify directory services; used by AD and other platforms (OpenLDAP).
- **LDAPS**: LDAP over TLS—encrypts directory queries; LDAP without S transmits data in cleartext.
- AD is the primary target for attackers in Windows environments—**Kerberoasting**, **Pass-the-Hash**, and **Golden/Silver Ticket** attacks all target AD.
- **Group Policy Objects (GPOs)** in AD enforce security configurations across domain-joined computers.

## Connections

- Parent: [[authentication]] — a centralized authentication infrastructure component
- See also: [[kerberos]]
