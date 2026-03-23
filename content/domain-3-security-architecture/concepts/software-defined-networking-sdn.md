---
title: "Software-Defined Networking (SDN)"
description: "programmatic control of network infrastructure; separates control plane from data plane"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
aliases:
  - SDN
---

> [!eli5] ELI5: What is Software-Defined Networking (SDN)?
> Normally, each network device makes its own decisions, like cars driving without traffic lights. SDN adds a central traffic controller that tells all the devices what to do from one place, making the whole network easier to manage and secure.

## Definition

Software-Defined Networking (SDN) is a network architecture approach that separates the control plane (decision-making: routing, policies, forwarding rules) from the data plane (packet forwarding). A centralized SDN controller makes network decisions and programs the underlying network hardware through standardized APIs, enabling the network to be managed, configured, and secured programmatically.

## Key Details

- Separates: control plane (SDN controller, runs software) from data plane (switches, carries traffic)
- Enables network-wide policy changes to be applied instantly from a central controller
- Security benefits: rapidly respond to threats by reprogramming network segments, blocking flows, or isolating devices
- Enables micro-segmentation at scale in virtualized and cloud environments
- OpenFlow is the original SDN protocol; modern implementations use vendor-specific APIs (Cisco ACI, VMware NSX)

## Connections

- Parent: [[network-security-architecture]] — SDN is a modern network architecture that enables programmable security
- See also: [[micro-segmentation]]
