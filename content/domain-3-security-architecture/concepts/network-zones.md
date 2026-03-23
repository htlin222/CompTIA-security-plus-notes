---
title: "Network zones"
description: "segments with different trust levels (DMZ, internal, guest, management)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What are Network zones?
> A school has different areas -- the playground, the classrooms, the principal's office -- and each has different rules about who can go there. Network zones work the same way, grouping parts of a network by how much they are trusted.

## Definition

Network zones are logically or physically separated network segments, each with a distinct security posture and trust level, that control how traffic flows between them using firewalls and access control lists. Assigning systems to appropriate zones based on their function and risk profile is a fundamental network security architecture practice.

## Key Details

- **DMZ/screened subnet**: hosts public-facing services; semi-trusted; isolated from internal network
- **Internal/trusted zone**: corporate systems and data; highest trust; access restricted from DMZ and guest
- **Guest zone**: visitor and personal devices; internet access only; completely isolated from internal resources
- **Management zone**: network management systems, out-of-band access; highest restriction on who can reach it
- **OT/ICS zone**: operational technology systems; may require air gap or strict industrial protocol filtering

## Connections

- Parent: [[network-security-architecture]] — network zones are the building blocks of security-conscious network design
- See also: [[defense-in-depth]]
