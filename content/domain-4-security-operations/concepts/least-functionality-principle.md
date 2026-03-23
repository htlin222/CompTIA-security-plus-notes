---
title: "Least functionality principle"
description: "Systems should only have the minimum capabilities needed for their role"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is the Least Functionality Principle?
> Only install what you actually need. It is like packing for a trip -- if you bring less stuff, there is less that can get lost or stolen.

## Definition

The least functionality principle is a security hardening concept that specifies that each system should be configured to provide only the minimum set of functions, services, and capabilities required for its designated role. Extra functionality represents unnecessary attack surface — every unused feature, service, or port is a potential vulnerability that serves no business purpose.

## Key Details

- Remove or disable all software, services, features, and user accounts not needed for the system's function
- Web servers should only run web server software — not database servers, email servers, etc.
- Closely related to the principle of least privilege (applied to systems rather than users)
- CIS Benchmarks and STIGs provide specific guidance on what to disable for different system types
- Regular reviews ensure no new unnecessary functionality has been added

## Connections

- Parent: [[hardening]] — least functionality is a guiding principle for system hardening
- See also: [[disable-unnecessary-services-and-ports]]
