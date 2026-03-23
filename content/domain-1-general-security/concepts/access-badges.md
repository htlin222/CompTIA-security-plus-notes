---
title: "Access badges"
description: "RFID or smart card-based identification for building entry"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Access badges are physical authentication tokens—typically RFID cards or smart cards—used to control entry to buildings, rooms, or secured areas. They work by transmitting a unique identifier to a reader, which then grants or denies access based on configured permissions. Access badges are a key component of physical security and are often integrated with visitor management and audit logging systems.

## Key Details

- **RFID badges** use radio frequency to communicate with readers without physical contact; **smart cards** contain embedded chips that may require contact or proximity.
- Badge data (card number, facility code) can be cloned if not protected—proximity card cloning is a known attack vector.
- Access control systems log badge swipes, providing an audit trail for physical access to sensitive areas.
- Badge issuance and revocation must be tied to HR processes (onboarding/offboarding) to prevent orphaned credentials.
- Multi-factor physical access combines badges with PINs or biometrics for higher-assurance environments.

## Connections

- Parent: [[physical-security]] — part of physical security controls for building access
- See also: [[access-control-vestibules-mantraps]]
