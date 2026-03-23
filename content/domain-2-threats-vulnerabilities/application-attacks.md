---
title: "Application Attacks"
description: "Attacks targeting software applications through input manipulation, logic flaws, and misconfigurations"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/high
aliases:
  - "Web Application Attacks"
---

## Overview

Application attacks exploit vulnerabilities in software applications — particularly web applications — through techniques like input manipulation, session hijacking, and exploiting logic flaws. As organizations expose more applications to the internet, the application layer has become a primary attack vector. The Security+ exam covers both attack techniques and the defenses that mitigate them.

## Key Concepts

- **[[buffer-overflow|Buffer overflow]]**: Sending more data than a buffer can hold, overwriting adjacent memory to execute arbitrary code
- **[[integer-overflow|Integer overflow]]**: Exceeding the maximum value of an integer variable, causing unexpected behavior
- **[[race-condition-toctou|Race condition / TOCTOU]]**: Exploiting the timing gap between checking a condition and using the result
- **[[directory-traversal|Directory traversal]]**: Using "../" sequences to access files outside the intended directory (e.g., `../../etc/passwd`)
- **[[session-hijacking|Session hijacking]]**: Stealing or predicting a valid session token to impersonate an authenticated user
- **[[session-replay|Session replay]]**: Capturing and retransmitting a valid authentication exchange
- **[[api-attacks|API attacks]]**: Exploiting insecure APIs through broken authentication, excessive data exposure, or lack of rate limiting
- **[[privilege-escalation|Privilege escalation]]**: Exploiting flaws to gain higher-level access than authorized (vertical) or access other users' data (horizontal)
- **[[resource-exhaustion|Resource exhaustion]]**: Consuming all available memory, CPU, disk, or connections to cause denial of service
- **Injection attacks**: Inserting malicious input into application commands — covered in detail in [[injection-attacks]]
- **[[server-side-request-forgery-ssrf|Server-Side Request Forgery (SSRF)]]**: Tricking the server into making requests to internal resources on behalf of the attacker

## Exam Tips

> [!tip] Remember
> Input validation is the #1 defense against application attacks. Buffer overflows = memory safety issue. Directory traversal = path validation issue. SSRF = the server becomes the attacker's proxy to internal systems.

- Memory-safe languages (Rust, Go, Java) prevent buffer overflows; C/C++ are vulnerable
- API security: always authenticate, authorize, rate-limit, and validate input
- TOCTOU: the gap between "check" and "use" can be exploited in concurrent environments

## Connections

- [[injection-attacks]] and [[xss-and-csrf]] are specific subcategories of application attacks
- [[penetration-testing]] actively exploits these vulnerabilities to demonstrate real-world impact
- Application-level weaknesses are categorized under [[vulnerability-types]]
- Web Application Firewalls (WAFs) as part of [[hardening]] mitigate many application attacks

## Scenario

> See [[case-application-attacks]] for a practical DevOps scenario applying these concepts.
