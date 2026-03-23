---
title: "Baseline-driven hunting"
description: "Identifying deviations from known-good baselines in network traffic, process execution, or user behavior"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Baseline-driven Hunting?
> You know what your neighborhood normally looks like. If a strange car suddenly parks there every day, you notice. Baseline-driven hunting means knowing what "normal" looks like so you can spot anything weird.

## Definition

Baseline-driven hunting is a threat hunting methodology that starts by establishing a well-understood "normal" state for systems, networks, and users, then actively searches for deviations from that baseline. By knowing what normal looks like, analysts can identify anomalies that may indicate attacker activity, even when no signature match or alert has been triggered.

## Key Details

- Requires a robust baseline of normal behavior — processes, network flows, user activity
- Deviations from baseline trigger investigation, not just known-bad signatures
- Effective at finding living-off-the-land attacks that blend with normal tools
- Complements signature-based detection by catching novel techniques
- Baselines must be regularly updated as the environment evolves

## Connections

- Parent: [[threat-hunting]] — baseline-driven hunting is a primary hunting methodology
- See also: [[behavioral-analysis]]
