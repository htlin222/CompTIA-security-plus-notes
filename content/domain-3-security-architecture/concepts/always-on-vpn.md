---
title: "Always-on VPN"
description: "automatically connects when the device is powered on; ensures consistent policy enforcement"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Always-on VPN is a VPN configuration in which the VPN client automatically establishes a tunnel when the device boots, before user login, and maintains the connection throughout the device's operation. This ensures that all traffic is routed through the corporate network, enabling consistent security policy enforcement regardless of where the user is located.

## Key Details

- Connects automatically at device startup — users cannot disable the VPN
- Ensures all traffic passes through corporate security controls (DLP, filtering, monitoring)
- Common in enterprise MDM solutions and remote workforce policies
- Can be implemented using technologies like DirectAccess (Windows) or commercial VPN solutions
- May use split tunneling or full tunneling depending on organizational policy

## Connections

- Parent: [[vpn]] — always-on is a deployment mode for VPN clients
- See also: [[authentication]]
