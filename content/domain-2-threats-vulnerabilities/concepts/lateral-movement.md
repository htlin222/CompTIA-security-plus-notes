---
title: "Lateral movement"
description: "Ransomware and attackers spread across the network before detonating to maximize impact"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Lateral movement refers to the techniques used by attackers after gaining initial access to a network to progressively access additional systems, escalate privileges, and position themselves for maximum impact. In the context of ransomware, attackers deliberately spread across the network—compromising as many systems as possible—before triggering encryption to ensure maximum damage and ransom leverage.

## Key Details

- Common lateral movement techniques: **Pass-the-Hash**, **Pass-the-Ticket**, **RDP (Remote Desktop Protocol)**, **PsExec**, **WMI**, **SMB exploitation**.
- **Living off the land**: Using legitimate system tools (PowerShell, WMI, RDP) for lateral movement to blend in with normal traffic.
- **Network segmentation** and **microsegmentation** are the primary defenses—limit an attacker's ability to move between zones.
- **Principle of least privilege** limits which systems a compromised account can access.
- **EDR** solutions with behavioral analytics can detect lateral movement patterns even when legitimate tools are used.

## Connections

- Parent: [[ransomware]] — lateral movement precedes ransomware detonation
- See also: [[network-segmentation]]
