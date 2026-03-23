---
title: "RFID cloning"
description: "Copying RFID badge data to create unauthorized duplicate access cards"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

RFID cloning involves reading the radio frequency identifier data from an RFID-enabled access badge or card without the owner's knowledge or consent, then writing that data to a blank RFID card or device to create a functional duplicate. The cloned card can then be used to gain physical access to secured areas that accept the original card. Many older proximity card systems (125 kHz HID) are vulnerable to this attack with low-cost tools.

## Key Details

- **125 kHz proximity cards** (older HID, EM4100): Extremely easy to clone—unencrypted, broadcast card number to any reader within range; can be read with devices like the Flipper Zero or specialized cloning devices.
- **13.56 MHz smart cards** (MIFARE, iClass, DESFire): More secure—some use encryption and challenge-response authentication, but older implementations (MIFARE Classic) have been broken.
- **Range**: Modern readers can capture card data from distances of 1+ meter with amplified antennas.
- Mitigation: upgrade to **modern encrypted smart card systems** (DESFire EV2/EV3, SEOS), add **PIN + badge** multi-factor authentication.
- Physical mitigation: **RFID-blocking sleeves/wallets** for individuals.

## Connections

- Parent: [[wireless-attacks]] — an RFID-based physical access attack
- See also: [[nfc-attacks]], [[access-badges]]
