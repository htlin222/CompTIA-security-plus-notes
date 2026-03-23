---
title: "Third-Party Risk"
description: "Third-party risk management addresses the security threats introduced by vendors, suppliers, and service providers."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/risk
  - weight/medium
aliases:
  - "Third-Party Risk Management"
  - "TPRM"
---

> [!eli5] ELI5: What is Third-Party Risk?
> Say you give your house key to a dog walker so they can come in while you're at school. You trust them, but what if they lose the key or leave the door unlocked? Third-party risk is the danger that comes from sharing your stuff (data, systems, or access) with outside helpers like vendors or partners. If their security is weak, bad guys could get to your data through them -- even if your own locks are strong.

## Overview

Third-party risk arises whenever an organization shares data, systems, or access with external entities such as vendors, contractors, cloud providers, or business partners. A compromise at a third party can directly impact your organization. Managing this risk requires due diligence before onboarding, continuous monitoring during the relationship, and secure offboarding at termination.

## Key Concepts

- **[[supply-chain-risk|Supply chain risk]]** — compromised hardware, software, or services introduced through the supply chain (e.g., SolarWinds)
- **[[vendor-assessment|Vendor assessment]]** — questionnaires, on-site audits, penetration test results, and SOC reports used to evaluate vendor security
- **[[service-level-agreements-slas|Service Level Agreements (SLAs)]]** — contractual terms defining uptime, response times, and security obligations
- **[[right-to-audit|Right to audit]]** — contractual clause allowing the organization to audit the vendor's security controls
- **[[data-ownership-and-processing-agreements|Data ownership and processing agreements]]** — clearly define who owns data and how it is handled, stored, and deleted
- **[[soc-reports|SOC reports]]** — SOC 2 Type I (point-in-time) and Type II (over a period) attest to a service provider's controls
- **[[vendor-lock-in|Vendor lock-in]]** — dependency risk when switching providers is costly or technically difficult
- **[[offboarding|Offboarding]]** — revoking access, retrieving data, and ensuring secure data destruction when a vendor relationship ends
- **[[fourth-party-risk|Fourth-party risk]]** — risk from your vendor's vendors; you may not have visibility into their supply chain

## Exam Tips

> [!tip] Remember
> SOC 2 Type II is more valuable than Type I because it covers a time period, not just a snapshot. The exam tests supply chain attacks and vendor assessment methods frequently.

## Connections

- Falls under the broader [[risk-management]] framework as a specific category of external risk
- Related to [[compliance]] because regulations often require organizations to ensure third-party data handling meets standards
- See also [[security-policies]] for acceptable use and vendor management policy requirements

## Scenario

> See [[case-third-party-risk]] for a practical DevOps scenario applying these concepts.
