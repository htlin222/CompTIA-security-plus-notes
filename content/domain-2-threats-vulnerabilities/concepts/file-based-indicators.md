---
title: "File-based indicators"
description: "Malicious file hashes, suspicious file names, unexpected file locations"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

File-based indicators of compromise are artifacts found on a system that suggest the presence of malware or attacker tools. These include the cryptographic hashes of known malicious files, suspicious file names that mimic legitimate system files, files in unexpected locations (malware often drops files in temp directories or masquerades as system files), and recently modified critical system files.

## Key Details

- **File hashes** (MD5, SHA-1, SHA-256): Unique fingerprints of files—used to match against threat intelligence databases (VirusTotal, MISP).
- **Suspicious names**: Malware often uses names similar to legitimate processes (svchost.exe in a non-system directory, lsass.exe in %TEMP%).
- **Unexpected locations**: `%TEMP%\`, `%APPDATA%\`, user profile directories—unusual places for executable files.
- **Recently modified system files**: Changes to Windows system files outside of patching cycles indicate tampering.
- Hash matching is a key function of **EDR** (Endpoint Detection and Response) solutions and **antivirus** software.

## Connections

- Parent: [[indicators-of-compromise]] — a host-based IoC category
- See also: [[host-based-indicators]]
