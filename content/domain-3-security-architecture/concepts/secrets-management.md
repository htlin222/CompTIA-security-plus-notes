---
title: "Secrets management"
description: "storing credentials, keys, and tokens securely in cloud environments"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Secrets management?
> Passwords, keys, and secret codes need a safe place to live. Secrets management is like having a combination-locked vault where all those important secrets are stored instead of leaving them written on sticky notes around the office.

## Definition

Secrets management is the practice of securely storing, accessing, and rotating sensitive credentials such as API keys, database passwords, service account credentials, and cryptographic keys used by applications and automated processes in cloud and on-premises environments. Hardcoded credentials in source code or configuration files are a leading cause of cloud breaches.

## Key Details

- **Never hardcode secrets**: credentials in source code are exposed if repositories are compromised or public
- Tools: AWS Secrets Manager, Azure Key Vault, HashiCorp Vault, AWS Parameter Store
- Dynamic secrets: some tools generate short-lived credentials on demand rather than using static ones
- Secrets rotation: automated rotation of credentials reduces the risk from leaked secrets
- Application code should retrieve secrets at runtime from a secrets manager, not from files or environment variables where possible

## Connections

- Parent: [[cloud-security]] — secrets management is critical for securing cloud-native applications
- See also: [[api-security]]
