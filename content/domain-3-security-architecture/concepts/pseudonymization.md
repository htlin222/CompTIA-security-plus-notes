---
title: "Pseudonymization"
description: "replaces identifiers with pseudonyms; reversible with a key"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Pseudonymization?
> It's like using a secret code name instead of your real name. Your teacher has a list that connects the code name back to you, but anyone else just sees the code name and does not know who it really is.

## Definition

Pseudonymization is a data protection technique that replaces directly identifying information (such as names, email addresses, or social security numbers) with artificial pseudonyms or reference codes, while maintaining a separate mapping that allows re-identification when necessary. Unlike anonymization, pseudonymization is reversible — the original data can be recovered using the mapping key.

## Key Details

- The mapping between pseudonyms and real identities must be stored and protected separately
- GDPR recognizes pseudonymization as a risk-reduction measure but considers pseudonymized data still personal data (reversible)
- Enables data to be used for analytics and testing while reducing privacy exposure
- The security of pseudonymized data depends entirely on protecting the mapping/key
- Differs from anonymization: anonymization is permanent/irreversible; pseudonymization can be reversed

## Connections

- Parent: [[data-protection]] — pseudonymization is a key data protection technique recognized by privacy regulations
- See also: [[anonymization]]
