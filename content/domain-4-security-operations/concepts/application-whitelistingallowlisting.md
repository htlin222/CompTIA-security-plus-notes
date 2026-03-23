---
title: "Application whitelisting/allowlisting"
description: "Only approved applications can execute on the endpoint"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Application Allowlisting?
> It is like a guest list at a party -- only programs on the approved list are allowed to run. Everything else gets turned away at the door, even if it looks harmless.

## Definition

Application whitelisting (also called allowlisting) is a security control that restricts endpoint execution to a pre-approved list of applications, scripts, and executables. Any software not on the approved list is automatically blocked from running, regardless of whether it is known malware. This is the inverse of traditional blacklisting and provides strong protection against zero-day malware and unauthorized software.

## Key Details

- Default-deny policy: only explicitly approved applications can execute
- Much more effective than blacklisting against zero-day and novel malware
- Can be implemented at the OS level (Windows AppLocker, WDAC) or via third-party tools
- Requires careful baseline management — legitimate software updates must be allowed
- High administrative overhead; best suited for high-security or locked-down systems

## Connections

- Parent: [[endpoint-security]] — allowlisting is a hardening control for endpoints
- See also: [[least-functionality-principle]]
