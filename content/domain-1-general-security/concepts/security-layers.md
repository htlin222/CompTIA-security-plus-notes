---
title: "Security layers"
description: "From outer to inner: perimeter, network, host, application, data — the layers of defense-in-depth"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Security layers represent the concentric zones of protection in a defense-in-depth architecture, arranged from the outermost perimeter to the most sensitive inner data layer. Each layer provides independent protection, so that an attacker who breaches one layer still faces additional defenses before reaching the protected asset. The classic model progresses from physical security through network, host, application, and data layers.

## Key Details

- **Perimeter (outer)**: Physical security (fencing, bollards), network firewall, DMZ—first line of defense.
- **Network**: Internal firewalls, VLANs, IDS/IPS, network access control (NAC)—controls traffic between zones.
- **Host**: Endpoint security (antivirus, EDR), host-based firewalls, OS hardening, patch management.
- **Application**: Application firewalls (WAF), secure coding practices, input validation, authentication and authorization controls.
- **Data (inner)**: Encryption at rest, database access controls, DLP, data classification—last line of defense.
- Each layer is protected independently—compromise at one layer does not automatically mean compromise at the next.

## Connections

- Parent: [[defense-in-depth]] — the layered architecture within defense-in-depth
- See also: [[control-diversity]]
