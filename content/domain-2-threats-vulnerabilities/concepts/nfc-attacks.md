---
title: "NFC attacks"
description: "Eavesdropping on or manipulating Near Field Communication transactions"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

NFC (Near Field Communication) attacks target the short-range wireless communication protocol used in contactless payment cards, transit passes, and mobile payment systems. Because NFC operates at very close range (typically less than 10 cm), attacks were historically considered difficult, but amplification devices have extended the practical range. Attacks include eavesdropping on transactions, relay attacks, and data manipulation.

## Key Details

- **Eavesdropping**: NFC signals can be intercepted with sensitive antennas even at ranges greater than the intended communication distance.
- **Relay attacks**: Attackers extend the effective NFC range using two devices—one near the victim's card (or phone) and one at a payment terminal—to conduct unauthorized transactions while the victim is unaware.
- **Data manipulation**: In some implementations, NFC data can be modified during transmission.
- **Contactless card cloning**: NFC card data can be read and cloned to create duplicate cards for unauthorized use.
- Mitigation: **RFID-blocking wallets**, **transaction limits** for contactless payments, **device authentication** in NFC implementations.

## Connections

- Parent: [[wireless-attacks]] — an NFC-specific wireless attack vector
- See also: [[rfid-cloning]], [[relay-attacks]]
