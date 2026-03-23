---
title: "Maintenance windows"
description: "Scheduled periods for implementing changes with minimal user impact"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What are Maintenance Windows?
> It's like how your school does construction work during summer break instead of during class. Maintenance windows are scheduled times when nobody's using the system, so updates and fixes can happen without bothering anyone.

## Definition

Maintenance windows are pre-scheduled time periods during which IT systems can be taken offline or modified for updates, patches, configuration changes, and other maintenance activities. By concentrating changes in defined windows—typically during low-usage periods (nights, weekends)—organizations minimize disruption to users and business operations while ensuring changes are implemented in a controlled, coordinated manner.

## Key Details

- Approved by the **Change Advisory Board (CAB)** and communicated to stakeholders in advance.
- Define the time bounds for a change—if the change can't be completed and rolled back within the window, it may be deferred.
- **Emergency changes** may require an expedited or out-of-window process with appropriate approvals.
- Critical security patches should still have defined maintenance windows, though emergency windows may be shorter.
- Systems with high availability requirements may have very small maintenance windows—requiring precise, well-tested procedures.

## Connections

- Parent: [[change-management]] — a scheduling component of change management
- See also: [[change-advisory-board-cab]], [[backoutrollback-plan]]
