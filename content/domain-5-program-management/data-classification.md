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

## Exam Tips

> [!tip] Remember
> Data owner = business leader who decides classification. Data custodian = IT person who implements technical controls. The exam tests these role distinctions heavily. Remember: owner decides, custodian protects.

## Connections

- Closely tied to [[data-protection]] which implements the technical controls based on classification levels
- Supports [[privacy]] by ensuring personal data is identified and handled according to regulations
- See also [[dlp]] for tools that enforce classification-based data handling rules

## Scenario

> See [[case-data-classification]] for a practical DevOps scenario applying these concepts.
