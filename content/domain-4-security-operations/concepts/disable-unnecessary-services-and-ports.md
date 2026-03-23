---
title: "Disable unnecessary services and ports"
description: "Reduce potential entry points by turning off what is not needed"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Disabling unnecessary services and closing unused ports is a fundamental system hardening practice that reduces the attack surface by eliminating network-accessible services that are not required for the system's intended function. Every running service and open port represents a potential entry point for attackers; removing unused ones reduces the number of potential vulnerabilities.

## Key Details

- Default OS and application installations often include services and ports that are not needed
- Port scanning (nmap) reveals all listening ports — any unexpected open port warrants investigation
- Services should be disabled both at the OS level and in the firewall
- Principle of least functionality: systems should only run services required for their intended role
- Common unnecessary services to disable: Telnet, FTP, SNMP v1/v2, NetBIOS, SMBv1

## Connections

- Parent: [[hardening]] — disabling unnecessary services is a core system hardening step
- See also: [[least-functionality-principle]]
