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

> [!eli5] ELI5: What is IDS/IPS?
> Think of IDS like a security camera that watches everything and sounds an alarm when it spots trouble. IPS is like a security camera plus a guard -- it does not just alert you, it actually stops the bad guy in their tracks. Together, they watch all the activity on a computer network, looking for anything suspicious, and either warn someone or block the threat right away.

> [!eli5] ELI5: IDS/IPS (繁體中文版)
> IDS 是警報器，發現有人翻牆就大叫；IPS 是守衛，發現有人翻牆會直接把他抓起來丟出去。
>
> ```ascii
> [流量] --> |IDS: 警報| / |IPS: 阻擋|
> ```

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
- **[[file-integrity-monitoring|FIM (File Integrity Monitoring)]]** — detects unauthorized changes to critical system files

## Exam Tips

> [!tip] Remember
> IDS = detect and alert (passive). IPS = detect and block (inline/active). Signature-based catches known threats; anomaly-based catches unknown threats. False negative = worst outcome (attack goes undetected).

## Connections

- Provides detection data to [[siem]] systems for correlation and analysis across the environment
- Complements [[firewalls]] by inspecting allowed traffic for malicious content
- Related to [[indicators-of-compromise]] which define the patterns IDS/IPS use for detection

## Practice Questions

> [!qbank]- Q-Bank: IDS/IPS (4 Questions)
>
> **Q1.** A company wants to automatically block malicious traffic in real time without requiring manual intervention from analysts. Which solution BEST meets this requirement?
>
> A. Network-based IDS (NIDS)
> B. Network-based IPS (NIPS)
> C. Host-based IDS (HIDS)
> D. SIEM system
>
> > [!answer]- Show Answer
> > **B. Network-based IPS (NIPS)**
> >
> > An [[ids-ips|IPS]] is deployed inline and can automatically block malicious traffic in real time. NIDS (A) detects and alerts but does not block traffic since it operates passively. HIDS (C) monitors individual hosts, not network traffic, and also only alerts. A SIEM (D) correlates and analyzes logs but does not directly block traffic.
>
> **Q2.** A newly deployed anomaly-based IDS is generating a large number of alerts for normal business activities. Which term BEST describes these alerts?
>
> A. True positives
> B. False positives
> C. True negatives
> D. False negatives
>
> > [!answer]- Show Answer
> > **B. False positives**
> >
> > [[ids-ips|False positives]] occur when normal activity is incorrectly flagged as malicious. Anomaly-based systems are particularly prone to this when baselines are not properly established. True positives (A) are correctly identified attacks. True negatives (C) are correctly identified normal traffic. False negatives (D) are missed attacks, which is the most dangerous outcome but not what is described here.
>
> **Q3.** A security team wants to detect a novel zero-day attack that has no known signature. Which IDS detection method is MOST likely to identify this threat?
>
> A. Signature-based detection
> B. Anomaly-based (behavioral) detection
> C. Pattern matching
> D. Checksum verification
>
> > [!answer]- Show Answer
> > **B. Anomaly-based (behavioral) detection**
> >
> > [[ids-ips|Anomaly-based detection]] establishes a baseline of normal behavior and flags deviations, making it capable of detecting previously unknown (zero-day) attacks. Signature-based detection (A) requires known attack patterns and cannot detect zero-days. Pattern matching (C) is a form of signature-based detection with the same limitation. Checksum verification (D) checks file integrity, not network traffic behavior.
>
> **Q4.** A network engineer needs to deploy an IDS that monitors traffic on a network segment. The IDS should receive copies of all traffic without being in the direct traffic path. Which deployment method is MOST appropriate?
>
> A. Deploy the IDS inline between the firewall and switch
> B. Connect the IDS to a span port (port mirror) on the switch
> C. Install the IDS as a host-based agent on each server
> D. Deploy the IDS as a transparent bridge
>
> > [!answer]- Show Answer
> > **B. Connect the IDS to a span port (port mirror) on the switch**
> >
> > An [[ids-ips|IDS operates passively]] and receives copies of traffic via span ports or network taps without being in the direct traffic path. Deploying inline (A) is how an IPS is deployed, not an IDS. Host-based agents (C) create HIDS, not NIDS for network segment monitoring. A transparent bridge (D) is an inline deployment method more suitable for IPS.

## Scenario

> See [[case-ids-ips]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [3.2 – Intrusion Prevention](https://www.youtube.com/watch?v=7QuYupuic3Q)
