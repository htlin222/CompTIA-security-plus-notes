---
title: "Session hijacking"
description: "Stealing or predicting a valid session token to impersonate an authenticated user"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Session Hijacking?
> When you log into a website, you get a special pass that proves who you are. Session hijacking is when someone steals that pass and uses it to pretend to be you on the website.

## Definition

Session hijacking occurs when an attacker obtains or crafts a valid session token (cookie, URL parameter, or header token) that belongs to an authenticated user, then uses it to make requests as that user without knowing their credentials. The attacker effectively impersonates the victim for the duration the session token remains valid. Session tokens are the primary mechanism web applications use to maintain authentication state.

## Key Details

- **Theft methods**: XSS (stealing session cookies via JavaScript), network sniffing (capturing unencrypted cookies), MitM attacks, database breaches.
- **Prediction**: Old applications with weak session token generation used sequential or predictable IDs—attackers could guess valid tokens.
- **HttpOnly flag**: Prevents JavaScript from accessing session cookies—mitigates XSS-based cookie theft.
- **Secure flag**: Instructs browser to only send the cookie over HTTPS—prevents theft via network sniffing.
- **Session fixation**: Attacker sets the victim's session ID before authentication—after login, attacker's known session ID becomes authenticated.

## Connections

- Parent: [[application-attacks]] — stealing authenticated session state
- See also: [[impact]], [[ssltls-stripping]]
