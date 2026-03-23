---
title: "Volumetric attacks"
description: "Flooding the target with massive traffic to saturate bandwidth (UDP floods, ICMP floods)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Volumetric attacks are the most common type of DDoS attack, aimed at consuming all available bandwidth between the target and the internet by flooding it with an enormous volume of traffic. The goal is to saturate the target's upstream internet connection, making the site or service unreachable—not by exploiting protocol weaknesses or application logic, but purely through traffic volume.

## Key Details

- **UDP flood**: Sends massive numbers of UDP packets to random ports—target must process each one (sending ICMP port unreachable if no listener), consuming resources.
- **ICMP flood**: Sends massive numbers of ping packets—overwhelms processing capacity (ping flood or "ping of death" with oversized packets).
- **DNS/NTP amplification**: The most powerful volumetric attacks—use third-party servers to amplify traffic to terabit levels.
- **Measurement**: Volumetric attacks are measured in bits per second (Gbps, Tbps); largest recorded attacks exceed 3 Tbps.
- **Mitigation**: **Cloud-based scrubbing centers** (Cloudflare, Akamai, AWS Shield) can absorb terabit-scale attacks; **anycast network diffusion**; **upstream filtering**.

## Connections

- Parent: [[denial-of-service]] — the bandwidth-saturation DDoS attack category
- See also: [[amplification-attack]], [[protocol-attacks]]
