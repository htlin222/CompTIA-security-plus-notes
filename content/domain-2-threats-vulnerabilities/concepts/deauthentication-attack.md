---
title: "Deauthentication attack"
description: "Sending forged 802.11 deauth frames to disconnect clients from a wireless network"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Deauthentication Attack?
> It's like someone repeatedly pulling the plug on your TV every time you try to watch. The attacker sends a "disconnect now" signal to kick you off your Wi-Fi over and over.

## Definition

A deauthentication attack exploits the 802.11 Wi-Fi protocol's management frames by sending forged deauthentication frames to one or more clients, forcing them to disconnect from the access point. Because management frames in older 802.11 protocols are unauthenticated, any device can forge them. This attack is used as a denial-of-service technique or as a precursor to capturing the WPA2 4-way handshake for offline cracking.

## Key Details

- Deauth frames are **unauthenticated** in 802.11a/b/g/n—anyone can send them to any client.
- Often the first step before an **evil twin** attack—force clients off the real network, then have them connect to the attacker's fake AP.
- Also used to capture the **WPA/WPA2 4-way handshake** for offline password cracking.
- **802.11w (Protected Management Frames / PMF)**: The fix—encrypts and authenticates management frames; requires WPA3 or explicitly enabled in WPA2.
- Tools: **aireplay-ng** (Aircrack-ng suite) is commonly used for deauth attacks.

## Connections

- Parent: [[wireless-attacks]] — a wireless-specific attack technique
- See also: [[evil-twin]], [[wpawpa2-handshake-capture]]
