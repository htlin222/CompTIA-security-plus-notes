---
title: "Amplification attack"
description: "Using protocols like DNS, NTP, or memcached to amplify a small request into a massive response"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is an Amplification Attack?
> It's like whispering a tiny question to a loudspeaker and having it blast the answer at someone's house. The attacker sends a small message but the response that hits the target is huge.

## Definition

An amplification attack is a type of distributed denial-of-service (DDoS) attack in which the attacker exploits protocols that produce responses much larger than the triggering request. By spoofing the victim's IP address as the source, the attacker directs all the amplified responses to the victim, overwhelming their bandwidth or resources with minimal effort on the attacker's part.

## Key Details

- **DNS amplification**: Small query (~60 bytes) can generate a response up to 3,000 bytes—a 50x amplification factor.
- **NTP amplification** uses the `monlist` command, which can return up to 206 records per query—amplification factor of 556x.
- **Memcached amplification** is the most powerful known—amplification factor can exceed 50,000x.
- Mitigation includes: **BCP38** (ingress filtering to block spoofed packets), disabling unnecessary services (e.g., NTP `monlist`), and rate limiting DNS responses.
- These attacks exploit the fact that UDP is connectionless—responses are sent without a handshake.

## Connections

- Parent: [[network-attacks]] — a category of network-layer attack technique
- See also: [[amplificationreflection]], [[volumetric-attacks]]
