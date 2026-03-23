---
title: "Rogue access point"
description: "Unauthorized AP connected to the corporate network, creating a backdoor past perimeter security"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A rogue access point is an unauthorized wireless access point that has been connected to a corporate network—either by a malicious insider seeking to create a backdoor, or by a well-intentioned employee trying to improve wireless coverage without authorization. Rogue APs bypass perimeter security controls (firewalls, NAC) because wireless clients connecting to them enter directly onto the corporate network.

## Key Details

- **Malicious installation**: Attacker physically connects a small AP to a network port in a shared space (conference room, lobby)—creates a wireless backdoor.
- **Naive installation**: Employee brings in a home router for better coverage—unintentionally creates an unmanaged, potentially insecure network segment.
- Different from **evil twin** (which impersonates a legitimate network externally); rogue APs are physically connected to the target network.
- **Detection**: **Wireless intrusion prevention systems (WIPS)**, **802.1X NAC** (prevents unauthorized devices from connecting to network ports), regular physical inspection.
- **802.1X** is the most effective control—requires authentication before network access is granted, preventing unauthorized APs from functioning.

## Connections

- Parent: [[wireless-attacks]] — a wireless infrastructure attack
- See also: [[evil-twin]]
