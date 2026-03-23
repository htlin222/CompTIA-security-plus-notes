---
title: "Virtual Network Security"
description: "Virtual switches, virtual firewalls, and micro-segmentation within virtualized environments"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Virtual network security encompasses the controls and mechanisms used to protect network traffic within virtualized environments. This includes virtual switches (vSwitches), virtual firewalls, and micro-segmentation techniques that enforce security policies between virtual machines running on the same physical host. Unlike traditional network security that relies on physical devices, virtual network security operates at the hypervisor level to inspect and control east-west traffic.

## Key Details

- Virtual switches (vSwitches) connect VMs within a host and can enforce VLAN tagging, port security, and traffic isolation
- Virtual firewalls inspect traffic between VMs on the same host — traffic that never crosses a physical network device
- Micro-segmentation applies granular security policies to individual workloads, limiting lateral movement after a breach
- East-west traffic (VM-to-VM within the data center) often exceeds north-south traffic and requires dedicated virtual security controls
- Software-defined networking (SDN) enables centralized policy management across virtual network infrastructure

## Connections

- Parent: [[virtualization-security]] — core virtualization security control
- See also: [[vm-isolation]], [[vlans-virtual-lans]]
