---
title: "Anonymization vs. pseudonymization"
description: "anonymization is irreversible; pseudonymization replaces identifiers but can be reversed with a key"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

## Definition

Anonymization permanently removes or destroys all identifying information from a dataset so that individuals can never be re-identified; once anonymized, data is no longer considered personal data under regulations like GDPR. Pseudonymization replaces identifying information with a pseudonym (e.g., a token or hash) but retains a key that allows re-identification; pseudonymized data is still considered personal data and subject to privacy regulations.

## Key Details

- Anonymization: irreversible — cannot re-identify individuals; data falls outside GDPR scope once truly anonymized
- Pseudonymization: reversible — a separate key or mapping table allows re-identification; GDPR explicitly names it as a recommended safeguard (Article 25)
- Examples of pseudonymization: tokenization, data masking with a key, hashing with a salt stored separately
- Re-identification risk exists with pseudonymization if the key is compromised or data is combined with other datasets
- Both techniques are used to reduce privacy risk when sharing or analyzing data; only anonymization fully removes regulatory obligations

## Connections

- Parent: [[privacy]] — core data minimization techniques in privacy management
- See also: [[pii-personally-identifiable-information]]
- See also: [[privacy-by-design]]
