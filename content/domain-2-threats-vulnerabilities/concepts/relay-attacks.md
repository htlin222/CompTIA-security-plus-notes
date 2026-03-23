---
title: "Relay attacks"
description: "Forwarding authentication exchanges between a victim and a legitimate service (common with NFC/RFID)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Relay Attacks?
> Two thieves stand between your car key and your car. One stands near you and picks up the key's signal, then beams it to the other thief near the car. The car thinks the key is right there and unlocks.

## Definition

A relay attack intercepts authentication communications between a legitimate client and server, forwarding them in real time to complete an unauthorized authentication without breaking any cryptographic security. The attacker acts as a transparent proxy—they don't need to understand or decrypt the authentication exchange; they simply relay it. This is particularly effective against NFC/RFID-based payment and access systems.

## Key Details

- **NFC relay**: Two attackers—one with a reader near the victim's contactless card, another at a payment terminal. The first reads and relays the card's response to the second in real time.
- **NTLM relay attacks**: A classic Windows network attack where the attacker captures an NTLM authentication attempt and relays it to authenticate to another server as the victim.
- **Kerberos relay**: Less common but possible in specific configurations.
- **Mitigation for NFC**: **Distance limits** (impractical with relay devices), **transaction amount limits**, **out-of-band confirmation** (app notification).
- **NTLM relay mitigation**: **SMB signing**, **LDAP signing**, **Extended Protection for Authentication (EPA)**, **disabling NTLM** in favor of Kerberos.

## Connections

- Parent: [[on-path-attacks]] — relay attacks as a form of on-path authentication abuse
- See also: [[nfc-attacks]], [[replay-attack]]
