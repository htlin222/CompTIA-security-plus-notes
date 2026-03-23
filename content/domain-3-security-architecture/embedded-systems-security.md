---
title: "Embedded Systems Security"
description: "Embedded systems security addresses the unique risks of securing purpose-built devices with limited resources and long lifecycles."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/endpoint
  - weight/medium
aliases:
  - "Embedded Systems"
  - "IoT Security"
---

## Overview

Embedded systems are purpose-built computing devices designed for specific functions, including IoT devices, SCADA/ICS systems, medical devices, automotive systems, and smart appliances. These systems often have constrained resources (limited CPU, memory, storage), run real-time operating systems (RTOS), and have long operational lifecycles. Their security challenges include limited patching capabilities, weak default configurations, and lack of built-in security features.

## Key Concepts

- **Types of embedded systems:**
  - **SCADA/ICS (Supervisory Control and Data Acquisition / Industrial Control Systems)** — manage critical infrastructure (power, water, manufacturing)
  - **IoT (Internet of Things)** — connected consumer and enterprise devices (cameras, sensors, thermostats)
  - **Medical devices** — pacemakers, infusion pumps, imaging systems
  - **RTOS (Real-Time Operating System)** — optimized for time-critical operations; not designed with security in mind
  - **SoC (System on a Chip)** — entire computing system on a single chip
- **Security challenges:**
  - Limited processing power prevents running traditional security software
  - Difficult or impossible to patch; firmware updates may require physical access
  - Long lifecycles mean devices outlive vendor support
  - Default credentials often left unchanged
  - Lack of encryption due to resource constraints
  - Large attack surface when internet-connected
- **Security controls:**
  - **Network segmentation** — isolate embedded devices on dedicated network segments
  - **Firmware updates** — apply updates when available; validate integrity with digital signatures
  - **Change default credentials** — first step in securing any embedded device
  - **Disable unnecessary services and ports** — reduce the attack surface
  - **Encryption** — use lightweight cryptographic protocols where possible
  - **Physical security** — many embedded systems are in accessible locations
  - **Wrappers** — placing security controls around devices that cannot be directly secured

## Exam Tips

> [!tip] Remember
> SCADA/ICS = critical infrastructure, high impact. IoT devices have weak security defaults. Always segment embedded devices onto their own network. Change default credentials immediately. Constrained resources limit security options.

## Connections

- Must be isolated using [[network-segmentation]] to prevent lateral movement from compromised devices
- Firmware integrity relies on concepts from [[hashing]] and digital signatures
- See also [[resilience-and-redundancy]] for ensuring availability of critical embedded systems in industrial environments

## Scenario

> See [[case-embedded-systems-security]] for a practical DevOps scenario applying these concepts.
