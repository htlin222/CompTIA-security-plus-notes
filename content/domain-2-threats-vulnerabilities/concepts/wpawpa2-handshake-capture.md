---
title: "WPA/WPA2 handshake capture"
description: "Capturing the 4-way handshake to perform offline brute-force password cracking"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is WPA/WPA2 Handshake Capture?
> When your device connects to Wi-Fi, they do a secret handshake. The attacker records that handshake and takes it home to try guessing the Wi-Fi password offline, where nobody can stop them.

## Definition

WPA/WPA2 handshake capture is a wireless attack technique that captures the 4-way authentication handshake exchanged between a wireless client and access point during connection. The captured handshake contains information derived from the Pre-Shared Key (PSK/passphrase)—allowing offline dictionary or brute-force attacks to recover the Wi-Fi password without further interaction with the network.

## Key Details

- The attacker puts their wireless interface in **monitor mode** and either waits for a client to connect, or uses a **deauthentication attack** to force clients to reconnect and capture the new handshake.
- The captured handshake is a **PBKDF2 hash** of the passphrase—must be brute-forced offline.
- Cracking tools: **Hashcat** (GPU-accelerated), **Aircrack-ng**—can test billions of passwords per second with modern GPUs.
- **Strong, long passphrases** (20+ characters, random) are essentially immune to brute-force even with powerful hardware.
- **WPA3 with SAE**: Replaces the 4-way handshake with Simultaneous Authentication of Equals—provides forward secrecy; captured handshakes cannot be cracked offline.

## Connections

- Parent: [[wireless-attacks]] — the fundamental WPA/WPA2 password attack technique
- See also: [[deauthentication-attack]], [[krack-key-reinstallation-attack]]
