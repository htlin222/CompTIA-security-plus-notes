---
title: "Pivoting"
description: "Using a compromised system as a launchpad to attack internal networks"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Pivoting?
> Once a tester gets into one system, pivoting means using it as a stepping stone to reach other systems. Like climbing through one window to unlock the front door from inside.

## Definition

Pivoting is a post-exploitation technique used in penetration testing (and by real attackers) in which a compromised system is used as a relay or launchpad to attack other systems that are otherwise unreachable from the attacker's original position. This technique is critical for understanding how an attacker with an initial foothold could spread through an internal network.

## Key Details

- After gaining access to one system, the tester uses it as a proxy to scan and attack internal systems
- Techniques include: SSH tunneling, SOCKS proxies through compromised hosts, Metasploit's route command
- Pivoting tests whether network segmentation controls effectively prevent lateral movement
- Demonstrates the concept of "blast radius" — what can an attacker reach from a single compromised host?
- Defense: network segmentation, micro-segmentation, and east-west traffic monitoring prevent or detect pivoting

## Connections

- Parent: [[penetration-testing]] — pivoting is a key post-exploitation technique in penetration testing
- See also: [[exploitation]]
