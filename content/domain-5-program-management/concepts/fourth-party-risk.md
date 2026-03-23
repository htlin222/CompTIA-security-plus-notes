---
title: "Fourth-party risk"
description: "risk from your vendor's vendors; you may not have visibility into their supply chain"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What is Fourth-Party Risk?
> You trust the pizza delivery person, but what about the company that made their delivery bags? Fourth-party risk is the danger from your partner's partners -- people you don't even know but who can still cause problems for you.

## Definition

Fourth-party risk (also called nth-party risk) is the risk that arises from the vendors, subcontractors, and service providers used by your direct vendors (third parties). While organizations can assess and contractually obligate their direct vendors, they typically have limited visibility into what controls their vendors' vendors have in place. A breach or failure at a fourth party can cascade up through the supply chain and ultimately impact your organization.

## Key Details

- The SolarWinds supply chain attack is a prime example: attackers compromised SolarWinds (a third party to many organizations), which then affected thousands of downstream customers
- Fourth-party risk is difficult to manage because contractual relationships do not extend to fourth parties directly
- Mitigation strategies: require vendors to flow down security requirements to their subcontractors; review vendor SOC 2 reports (which may address subprocessor controls); include right-to-audit clauses
- TPRM (Third-Party Risk Management) programs are evolving to address fourth-party risk through vendor due diligence questionnaires that ask about sub-vendor controls
- Exam tip: supply chain risk and fourth-party risk are closely related; both involve threats from entities outside the direct vendor relationship

## Connections

- Parent: [[third-party-risk]] — fourth-party risk extends the third-party risk problem further up the supply chain
- See also: [[supply-chain-risk]]
- See also: [[vendor-assessment]]
