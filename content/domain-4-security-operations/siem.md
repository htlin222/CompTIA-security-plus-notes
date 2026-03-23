---
title: "Security Information and Event Management"
description: "Centralized platform for collecting, correlating, and analyzing security events across an organization"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/incident
  - weight/high
aliases:
  - "SIEM"
---

## Overview

Security Information and Event Management (SIEM) combines Security Information Management (SIM) and Security Event Management (SEM) into a single platform. SIEM collects log data from across the organization, normalizes it, correlates events, and generates alerts for potential security incidents. It is the central nervous system of a security operations center (SOC).

## Key Concepts

- **[[log-aggregation|Log aggregation]]**: Collecting logs from firewalls, servers, endpoints, applications, and cloud services into one platform
- **[[normalization|Normalization]]**: Converting logs from different formats into a common schema for analysis
- **[[correlation-rules|Correlation rules]]**: Logic that identifies patterns across multiple events that indicate an attack (e.g., failed logins followed by successful login from new IP)
- **[[real-time-alerting|Real-time alerting]]**: Immediate notification when correlation rules or thresholds are triggered
- **[[dashboards-and-reporting|Dashboards and reporting]]**: Visual representation of security posture, trends, and compliance metrics
- **[[retention-and-archival|Retention and archival]]**: Storing log data for compliance requirements and forensic investigations
- **[[user-and-entity-behavior-analytics-ueba|User and Entity Behavior Analytics (UEBA)]]**: Machine learning that baselines normal behavior and detects anomalies
- **[[common-siem-platforms|Common SIEM platforms]]**: Splunk, Microsoft Sentinel, IBM QRadar, Elastic Security

## Exam Tips

> [!tip] Remember
> SIEM = Collect, Correlate, Alert. It does NOT block attacks — it detects and notifies. For automated response, you need [[soar]]. Think of SIEM as the "security dashboard" that watches everything.

- SIEM is useless without proper tuning — too many false positives cause alert fatigue
- Know the difference: SIEM detects, SOAR responds, EDR focuses on endpoints
- Log sources for SIEM: firewalls, IDS/IPS, OS logs, application logs, authentication logs

## Connections

- Ingests data from [[ids-ips]] to correlate network-level events with other security telemetry
- Detects [[indicators-of-compromise]] by matching log patterns against known threat signatures
- Supports [[compliance]] requirements by providing audit trails and retention of security logs
- Enhanced by [[soar]] to automate incident response workflows triggered by SIEM alerts
- Relies on [[log-management]] for proper collection and forwarding of source data

## Scenario

> See [[case-siem]] for a practical DevOps scenario applying these concepts.
