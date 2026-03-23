---
title: "Defenses"
description: "HTTPS everywhere, HSTS, certificate pinning, mutual TLS, encrypted protocols; anti-CSRF tokens, SameSite cookies"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Defenses?
> These are the shields and locks that protect websites -- things like scrambling messages so snoops can't read them, and adding secret stamps to forms so only the real website can send requests.

## Definition

This concept covers the key technical defenses against on-path (MitM) attacks and cross-site request forgery (CSRF). For on-path attacks, the primary defenses involve encrypting communications so intercepted traffic cannot be read or modified. For CSRF, defenses focus on proving that requests originate from the legitimate application rather than an attacker-controlled site.

## Key Details

- **On-path defenses**: HTTPS everywhere, **HSTS** (HTTP Strict Transport Security—forces HTTPS on subsequent visits), **certificate pinning** (rejects unexpected certificates), **mutual TLS** (both sides authenticate with certificates).
- **CSRF defenses**: **Anti-CSRF tokens** (unique per-session or per-request values embedded in forms), **SameSite cookie attribute** (prevents cookies from being sent on cross-site requests), **re-authentication for sensitive actions**.
- **XSS defenses**: Output encoding/escaping, **Content Security Policy (CSP)** headers, input validation, **HttpOnly cookie flag** (prevents JavaScript access to session cookies).
- HSTS with a long `max-age` and `includeSubDomains` provides strong SSL stripping protection.
- Defense-in-depth is key—combine multiple controls since no single control is foolproof.

## Connections

- Parent: [[on-path-attacks]] — defenses against interception attacks
- See also: [[ssltls-stripping]], [[defenses]]
