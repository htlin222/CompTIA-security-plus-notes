---
title: "Vendor diversity"
description: "Using products from multiple vendors so a vulnerability in one doesn't compromise all security layers"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Vendor Diversity?
> Don't buy all your locks from the same company. If that company's locks all have the same flaw, every door in your building becomes easy to open at once. Using different brands means one flaw won't break everything.

## Definition

Vendor diversity is a defense-in-depth strategy that uses security products from different vendors at different layers of the security architecture. By avoiding a single-vendor monoculture, organizations ensure that a vulnerability, supply chain compromise, or zero-day affecting one vendor's products does not simultaneously disable all security controls. It is a risk management approach to reduce the single-vendor dependency risk.

## Key Details

- **Risk of single-vendor**: A vulnerability in one vendor's product (e.g., a perimeter firewall) could bypass all defenses if all security layers use the same platform.
- Common application: different vendors for **perimeter firewall** vs. **internal firewall** vs. **EDR** vs. **SIEM**.
- **Tradeoffs**: Increased operational complexity, integration challenges, higher training costs vs. reduced single-vendor risk.
- Particularly relevant for **supply chain attacks**: A compromised update for one vendor's product affects only that layer, not all defenses.
- Balancing act: excessive diversity creates unmanageable complexity—most organizations use 2-3 core security vendors with diversity at critical control points.

## Connections

- Parent: [[defense-in-depth]] — a vendor-level control diversity strategy
- See also: [[control-diversity]]
