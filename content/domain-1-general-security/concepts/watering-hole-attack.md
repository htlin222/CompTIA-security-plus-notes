---
title: "Watering hole attack"
description: "Compromising a website frequently visited by the target group to infect visitors"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is a Watering Hole Attack?
> Instead of chasing you directly, the attacker puts a trap on a website you visit all the time -- like a predator waiting at the watering hole where animals always come to drink.

## Definition

A watering hole attack targets a specific group or organization by compromising websites that members of that group are known to frequently visit. Like a predator waiting at a watering hole for prey, the attacker identifies websites the target group uses—industry association sites, vendor portals, professional forums—compromises them, and implants malware that infects visitors. This approach bypasses the need to target victims directly.

## Key Details

- Highly targeted: research is done to identify which websites the victim organization/group regularly visits.
- Particularly effective against **industrial, government, and sector-specific** targets who share common online resources.
- Compromise often involves a **drive-by download** exploit that leverages browser or plugin vulnerabilities to silently install malware.
- Attackers may target only visitors from specific IP ranges (the target organization), making the attack harder to detect.
- **Defense**: Keep browsers and plugins patched, use **script blockers** (NoScript), employ endpoint protection, use **browser isolation** technologies.

## Connections

- Parent: [[social-engineering]] — an indirect social engineering attack technique
- See also: [[phishing]]
