---
title: "Network Security Architecture"
description: "Network security architecture defines the design principles and components used to protect an organization's network infrastructure."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/high
aliases:
  - "Network Security Architecture"
---

> [!eli5] ELI5: What is Network Security Architecture?
> Think of a castle with walls, a moat, drawbridges, and guards at every gate. Network security architecture is like the blueprint for building all those defenses around a computer network. It plans where the walls go, who guards each entrance, and how to keep intruders from moving around inside if they do get in. The idea is that no single defense has to be perfect, because there are many layers backing it up.

## Overview

Network security architecture is the design and structure of network defenses that protect data, systems, and communications from unauthorized access and attack. It applies defense-in-depth principles by layering multiple security controls throughout the network. A well-designed architecture accounts for both north-south traffic (entering/leaving the network) and east-west traffic (lateral movement within the network).

## Key Concepts

- **[[defense-in-depth|Defense in depth]]** — layered security controls so that if one fails, others still protect the environment
- **[[zero-trust-architecture|Zero trust architecture]]** — never trust, always verify; authenticate and authorize every access request regardless of location
  - **Control plane** — policy engine and policy administrator that make access decisions
  - **Data plane** — policy enforcement point that allows or blocks traffic based on decisions
- **[[network-zones|Network zones]]** — segments with different trust levels (DMZ, internal, guest, management)
- **[[dmz-demilitarized-zone|DMZ (Demilitarized Zone)]]** — screened subnet between the internet and internal network for public-facing services
- **[[east-west-vs-north-south-traffic|East-west vs. north-south traffic]]** — east-west is internal lateral; north-south crosses the network boundary
- **[[software-defined-networking-sdn|Software-Defined Networking (SDN)]]** — programmatic control of network infrastructure; separates control plane from data plane
- **[[secure-access-service-edge-sase|Secure Access Service Edge (SASE)]]** — cloud-delivered convergence of network and security services
- **[[micro-segmentation|Micro-segmentation]]** — granular segmentation within a network, often at the workload level
- **[[implicit-deny|Implicit deny]]** — the default stance; all traffic is blocked unless explicitly allowed
- **[[ssltls-offloading|SSL/TLS offloading]]** — terminating encrypted connections at a load balancer or proxy to reduce backend server load
- **Broadcast storm prevention** — loop protection and BPDU guard on switches to prevent network loops
- **DHCP snooping** — switch feature that filters untrusted DHCP messages to prevent rogue DHCP servers
- **[[unified-threat-management-utm|UTM (Unified Threat Management)]]** — single appliance combining firewall, IDS/IPS, antivirus, content filtering, and VPN

## Exam Tips

> [!tip] Remember
> Zero trust = "never trust, always verify." The exam heavily tests zero trust concepts including the control plane (decision-making) and data plane (enforcement). Implicit deny is the default firewall rule.

## Connections

- Implemented through [[firewalls]], [[ids-ips]], and [[network-segmentation]] as core architectural components
- Zero trust principles extend into [[cloud-security]] where perimeter-based models are insufficient
- See also [[vpn]] for secure remote access as part of the network architecture

## Practice Questions

> [!qbank]- Q-Bank: Network Security Architecture (4 Questions)
>
> **Q1.** An organization implements a security model where every access request is authenticated and authorized, regardless of whether the request originates from inside or outside the corporate network. Which architecture does this describe?
>
> A. Defense in depth
> B. Zero trust architecture
> C. Screened subnet (DMZ)
> D. Software-defined networking
>
> > [!answer]- Show Answer
> > **B. Zero trust architecture**
> >
> > [[zero-trust-architecture|Zero trust]] follows the principle of "never trust, always verify" — every access request must be authenticated and authorized regardless of network location. Defense in depth (A) layers multiple controls but does not inherently require verification of every request. A DMZ (C) is a specific network zone, not an access philosophy. SDN (D) is a network management approach that separates control and data planes but does not define trust policy.
>
> **Q2.** In a zero trust architecture, the policy engine decides whether to grant access and the policy enforcement point blocks or allows traffic. Which planes do these components belong to, respectively?
>
> A. Data plane and control plane
> B. Control plane and data plane
> C. Management plane and data plane
> D. Control plane and management plane
>
> > [!answer]- Show Answer
> > **B. Control plane and data plane**
> >
> > In [[zero-trust-architecture|zero trust architecture]], the policy engine and policy administrator reside in the control plane (making access decisions), while the policy enforcement point resides in the data plane (enforcing those decisions on actual traffic). The reverse (A) is incorrect. The management plane (C, D) relates to network device administration, not zero trust access decisions.
>
> **Q3.** A company places its public web servers in a network zone between two firewalls — one facing the internet and one facing the internal network. Which architecture component does this describe?
>
> A. Micro-segmentation
> B. SASE (Secure Access Service Edge)
> C. DMZ (Demilitarized Zone) / screened subnet
> D. Software-defined networking
>
> > [!answer]- Show Answer
> > **C. DMZ (Demilitarized Zone) / screened subnet**
> >
> > A [[dmz-demilitarized-zone|DMZ or screened subnet]] is a buffer zone between the internet and internal network, typically separated by two firewalls, where public-facing services are placed. Micro-segmentation (A) provides granular workload-level isolation, not a perimeter zone between two firewalls. SASE (B) is a cloud-delivered security service model. SDN (D) is a network management architecture, not a specific zone design.
>
> **Q4.** A network architect wants to ensure that a breach in one part of the network cannot easily spread to other areas. The design should include multiple overlapping security controls at different layers. Which principle BEST describes this approach?
>
> A. Single point of failure elimination
> B. Defense in depth
> C. Implicit allow
> D. Split tunneling
>
> > [!answer]- Show Answer
> > **B. Defense in depth**
> >
> > [[defense-in-depth|Defense in depth]] layers multiple security controls so that if one fails, others still protect the environment, limiting breach propagation. Single point of failure elimination (A) addresses availability and redundancy, not layered security controls. Implicit allow (C) is the opposite of secure design — the correct stance is [[implicit-deny|implicit deny]]. Split tunneling (D) is a VPN configuration, not a network security design principle.

## Scenario

> See [[case-network-security-architecture]] for a practical DevOps scenario applying these concepts.
