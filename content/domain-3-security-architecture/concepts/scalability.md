---
title: "Scalability"
description: "vertical (scale up: more resources) vs. horizontal (scale out: more instances)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Scalability is the ability of a system to handle increased workload by adding resources. In security architecture, scalability is important for availability — systems that cannot scale to meet demand become unavailable under load. Cloud environments enable dynamic scalability that was previously difficult to achieve on-premises.

## Key Details

- **Vertical scaling (scale up)**: adding more resources (CPU, RAM) to an existing server; has hardware limits; can cause downtime
- **Horizontal scaling (scale out)**: adding more server instances; requires load balancing; theoretically unlimited; preferred for cloud-native architectures
- Cloud auto-scaling groups automatically add or remove instances based on demand metrics
- Horizontal scaling is inherently more resilient — no single point of failure
- DDoS attacks can overwhelm scalability — cloud-based DDoS mitigation services can absorb massive traffic volumes

## Connections

- Parent: [[resilience-and-redundancy]] — scalability is a key component of resilient architecture design
- See also: [[capacity-planning]]
