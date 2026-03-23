---
title: "Air gap"
description: "complete physical isolation with no network connectivity; highest security, used for critical systems"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is an Air gap?
> An air gap means a computer is completely disconnected from all other networks -- no wifi, no cables, nothing. It's like keeping your most important treasure on a desert island with no bridges or boats. Nobody can reach it remotely.

## Definition

An air gap is a physical network isolation technique in which a system or network has absolutely no connection to any external network, including the internet or other internal networks. This complete physical separation ensures that network-based attacks cannot reach the system. Air-gapped systems are used in the most sensitive environments such as industrial control systems, military networks, and classified government systems.

## Key Details

- Provides the highest level of network isolation — no wired or wireless connectivity
- Common in industrial control systems (ICS/SCADA), nuclear facilities, and classified environments
- Data transfer requires physical media (USB drives, CDs), which introduces its own risks (e.g., Stuxnet)
- Air gaps do not protect against insider threats or physical access attacks
- Monitoring air-gapped systems requires local logging and physical access for review

## Connections

- Parent: [[network-segmentation]] — air gap is the most extreme form of network segmentation
- See also: [[physical-segmentation]]
