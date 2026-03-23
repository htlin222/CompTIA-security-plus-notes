---
title: "Implicit trust zones"
description: "Zero Trust aims to eliminate these; every zone is treated as untrusted by default"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Implicit trust zones are network areas where users and systems are automatically trusted simply because of their location—typically the internal network or corporate LAN. Traditional "castle and moat" security granted implicit trust to anyone inside the perimeter. Zero Trust architecture explicitly rejects this model, treating every request as potentially hostile regardless of whether it originates from inside or outside the network perimeter.

## Key Details

- **Traditional model**: Inside = trusted, outside = untrusted—attackers who breach the perimeter gain implicit trust.
- **Zero Trust rejects** implicit trust: "never trust, always verify"—every access request is authenticated and authorized regardless of origin.
- Lateral movement is enabled by implicit trust—once inside, attackers can move freely to other "trusted" systems.
- **Microsegmentation** eliminates implicit trust between segments even within the same network.
- Cloud and remote work have already eliminated the concept of a clearly defined "inside"—making Zero Trust essential.

## Connections

- Parent: [[zero-trust]] — a core concept that Zero Trust architecture eliminates
- See also: [[adaptive-identity]], [[policy-enforcement-point-pep]]
