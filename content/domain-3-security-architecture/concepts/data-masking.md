---
title: "Data masking"
description: "obscures portions of data (e.g., showing only last 4 digits of a credit card)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Data masking?
> It's like putting a sticker over most of a phone number so only the last few digits show. The full number is still there underneath, but casual viewers cannot see it.

## Definition

Data masking is a data protection technique that obscures or replaces sensitive data with a similar but non-sensitive substitute, making it usable for non-production purposes such as testing and development without exposing real data. Static masking permanently replaces data, while dynamic masking applies transformations in real time when data is accessed by users who lack authorization to see the full value.

## Key Details

- Common example: showing only the last 4 digits of a credit card number (****-****-****-1234)
- Static masking creates a permanently masked copy of a database for use in test environments
- Dynamic masking applies masking in real time based on the user's role or access level
- Differs from encryption: masked data is usable in its masked form without decryption
- Used to comply with PCI DSS, HIPAA, and other regulations requiring protection of sensitive data in non-production environments

## Connections

- Parent: [[data-protection]] — data masking is a technique to protect sensitive data while maintaining usability
- See also: [[tokenization]]
