---
title: "Playbooks/Runbooks"
description: "Predefined workflows that codify incident response procedures into automated steps"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Playbooks and runbooks are documented, structured workflows that define the step-by-step procedures for responding to specific types of security incidents or operational tasks. In SOAR platforms, these workflows are codified into automation that executes the steps automatically when triggered. Even when not automated, playbooks ensure consistent, repeatable responses by guiding analysts through the correct steps.

## Key Details

- **Playbooks**: define the overall incident response strategy for a scenario (e.g., ransomware response, phishing response)
- **Runbooks**: lower-level operational procedures for specific tasks within a playbook (e.g., "how to isolate an endpoint")
- Automated playbooks in SOAR execute decisions and actions without analyst intervention
- Regular review and updating of playbooks based on lessons learned is essential
- Playbooks reduce response time, ensure consistency, and enable less experienced analysts to handle complex incidents

## Connections

- Parent: [[soar]] — playbooks are the primary mechanism for encoding security automation logic
- See also: [[automation]]
