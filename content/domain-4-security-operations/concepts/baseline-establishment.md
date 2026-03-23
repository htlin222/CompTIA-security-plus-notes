---
title: "Baseline establishment"
description: "Defining normal network behavior to identify deviations and anomalies"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Baseline establishment is the process of documenting and quantifying normal operational parameters for network traffic, system behavior, and user activity so that security tools and analysts have a reference point for detecting anomalies. A well-defined baseline is foundational to anomaly-based detection systems and threat hunting, as it defines what "normal" looks like in a specific environment.

## Key Details

- Baselines capture metrics such as typical bandwidth, common protocols, normal login times, and expected processes
- Must be established during a representative period of normal operations
- Used by SIEM, IDS/IPS, UEBA, and network monitoring tools for anomaly detection
- Baselines must be updated when the environment changes significantly
- Without a good baseline, anomaly detection produces excessive false positives

## Connections

- Parent: [[network-monitoring]] — baseline establishment enables anomaly-based network monitoring
- See also: [[user-and-entity-behavior-analytics-ueba]]
