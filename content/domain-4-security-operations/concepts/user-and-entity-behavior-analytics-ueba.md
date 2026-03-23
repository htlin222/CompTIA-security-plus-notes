---
title: "User and Entity Behavior Analytics (UEBA)"
description: "uses ML to baseline normal user/entity behavior and detect anomalies indicating insider threats or compromise"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - UEBA
---

## Definition

User and Entity Behavior Analytics (UEBA) is a security analytics capability that uses machine learning and statistical modeling to establish baselines of normal behavior for users, devices, applications, and other entities within an environment. UEBA then detects deviations from these baselines that may indicate insider threats, compromised accounts, data exfiltration, or lateral movement — threats that often evade rule-based detection because they don't match known attack signatures.

## Key Details

- Analyzes logs from AD, VPN, email, endpoint, cloud, and other sources to build behavioral profiles
- Detects insider threats: unusual access patterns, after-hours activity, bulk data downloads
- Identifies compromised accounts: impossible travel, credential stuffing, privilege escalation anomalies
- Reduces alert fatigue compared to rule-based SIEM by focusing on contextual anomalies with risk scoring
- Often integrated into SIEM platforms (Microsoft Sentinel, Splunk) or as standalone products

## Connections

- Parent: [[siem]] — UEBA extends SIEM capabilities with behavioral analytics and ML-based anomaly detection
- See also: [[behavioral-analysis]], [[threat-hunting]], [[telemetry-correlation-xdr]], [[continuous-monitoring]]
