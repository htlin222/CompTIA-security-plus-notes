---
title: "Hardening the hypervisor"
description: "patching, disabling unnecessary services, restricting management access, enabling secure boot"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Hardening the hypervisor?
> The hypervisor is the "building manager" that controls all the virtual computers. Hardening it means locking all the doors, closing windows, and removing anything the manager does not need -- making it as tough as possible so attackers cannot take over the whole building.

## Definition

Hardening the hypervisor refers to the process of securing the hypervisor layer (the software or firmware that creates and manages virtual machines) by applying security best practices to reduce its attack surface. Because the hypervisor controls all VMs running on a host, a compromised hypervisor can expose all guest VMs — making hypervisor security critically important.

## Key Details

- Apply all vendor patches promptly — hypervisor vulnerabilities are high-value targets
- Disable all unnecessary hypervisor services, features, and hardware pass-through capabilities
- Restrict management access: use dedicated management networks and strong authentication
- Enable Secure Boot to verify hypervisor firmware integrity at startup
- Minimize the hypervisor's attack surface by not running unrelated services on the hypervisor host

## Connections

- Parent: [[virtualization-security]] — hypervisor hardening is the foundation of virtualization security
- See also: [[vm-escape]]
