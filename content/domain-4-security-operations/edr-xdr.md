---
title: "Endpoint Detection and Response / Extended Detection and Response"
description: "Advanced security solutions that detect, investigate, and respond to threats across endpoints and beyond"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/endpoint
  - weight/high
aliases:
  - "EDR"
  - "XDR"
---

## Overview

Endpoint Detection and Response (EDR) continuously monitors endpoints to detect suspicious behavior, investigate threats, and enable rapid response. Extended Detection and Response (XDR) expands this capability beyond endpoints to include network, cloud, email, and identity telemetry in a unified platform. Both represent the evolution beyond traditional antivirus toward proactive threat detection.

## Key Concepts

- **[[behavioral-analysis|Behavioral analysis]]**: Detects threats based on anomalous behavior rather than known signatures
- **[[continuous-monitoring|Continuous monitoring]]**: Agents on endpoints record process execution, file changes, registry modifications, and network connections
- **[[threat-containment|Threat containment]]**: Ability to isolate a compromised endpoint from the network in real time
- **[[automated-response|Automated response]]**: Predefined playbooks can kill processes, quarantine files, or block IPs without human intervention
- **[[root-cause-analysis|Root cause analysis]]**: EDR tools trace the full attack chain from initial access to impact
- **[[telemetry-correlation-xdr|Telemetry correlation (XDR)]]**: Combines data from endpoints, network, cloud, and email to detect multi-vector attacks
- **[[threat-intelligence-integration|Threat intelligence integration]]**: EDR/XDR platforms cross-reference activity with known threat indicators
- **[[fileless-malware-detection|Fileless malware detection]]**: Identifies threats that operate in memory without writing to disk

## Exam Tips

> [!tip] Remember
> EDR = endpoints only. XDR = everything (endpoints + network + cloud + email). Both go beyond signatures to use behavioral analytics. EDR is to antivirus what a security camera system is to a door lock.

- EDR provides visibility into HOW an attack happened, not just THAT it happened
- XDR reduces alert fatigue by correlating events across multiple security layers
- Know that EDR requires an agent installed on each endpoint

## Connections

- Extends the capabilities of [[endpoint-security]] from prevention to detection and response
- Feeds critical data into [[siem]] for centralized security event correlation
- Supports [[threat-hunting]] by providing the telemetry analysts need to proactively search for threats
- Works alongside [[incident-response]] to enable rapid containment and remediation

## Scenario

> See [[case-edr-xdr]] for a practical DevOps scenario applying these concepts.
