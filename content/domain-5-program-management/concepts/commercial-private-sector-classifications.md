---
title: "Commercial / private sector classifications"
description: "Confidential/Restricted, Private/Internal, Public"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What are Commercial / Private Sector Classifications?
> Regular companies sort their data into levels like "anyone can see this," "only people who work here can see this," and "only a few trusted people can see this." It's like public, friends-only, and private settings on a social media post.

## Definition

Private sector organizations typically use a three- or four-tier classification scheme for their data. Common levels include: **Confidential/Restricted** (highest sensitivity — trade secrets, financial data, PII, PHI), **Private/Internal** (not for external disclosure but not critically sensitive — internal memos, HR data), and **Public** (information intended for external audiences — press releases, marketing materials). Some organizations add a "Sensitive" tier between Confidential and Internal.

## Key Details

- Classification labels vary by organization; what matters is that they are consistently defined and applied
- Confidential/Restricted data typically requires encryption at rest and in transit, strict access controls, and audit logging
- Internal data requires basic access controls but typically does not require encryption at rest
- Public data has no access restrictions but should still be protected from unauthorized modification
- Exam tip: contrast with government classifications (Top Secret, Secret, Confidential, Unclassified); the terminology differs

## Connections

- Parent: [[data-classification]] — commercial classifications define the tiers used in private organizations
- See also: [[government-military-classifications]]
- See also: [[handling-procedures]]
