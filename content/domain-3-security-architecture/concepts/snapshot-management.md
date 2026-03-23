---
title: "Snapshot management"
description: "snapshots capture VM state; old snapshots may contain outdated or vulnerable configurations"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

VM snapshot management involves the creation, maintenance, and lifecycle governance of point-in-time captures of virtual machine state. While snapshots are valuable for rapid rollback after changes or incidents, poorly managed snapshots — particularly old, forgotten ones — can create security risks because they preserve outdated configurations and unpatched software that would otherwise have been updated.

## Key Details

- Snapshots capture the complete VM state: disk, memory, and configuration at a point in time
- Old snapshots may contain vulnerable software versions, weak configurations, or outdated OS patches
- Snapshots should not be used as long-term backups — use dedicated backup solutions instead
- Snapshot chains grow over time and can significantly impact performance and storage consumption
- Organizations should have snapshot retention policies: automatically delete snapshots older than defined thresholds

## Connections

- Parent: [[virtualization-security]] — snapshot management is an important virtualization security hygiene practice
- See also: [[vm-sprawl]]
