---
title: "Guest networking"
description: "NAC can direct unknown or personal devices to an isolated guest network"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Guest networking in the context of NAC is the practice of automatically placing unrecognized or non-compliant devices (such as personal devices of visitors or employees) into an isolated guest network segment with internet access but no access to internal corporate resources. NAC systems enforce this by evaluating device posture and identity and directing non-compliant devices to the appropriate network segment.

## Key Details

- Guest network is isolated from internal corporate resources using VLANs and firewall rules
- Provides internet access for guests without exposing internal systems
- NAC can dynamically assign devices to the guest VLAN based on authentication result or compliance check
- Reduces risk of unmanaged personal devices being used as attack vectors against internal systems
- Wireless guest networks should be on separate SSIDs and VLANs from corporate wireless

## Connections

- Parent: [[nac]] — guest networking is a key use case and capability of NAC implementations
- See also: [[remediation-network]]
