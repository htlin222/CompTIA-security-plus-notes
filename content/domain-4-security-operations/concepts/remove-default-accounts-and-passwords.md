---
title: "Remove default accounts and passwords"
description: "Default credentials are publicly known and easily exploited"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What does Removing Default Accounts and Passwords mean?
> Many devices come with usernames like "admin" and passwords like "password." Removing them is like changing the locks on a new house because the old owner still has copies of the key.

## Definition

Removing default accounts and changing default passwords is one of the most fundamental and critical hardening steps for any device or system. Manufacturers ship devices with known default credentials (often documented publicly or easily searchable) that attackers can use immediately to gain access if they are not changed before deployment.

## Key Details

- Default credentials are cataloged in databases like CIRT.net and Shodan — widely known to attackers
- Applies to: network devices (routers, switches, firewalls), IoT devices, applications, databases, operating systems
- Some devices cannot change the default account name — the password must at minimum be changed
- Automated scanning for default credentials is common in both vulnerability assessments and attacker toolkits
- NIST and CIS guidelines both emphasize changing defaults as a foundational security step

## Connections

- Parent: [[hardening]] — removing default credentials is a baseline hardening requirement
- See also: [[cis-benchmarks]]
