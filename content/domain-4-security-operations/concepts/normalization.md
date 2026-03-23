---
title: "Normalization"
description: "Converting logs from different formats into a common schema for analysis"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Normalization?
> Different devices write logs in different formats. Normalization is like translating everyone's diary into the same language so you can compare them side by side.

## Definition

Normalization in SIEM and log management is the process of parsing and transforming log data from diverse sources with different formats and field names into a common, standardized data model or schema. Without normalization, writing queries and correlation rules that work across different log sources would require knowing the unique format of every source, making consistent analysis impossible.

## Key Details

- Different systems use different field names for the same concept (e.g., "src_ip", "source_address", "clientip" all mean the same thing)
- Normalized data uses a common schema where equivalent fields have consistent names across all sources
- Common schemas: OCSF (Open Cybersecurity Schema Framework), CEF (Common Event Format), ECS (Elastic Common Schema)
- Enables correlation rules to be written once and applied across all normalized data sources
- Parsing rules extract structured fields from unstructured log text (regex, Grok patterns)

## Connections

- Parent: [[siem]] — normalization is a critical SIEM data processing step
- See also: [[log-aggregation]]
