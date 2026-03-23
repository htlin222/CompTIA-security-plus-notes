---
title: "API attacks"
description: "Exploiting insecure APIs through broken authentication, excessive data exposure, or lack of rate limiting"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are API Attacks?
> An API is like a drive-through window where apps order information. An API attack is when someone figures out how to trick the window into giving out free food -- or everyone else's orders.

## Definition

API attacks target application programming interfaces (APIs) that expose backend services to clients. Common vulnerabilities include broken authentication (weak or missing token validation), excessive data exposure (returning more data than necessary), injection flaws in API parameters, and lack of rate limiting enabling brute-force or enumeration attacks. APIs have become a primary attack surface as organizations move to microservices and cloud architectures.

## Key Details

- **OWASP API Security Top 10** covers the most critical API vulnerabilities including Broken Object Level Authorization (BOLA/IDOR), Broken Authentication, and Excessive Data Exposure.
- **Lack of rate limiting** enables credential stuffing, brute force, and resource exhaustion against APIs.
- APIs often expose more data than UI applications—attackers can query hidden endpoints or parameter-mine responses.
- **API keys** and **OAuth tokens** must be properly validated; leaked keys in public repositories are a common finding.
- Defenses include: authentication on all endpoints, input validation, rate limiting, and WAF rules.

## Connections

- Parent: [[application-attacks]] — a category of application-layer attacks
- See also: [[injection-attacks]], [[server-side-request-forgery-ssrf]]
