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

> [!eli5] ELI5: What is Embedded Systems Security?
> Think about all the smart gadgets around you -- a thermostat, a traffic light, or a medical device. These are tiny computers built to do one specific job, and most of them cannot be easily updated like your phone or laptop. Keeping these devices safe is tricky because they often run for years without anyone checking on them, and bad guys know they are easy targets. Embedded systems security is about protecting these little computers from being hacked.

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
- **FPGA (Field-Programmable Gate Array)** — reprogrammable hardware that can be customized after manufacturing
- **Zigbee** — low-power, low-data-rate wireless protocol for IoT mesh networks (home automation, industrial sensors)
- **Narrowband IoT (NB-IoT)** — cellular technology optimized for low-power, wide-area IoT connectivity
- **Baseband** — firmware that manages radio communications on mobile devices

## Exam Tips

> [!tip] Remember
> SCADA/ICS = critical infrastructure, high impact. IoT devices have weak security defaults. Always segment embedded devices onto their own network. Change default credentials immediately. Constrained resources limit security options.

## Connections

- Must be isolated using [[network-segmentation]] to prevent lateral movement from compromised devices
- Firmware integrity relies on concepts from [[hashing]] and digital signatures
- See also [[resilience-and-redundancy]] for ensuring availability of critical embedded systems in industrial environments

## Practice Questions

> [!qbank]- Q-Bank: Embedded Systems Security (4 Questions)
>
> **Q1.** A water treatment facility connects its SCADA system to the corporate network for remote monitoring. Which security control should be implemented FIRST?
>
> A. Install antivirus software on the SCADA controllers
> B. Place the SCADA system on an isolated network segment
> C. Upgrade all SCADA devices to the latest consumer-grade OS
> D. Enable remote desktop access for all operators
>
> > [!answer]- Show Answer
> > **B. Place the SCADA system on an isolated network segment**
> >
> > [[network-segmentation|Network segmentation]] is the FIRST and most critical control for [[embedded-systems-security|SCADA/ICS systems]]. Isolating these devices prevents lateral movement from the corporate network. Antivirus (A) often cannot run on resource-constrained SCADA controllers. Upgrading to consumer-grade OS (C) is impractical since SCADA systems run specialized RTOS software. Enabling remote desktop (D) increases the attack surface rather than reducing it.
>
> **Q2.** A hospital's security team discovers that several IoT medical devices are still using factory default credentials. What is the PRIMARY risk of this situation?
>
> A. The devices will consume excessive network bandwidth
> B. Attackers can easily gain unauthorized access to the devices
> C. The devices cannot receive firmware updates
> D. The devices will be incompatible with network encryption
>
> > [!answer]- Show Answer
> > **B. Attackers can easily gain unauthorized access to the devices**
> >
> > Default credentials on [[embedded-systems-security|IoT devices]] are publicly known and easily exploited, making unauthorized access the primary risk. Bandwidth consumption (A) is a performance concern, not a direct consequence of default credentials. Firmware update capability (C) is unrelated to credential configuration. Network encryption compatibility (D) is not affected by authentication credentials.
>
> **Q3.** An organization has legacy industrial sensors that cannot be updated or patched and do not support encryption. Which security approach is MOST appropriate to protect these devices?
>
> A. Replace all sensors with modern encrypted alternatives immediately
> B. Place a security wrapper around the devices and segment the network
> C. Connect the sensors directly to the internet for cloud-based monitoring
> D. Disable all network connectivity and rely on manual data collection
>
> > [!answer]- Show Answer
> > **B. Place a security wrapper around the devices and segment the network**
> >
> > [[embedded-systems-security|Wrappers]] place security controls around devices that cannot be directly secured, combined with network segmentation to limit exposure. Immediate replacement (A) may not be feasible due to cost, availability, or operational requirements. Connecting directly to the internet (C) maximizes the attack surface. Disabling connectivity (D) eliminates the monitoring capability the network provides.
>
> **Q4.** A manufacturing company is evaluating the security of its embedded control systems. Which characteristic of these systems makes them MOST difficult to secure compared to traditional IT systems?
>
> A. They use TCP/IP networking protocols
> B. They have constrained resources that prevent running standard security software
> C. They are located in climate-controlled server rooms
> D. They are managed by the IT department
>
> > [!answer]- Show Answer
> > **B. They have constrained resources that prevent running standard security software**
> >
> > [[embedded-systems-security|Embedded systems]] have limited CPU, memory, and storage, which prevents running traditional security tools like antivirus or host-based firewalls. Using TCP/IP (A) is common across both IT and embedded systems. Being in server rooms (C) is not typical of embedded systems, which are often in operational environments. Being managed by IT (D) would actually improve security; most embedded systems are managed by OT teams with less security focus.

## Scenario

> See [[case-embedded-systems-security]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [3.1 – Other Infrastructure Concepts](https://www.youtube.com/watch?v=HDiNPPrGhzE)
