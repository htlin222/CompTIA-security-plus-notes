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

> [!eli5] ELI5: What is SIEM?
> Think of a giant bulletin board in a security guard's office where every camera, door sensor, and alarm in the building reports what it sees. A SIEM is that bulletin board for computers. It collects alerts from every device across the entire network, puts them all in one place, and connects the dots. If the front door alarm and a camera alert happen at the same time, the SIEM figures out they are probably related and warns the security team.
>
> > [!eli5] ELI5: SIEM (繁體中文版)
> > SIEM 就像是公司的總控中心。它會收集所有監視器 (日誌) 的畫面，一旦發現哪裡有小偷，就會立刻發出警報。
> >
> > ```ascii
> > [日誌 A/B/C] --(彙整)--> |SIEM 控制台| --(警報)--> [管理員]
> > ```

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
- **[[syslog|Syslog]]**: Standard protocol for forwarding log messages (UDP 514, TCP 514, or TLS 6514)
- **[[syslog-severity-levels|Syslog severity levels]]**: 0=Emergency, 1=Alert, 2=Critical, 3=Error, 4=Warning, 5=Notice, 6=Info, 7=Debug
- **[[journalctl|journalctl]]**: Linux command for querying systemd journal logs

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

## Practice Questions

> [!qbank]- Q-Bank: SIEM (4 Questions)
>
> **Q1.** A SOC team deploys a new SIEM platform but within the first week, analysts are overwhelmed by thousands of alerts per day, most of which turn out to be benign. What is the MOST likely cause and the BEST remediation?
>
> A. The SIEM hardware is undersized and needs more memory
> B. The correlation rules need tuning to reduce false positives and alert fatigue
> C. The SIEM should be replaced with an EDR solution
> D. The SOC team needs to hire more Tier 1 analysts
>
> > [!answer]- Show Answer
> > **B. The correlation rules need tuning to reduce false positives and alert fatigue**
> >
> > [[correlation-rules]] must be tuned to match the organization's environment to minimize false positives. A SIEM is only effective when alerts are meaningful and actionable. Option A may help with performance but does not address alert accuracy. Option C replaces detection scope (SIEM covers all sources; EDR covers endpoints only). Option D adds headcount but does not fix the root cause of excessive false alerts.
>
> **Q2.** An organization collects logs from firewalls, Windows servers, Linux servers, and cloud applications. Each source uses a different log format. What SIEM function ensures these disparate logs can be searched and correlated effectively?
>
> A. Log retention and archival
> B. Normalization
> C. Real-time alerting
> D. Dashboard visualization
>
> > [!answer]- Show Answer
> > **B. Normalization**
> >
> > [[normalization]] converts logs from different sources and formats into a common schema, enabling the SIEM to search, compare, and correlate events across all sources effectively. Option A governs how long logs are stored, not how they are formatted. Option C triggers notifications based on rules but requires normalized data to function. Option D presents data visually but depends on normalized data underneath.
>
> **Q3.** A SIEM correlation rule detects the following sequence: five failed login attempts on a domain controller from one IP, followed by a successful login from the same IP, followed by an unusual file download from a sensitive file server within 10 minutes. This type of detection is BEST described as:
>
> A. Signature-based antivirus detection
> B. Multi-event correlation across log sources
> C. Vulnerability scanning
> D. Network bandwidth monitoring
>
> > [!answer]- Show Answer
> > **B. Multi-event correlation across log sources**
> >
> > [[correlation-rules]] in a SIEM connect events from multiple sources (authentication logs, file server logs) across time to detect attack patterns that no single log source would reveal alone. Option A matches known malware signatures on endpoints, not cross-source event patterns. Option C identifies system weaknesses, not active attack sequences. Option D measures traffic volume, not authentication and access patterns.
>
> **Q4.** A SIEM platform uses machine learning to establish behavioral baselines for each user and alerts when a user accesses systems they have never accessed before at an unusual time. What is this capability called?
>
> A. Vulnerability assessment
> B. User and Entity Behavior Analytics (UEBA)
> C. Data loss prevention
> D. Patch management
>
> > [!answer]- Show Answer
> > **B. User and Entity Behavior Analytics (UEBA)**
> >
> > [[user-and-entity-behavior-analytics-ueba|UEBA]] uses machine learning to baseline normal user and entity behavior and detect anomalies such as unusual access patterns, times, or volumes. Option A identifies system weaknesses, not behavioral anomalies. Option C monitors for sensitive data leaving the organization. Option D manages software updates and is unrelated to behavioral analysis.

## Scenario

> See [[case-siem]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [4.4 – Security Tools](https://www.youtube.com/watch?v=nNiNTviiacU)
