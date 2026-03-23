---
title: "Port scanning"
description: "Enumerating open ports and services on target systems during the reconnaissance phase"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Port scanning is a reconnaissance technique used to enumerate which TCP and UDP ports are open on a target system, revealing what services and potentially what software versions are running. It is typically one of the first steps in a cyberattack or penetration test—providing attackers with a map of the target's exposed services and potential attack vectors. Nmap is the most widely used port scanning tool.

## Key Details

- **TCP SYN scan (stealth scan)**: Sends SYN packets; open ports respond with SYN-ACK; doesn't complete the handshake—harder to detect in logs.
- **TCP Connect scan**: Full 3-way handshake—logged by target systems.
- **UDP scan**: Slower; open ports typically don't respond; closed ports send ICMP port unreachable.
- **OS fingerprinting**: Analyzing TCP/IP stack behavior to identify the target OS version.
- **Service version detection** (`-sV` in nmap): Identifies software and version running on open ports—crucial for finding specific vulnerabilities.

## Connections

- Parent: [[network-attacks]] — reconnaissance technique preceding network attacks
- See also: [[open-service-ports]]
