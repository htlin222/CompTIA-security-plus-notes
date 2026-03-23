---
title: "Single point of failure (SPOF)"
description: "any component whose failure would bring down an entire system"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
aliases:
  - SPOF
---

> [!eli5] ELI5: What is a Single Point of Failure?
> Imagine a bridge held up by just one rope. If that one rope snaps, the whole bridge falls. A single point of failure is that one rope you really need a backup for.

## Definition

A single point of failure (SPOF) is any component — hardware, software, network path, personnel, or third-party service — whose failure would cause an entire system, service, or business process to become unavailable. SPOFs represent unacceptable availability risk for critical systems and should be identified during the BIA and eliminated through redundancy (RAID, clustering, load balancing, failover) or acceptance (documented risk with compensating controls).

## Key Details

- Hardware SPOFs: a single power supply, network switch, or server with no failover
- Network SPOFs: a single ISP connection, single network path, or single DNS server
- Personnel SPOFs: a single person with exclusive knowledge of a critical system or process (addressed through succession planning and documentation)
- Vendor SPOFs: sole-source vendors for critical services with no alternative provider
- Eliminating SPOFs: RAID (disk redundancy), clustering (server redundancy), dual ISP connections (network redundancy), hot standby systems (application redundancy)

## Connections

- Parent: [[business-impact-analysis]] — SPOF identification is a key deliverable of the BIA and dependency analysis
- See also: [[dependencies]]
- See also: [[mean-time-between-failures-mtbf]]
