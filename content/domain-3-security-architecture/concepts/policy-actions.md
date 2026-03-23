---
title: "Policy actions"
description: "alert, block, encrypt, quarantine, log, notify manager"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

DLP policy actions define what the system does when it detects a policy violation — specifically, when sensitive data is identified in an unauthorized context. The appropriate action depends on the severity of the violation, the sensitivity of the data, and the organizational risk tolerance. Actions range from passive (log only) to active (block and quarantine).

## Key Details

- **Alert**: notify the security team or manager about a potential violation for investigation
- **Block**: prevent the transfer, email, or upload from completing
- **Encrypt**: automatically encrypt the data before allowing transfer (enables monitoring without blocking)
- **Quarantine**: hold the data or email for security review before release or delivery
- **Log**: record the event for compliance and investigation without taking blocking action
- **Notify manager**: alert the user's manager about a potential policy violation

## Connections

- Parent: [[dlp]] — policy actions define how DLP enforces data protection rules
- See also: [[data-loss-prevention-dlp]]
