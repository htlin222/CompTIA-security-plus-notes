---
title: "Bluetooth attacks"
description: "Bluejacking (unsolicited messages), Bluesnarfing (data theft), Bluebugging (full device control)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Bluetooth Attacks?
> Bluetooth is like a short-range walkie-talkie for your devices. These attacks happen when someone nearby tunes in to steal your contacts, send you weird messages, or even take control of your phone.

## Definition

Bluetooth attacks exploit weaknesses in the Bluetooth wireless protocol or its implementation to target devices within short range (typically up to 10–100 meters). The three primary Bluetooth attack types are: Bluejacking (sending unsolicited messages), Bluesnarfing (unauthorized data access), and Bluebugging (gaining full remote control over a device). These attacks require proximity and often exploit devices in discoverable mode.

## Key Details

- **Bluejacking**: Sends unsolicited messages or vCards to Bluetooth-enabled devices—annoying but relatively harmless.
- **Bluesnarfing**: Unauthorized access to device data (contacts, messages, files) via Bluetooth; more serious privacy threat.
- **Bluebugging**: Full device takeover—attacker can make calls, send messages, access internet; most severe attack.
- Mitigation: **disable Bluetooth when not in use**, **set devices to non-discoverable mode**, **keep firmware updated**.
- Bluetooth Low Energy (BLE) attacks are increasingly relevant with IoT and wearable devices.

## Connections

- Parent: [[wireless-attacks]] — Bluetooth is a wireless attack vector
- See also: [[nfc-attacks]]
