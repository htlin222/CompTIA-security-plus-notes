---
title: "Firmware updates"
description: "BIOS/UEFI and device firmware must be kept current"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Firmware updates involve applying patches to the low-level software embedded in hardware devices such as BIOS/UEFI firmware, network device firmware, printer firmware, and IoT device firmware. Firmware vulnerabilities can be exploited to achieve persistence below the OS level, making them particularly dangerous — firmware-level malware (rootkits) can survive OS reinstallation and disk formatting.

## Key Details

- BIOS/UEFI firmware updates fix vulnerabilities that could be exploited for pre-boot attacks or Secure Boot bypass
- Network device firmware (routers, switches, firewalls) must be updated regularly
- Firmware update management is often neglected compared to OS and application patching
- Secure Boot helps verify that firmware updates are from trusted sources
- Some firmware vulnerabilities (e.g., BootHole) require coordinated vendor-OS updates

## Connections

- Parent: [[hardening]] — firmware updates are a critical but often overlooked hardening activity
- See also: [[patch-management]]
