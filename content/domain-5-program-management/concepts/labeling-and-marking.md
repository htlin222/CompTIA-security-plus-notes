---
title: "Labeling and marking"
description: "applying headers, footers, watermarks, or metadata tags to classified data"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What is Labeling and Marking?
> You know those "FRAGILE" stickers on packages? Labeling data works the same way -- you put a visible tag on it (like "Confidential" or "Public") so everyone handling it knows how careful to be.

## Definition

Labeling and marking is the practice of visibly identifying the classification level of data so that anyone who encounters it knows what handling procedures apply. For physical documents, this means stamping or printing classification markings on headers, footers, and covers. For electronic data, it means applying classification metadata tags, watermarks, email banners, or DLP-enforced labels (such as Microsoft Purview sensitivity labels). Proper labeling enables DLP tools to automatically enforce handling restrictions.

## Key Details

- Physical documents: classification markings appear on top and bottom of every page, on covers, and on storage media
- Electronic files: sensitivity labels (e.g., Confidential, Restricted) applied via DLP tools or manually by users
- Email: classification banners in the subject line or body indicate sensitivity (e.g., "[CONFIDENTIAL]")
- Labels enable automated DLP policy enforcement — a DLP system can block a "Confidential" labeled document from being emailed externally
- Exam tip: labeling is a prerequisite for effective DLP enforcement; DLP tools use labels to identify sensitive data and apply handling policies

## Connections

- Parent: [[data-classification]] — labeling translates classification decisions into visible markers on data
- See also: [[handling-procedures]]
- See also: [[data-states]]
