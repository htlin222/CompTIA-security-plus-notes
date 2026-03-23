---
title: "HOTP (HMAC-based One-Time Password)"
description: "Counter-based OTP that remains valid until used"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - HOTP
---

## Definition

HOTP (HMAC-based One-Time Password) is a one-time password algorithm defined in RFC 4226 that generates passwords based on a counter value and a shared secret key using HMAC. Unlike TOTP (time-based), HOTP codes do not expire after a fixed time window — they remain valid until used (or until the counter advances past a resynchronization window). Each use increments the counter.

## Key Details

- Counter increments with each code generation; server and token must stay synchronized
- Codes are valid until used, unlike TOTP which expires after ~30 seconds
- Desynchronization can occur if codes are generated but not used, requiring manual resync
- Defined in RFC 4226; TOTP (RFC 6238) is derived from HOTP by using time instead of a counter
- Used in hardware tokens like RSA SecurID (some models) and YubiKey OATH applications

## Connections

- Parent: [[mfa]] — HOTP is one of the OTP methods used as an MFA factor
- See also: [[totp-time-based-one-time-password]]
