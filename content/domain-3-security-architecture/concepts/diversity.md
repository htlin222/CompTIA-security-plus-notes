---
title: "Diversity"
description: "using different vendors, technologies, or paths to avoid common-mode failures"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Diversity as a resilience strategy involves using different vendors, technologies, platforms, or network paths so that a single vulnerability, failure, or attack cannot simultaneously compromise all redundant components. When redundant systems use identical software or hardware, a single vulnerability can affect all of them — diversity eliminates this common-mode failure risk.

## Key Details

- Vendor diversity: using different products for redundant components (e.g., two different firewall vendors)
- Technology diversity: using different OS platforms in multi-tier architectures
- Path diversity: using physically separate network routes for redundant connectivity
- Addresses the risk that identical redundant systems share the same vulnerabilities
- Trade-off: diversity increases management complexity and training requirements

## Connections

- Parent: [[resilience-and-redundancy]] — diversity strengthens resilience by preventing common-mode failures
- See also: [[high-availability-ha]]
