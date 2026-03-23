---
title: "Replay attack"
description: "Capturing and retransmitting valid network traffic to gain unauthorized access or duplicate transactions"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Replay Attack?
> The attacker records your "password handshake" with a server and plays it back later, like recording someone saying "Open sesame" and replaying the recording to open the door.

## Definition

A replay attack occurs when an attacker captures a legitimate authentication exchange or transaction and retransmits it later to gain unauthorized access or repeat a transaction. Unlike relay attacks (which are real-time), replay attacks involve recording valid communications and replaying them at a later time. They exploit authentication systems that don't include temporal components to verify freshness.

## Key Details

- Classic example: capturing an authentication token and replaying it later to authenticate as the victim.
- **Kerberos** protects against replay attacks using **timestamps**—authentication requests more than 5 minutes old are rejected.
- **Nonces** (Numbers used Once): Random values included in authentication protocols that must be unique—replayed packets fail because the nonce has already been used.
- **Sequence numbers**: TCP uses sequence numbers; replay of old packets is detected because they have already-used sequence numbers.
- **Session tokens** must be properly invalidated after logout to prevent replay of captured session cookies.

## Connections

- Parent: [[network-attacks]] — a network-layer authentication attack
- See also: [[relay-attacks]], [[session-hijacking]]
