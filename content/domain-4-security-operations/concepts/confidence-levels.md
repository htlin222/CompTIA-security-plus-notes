---
title: "Confidence levels"
description: "Rating how reliable and accurate a piece of intelligence is"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Confidence Levels?
> Not every tip is equally trustworthy. Confidence levels are like star ratings -- a five-star tip is very reliable, while a one-star tip might just be a rumor you should double-check.

## Definition

Confidence levels are ratings assigned to threat intelligence items that reflect the analyst's or source's degree of certainty in the accuracy and reliability of the information. These ratings help analysts prioritize how much weight to give intelligence when making decisions about detections, hunting activities, and defensive measures.

## Key Details

- Common scales include High/Medium/Low or numeric scales (e.g., 1-100)
- Intelligence sharing standards like STIX support structured confidence rating fields
- High-confidence IoCs can be used for automated blocking; low-confidence ones warrant investigation only
- Source reliability and information credibility are assessed separately (similar to intelligence community methods)
- Confidence degrades over time — an IoC from 2 years ago has lower confidence than one from yesterday

## Connections

- Parent: [[threat-intelligence]] — confidence levels are essential metadata for threat intelligence
- See also: [[stix-structured-threat-information-expression]]
