---
title: "Honeyfiles"
description: "Fake files placed on systems to trigger alerts when accessed by attackers"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Honeyfiles are fictitious files placed strategically on systems or file shares with enticing names (such as "passwords.xlsx," "salary_data.csv," or "backup_keys.txt") designed to attract attackers who have already gained access to a system. Any access to a honeyfile triggers an alert, providing immediate detection of unauthorized access with minimal false positives—legitimate users have no reason to access files they don't know about.

## Key Details

- Placed in directories where attackers are likely to look: shared drives, document folders, administrative shares.
- Access monitoring is configured to alert **immediately** when any honeyfile is opened, copied, or modified.
- **Very low false positive rate**—there's no legitimate reason for users to access files they weren't told about.
- Names should be enticing to attackers: "passwords," "credentials," "backup," "keys," "financial data."
- Can detect both **external attackers** who've gained access and **malicious insiders** exploring beyond their role.

## Connections

- Parent: [[deception-technologies]] — a file-based deception technique
- See also: [[honeytokens]], [[honeypots]]
