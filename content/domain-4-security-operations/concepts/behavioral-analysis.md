---
title: "Behavioral analysis"
description: "Detects threats based on anomalous behavior rather than known signatures"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Behavioral Analysis?
> Instead of checking if someone has a known bad face, behavioral analysis watches how they act. If someone who normally walks slowly suddenly starts running, that is suspicious even if you have never seen them before.

## Definition

Behavioral analysis is a detection approach used by EDR, XDR, and UEBA platforms that identifies threats by monitoring and evaluating the actions and behaviors of users, processes, and systems rather than relying on signatures of known malware. This allows detection of zero-day threats, fileless malware, and insider threats that have no matching signatures.

## Key Details

- Monitors process behaviors: spawning of child processes, network connections, file modifications
- Can detect "living off the land" (LotL) attacks that misuse legitimate system tools
- Machine learning algorithms identify statistical deviations from established behavior baselines
- Produces more false positives than signature detection — requires tuning and analyst review
- Key capability of modern EDR and XDR platforms

## Connections

- Parent: [[edr-xdr]] — behavioral analysis is a core detection method in EDR/XDR
- See also: [[user-and-entity-behavior-analytics-ueba]]
