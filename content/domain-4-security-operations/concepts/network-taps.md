---
title: "Network taps"
description: "Hardware devices that copy network traffic for monitoring without affecting the traffic flow"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Network taps (Test Access Points) are passive or active hardware devices inserted into a network cable or optical fiber that create an exact copy of all traffic passing through the link and send that copy to a monitoring port. Unlike port mirroring (SPAN), hardware taps are completely passive and do not affect the original traffic flow — making them more reliable for full-fidelity traffic capture.

## Key Details

- Passive optical taps split the light signal — physically impossible to interfere with traffic
- Copper taps (active) require power but provide bidirectional traffic copying
- Network taps capture 100% of traffic with no packet drops (unlike SPAN which may drop packets at high load)
- Traffic from the tap goes to network packet brokers, IDS/IPS, forensic capture systems, or network analyzers
- Taps are transparent — they are invisible to network devices and cannot be detected on the network

## Connections

- Parent: [[network-monitoring]] — network taps are the preferred hardware method for passive traffic collection
- See also: [[port-mirroring-span]]
