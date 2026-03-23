---
title: "Host-based indicators"
description: "Unexpected processes, registry changes, scheduled tasks, unauthorized accounts, modified system files"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Host-Based Indicators?
> These are clues you find by looking directly at a computer -- unexpected programs running, new accounts nobody created, or files that were changed. It's like noticing someone rearranged your room.

## Definition

Host-based indicators of compromise are artifacts and anomalies observed directly on a system that suggest malicious activity or compromise. Unlike network-based indicators, they are found through endpoint analysis—reviewing running processes, registry entries, scheduled tasks, user accounts, and file system changes. EDR (Endpoint Detection and Response) solutions are the primary tool for collecting and analyzing host-based IoCs at scale.

## Key Details

- **Unexpected processes**: Processes running from unusual locations (e.g., PowerShell spawned by a Word document).
- **Registry changes**: New Run keys, autostart entries, or modified security settings—common malware persistence mechanism.
- **Scheduled tasks**: New tasks created by malware for persistence or periodic execution of payloads.
- **Unauthorized user accounts**: Newly created local admin accounts are a post-exploitation red flag.
- **Modified system files**: Changes to Windows DLLs, system executables, or configuration files outside patching cycles indicate tampering.

## Connections

- Parent: [[indicators-of-compromise]] — the host-based IoC category
- See also: [[file-based-indicators]], [[behavioral-indicators]]
