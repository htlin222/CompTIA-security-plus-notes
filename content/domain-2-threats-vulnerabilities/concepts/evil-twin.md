---
title: "Evil twin"
description: "Rogue access point that mimics a legitimate network's SSID to trick users into connecting"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

An evil twin attack involves setting up a rogue wireless access point that broadcasts the same SSID (network name) as a legitimate network, often with a stronger signal, to lure users into connecting to the attacker's AP instead of the real one. Once connected, all the victim's wireless traffic passes through the attacker's device, enabling interception, credential harvesting, and malware injection.

## Key Details

- Often preceded by a **deauthentication attack** to force clients off the legitimate AP.
- Can target **public Wi-Fi** (cafes, airports, hotels) or **corporate networks** by mimicking the corporate SSID.
- Once connected, the attacker performs a **man-in-the-middle attack**—capturing credentials, session tokens, and data.
- **WPA3** with **Simultaneous Authentication of Equals (SAE)** and **Protected Management Frames** reduces evil twin effectiveness.
- Defense: use a **VPN** when on public/untrusted Wi-Fi, verify the SSID and AP BSSID (MAC address) before connecting to known networks.

## Connections

- Parent: [[wireless-attacks]] — a wireless network impersonation attack
- See also: [[deauthentication-attack]], [[rogue-access-point]]
