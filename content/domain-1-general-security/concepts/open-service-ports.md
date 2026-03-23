---
title: "Open service ports"
description: "Unnecessary services listening on the network increase the attack surface"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Open service ports represent network-accessible entry points into a system—each service listening on a port is a potential attack vector. Unnecessary services that are running and accessible from the network unnecessarily expand the attack surface, providing attackers with additional opportunities to find vulnerabilities. Closing unnecessary ports is one of the most fundamental hardening steps.

## Key Details

- Each open port represents a service that could have **vulnerabilities**, be attacked via **credential brute-force**, or be **misconfigured**.
- **Principle of least function**: Systems should only run and expose the services required for their intended purpose.
- Discovery via **port scanning** (nmap): attackers enumerate open ports before selecting their attack approach.
- Mitigation: **host-based and network firewalls** to block access to ports that must remain open, **disable unnecessary services**, use **network access control**.
- Common unnecessary open ports in enterprise environments: Telnet (23), FTP (21), TFTP (69), unnecessary RPC services.

## Connections

- Parent: [[attack-vectors]] — open ports as network attack vectors
- See also: [[attack-surface-management]]
