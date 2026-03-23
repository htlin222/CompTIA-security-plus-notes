---
title: "Dependencies"
description: "upstream and downstream systems that a critical function relies on"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What are Dependencies?
> You can't eat cereal without milk, and you can't pour milk without opening the fridge. Dependencies are the things that rely on each other -- if one breaks, the others can't work either.

## Definition

In the context of business impact analysis and continuity planning, dependencies are the upstream and downstream systems, people, processes, and third parties that a critical business function relies upon to operate. Upstream dependencies provide inputs (e.g., a database that feeds an application); downstream dependencies consume outputs (e.g., customers or partners that rely on the service). Understanding dependencies is essential for accurate RTO/RPO planning and identifying single points of failure.

## Key Details

- IT dependencies: servers, databases, network infrastructure, storage, cloud services
- Human dependencies: key personnel, on-call staff, vendors with specialized knowledge
- Third-party dependencies: cloud providers, SaaS vendors, payment processors, utilities
- Dependency mapping reveals hidden single points of failure not obvious from a system inventory alone
- Exam tip: a BIA without dependency mapping will underestimate recovery complexity and time

## Connections

- Parent: [[business-impact-analysis]] — dependency mapping is a core BIA activity
- See also: [[single-point-of-failure-spof]]
- See also: [[critical-business-functions]]
