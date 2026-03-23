---
title: "Jamming"
description: "Flooding the wireless spectrum with noise to prevent legitimate wireless communication (DoS)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Jamming?
> It's like someone blasting a loud horn right next to you while you're trying to have a conversation. The noise drowns out everything, and you can't communicate wirelessly anymore.

## Definition

Wireless jamming is a denial-of-service attack that transmits radio frequency (RF) noise or interference on the same frequency band as a target wireless network, disrupting legitimate communication. By overwhelming the spectrum with noise, jamming prevents clients from connecting to or communicating with wireless access points. It is a physical-layer attack that does not require any knowledge of the target network's configuration.

## Key Details

- Operates at the **physical (Layer 1) level**—cannot be blocked by authentication or encryption controls.
- Can target: **Wi-Fi (2.4 GHz, 5 GHz)**, **cellular networks**, **GPS**, **Bluetooth**, and any other RF-based communication.
- **Spectrum analyzers** can detect jamming by identifying abnormal RF energy patterns on monitored frequencies.
- Legal note: intentional RF interference is **illegal** in most jurisdictions (FCC regulations in the US).
- Mitigation: **frequency hopping** (FHSS), **spread spectrum** technologies, **backup communication channels**.

## Connections

- Parent: [[wireless-attacks]] — a physical-layer wireless denial-of-service attack
- See also: [[deauthentication-attack]]
