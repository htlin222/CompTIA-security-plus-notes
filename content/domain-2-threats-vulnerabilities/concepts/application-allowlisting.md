---
title: "Application allowlisting"
description: "Only permitting approved software to execute — stronger than blocklisting"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Application Allowlisting?
> It's like your parents saying "You can only play with these three apps on the tablet." Anything not on the approved list simply won't run.

## Definition

Application allowlisting is a security control that permits only pre-approved applications to execute on a system, blocking everything else by default. Unlike blocklisting (which tries to identify and block known-bad software), allowlisting operates on a default-deny principle—only explicitly trusted applications run, providing much stronger protection against malware and unauthorized software.

## Key Details

- **Stronger than blocklisting** because it doesn't rely on knowing what's bad; it defines only what's good.
- Implemented via tools like **Windows AppLocker**, **WDAC (Windows Defender Application Control)**, or **SELinux**.
- Can be based on file path, file hash, publisher signature, or a combination.
- Particularly effective against **fileless malware** that tries to abuse unknown executables.
- High administrative overhead—requires maintaining and updating the approved list; legitimate software updates can break allowlists.

## Connections

- Parent: [[mitigation-techniques]] — a key mitigation against malware execution
- See also: [[fileless-malware]], [[patching]]
