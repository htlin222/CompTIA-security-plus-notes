---
title: "VLANs (Virtual LANs)"
description: "logically separate broadcast domains on a single switch; require a router or Layer 3 switch to route between VLANs"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

VLANs (Virtual Local Area Networks) are a Layer 2 network segmentation technique that logically divides a single physical switch into multiple isolated broadcast domains. Each VLAN acts as a separate network segment — traffic within a VLAN stays contained, and inter-VLAN routing requires a router or Layer 3 switch. VLANs are a foundational tool for network segmentation, enabling security isolation without requiring separate physical hardware.

## Key Details

- Defined by IEEE 802.1Q; trunk ports carry tagged frames for multiple VLANs between switches
- Traffic between VLANs requires a router or Layer 3 switch (not just a switch)
- Common VLAN designs: management VLAN, user VLAN, server VLAN, guest VLAN, IoT VLAN
- VLAN hopping attacks (double tagging, switch spoofing) exploit misconfigured trunk ports
- Mitigation: disable dynamic trunking, set native VLAN to an unused ID, use dedicated management VLAN

## Connections

- Parent: [[network-segmentation]] — VLANs are the primary Layer 2 tool for logical network segmentation
- See also: [[logical-segmentation]], [[physical-segmentation]], [[micro-segmentation]]
