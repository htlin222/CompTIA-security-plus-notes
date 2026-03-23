---
title: "Amplification/Reflection"
description: "Using third-party servers (DNS, NTP, memcached) to amplify and reflect traffic at the victim"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Amplification/Reflection is a DDoS technique that combines two concepts: reflection (directing responses from third-party servers toward the victim by spoofing the victim's IP) and amplification (exploiting protocols where the response is much larger than the request). The attacker essentially uses the internet's open infrastructure as an involuntary weapon against the victim.

## Key Details

- **Reflection** alone uses third-party servers to hide the attacker's true source IP.
- **Amplification** multiplies the attack traffic volume using protocols with high response-to-request size ratios.
- Common protocols exploited: **DNS** (~50x), **NTP monlist** (~556x), **SSDP** (~30x), **memcached** (~50,000x).
- Victim receives traffic from thousands of legitimate servers, making it difficult to block by source IP.
- Defense requires **BCP38 ingress filtering**, rate limiting, and disabling amplifiable services on internet-facing servers.

## Connections

- Parent: [[denial-of-service]] — a sub-type of DDoS attack
- See also: [[amplification-attack]], [[volumetric-attacks]]
