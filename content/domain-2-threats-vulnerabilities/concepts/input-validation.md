---
title: "Input validation"
description: "Allowlisting acceptable characters and rejecting or sanitizing everything else"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Input validation is a security control that checks all user-supplied data against defined rules before processing it, rejecting or sanitizing any input that doesn't conform to expected formats or character sets. It is a foundational defense against injection attacks (SQL, command, LDAP), XSS, and buffer overflows. Effective input validation uses allowlisting (defining what IS acceptable) rather than blocklisting (trying to identify all bad inputs).

## Key Details

- **Allowlisting (preferred)**: Define exactly what characters or patterns are acceptable—reject everything else.
- **Blocklisting (insufficient alone)**: Trying to identify and block known-bad inputs—attackers can always find bypasses.
- Must be applied **server-side**—client-side validation is easily bypassed and should only be for usability.
- Context-specific validation: a name field should only accept letters, spaces, hyphens; a phone number field only digits and formatting chars.
- **Input sanitization**: Escaping or encoding special characters rather than rejecting them—appropriate for some contexts (HTML output encoding).

## Connections

- Parent: [[injection-attacks]] — the primary defense against injection vulnerabilities
- See also: [[parameterized-queries-prepared-statements]]
