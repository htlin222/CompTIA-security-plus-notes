---
title: "Handling procedures"
description: "storage, transmission, retention, and destruction rules per classification level"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

## Definition

Handling procedures are the specific rules that govern how data of each classification level must be stored, transmitted, accessed, retained, and destroyed. They translate classification labels into actionable requirements for employees. For example, Confidential data may require AES-256 encryption at rest, TLS in transit, strict access controls, a 7-year retention period, and secure shredding or cryptographic erasure at end of life.

## Key Details

- **Storage**: encryption requirements, approved storage media, physical security controls (locked cabinets, restricted server rooms)
- **Transmission**: approved protocols (TLS, VPN), prohibition on sending via personal email or unencrypted channels
- **Retention**: how long data must be kept (driven by legal, regulatory, or business requirements)
- **Destruction**: methods vary by media — shredding for paper, degaussing or physical destruction for hard drives, secure erasure for SSDs
- Handling procedures are part of the data classification policy and are tied to employee training

## Connections

- Parent: [[data-classification]] — handling procedures operationalize classification labels into daily behavior
- See also: [[data-states]]
- See also: [[labeling-and-marking]]
