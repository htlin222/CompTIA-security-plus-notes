---
title: "Push notifications"
description: "Authentication apps send approve/deny prompts to registered devices"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Push notification-based MFA is an authentication method where, after a user enters their password, the authentication system sends a push notification to the user's registered mobile device. The user reviews the notification details and taps Approve or Deny to complete or reject the authentication attempt. This provides a user-friendly MFA experience without requiring users to manually enter OTP codes.

## Key Details

- More user-friendly than TOTP: no code to copy; one-tap approval
- Modern push notifications should include context: application name, location, IP address of login attempt
- Vulnerable to MFA fatigue attacks (push bombing) — mitigated by number matching and location-based verification
- Requires internet connectivity on the user's mobile device to receive push notifications
- Number matching (showing a code in the login page that must match the code in the push) defeats MFA fatigue attacks

## Connections

- Parent: [[mfa]] — push notifications are a common MFA factor implementation
- See also: [[mfa-fatigue-attacks]]
