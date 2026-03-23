---
title: "API security"
description: "cloud services are API-driven; securing APIs is critical to cloud security"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

API security encompasses the practices, tools, and policies used to protect Application Programming Interfaces from unauthorized access, abuse, and exploitation. In cloud environments, virtually all services are accessed and managed through APIs, making API security a critical component of the overall cloud security posture. Threats include broken authentication, injection attacks, and excessive data exposure.

## Key Details

- APIs should require authentication (API keys, OAuth 2.0, JWT tokens) for every request
- Rate limiting prevents API abuse and denial-of-service attacks
- Input validation prevents injection attacks (SQL injection, command injection via API parameters)
- API gateways centralize authentication, logging, and traffic management for APIs
- OWASP API Security Top 10 provides a framework for API-specific vulnerabilities

## Connections

- Parent: [[cloud-security]] — API security is essential for securing cloud-native architectures
- See also: [[secrets-management]]
