---
title: "Policy administrator"
description: "Establishes and removes communication paths based on policy engine decisions in Zero Trust"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

In NIST's Zero Trust Architecture (ZTA), the policy administrator is the component responsible for establishing, configuring, and shutting down the communication paths between subjects (users/devices) and enterprise resources. It acts on decisions made by the policy engine—translating access decisions into concrete actions that enable or block communication, such as issuing session tokens or configuring network paths.

## Key Details

- Works in conjunction with the **policy engine** (which makes access decisions) and the **policy enforcement point** (which enforces them).
- Functions include: generating authentication tokens, configuring session keys, and commanding network infrastructure to establish or terminate connections.
- Can be thought of as the **orchestrator**—turning policy engine decisions into real-time network and access configuration changes.
- In practice, often implemented via **IAM systems**, **API gateways**, and **software-defined networking** components.
- Part of the NIST SP 800-207 Zero Trust Architecture model.

## Connections

- Parent: [[zero-trust]] — a core component of the Zero Trust architecture model
- See also: [[policy-engine]], [[policy-enforcement-point-pep]]
