---
title: "VM escape"
description: "attacker breaks out of a VM and accesses the hypervisor or other VMs; a critical virtualization threat"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is VM escape?
> A VM escape is like a prisoner breaking out of their cell and getting into the guard's control room. An attacker breaks out of their virtual computer and gains access to the system that controls all the other virtual computers -- one of the most dangerous things that can happen.

## Definition

VM escape is a critical virtualization attack in which a malicious actor exploits a vulnerability in the hypervisor or virtual hardware to break out of an isolated virtual machine and gain unauthorized access to the underlying host system or other co-located VMs. Because the hypervisor controls all VMs on a host, a successful VM escape compromises every VM on that system and potentially the entire physical host.

## Key Details

- Exploits hypervisor vulnerabilities, emulated device drivers, or shared memory interfaces
- Grants attacker access to the hypervisor, host OS, and all other VMs on the same physical host
- Among the most severe virtualization threats; severity is amplified in multi-tenant cloud environments
- Mitigations: keep hypervisor patched, minimize attack surface (disable unused virtual devices), use hardware-enforced isolation (Intel VT-x, AMD-V)
- Defense also includes VM isolation controls and network segmentation between VMs

## Connections

- Parent: [[virtualization-security]] — VM escape is one of the most critical virtualization-specific threats
- See also: [[vm-isolation]], [[hardening-the-hypervisor]], [[multitenancy-risks]]
