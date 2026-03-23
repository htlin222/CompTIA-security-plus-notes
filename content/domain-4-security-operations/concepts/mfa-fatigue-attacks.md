---
title: "MFA fatigue attacks"
description: "Attackers bombard users with push notifications hoping they approve one"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are MFA Fatigue Attacks?
> An attacker keeps sending login approval requests to your phone until you get so annoyed you tap "approve" just to make it stop. It is like someone ringing your doorbell over and over until you open the door.

## Definition

MFA fatigue attacks (also called MFA bombing or push spam) are social engineering attacks that exploit push notification-based MFA by flooding the victim with repeated authentication requests until they approve one out of frustration, confusion, or the mistaken belief that it is legitimate. This attack bypasses push-based MFA without the attacker needing to intercept or steal the OTP code.

## Key Details

- Attacker has already obtained the target's credentials (password) through phishing or credential stuffing
- Attacker repeatedly triggers MFA requests; victim approves one to stop the notifications
- High-profile incidents: Uber breach (2022) used MFA fatigue to gain initial access
- Mitigations: number matching (user must enter a code shown in the app), additional context in push (IP, location), phishing-resistant MFA (FIDO2/WebAuthn)
- FIDO2/passkeys are immune to this attack — they use challenge-response with no push notification

## Connections

- Parent: [[mfa]] — MFA fatigue is a significant attack vector against push-based MFA
- See also: [[something-you-have]]
