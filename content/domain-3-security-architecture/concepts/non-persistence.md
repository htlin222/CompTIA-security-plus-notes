---
title: "Non-persistence"
description: "systems rebuilt from known-good images; live boot media, revert to snapshot"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Non-persistence is a security design approach in which system state does not persist between uses — the system is automatically reverted to a known-good baseline state at the end of each session or use. This eliminates the risk of malware persisting on endpoints between user sessions and reduces the blast radius of any compromise to a single session.

## Key Details

- **Live boot media**: boot from CD/USB — no changes persist after shutdown
- **Revert to snapshot**: VMs revert to clean snapshot after each use
- **VDI (Virtual Desktop Infrastructure)**: non-persistent desktops reset at logoff
- Eliminates attacker persistence — any changes the attacker makes are wiped on reboot
- User data must be stored separately (roaming profiles, cloud storage) to allow non-persistent endpoints
- Kiosk and public-access terminals are common use cases for non-persistent computing

## Connections

- Parent: [[resilience-and-redundancy]] — non-persistence is a resilience technique that ensures clean system state
- See also: [[immutable-infrastructure]]
