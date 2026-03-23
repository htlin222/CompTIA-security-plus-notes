---
title: "Data loss prevention (DLP)"
description: "tools that detect and prevent unauthorized data exfiltration"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
aliases:
  - DLP
---

> [!eli5] ELI5: What is Data loss prevention (DLP)?
> DLP is like a teacher watching the classroom doors to make sure nobody walks out with test answers. It checks everything leaving the network and stops secret information from getting out.

## Definition

Data Loss Prevention (DLP) is a set of tools and processes designed to detect and prevent unauthorized transfer, sharing, or disclosure of sensitive information. DLP solutions inspect content in motion (network), at rest (storage), and in use (endpoints) to identify sensitive data and enforce policies that prevent it from leaving the organization's control.

## Key Details

- DLP can operate at network level (gateway DLP), endpoint level, or on cloud storage
- Uses content inspection techniques: keyword matching, regular expressions, data fingerprinting, machine learning
- Common use cases: prevent PII/PHI from being emailed externally, block uploading to personal cloud storage
- Actions include: block, quarantine, encrypt, alert, and log the incident
- Integration with email security gateways enables scanning of outbound emails for sensitive data

## Connections

- Parent: [[data-protection]] — DLP is a primary technical control for data protection
- See also: [[data-masking]]
