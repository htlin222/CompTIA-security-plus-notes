---
title: "Attack Vectors"
description: "Pathways and methods that threat actors use to gain unauthorized access to systems"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/medium
aliases:
  - "Attack Surface"
---

## Overview

An attack vector is the path or method a threat actor uses to gain unauthorized access to a target system or network. Understanding attack vectors is crucial for identifying vulnerabilities, implementing appropriate controls, and reducing the overall attack surface. The SY0-701 exam tests the ability to recognize common vectors and recommend appropriate mitigations.

## Key Concepts

- **Message-based vectors**
  - Email — phishing, spear phishing, malicious attachments (see [[social-engineering]])
  - SMS — smishing attacks targeting mobile users
  - Instant messaging — malicious links through chat platforms
- **Image-based vectors**
  - Steganography — hiding malicious code within images
  - Malicious image files — exploiting image parser vulnerabilities
- **File-based vectors**
  - Malicious documents (macros in Office files, PDF exploits)
  - Infected removable media (USB drives)
  - Malicious software packages and updates
- **Voice-based vectors**
  - Vishing — phone-based social engineering
  - Voice deepfakes — AI-generated impersonation
- **Removable device vectors**
  - USB drop attacks — leaving infected drives for targets to find
  - Rubber Ducky — USB device that emulates a keyboard and executes payloads
- **Vulnerable software vectors**
  - Unsupported/unpatched systems, client-based vs. agentless
  - Zero-day vulnerabilities — no patch available yet
- **[[open-service-ports|Open service ports]]** — unnecessary services listening on the network
- **Supply chain vectors**
  - Compromised hardware, software, or managed service providers
  - SolarWinds-style attacks through trusted update mechanisms
- **[[human-vectors|Human vectors]]** — social engineering exploiting human psychology
- **[[attack-surface-management|Attack surface management]]** — continuously identifying and reducing exposure across all vectors

## Exam Tips

> [!tip] Remember
> The exam categorizes vectors as: **message-based, image-based, file-based, voice-based, removable device, vulnerable software, unsecure network, open service ports, default credentials, and supply chain**. Be able to identify each from a scenario.

> [!tip] Supply Chain Attacks
> These are high-weight on the SY0-701. A supply chain attack compromises a trusted vendor or software to reach the ultimate target. Think SolarWinds, Kaseya, or compromised npm packages.

## Connections

- Exploited by [[threat-actors]] based on their capabilities and motivations
- Social engineering is a major human-based attack vector (see [[social-engineering]])
- Mitigated through [[vulnerability-management]] and regular patching
- Network-based vectors defended by [[firewalls]], [[ids-ips]], and [[network-segmentation]]
- Supply chain vectors addressed through [[third-party-risk]] management programs

## Scenario

> See [[case-attack-vectors]] for a practical DevOps scenario applying these concepts.
