---
title: "Sandboxing"
description: "using VMs as isolated environments for testing suspicious code or malware analysis"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Sandboxing?
> A sandbox is a safe play area where kids can dig and build without messing up the rest of the yard. In computers, sandboxing runs suspicious programs in an isolated space where they cannot damage anything real, so you can safely see what they do.

## Definition

Sandboxing is the practice of using isolated, controlled environments (typically virtual machines or containers) to safely execute suspicious code, malware samples, or untested applications without risk to production systems. The sandbox provides complete isolation — any malicious actions taken by the code are contained within the sandbox and cannot affect the host system or network.

## Key Details

- Malware analysis sandboxes (Cuckoo, Any.run, VirusTotal) observe and record malware behavior when executed
- Email security gateways use sandboxing to safely execute attachments before delivery to users
- VM snapshots allow rapid restoration to a clean state after analysis
- Sandbox evasion is a concern: advanced malware detects sandbox environments and modifies its behavior to avoid detection
- Used in both security research (malware analysis) and operational security (email attachment detonation)

## Connections

- Parent: [[virtualization-security]] — sandboxing leverages virtualization for security isolation
- See also: [[antivirus-anti-malware]]
