---
title: "Data Protection"
description: "Data protection encompasses the technical and administrative controls used to safeguard data throughout its lifecycle."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/data
  - weight/high
aliases:
  - "Data Protection"
---

## Overview

Data protection involves implementing controls to ensure that data remains confidential, intact, and available throughout its lifecycle — from creation through storage, use, sharing, archival, and destruction. Effective data protection addresses data in all three states (at rest, in transit, in use) and applies technical controls like encryption, access controls, and data loss prevention alongside administrative controls like policies and classification.

## Key Concepts

- **Data states:**
  - **At rest** — stored on disk, database, or backup media; protect with encryption (AES-256, BitLocker, FileVault)
  - **In transit** — moving across networks; protect with TLS, IPSec, SSH
  - **In use** — actively being processed in memory; protect with secure enclaves, process isolation
- **[[data-sovereignty|Data sovereignty]]** — data is governed by the laws of the country where it physically resides
- **[[data-loss-prevention-dlp|Data loss prevention (DLP)]]** — tools that detect and prevent unauthorized data exfiltration
- **[[rights-management-drmirm|Rights management (DRM/IRM)]]** — controls that persist with the data (who can view, edit, print, forward)
- **[[tokenization|Tokenization]]** — replaces sensitive data with non-sensitive tokens; original data stored in a secure vault
- **[[data-masking|Data masking]]** — obscures portions of data (e.g., showing only last 4 digits of a credit card)
- **[[anonymization|Anonymization]]** — irreversibly removes identifying information
- **[[pseudonymization|Pseudonymization]]** — replaces identifiers with pseudonyms; reversible with a key
- **[[data-retention-policies|Data retention policies]]** — define how long data must be kept and when it must be destroyed
- **Secure data destruction:**
  - **Overwriting** — writing patterns over data multiple times
  - **Degaussing** — magnetic field destroys data on magnetic media; does not work on SSDs
  - **Physical destruction** — shredding, incineration, pulverizing
  - **Cryptographic erasure** — destroying the encryption key renders encrypted data unrecoverable

## Exam Tips

> [!tip] Remember
> Tokenization replaces data with tokens (PCI DSS loves this). Masking hides parts of data. Degaussing only works on magnetic media, NOT SSDs. Cryptographic erasure = destroy the key to destroy the data. Know all three data states.

## Connections

- Applied based on levels defined by [[data-classification]] — more sensitive data gets stronger controls
- Technical enforcement provided by [[dlp]] tools that monitor and block unauthorized data movement
- [[encryption]] is the primary technical control for protecting data at rest and in transit
- See also [[privacy]] for regulatory requirements around personal data protection

## Scenario

> See [[case-data-protection]] for a practical DevOps scenario applying these concepts.
