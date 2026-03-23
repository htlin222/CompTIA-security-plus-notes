---
title: "TOTP (Time-based One-Time Password)"
description: "Algorithm that generates codes valid for a short time window (e.g., Google Authenticator)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - TOTP
---

> [!eli5] ELI5: What is TOTP?
> TOTP generates a new code every 30 seconds based on the current time. It is like a password that keeps changing -- even if someone sees the old one, it has already expired.

## Definition

TOTP (Time-based One-Time Password) is an algorithm defined in RFC 6238 that generates a new one-time password approximately every 30 seconds based on a shared secret key and the current time. It is the most widely deployed OTP algorithm, used by authenticator apps like Google Authenticator and Microsoft Authenticator as a software-based MFA factor.

## Key Details

- Codes are valid for approximately 30 seconds (configurable time window)
- Based on HMAC-SHA1 with the shared secret and current Unix time (truncated to 30-second epochs)
- The shared secret is established during setup (scanning a QR code) and stored in both the app and the server
- Requires time synchronization between the client and server (usually within 1-2 time steps to accommodate clock drift)
- Vulnerable to real-time phishing: attacker captures OTP and uses it immediately before it expires

## Connections

- Parent: [[mfa]] — TOTP is the most common software OTP implementation for MFA
- See also: [[hotp-hmac-based-one-time-password]]
