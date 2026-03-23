---
title: "Firewalls"
description: "Firewalls filter network traffic based on rules to enforce security boundaries between trusted and untrusted networks."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/high
aliases:
  - "Firewalls"
---

## Overview

A firewall is a network security device or software that monitors and controls incoming and outgoing traffic based on predetermined security rules. Firewalls establish a barrier between trusted internal networks and untrusted external networks. They are the most fundamental network security control and are deployed at network perimeters, between zones, and on individual hosts.

## Key Concepts

- **Firewall types:**
  - **Packet filtering** — inspects headers (source/dest IP, port, protocol); stateless; fast but limited
  - **Stateful inspection** — tracks connection state; allows return traffic for established sessions
  - **Application layer / proxy** — inspects payload content; understands protocols (HTTP, FTP); slower but thorough
  - **Next-Generation Firewall (NGFW)** — combines stateful inspection, deep packet inspection, IPS, and application awareness
  - **Web Application Firewall (WAF)** — specifically protects web applications against attacks like SQLi and XSS
- **[[host-based-vs-network-based|Host-based vs. network-based]]** — host firewalls protect individual systems; network firewalls protect entire segments
- **[[unified-threat-management-utm|Unified Threat Management (UTM)]]** — all-in-one appliance combining firewall, IDS/IPS, antivirus, content filtering, VPN
- **Rule configuration:**
  - Rules processed top-down; first match wins
  - Implicit deny at the bottom (block everything not explicitly allowed)
  - Principle of least privilege in rule design
- **[[access-control-lists-acls|Access Control Lists (ACLs)]]** — ordered lists of permit/deny rules based on traffic attributes
- **[[screened-subnet-dmz|Screened subnet (DMZ)]]** — uses firewalls to create a buffer zone for public-facing services

## Exam Tips

> [!tip] Remember
> NGFW = stateful + DPI + IPS + app awareness. WAF = web apps specifically (Layer 7). Implicit deny = the last rule blocks everything else. Rules are processed top to bottom; order matters.

## Connections

- Core component of [[network-security-architecture]] providing boundary enforcement
- Works alongside [[ids-ips]] which detects and prevents threats that pass through firewall rules
- See also [[network-segmentation]] for how firewalls enforce zone boundaries within the network

## Scenario

> See [[case-firewalls]] for a practical DevOps scenario applying these concepts.
