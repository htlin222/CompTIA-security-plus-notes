---
title: "Zero-day vulnerabilities"
description: "Flaws unknown to the vendor with no available patch — exploits are highly valued by attackers"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Zero-Day Vulnerabilities?
> Nobody knows about the hole in the fence -- not even the people who built it. Since there's no fix yet, attackers who find it first can sneak through before anyone even realizes it exists.

## Definition

Zero-day vulnerabilities are security flaws that are unknown to the software or hardware vendor and therefore have no official patch available. The term "zero-day" refers to the fact that developers have had zero days to address the flaw. Because no fix exists, systems remain vulnerable regardless of patch management practices, making zero-days highly valued by attackers and in the exploit market.

## Key Details

- "Zero-day" means the vendor has had **zero days** to produce a fix—the vulnerability is actively exploitable before any official remediation exists.
- Highly valuable in criminal and nation-state markets; zero-day exploit brokers (e.g., Zerodium) pay millions for reliable exploits against high-value targets.
- Used in sophisticated APT attacks—Stuxnet famously used **four simultaneous zero-days** against Windows to sabotage Iranian nuclear centrifuges.
- Mitigation without a patch: **network segmentation**, **application whitelisting**, **exploit mitigations** (ASLR, DEP), **enhanced monitoring**, and **compensating controls**.
- Once a zero-day becomes publicly known (through disclosure or exploit leak), it becomes an **N-day** vulnerability—a race begins between vendors releasing patches and attackers weaponizing the exploit.

## Connections

- Parent: [[vulnerability-types]] — the most severe and difficult-to-mitigate vulnerability class
- See also: [[unpatched-software]], [[compensating-controls]]
