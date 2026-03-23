---
title: "Patching"
description: "Applying vendor-supplied fixes to close known vulnerabilities — the most fundamental mitigation"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Patching?
> When a company finds a hole in their software, they release a fix -- like a repair patch for a torn jacket. Installing that patch closes the hole before bad guys can crawl through it.

## Definition

Patching is the process of applying vendor-supplied software updates that fix security vulnerabilities, bugs, and other flaws in operating systems, applications, and firmware. It is the single most impactful mitigation technique for reducing vulnerability exposure, as it directly eliminates known weaknesses that attackers actively exploit. Effective patch management requires a systematic process including testing, scheduling, and verification.

## Key Details

- **Most fundamental vulnerability mitigation**: The majority of successful cyberattacks exploit known, patchable vulnerabilities—not zero-days.
- **Patch management cycle**: Discover (identify what needs patching), prioritize (by CVSS score and exploitability), test (in non-production), deploy (in maintenance windows), verify (confirm application).
- **Critical/Emergency patches**: High-CVSS, actively exploited vulnerabilities may require out-of-cycle emergency patching.
- **Patch Tuesday**: Microsoft releases patches on the second Tuesday of each month; often followed by "Exploit Wednesday" as attackers reverse-engineer fixes.
- **Unpatched systems** remain vulnerable indefinitely—attackers scan for and target known unpatched vulnerabilities using tools like Shodan.

## Connections

- Parent: [[mitigation-techniques]] — the foundational vulnerability mitigation technique
- See also: [[unpatched-software]], [[compensating-controls]]
