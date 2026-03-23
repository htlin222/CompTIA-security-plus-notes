---
title: "SSL/TLS stripping"
description: "Downgrading an HTTPS connection to HTTP so the attacker can read traffic in plaintext"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is SSL/TLS Stripping?
> You think you're using a locked mailbox (secure connection), but the attacker secretly downgrades it to a regular open mailbox. Your messages travel without protection and the attacker reads everything.

## Definition

SSL/TLS stripping is an attack where an on-path attacker intercepts a user's initial HTTP connection to a website and establishes a separate HTTPS connection with the server, while maintaining an unencrypted HTTP connection with the victim. The user believes they are communicating securely with the server (the attacker's HTTPS connection is secure), but their traffic to the attacker is in plaintext—allowing credential theft and data interception.

## Key Details

- Requires the attacker to be **on-path** (MitM position)—ARP spoofing or rogue AP used to intercept traffic first.
- Works because the victim initiates an HTTP connection—the attacker intercepts it before any redirect to HTTPS.
- **HSTS (HTTP Strict Transport Security)**: Instructs browsers to always use HTTPS—prevents stripping for sites the browser has previously visited (or in the HSTS preload list).
- **HSTS Preloading**: Browsers ship with a built-in list of HSTS-enabled sites—provides protection even on first visit.
- Tool: **SSLstrip** (Moxie Marlinspike, 2009) popularized this attack.

## Connections

- Parent: [[on-path-attacks]] — a technique to strip HTTPS protection for traffic interception
- See also: [[defenses]], [[downgrade-attack]]
