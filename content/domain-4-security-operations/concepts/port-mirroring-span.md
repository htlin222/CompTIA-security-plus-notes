---
title: "Port mirroring (SPAN)"
description: "Switch feature that copies traffic from one port to a monitoring port"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - SPAN
---

> [!eli5] ELI5: What is Port Mirroring?
> Port mirroring copies all the traffic from one network connection and sends it to a monitoring tool. Like putting a mirror at a street corner so a guard can see traffic from both directions.

## Definition

Port mirroring, also called SPAN (Switched Port ANalyzer), is a switch feature that creates copies of network traffic from selected ports or VLANs and sends them to a designated monitoring port. Security monitoring tools (IDS, packet capture systems) connected to the monitoring port receive copies of the traffic for analysis without interrupting or affecting the original traffic flow.

## Key Details

- SPAN port receives a copy of traffic — the monitoring device cannot inject or modify the original traffic
- Local SPAN: copies traffic within the same switch
- Remote SPAN (RSPAN): copies traffic across different switches using a dedicated VLAN
- Limitation: at very high traffic volumes, SPAN ports may drop packets — hardware taps are more reliable
- SPAN is software-based (configured on the switch) vs. hardware taps which are physical devices

## Connections

- Parent: [[network-monitoring]] — port mirroring is a primary method for connecting monitoring tools to network traffic
- See also: [[network-taps]]
