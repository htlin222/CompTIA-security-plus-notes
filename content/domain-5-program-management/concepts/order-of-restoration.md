---
title: "Order of restoration"
description: "critical systems first, based on BIA priorities and RTO requirements"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

## Definition

The order of restoration (also called restoration sequence) defines the priority sequence in which systems and services are brought back online during disaster recovery. The order is determined by the Business Impact Analysis (BIA) — systems supporting the most critical business functions with the tightest RTOs are restored first. Infrastructure dependencies must also be considered: foundational systems (network, DNS, directory services) must be restored before application systems that depend on them.

## Key Details

- Typical restoration sequence: 1) Core infrastructure (network, power, DNS, AD), 2) Security systems (firewalls, IDS/IPS), 3) Critical business applications (ERP, payment processing), 4) Secondary applications, 5) Non-critical systems
- The order must account for dependencies — restoring an application server before its database is online will fail
- BIA priorities and RTO values drive the sequence; the most business-critical systems with tightest RTOs are restored first
- The order of restoration should be documented in the DRP and tested regularly
- Exam tip: order of restoration flows from the BIA; know that infrastructure (network, directory) comes before applications

## Connections

- Parent: [[business-continuity]] — restoration order is a critical output of BCP and DRP planning
- See also: [[bia-as-the-foundation]]
- See also: [[recovery-time-objective-rto]]
