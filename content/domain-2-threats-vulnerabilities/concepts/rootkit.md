---
title: "Rootkit"
description: "Hides deep in the OS (kernel-level or boot-level) to maintain persistent, stealthy access"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Rootkit?
> A rootkit hides so deep in your computer that even your security software can't see it. It's like a spy who puts on an invisibility cloak and lives inside your house, and none of your alarms can detect them.

## Definition

A rootkit is malware designed to conceal itself and other malicious software from detection while maintaining privileged access to a system. By operating at deep system levels—kernel mode, bootloader, or firmware—rootkits can hide processes, files, network connections, and registry entries from the operating system itself, making them extremely difficult to detect using traditional security tools running on the same compromised OS.

## Key Details

- **Kernel-mode rootkits**: Operate at the OS kernel level—can modify kernel data structures to hide themselves from all user-space tools.
- **Bootloader/MBR rootkits (bootkits)**: Infect the Master Boot Record or bootloader—persist across OS reinstallation; load before the OS.
- **Firmware rootkits**: Infect device firmware (UEFI/BIOS, NIC firmware)—survive disk wiping and hardware replacement may be the only remedy.
- **Detection**: **Rootkit scanners** that compare OS views with direct disk access, **Secure Boot** (UEFI), **TPM attestation**, **bootable offline scanners**.
- Famous examples: **Sony DRM rootkit** (2005), **ZeroAccess**, **TDL4 (Alureon)** bootkit.

## Connections

- Parent: [[malware-types]] — a stealthy persistence malware category
- See also: [[fileless-malware]]
