---
title: "KRACK (Key Reinstallation Attack)"
description: "Exploiting a flaw in WPA2's 4-way handshake to decrypt wireless traffic"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - KRACK
---

## Definition

KRACK (Key Reinstallation Attack), disclosed in 2017, exploits a fundamental flaw in the WPA2 four-way handshake process. The attack tricks a client into reinstalling an already-in-use session key by replaying or manipulating handshake messages. Reinstalling a used key resets the nonce (random number used once) counter, allowing the attacker to replay, decrypt, or forge packets depending on the cipher suite in use.

## Key Details

- Affects **WPA2** on all platforms (Windows, Android, iOS, Linux)—a protocol-level flaw, not vendor-specific.
- Most severe on **Linux and Android**: certain implementations used all-zero keys after reinstallation, enabling full decryption.
- **Counter**: Traffic using **HTTPS/TLS** remains encrypted even if the WPA2 layer is compromised—KRACK exposed only unencrypted application traffic.
- Patch applied quickly by major vendors—**keeping devices updated** was and remains the key mitigation.
- **WPA3** with **SAE (Simultaneous Authentication of Equals)** replaces the vulnerable 4-way handshake and prevents KRACK.

## Connections

- Parent: [[wireless-attacks]] — a protocol-level WPA2 attack
- See also: [[wpawpa2-handshake-capture]]
