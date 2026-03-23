---
title: "Diversity"
description: "using different vendors, technologies, or paths to avoid common-mode failures"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Diversity?
> If everyone on a soccer team wears the same shoes and those shoes break, the whole team is stuck. But if different players wear different brands, one shoe recall will not take out everyone. Diversity in security means using different tools and providers so one flaw does not break everything.

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
