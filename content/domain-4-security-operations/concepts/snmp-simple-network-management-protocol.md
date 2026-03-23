---
title: "SNMP (Simple Network Management Protocol)"
description: "Used to monitor and manage network devices; SNMPv3 adds encryption and authentication"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

SNMP (Simple Network Management Protocol) is an internet protocol used to monitor, manage, and collect performance data from network devices such as routers, switches, firewalls, servers, and printers. It enables network management systems (NMS) to query device status, receive alerts (traps), and modify device configurations.

## Key Details

- **SNMPv1/v2c**: use "community strings" as passwords; transmitted in cleartext — considered insecure
- **SNMPv3**: adds authentication (MD5/SHA) and privacy (DES/AES encryption) — use SNMPv3 exclusively for security
- SNMP traps are unsolicited alerts sent by devices to the management system when events occur
- SNMP runs on UDP port 161 (queries) and 162 (traps)
- Misconfigured SNMP with default community strings ("public," "private") is a common vulnerability

## Connections

- Parent: [[network-monitoring]] — SNMP is a key protocol for network device monitoring
- See also: [[bandwidth-monitoring]]
