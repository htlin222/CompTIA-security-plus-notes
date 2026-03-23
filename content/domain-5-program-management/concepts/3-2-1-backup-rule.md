---
title: "3-2-1 backup rule"
description: "3 copies of data, on 2 different media types, with 1 copy off-site"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What is the 3-2-1 Backup Rule?
> Keep 3 copies of your homework, save them in 2 different places (like your backpack and your computer), and keep 1 copy at a friend's house. That way, no single disaster can wipe out everything.

## Definition

The 3-2-1 backup rule is a widely recognized best practice for data protection: maintain 3 copies of data (the original plus two backups), stored on 2 different media types (e.g., disk and tape), with at least 1 copy stored off-site. This strategy protects against hardware failure, site-level disasters, and ransomware attacks by ensuring that no single event can destroy all copies.

## Key Details

- The "3" means original data plus two backup copies — not three backups
- The "2" means two different storage media types (e.g., SSD/HDD and tape or cloud), reducing simultaneous failure risk
- The "1" means one copy must be off-site (physical or cloud), protecting against facility-level disasters such as fire or flood
- Off-site copies defend against ransomware; air-gapped backups add additional protection
- RTO and RPO goals drive how frequently backups are taken and how quickly they can be restored

## Connections

- Parent: [[disaster-recovery]] — the 3-2-1 rule is a foundational backup strategy in disaster recovery planning
- See also: [[recovery-point-objective-rpo]]
- See also: [[replication]]
