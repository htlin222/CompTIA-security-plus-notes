---
title: "Root cause analysis"
description: "EDR tools trace the full attack chain from initial access to impact"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Root Cause Analysis?
> Root cause analysis keeps asking "why" until you find the real reason something went wrong. The server crashed -- why? It ran out of memory -- why? A program had a bug. Now you fix the bug.

## Definition

Root cause analysis in EDR/XDR is the process of tracing an attack or security incident back through the complete chain of events to identify the original entry point and the sequence of actions that led to the observed impact. EDR platforms provide the telemetry and visualization tools needed to reconstruct attack chains from initial access through lateral movement to the final impact.

## Key Details

- EDR attack tree visualizations show the complete process hierarchy from initial execution to final impact
- Identifies: initial infection vector, persistence mechanism, privilege escalation path, lateral movement methods, impact
- Enables complete remediation — without root cause analysis, remnants of the attack may be missed
- Process trees show parent-child process relationships that reveal malicious activity patterns
- Root cause analysis informs detection improvements — new detection rules to catch the same technique earlier

## Connections

- Parent: [[edr-xdr]] — root cause analysis is a key capability provided by EDR/XDR platforms
- See also: [[timeline-analysis]]
