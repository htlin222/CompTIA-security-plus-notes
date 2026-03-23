---
title: "Service account management"
description: "Tracking and securing non-human accounts used by applications and scripts"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Service account management involves the tracking, securing, and governance of non-human accounts used by applications, services, automated processes, and scripts to authenticate and perform operations. Service accounts are frequently overlooked in identity management programs, yet they often hold significant privileges and can be exploited by attackers for lateral movement or persistence.

## Key Details

- Service accounts should have the minimum permissions necessary for their specific function
- Passwords should be complex, rotated regularly, and managed through PAM vaults (never hardcoded)
- Service accounts should not be able to log in interactively — restrict to service authentication only
- Monitor service account activity for anomalies: logins from unexpected systems, off-hours activity
- Managed Service Accounts (MSA) and Group Managed Service Accounts (gMSA) in Windows automate password management for service accounts

## Connections

- Parent: [[privileged-access-management]] — service account management is a key PAM function
- See also: [[credential-rotation]]
