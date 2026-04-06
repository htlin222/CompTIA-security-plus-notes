---
title: "Data Classification"
description: "Data classification assigns sensitivity levels to information assets to ensure appropriate handling, storage, and protection controls."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/data
  - weight/medium
aliases:
  - "Data Classification"
---

> [!eli5] ELI5: What is Data Classification?
> Think about how a library organizes books. Some are on open shelves anyone can grab, some are in a special section you need a library card for, and some rare books are locked in a glass case. Data classification works the same way -- a company sorts its information into groups based on how secret or important it is, then decides who can see it and how carefully it needs to be protected. The most sensitive stuff gets the strongest locks.

## Overview

Data classification is the process of categorizing data based on its sensitivity, value, and regulatory requirements to determine the appropriate level of protection. Proper classification ensures that the most sensitive data receives the strongest controls while avoiding excessive spending on low-value data. Classification is a prerequisite for effective data loss prevention and access control.

## Key Concepts

- **[[government-military-classifications|Government / military classifications:]]** Top Secret, Secret, Confidential, Unclassified
- **[[commercial-private-sector-classifications|Commercial / private sector classifications:]]** Confidential/Restricted, Private/Internal, Public
- **[[classification-criteria|Classification criteria]]** — regulatory requirements, business value, sensitivity, impact if disclosed
- **Data roles:**
  - **Data owner** — senior leader accountable for the data; sets classification level
  - **Data custodian** — IT staff responsible for implementing controls (backups, encryption)
  - **Data steward** — ensures data quality and proper use of metadata
  - **Data processor** — entity that processes data on behalf of the controller (GDPR term)
  - **Data controller** — entity that determines purposes and means of processing (GDPR term)
- **[[data-states|Data states]]** — data at rest, data in transit, data in use; each requires appropriate protection
- **[[labeling-and-marking|Labeling and marking]]** — applying headers, footers, watermarks, or metadata tags to classified data
- **[[handling-procedures|Handling procedures]]** — storage, transmission, retention, and destruction rules per classification level
- **[[declassification|Declassification]]** — reducing the classification level when sensitivity decreases over time
- **Information life cycle** — creation, classification, storage, usage, archival, destruction
- **[[privacy-impact-assessment-pia|PIA (Privacy Impact Assessment)]]** — analysis of how personally identifiable information is collected, used, shared, and protected
- **DPO (Data Protection Officer)** — role responsible for ensuring the organization's compliance with privacy regulations
- **Pseudo-anonymization** — replacing identifying fields with artificial identifiers; reversible with the right key (unlike full anonymization)

## Exam Tips

> [!tip] Remember
> Data owner = business leader who decides classification. Data custodian = IT person who implements technical controls. The exam tests these role distinctions heavily. Remember: owner decides, custodian protects.

## Connections

- Closely tied to [[data-protection]] which implements the technical controls based on classification levels
- Supports [[privacy]] by ensuring personal data is identified and handled according to regulations
- See also [[dlp]] for tools that enforce classification-based data handling rules

## Practice Questions

> [!qbank]- Q-Bank: Data Classification (4 Questions)
>
> **Q1.** A company's VP of Marketing determines that customer survey results should be labeled as "Internal Use Only." Which data role is this person fulfilling?
>
> A. Data custodian
> B. Data steward
> C. Data owner
> D. Data processor
>
> > [!answer]- Show Answer
> > **C. Data owner**
> >
> > The [[data-classification|data owner]] is a senior leader who is accountable for the data and sets its classification level. A data custodian (A) implements technical controls but does not determine classification. A data steward (B) ensures data quality and metadata standards. A data processor (D) is a GDPR term for an entity that processes data on behalf of the controller.
>
> **Q2.** A government contractor receives a document marked "Secret." An employee copies its contents into an unclassified email and sends it to an external partner. Which data classification control failure does this MOST directly represent?
>
> A. Improper declassification
> B. Failure to follow handling procedures
> C. Incorrect labeling and marking
> D. Missing data steward assignment
>
> > [!answer]- Show Answer
> > **B. Failure to follow handling procedures**
> >
> > [[handling-procedures|Handling procedures]] define how data at each classification level must be stored, transmitted, and shared. Sending Secret data via unclassified email violates transmission rules. Declassification (A) is a formal process to reduce classification level, which did not occur here. Labeling and marking (C) applies to tagging the document itself, which was already marked correctly. A missing data steward (D) is an organizational gap, not the direct cause of this incident.
>
> **Q3.** An IT administrator is tasked with encrypting a database containing employee Social Security numbers and configuring backup schedules for the server. Which data role BEST describes this administrator's responsibilities?
>
> A. Data owner
> B. Data controller
> C. Data custodian
> D. Data steward
>
> > [!answer]- Show Answer
> > **C. Data custodian**
> >
> > The [[data-classification|data custodian]] is the IT staff member responsible for implementing technical controls such as encryption and backups. The data owner (A) is the business leader who sets classification and policy, not the person implementing technical controls. The data controller (B) is a GDPR term for the entity that determines purposes of processing. The data steward (D) focuses on data quality and metadata management.
>
> **Q4.** A private-sector company is designing its data classification scheme. Executives want three tiers that map to increasing levels of protection. Which classification model is MOST appropriate?
>
> A. Top Secret, Secret, Confidential
> B. Confidential, Private, Public
> C. Classified, Unclassified, Restricted
> D. Critical, High, Medium, Low
>
> > [!answer]- Show Answer
> > **B. Confidential, Private, Public**
> >
> > [[commercial-private-sector-classifications|Commercial/private sector classifications]] typically use Confidential (or Restricted), Private (or Internal), and Public as their three tiers. Top Secret/Secret/Confidential (A) is the government/military classification scheme. Classified/Unclassified/Restricted (C) mixes government and commercial terms inconsistently. Critical/High/Medium/Low (D) is a risk rating scale, not a standard data classification model.

## Scenario

> See [[case-data-classification]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [3.3 – Data Types and Classifications](https://www.youtube.com/watch?v=R0W0_gZCVzk)
