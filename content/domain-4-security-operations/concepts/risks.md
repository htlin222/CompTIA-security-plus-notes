---
title: "Risks"
description: "Automation of bad processes amplifies mistakes; credential management for automated tools; single point of failure"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are the Risks of Automation?
> If you teach a robot to do something wrong, it will do that wrong thing really fast, over and over. Automation risks are the bad things that happen when nobody double-checks the robot's instructions.

## Definition

Security automation introduces unique risks that must be carefully managed to prevent the automation itself from becoming a security liability. These risks include the amplification of incorrect processes, the challenge of securely managing credentials used by automated tools, and the creation of single points of failure in the security operation when automation is unavailable.

## Key Details

- **Amplification of mistakes**: automation at scale makes wrong decisions faster and at greater volume than humans would
- **Credential management**: automated tools need credentials to act; these must be secured, rotated, and monitored
- **Single point of failure**: if the SOAR platform is down, automated responses stop — need manual backup procedures
- **Unintended consequences**: automated actions (blocking, disabling accounts) must be carefully scoped to avoid business disruption
- **Testing gaps**: automation may work in test environments but fail subtly in production in ways not immediately detected

## Connections

- Parent: [[automation-and-scripting]] — these risks must be managed when implementing security automation
- See also: [[guardrails]]
