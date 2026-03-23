---
title: "HTTPS spoofing"
description: "Presenting a fraudulent certificate to intercept encrypted web traffic"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is HTTPS Spoofing?
> You see the little padlock icon in your browser and think you're safe, but the attacker has set up a look-alike website with its own padlock. It's like a fake store with a real-looking "Open" sign.

## Definition

HTTPS spoofing involves deceiving users into believing they have a secure HTTPS connection with a legitimate site while actually connecting to an attacker-controlled server presenting a fraudulent or misleading certificate. Techniques include using look-alike domain names with valid certificates, IDN homograph attacks (using visually similar Unicode characters), or compromising a Certificate Authority to issue rogue certificates for legitimate domains.

## Key Details

- **Homograph attack**: Uses Unicode characters that look identical to ASCII (e.g., Cyrillic "а" looks like Latin "a") to register look-alike domains with valid HTTPS certificates.
- **Rogue CA certificate**: If a trusted CA is compromised, fraudulent certificates for any domain can be issued—detected via **Certificate Transparency (CT) logs**.
- **Certificate Transparency (CT)**: A public, append-only log of all issued certificates—allows organizations to monitor for unauthorized certificate issuance for their domains.
- **HSTS Preloading**: Browsers that have preloaded HSTS will reject connections using non-HTTPS or unexpected certificates.
- **Certificate pinning**: Applications reject certificates not matching a pinned key/certificate—prevents rogue CA attacks for pinned apps.

## Connections

- Parent: [[on-path-attacks]] — a technique to intercept HTTPS traffic
- See also: [[ssltls-stripping]], [[defenses]]
