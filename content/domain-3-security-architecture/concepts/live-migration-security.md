---
title: "Live migration security"
description: "encrypting VM data during migration between hosts to prevent interception"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Live migration security?
> When you move a goldfish from one tank to another while it is still swimming, you need to make sure nobody can grab it during the transfer. Live migration security protects virtual computers while they are being moved between physical machines.

## Definition

Live migration security refers to the protection of virtual machine data as it is moved between physical host servers while the VM continues to run, a process common in virtualized and cloud environments for load balancing and maintenance. During migration, VM memory contents (which may include sensitive data) traverse the network — encryption of this migration traffic is essential to prevent interception.

## Key Details

- VM memory is transferred over the network during live migration — contains sensitive data in plaintext if unencrypted
- Migration traffic should traverse a dedicated, isolated management network (not production)
- Encryption of migration traffic prevents interception of VM memory contents
- VMware vSphere and Hyper-V support encrypted live migration
- Migration authentication prevents unauthorized hosts from initiating or receiving migrations

## Connections

- Parent: [[virtualization-security]] — live migration security is a specific risk in virtualized environments
- See also: [[vm-isolation]]
