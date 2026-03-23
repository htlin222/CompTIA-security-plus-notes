---
title: "Screened subnet (DMZ)"
description: "uses firewalls to create a buffer zone for public-facing services"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
aliases:
  - DMZ
---

## Definition

A screened subnet (commonly called a DMZ — Demilitarized Zone) is a network architecture pattern that uses firewalls to create an intermediate network segment between an untrusted external network (internet) and the trusted internal network. Public-facing servers are placed in this buffer zone, which limits exposure of the internal network while still allowing controlled public access.

## Key Details

- Classic three-legged firewall design: one firewall with three interfaces (internet, DMZ, internal)
- Dual-firewall design: internet-facing firewall and internal-facing firewall sandwich the DMZ for additional security
- Systems in the DMZ should be hardened and assumed to be potentially compromised
- Traffic from DMZ to internal network should be strictly restricted and filtered
- Common DMZ services: web servers, mail relays, DNS resolvers, reverse proxies, bastion hosts

## Connections

- Parent: [[firewalls]] — screened subnets are created using firewall configurations
- See also: [[dmz-demilitarized-zone]]
