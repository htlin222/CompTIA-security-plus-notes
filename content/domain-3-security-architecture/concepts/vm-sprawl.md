---
title: "VM sprawl"
description: "uncontrolled proliferation of VMs that become unpatched, unmonitored, and forgotten security liabilities"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

VM sprawl refers to the uncontrolled proliferation of virtual machines within an environment — VMs that are created for temporary purposes but never decommissioned, leaving them unpatched, unmonitored, and outside normal security management processes. Because VMs are easy to create, organizations often accumulate far more than they can effectively manage, creating a significant attack surface of forgotten, vulnerable systems.

## Key Details

- Root cause: ease of VM creation without corresponding governance or lifecycle management
- Dormant VMs often miss patches, creating high-severity unmanaged vulnerabilities
- Attackers can exploit forgotten VMs as pivot points within a network
- Mitigations: VM lifecycle management policies, automated discovery and inventory, snapshot cleanup schedules
- Non-persistence and immutable infrastructure practices help prevent sprawl by design

## Connections

- Parent: [[virtualization-security]] — VM sprawl is a management and security risk specific to virtualized environments
- See also: [[non-persistence]], [[snapshot-management]], [[configuration-drift]]
