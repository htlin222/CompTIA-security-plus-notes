---
title: "VLAN hopping"
description: "Exploiting trunk port configurations to access traffic on VLANs other than the attacker's assigned VLAN"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is VLAN Hopping?
> A building is divided into separate sections with locked doors between them. VLAN hopping is finding a trick to jump from your section into a restricted one you're not supposed to enter.

## Definition

VLAN hopping is a network attack that exploits VLAN configuration weaknesses to allow an attacker to send or receive traffic from VLANs that their port should not have access to, bypassing VLAN-based network segmentation. There are two primary techniques: switch spoofing (tricking a switch into establishing a trunk link) and double tagging (nesting 802.1Q tags to send frames to a different VLAN).

## Key Details

- **Switch spoofing**: Attacker's device negotiates a trunk link using Dynamic Trunking Protocol (DTP)—gaining access to all VLANs carried by the trunk.
- **Double tagging**: Attacker adds two 802.1Q VLAN tags; the switch strips the outer tag and forwards based on the inner tag—sends frames to a different VLAN (one-way attack only).
- **Mitigation**: **Disable DTP** (configure trunk ports as static, not dynamic); set all unused access ports to a dedicated unused VLAN; change the native VLAN from the default VLAN 1 to an unused VLAN.
- Undermines network segmentation—VLANs are a key control for isolating PCI DSS cardholder data environments, securing IoT, and limiting lateral movement.
- Most modern managed switches can be properly configured to prevent both attack vectors.

## Connections

- Parent: [[network-attacks]] — a network segmentation bypass attack
- See also: [[network-segmentation]]
