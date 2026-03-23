---
title: "Replication"
description: "real-time or near-real-time copying of data to a secondary location"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

## Definition

Replication is the process of continuously or near-continuously copying data from a primary system or site to a secondary (replica) system or site, maintaining a synchronized or near-synchronized copy. Unlike traditional backups (which are point-in-time snapshots), replication provides a current or nearly current copy of data, enabling very low RPOs (near zero for synchronous replication). Replication is essential for high-availability and hot-site disaster recovery strategies.

## Key Details

- **Synchronous replication**: writes are committed to both primary and replica simultaneously; near-zero RPO but adds write latency; typically used within the same data center or metropolitan area
- **Asynchronous replication**: writes are committed to primary first, then replicated to secondary with a small lag; allows greater geographic distance; small RPO gap
- Replication is not a backup substitute — it replicates corruption and ransomware encryption in real time; separate backup copies are still required
- Cloud-based replication services (AWS RDS Multi-AZ, Azure Site Recovery) are common enterprise solutions
- Exam tip: synchronous = zero data loss but latency; asynchronous = slight data loss risk but geographic flexibility

## Connections

- Parent: [[disaster-recovery]] — replication is the technical mechanism for achieving low RPO in DR architectures
- See also: [[recovery-point-objective-rpo]]
- See also: [[3-2-1-backup-rule]]
