---
title: "Host-based firewall"
description: "Controls inbound and outbound traffic at the individual device level"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is a Host-based Firewall?
> A host-based firewall is a personal bouncer for one computer. It decides which connections are allowed in and out, like a gate that only opens for people on the list.

## Definition

A host-based firewall is a software firewall installed directly on an endpoint device (workstation, server) that controls network traffic entering and leaving that specific host. Unlike network firewalls that protect network segments, host-based firewalls provide granular, per-device control and continue to protect devices when they are outside the corporate network perimeter.

## Key Details

- Windows Defender Firewall and iptables/nftables (Linux) are common host-based firewall implementations
- Provides last-line-of-defense protection even when network firewalls are bypassed or unavailable
- Protects mobile devices when connected to untrusted networks (home, hotel, coffee shop)
- Rules can restrict inbound connections to only necessary services and source IP ranges
- MDM solutions can remotely manage host-based firewall policies on managed devices

## Connections

- Parent: [[endpoint-security]] — host-based firewall is a critical endpoint security control
- See also: [[host-based-vs-network-based]]
