---
title: "IDS/IPS"
description: "Intrusion Detection and Prevention Systems monitor network traffic and system activity to identify and respond to malicious behavior."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/high
aliases:
  - "IDS"
  - "IPS"
---

## Overview

Intrusion Detection Systems (IDS) monitor network traffic or host activity to identify suspicious behavior and generate alerts. Intrusion Prevention Systems (IPS) go further by actively blocking detected threats in real time. Both use signature-based, anomaly-based, or heuristic detection methods. IDS/IPS are critical components of a defense-in-depth strategy.

## Key Concepts

- **IDS vs. IPS:**
  - **IDS** — passive; detects and alerts; does not block traffic
  - **IPS** — inline; detects and blocks malicious traffic automatically
- **Deployment:**
  - **Network-based (NIDS/NIPS)** — monitors traffic on a network segment; uses span ports or taps
  - **Host-based (HIDS/HIPS)** — monitors activity on a single host; examines logs, file integrity, system calls
- **Detection methods:**
  - **Signature-based** — matches traffic against known attack patterns; fast, low false positives; cannot detect zero-days
  - **Anomaly-based (behavioral)** — establishes a baseline of normal activity; detects deviations; higher false positives but catches novel attacks
  - **Heuristic** — uses rules and algorithms to identify potentially malicious behavior
- **Alert types:**
  - **True positive** — correctly identified an attack
  - **False positive** — alert triggered by normal activity (most common operational issue)
  - **True negative** — correctly identified normal traffic
  - **False negative** — missed an actual attack (most dangerous)
- **[[tuning|Tuning]]** — adjusting sensitivity and rules to reduce false positives without increasing false negatives
- **[[inline-vs-passive-deployment|Inline vs. passive deployment]]** — IPS must be inline to block; IDS can be passive via port mirroring

## Exam Tips

> [!tip] Remember
> IDS = detect and alert (passive). IPS = detect and block (inline/active). Signature-based catches known threats; anomaly-based catches unknown threats. False negative = worst outcome (attack goes undetected).

## Connections

- Provides detection data to [[siem]] systems for correlation and analysis across the environment
- Complements [[firewalls]] by inspecting allowed traffic for malicious content
- Related to [[indicators-of-compromise]] which define the patterns IDS/IPS use for detection

## Scenario

> See [[case-ids-ips]] for a practical DevOps scenario applying these concepts.
