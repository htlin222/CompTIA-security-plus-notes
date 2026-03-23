---
title: "Hardware vulnerabilities"
description: "Side-channel attacks, firmware flaws (Spectre, Meltdown), end-of-life hardware"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Hardware vulnerabilities are security flaws that exist in the physical components of computing systems—processors, firmware, memory, or peripheral devices. Unlike software vulnerabilities, hardware vulnerabilities are often very difficult or impossible to patch fully without hardware replacement, and they can affect entire product generations across multiple vendors. Famous examples include the Spectre and Meltdown CPU vulnerabilities discovered in 2018.

## Key Details

- **Spectre and Meltdown (2018)**: CPU speculative execution flaws affecting nearly all modern processors—allow unprivileged code to read privileged memory contents.
- **Side-channel attacks**: Exploit physical characteristics (timing, power consumption, electromagnetic emissions) to extract cryptographic keys without breaking the algorithm.
- **Firmware vulnerabilities**: Flaws in UEFI/BIOS or device firmware—often difficult to patch and can persist through OS reinstallation.
- **End-of-life hardware**: No longer receives firmware updates—permanent vulnerability exposure.
- **Supply chain attacks** on hardware: Malicious firmware or implants inserted during manufacturing or distribution.

## Connections

- Parent: [[vulnerability-types]] — a category of non-software vulnerability
- See also: [[side-channel-attacks]]
