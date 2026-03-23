---
title: "War driving"
description: "Scanning for wireless networks while moving through an area to map vulnerable access points"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is War Driving?
> Someone drives around a neighborhood with a laptop scanning for Wi-Fi networks, making a map of which ones are open or poorly protected. It's like walking down the street checking which houses left their doors unlocked.

## Definition

War driving is the practice of searching for and mapping wireless networks while traveling through an area—typically by car, hence the name—using a Wi-Fi-enabled device with scanning software. Originally a reconnaissance activity, war driving is used to find open or poorly secured networks for unauthorized access, gather intelligence on corporate Wi-Fi deployments, or identify rogue access points.

## Key Details

- Uses a **wireless adapter in monitor mode** and scanning tools (Kismet, inSSIDer, NetStumbler) to detect all nearby SSIDs.
- **War walking/flying/biking**: Variants using different modes of transportation.
- **WiGLE.net**: A public database of wardrive-collected Wi-Fi networks—millions of networks mapped globally.
- Legal status: Passive detection (scanning) is generally legal; unauthorized connection to networks is illegal.
- **Corporate risk**: War driving can reveal corporate wireless network names, encryption types, and BSSID information—used for targeted attacks (evil twin, deauth).

## Connections

- Parent: [[wireless-attacks]] — a wireless reconnaissance technique
- See also: [[rogue-access-point]]
