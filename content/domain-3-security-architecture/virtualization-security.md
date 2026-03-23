---
title: "Virtualization Security"
description: "Virtualization security addresses the risks and controls specific to hypervisors, virtual machines, and virtualized infrastructure."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cloud
  - weight/medium
aliases:
  - "Virtualization Security"
---

> [!eli5] ELI5: What is Virtualization Security?
> Picture one big apartment building where each apartment is completely separate -- you cannot hear your neighbors or walk into their space. Virtualization lets one powerful computer pretend to be many smaller computers, each in its own "apartment." But if the building manager (the hypervisor) is not careful, someone could break through the walls. Virtualization security is about keeping each apartment safe and the building itself locked down.

## Overview

Virtualization allows multiple virtual machines (VMs) to run on a single physical host using a hypervisor. While virtualization provides efficiency and flexibility, it introduces unique security risks including hypervisor attacks, VM escape, resource contention, and sprawl. Securing virtualized environments requires protecting the hypervisor, isolating VMs, and managing the virtual infrastructure lifecycle.

## Key Concepts

- **Hypervisor types:**
  - **Type 1 (bare-metal)** — runs directly on hardware (VMware ESXi, Microsoft Hyper-V, Xen); more secure and performant
  - **Type 2 (hosted)** — runs on top of an OS (VMware Workstation, VirtualBox); additional attack surface from the host OS
- **[[vm-escape|VM escape]]** — attacker breaks out of a VM and accesses the hypervisor or other VMs; critical threat
- **[[vm-sprawl|VM sprawl]]** — uncontrolled proliferation of VMs that become unpatched, unmonitored, and forgotten
- **[[resource-contention|Resource contention]]** — VMs competing for shared CPU, memory, storage, and network resources
- **[[vm-isolation|VM isolation]]** — ensuring one VM cannot access another VM's memory or data
- **[[snapshot-management|Snapshot management]]** — snapshots capture VM state; old snapshots may contain outdated or vulnerable configurations
- **[[virtual-network-security|Virtual network security]]** — virtual switches, virtual firewalls, and micro-segmentation within the virtualized environment
- **[[hardening-the-hypervisor|Hardening the hypervisor]]** — patching, disabling unnecessary services, restricting management access, enabling secure boot
- **[[live-migration-security|Live migration security]]** — encrypting VM data during migration between hosts to prevent interception
- **[[sandboxing|Sandboxing]]** — using VMs as isolated environments for testing suspicious code or malware analysis

## Exam Tips

> [!tip] Remember
> Type 1 hypervisor = bare-metal, more secure. Type 2 = hosted, less secure. VM escape is the most critical virtualization threat. VM sprawl creates unmanaged attack surface. Always encrypt live migrations.

## Connections

- Foundation of [[cloud-security]] since all major cloud platforms run on virtualization technology
- VM isolation is a form of [[network-segmentation]] at the compute level
- See also [[serverless-and-containers]] for alternative virtualization approaches with different security profiles

## Scenario

> See [[case-virtualization-security]] for a practical DevOps scenario applying these concepts.
