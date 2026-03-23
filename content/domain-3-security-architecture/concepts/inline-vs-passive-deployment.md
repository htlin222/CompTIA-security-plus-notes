---
title: "Inline vs. passive deployment"
description: "IPS must be inline to block; IDS can be passive via port mirroring"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Inline vs. passive deployment?
> Inline is like a crossing guard standing in the road who can actually stop cars. Passive is like a security camera on the side of the road that records everything but cannot stop anyone. One blocks threats directly; the other just watches and reports.

## Definition

Intrusion detection and prevention systems can be deployed in two fundamental modes: inline (in-band) or passive (out-of-band). The deployment mode determines whether the system can actively block traffic or can only detect and alert. Inline systems sit directly in the traffic path and can block malicious packets; passive systems receive copies of traffic and can only detect and alert.

## Key Details

- **Inline (IPS mode)**: device sits in the traffic path; can actively drop or modify packets to block attacks; adds latency; if device fails, traffic may be disrupted
- **Passive (IDS mode)**: device receives copies of traffic via port mirroring (SPAN) or network TAP; cannot block; zero impact if device fails
- Fail-open vs. fail-close: inline devices must decide whether to pass or drop traffic if the inspection engine fails
- IPS requires inline deployment; IDS can use passive or inline deployment
- Modern NGFWs are inline and combine firewall + IPS + application control

## Connections

- Parent: [[ids-ips]] — deployment mode is a fundamental IDS/IPS configuration decision
- See also: [[network-taps]]
