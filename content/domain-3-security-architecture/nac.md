---
title: "NAC"
description: "Network Access Control restricts network access to devices and users that meet security policy requirements."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/medium
aliases:
  - "NAC"
---

> [!eli5] ELI5: What is NAC?
> It's like a health check before you enter a theme park. Before you get on the rides, someone checks your ticket and makes sure you are tall enough. NAC (Network Access Control) does the same for devices joining a network -- it checks that your computer has the right updates and security software before letting you in. If your device does not pass the check, it gets sent to a waiting area until it is fixed.

## Overview

Network Access Control (NAC) is a security solution that enforces policies on devices attempting to access the network. NAC verifies that endpoints meet security requirements (patching, antivirus, configuration) before granting access. Non-compliant devices can be quarantined, given limited access, or blocked entirely. NAC is critical for managing BYOD environments and IoT devices.

## Key Concepts

- **Pre-admission vs. post-admission:**
  - **Pre-admission** — checks device compliance before allowing network access
  - **Post-admission** — monitors device behavior after access is granted and can revoke access if policy violations are detected
- **Agent-based vs. agentless:**
  - **Agent-based** — software installed on the endpoint performs health checks (persistent or dissolvable agent)
  - **Agentless** — NAC scans the device remotely; less intrusive but less thorough
- **Health checks (posture assessment):**
  - Antivirus up to date
  - OS patches applied
  - Firewall enabled
  - Disk encryption active
  - No prohibited software installed
- **[[8021x|802.1X]]** — IEEE standard for port-based network access control; uses EAP for authentication
  - **Supplicant** — the client device requesting access
  - **Authenticator** — the switch or access point enforcing policy
  - **Authentication server** — RADIUS server that validates credentials
- **[[remediation-network|Remediation network]]** — quarantine VLAN where non-compliant devices are placed to receive updates
- **[[guest-networking|Guest networking]]** — NAC can direct unknown or personal devices to an isolated guest network

## Exam Tips

> [!tip] Remember
> 802.1X has three components: supplicant (client), authenticator (switch/AP), authentication server (RADIUS). NAC quarantines non-compliant devices rather than outright blocking them, allowing remediation. Agent-based is more thorough than agentless.

## Connections

- Enforces access to segments created by [[network-segmentation]] by controlling which devices enter each zone
- Uses [[firewalls]] and VLAN assignments to quarantine or restrict non-compliant devices
- See also [[network-security-architecture]] for how NAC fits into a zero trust model

## Scenario

> See [[case-nac]] for a practical DevOps scenario applying these concepts.
