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

## Exam Tips

> [!tip] Remember
> Zero trust = "never trust, always verify." The exam heavily tests zero trust concepts including the control plane (decision-making) and data plane (enforcement). Implicit deny is the default firewall rule.

## Connections

- Implemented through [[firewalls]], [[ids-ips]], and [[network-segmentation]] as core architectural components
- Zero trust principles extend into [[cloud-security]] where perimeter-based models are insufficient
- See also [[vpn]] for secure remote access as part of the network architecture

## Scenario

> See [[case-network-security-architecture]] for a practical DevOps scenario applying these concepts.
