---
title: "Jumpbox / jump server"
description: "hardened system used to access management networks securely"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

A jumpbox (also called a jump server or bastion host) is a hardened, highly monitored system that serves as the single authorized entry point for administrative access to systems in a secure or isolated network segment. Administrators must first authenticate to the jumpbox before they can access any other systems in the management network, creating a single, auditable chokepoint for privileged access.

## Key Details

- Forces all administrative traffic through a single, controlled system with full session logging
- Minimizes the attack surface: only the jumpbox is exposed rather than all managed systems
- Should be hardened: minimal services, MFA required, all sessions recorded
- Privileged Access Workstations (PAWs) extend this concept to the client side
- Jumpboxes should be on dedicated management network segments separated from production

## Connections

- Parent: [[network-segmentation]] — jumpboxes are a key tool for controlling access to segmented networks
- See also: [[session-recording]]
