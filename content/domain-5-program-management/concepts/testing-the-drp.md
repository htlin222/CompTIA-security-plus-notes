---
title: "Testing the DRP"
description: "same test types as BCP (tabletop, simulation, parallel, full interruption)"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

## Definition

Testing the Disaster Recovery Plan (DRP) ensures that recovery procedures, personnel, and systems will actually work when needed. DRP testing uses the same progression of test types as BCP testing: **tabletop exercises** (discussion-based walkthrough), **simulation exercises** (scenario-based practice without real system changes), **parallel tests** (activating the DR site while production continues normally), and **full interruption tests** (actually switching operations to the DR site). Each type increases realism and confidence at the cost of higher risk and effort.

## Key Details

- **Tabletop exercise**: lowest risk, highest accessibility; team walks through the plan verbally; identifies gaps without any system changes
- **Simulation exercise**: teams practice their roles in a realistic scenario; no actual failover occurs
- **Parallel test**: DR systems are activated and tested alongside production; production remains unaffected; validates recovery capability
- **Full interruption test**: production is actually shut down and operations transferred to DR site; highest confidence but highest risk
- Tests should be conducted at least annually; after significant infrastructure changes, re-testing is essential

## Connections

- Parent: [[disaster-recovery]] — testing validates that DR plans will actually work when invoked
- See also: [[after-action-review]]
- See also: [[documentation]]
