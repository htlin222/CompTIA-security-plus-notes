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

> [!eli5] ELI5: What is Data Protection?
> It's like keeping your diary safe. You might put a lock on it so nobody can read it, hide it in a secret spot, and decide when to throw away old pages. Data protection means all the different ways we keep important information safe -- locking it up, controlling who can see it, and making sure it does not end up somewhere it should not be. Every step of the way, from creating data to deleting it, needs a plan.

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

## Practice Questions

> [!qbank]- Q-Bank: Data Protection (4 Questions)
>
> **Q1.** A healthcare organization needs to decommission old hard drives that contain patient records. The drives are SSDs. Which data destruction method is MOST appropriate?
>
> A. Degaussing
> B. Overwriting with multiple passes
> C. Physical destruction (shredding)
> D. Reformatting the drives
>
> > [!answer]- Show Answer
> > **C. Physical destruction (shredding)**
> >
> > For SSDs, [[data-protection|physical destruction]] is the most reliable method. Degaussing (A) only works on magnetic media and has no effect on SSDs. Overwriting (B) is unreliable on SSDs due to wear leveling and spare blocks that may retain data. Reformatting (D) does not securely erase data and leaves recoverable remnants.
>
> **Q2.** A payment processing company wants to protect stored credit card numbers while still allowing customer service representatives to verify the last four digits. Which technique BEST meets this requirement?
>
> A. Anonymization
> B. Tokenization
> C. Data masking
> D. Full disk encryption
>
> > [!answer]- Show Answer
> > **C. Data masking**
> >
> > [[data-masking|Data masking]] obscures portions of data while leaving part visible (such as showing only the last four digits), which is exactly what is needed. Anonymization (A) irreversibly removes identifying information entirely. Tokenization (B) replaces the entire value with a non-sensitive token — it does not allow viewing partial data. Full disk encryption (D) protects data at rest but does not address display-level data visibility.
>
> **Q3.** An organization is encrypting a large database before migrating it to the cloud. Once migration is complete, they want the option to render the old on-premises copy unrecoverable without physical destruction. Which method BEST achieves this?
>
> A. Degaussing the database server
> B. Cryptographic erasure
> C. Data masking the database fields
> D. Pseudonymization of all records
>
> > [!answer]- Show Answer
> > **B. Cryptographic erasure**
> >
> > [[data-protection|Cryptographic erasure]] destroys the encryption key, rendering the encrypted data permanently unrecoverable without physical destruction. Degaussing (A) only works on magnetic media and would not work if the server uses SSDs. Data masking (C) obscures data for display but does not destroy it. Pseudonymization (D) replaces identifiers with pseudonyms but is reversible with the mapping key.
>
> **Q4.** A security analyst discovers that sensitive employee records are being processed in memory on an application server. The data is already encrypted at rest and in transit. Which additional control BEST protects this data?
>
> A. Implementing TLS 1.3 for network connections
> B. Adding BitLocker full disk encryption
> C. Using secure enclaves for processing
> D. Applying data classification labels
>
> > [!answer]- Show Answer
> > **C. Using secure enclaves for processing**
> >
> > Data in use (being processed in memory) requires protection through [[data-protection|secure enclaves]] or process isolation. TLS 1.3 (A) protects data in transit, which is already covered. BitLocker (B) protects data at rest, which is also already covered. Data classification labels (C) are administrative controls that guide handling but do not technically protect data during processing.

## Scenario

> See [[case-data-protection]] for a practical DevOps scenario applying these concepts.
