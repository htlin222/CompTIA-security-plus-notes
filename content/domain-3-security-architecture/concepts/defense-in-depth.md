---
title: "Defense in depth"
description: "layered security controls so that if one fails, others still protect the environment"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Defense in depth is a security architecture principle that advocates for multiple layers of security controls so that if any single control fails or is bypassed, additional controls remain in place to prevent or limit the impact of an attack. The concept is borrowed from military strategy and recognizes that no single security control is perfect.

## Key Details

- Multiple layers: perimeter (firewall), network (IDS/IPS), host (endpoint security), application, data
- An attacker who bypasses the outer perimeter still faces internal network controls, host controls, and data encryption
- Defense in depth also refers to combining different types of controls: preventive, detective, and corrective
- Failure of any one control is expected and planned for — no single point of security failure
- Contrasts with "security through obscurity," which relies on secrecy rather than layered controls

## Connections

- Parent: [[network-security-architecture]] — defense in depth is a foundational design principle for security architecture
- See also: [[network-zones]]
