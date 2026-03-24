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

## Practice Questions

> [!qbank]- Q-Bank: Network Segmentation (4 Questions)
>
> **Q1.** A security engineer needs to isolate a classified research lab so it has absolutely no connectivity to any other network, including the internet. Which segmentation approach provides the HIGHEST level of isolation?
>
> A. VLAN with ACLs
> B. Micro-segmentation
> C. Air gap
> D. Screened subnet (DMZ)
>
> > [!answer]- Show Answer
> > **C. Air gap**
> >
> > An [[air-gap|air gap]] provides complete physical isolation with no network connectivity, offering the highest security level. VLANs with ACLs (A) provide logical segmentation but still have network connectivity. Micro-segmentation (B) provides granular controls within a connected network. A DMZ (D) is a buffer zone that specifically requires connectivity to both the internet and internal network.
>
> **Q2.** After a security breach, investigators discover that the attacker moved laterally from a compromised workstation to a database server on the same network. Which control would MOST effectively prevent this lateral movement in the future?
>
> A. Installing antivirus on all workstations
> B. Implementing network segmentation with firewalls between zones
> C. Upgrading to faster network switches
> D. Enabling full disk encryption on all servers
>
> > [!answer]- Show Answer
> > **B. Implementing network segmentation with firewalls between zones**
> >
> > [[network-segmentation|Network segmentation]] with firewalls between zones controls [[east-west-traffic-control|east-west (lateral) traffic]], preventing an attacker from moving between segments. Antivirus (A) may detect malware but does not prevent network-level lateral movement. Faster switches (C) improve performance but not security. Full disk encryption (D) protects data at rest but does not prevent lateral network movement.
>
> **Q3.** A network administrator creates VLANs to separate departments but does not configure any ACLs or firewall rules between them. What is the PRIMARY security concern?
>
> A. VLANs will cause excessive broadcast traffic
> B. VLANs alone are not a security boundary and inter-VLAN traffic may still be permitted
> C. VLANs prevent all communication between departments by default
> D. VLANs require physical network separation to function
>
> > [!answer]- Show Answer
> > **B. VLANs alone are not a security boundary and inter-VLAN traffic may still be permitted**
> >
> > [[vlans-virtual-lans|VLANs]] provide logical separation of broadcast domains but require ACLs or firewalls to enforce security policies between them. Without access controls, a Layer 3 switch or router can route traffic between VLANs freely. VLANs reduce broadcast traffic (A), not increase it. VLANs do not prevent all communication by default (C) — they require routing to communicate, but that routing is commonly configured. VLANs are logical, not physical (D).
>
> **Q4.** An administrator needs to securely manage network switches and routers without exposing the management interfaces to regular user traffic. Which segmentation approach is MOST appropriate?
>
> A. Placing management interfaces on a dedicated management network segment
> B. Using the same VLAN as regular user traffic with strong passwords
> C. Connecting management interfaces to the guest network
> D. Disabling management interfaces entirely
>
> > [!answer]- Show Answer
> > **A. Placing management interfaces on a dedicated management network segment**
> >
> > A dedicated [[network-segmentation|management network]] isolates administrative access to network devices, preventing regular users from reaching management interfaces. Using the same VLAN as user traffic (B) exposes management interfaces to unnecessary risk regardless of password strength. The guest network (C) is the least trusted segment and completely inappropriate for management. Disabling management interfaces (D) would make the devices unmanageable.

## Scenario

> See [[case-network-segmentation]] for a practical DevOps scenario applying these concepts.
