---
title: "Host-based vs. network-based"
description: "host firewalls protect individual systems; network firewalls protect entire segments"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Host-based firewalls are installed directly on individual systems and control traffic to and from that specific host, while network-based firewalls are dedicated appliances or systems that control traffic flowing between network segments. Both types are needed in a defense-in-depth architecture — network firewalls protect the perimeter, while host-based firewalls protect each individual system from lateral attacks.

## Key Details

- Network-based: centrally managed, protects entire segments, inspects traffic between subnets
- Host-based: installed on each device, provides device-level control, works even outside corporate network
- Network firewalls protect systems from each other; host firewalls protect individual systems from the network
- Modern next-generation firewalls (NGFW) perform deep packet inspection and application control
- Defense in depth uses both: network firewalls reduce lateral movement, host firewalls provide final protection

## Connections

- Parent: [[firewalls]] — this distinction is fundamental to understanding firewall deployment options
- See also: [[defense-in-depth]]
