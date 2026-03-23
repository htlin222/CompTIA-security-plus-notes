---
title: "Anonymization"
description: "irreversibly removes identifying information"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Anonymization?
> Anonymization is like completely erasing someone's name, face, and all clues from a story so that nobody could ever figure out who it was about. Once it is done, there is no way to undo it.

## Definition

Anonymization is a data protection technique that permanently removes or transforms all identifying information from a dataset so that the original individual can never be re-identified, even with additional data or context. Unlike pseudonymization, anonymization is a one-way process with no mapping back to the original data. It is commonly used to enable sharing of data sets for research or analytics without exposing personal information.

## Key Details

- Irreversible — there is no key or mapping to re-identify subjects (unlike pseudonymization)
- Common techniques include data aggregation, generalization, noise addition, and suppression
- Used to comply with privacy regulations by removing personal data entirely
- Risk: if not done correctly, re-identification attacks are possible using auxiliary data
- Contrast with pseudonymization, which replaces identifiers but can be reversed with the key

## Connections

- Parent: [[data-protection]] — anonymization is a privacy-preserving data protection technique
- See also: [[pseudonymization]]
