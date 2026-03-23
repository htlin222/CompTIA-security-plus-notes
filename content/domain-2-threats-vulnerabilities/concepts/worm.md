---
title: "Worm"
description: "Self-replicating malware that spreads across networks without user interaction"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Worm?
> Unlike a virus, a worm doesn't need you to do anything. It crawls from computer to computer all by itself through the network, like a real worm tunneling through the ground from garden to garden.

## Definition

A worm is self-replicating malware that propagates across networks autonomously—without requiring a host file or user interaction to spread. Worms exploit network vulnerabilities, open shares, or other network connectivity to copy themselves to new systems, often causing significant network performance degradation simply through the volume of their propagation traffic, in addition to whatever malicious payload they carry.

## Key Details

- **Key distinction from viruses**: Worms spread autonomously through networks; viruses require infected files to be shared and executed.
- Famous worms: **Morris Worm (1988)**—first major internet worm; **Code Red (2001)**—web server worm exploiting IIS; **WannaCry (2017)**—ransomware worm using EternalBlue SMB exploit; **Slammer (2003)**—fastest spreading worm ever.
- **Propagation vectors**: Network service exploits (SMB, RDP), email (self-mailing), network shares, removable media.
- **Payload**: Some worms are purely for propagation; others deliver ransomware, backdoors, or serve as DoS agents.
- **Defense**: **Patching** (most worms exploit known vulnerabilities), **network segmentation**, **firewall rules** blocking worm propagation ports.

## Connections

- Parent: [[malware-types]] — autonomous network-propagating malware
- See also: [[virus], [[botnet]]
