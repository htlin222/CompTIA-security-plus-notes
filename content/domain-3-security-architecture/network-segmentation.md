---
title: "Network Segmentation"
description: "Network segmentation divides a network into isolated zones to limit lateral movement, contain breaches, and enforce access controls."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/high
aliases:
  - "Network Segmentation"
---

> [!eli5] ELI5: What is Network Segmentation?
> You know how a submarine has separate compartments with heavy doors? If water floods one room, the doors keep it from spreading to the rest of the submarine. Network segmentation works the same way -- it divides a big network into smaller sections with barriers between them. If a hacker breaks into one section, they cannot easily reach everything else. It limits the damage.

## Overview

Network segmentation is the practice of dividing a network into smaller, isolated segments or subnets, each with its own security controls and access policies. Segmentation limits the blast radius of a breach by preventing attackers from moving laterally across the entire network. It is a foundational element of zero trust architecture and defense in depth.

## Key Concepts

- **[[physical-segmentation|Physical segmentation]]** — separate physical network infrastructure for different zones
- **[[logical-segmentation|Logical segmentation]]** — VLANs, subnets, and software-defined boundaries on shared infrastructure
- **[[vlans-virtual-lans|VLANs (Virtual LANs)]]** — logically separate broadcast domains on a single switch; require a router or Layer 3 switch to communicate between VLANs
- **[[micro-segmentation|Micro-segmentation]]** — granular, workload-level segmentation typically implemented in virtualized or cloud environments
- **Common network zones:**
  - **DMZ / screened subnet** — public-facing services isolated from internal network
  - **Internal / trusted zone** — corporate resources and users
  - **Guest network** — isolated network for visitors; no access to internal resources
  - **Management network** — dedicated segment for network device administration
  - **IoT / OT network** — isolated segment for Internet of Things and operational technology devices
- **[[air-gap|Air gap]]** — complete physical isolation with no network connectivity; highest security, used for critical systems
- **[[jumpbox-jump-server|Jumpbox / jump server]]** — hardened system used to access management networks securely
- **[[east-west-traffic-control|East-west traffic control]]** — segmentation is essential for monitoring and controlling internal lateral movement

## Exam Tips

> [!tip] Remember
> VLANs provide logical segmentation but are not a security boundary by themselves — you still need ACLs or firewalls between VLANs. Air gap = most secure isolation. Micro-segmentation = zero trust at the workload level.

## Connections

- Enforced by [[firewalls]] and ACLs that control traffic between segments
- Core principle in [[network-security-architecture]] and zero trust design
- See also [[nac]] for controlling which devices are allowed onto each network segment

## Scenario

> See [[case-network-segmentation]] for a practical DevOps scenario applying these concepts.
