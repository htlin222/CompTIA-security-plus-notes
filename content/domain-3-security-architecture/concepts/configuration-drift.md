---
title: "Configuration drift"
description: "when running infrastructure diverges from its defined state; IaC detects and corrects this"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Configuration drift?
> You know how a sandcastle slowly changes shape as waves wash over it? Configuration drift is when computer settings slowly change from what they are supposed to be, usually because people make small tweaks over time. Before you know it, the system looks nothing like the original plan.

## Definition

Configuration drift occurs when the actual configuration of deployed systems gradually diverges from their intended, documented, or baseline configuration state over time — typically due to manual changes, failed updates, or unauthorized modifications. IaC tools can detect drift by comparing the current state of infrastructure against the code definition, and can automatically remediate drift by re-applying the intended configuration.

## Key Details

- Drift accumulates over time when manual changes bypass the IaC workflow
- Drifted systems may have security controls disabled or misconfigured without being noticed
- IaC tools like Terraform detect drift with state reconciliation (terraform plan)
- Configuration management tools (Ansible, Puppet, Chef) enforce desired state continuously
- Detecting and correcting drift is a key security benefit of adopting IaC practices

## Connections

- Parent: [[infrastructure-as-code]] — configuration drift is a key problem that IaC solves
- See also: [[immutable-infrastructure]]
