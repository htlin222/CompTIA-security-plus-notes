---
title: "Domain hijacking"
description: "Taking control of a domain name through social engineering or exploiting weak registrar account security"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Domain Hijacking?
> It's like someone tricking the phone company into giving them your phone number. Now all calls meant for you go to the thief, and they can pretend to be you.

## Definition

Domain hijacking is the unauthorized takeover of a domain name by gaining control of the domain's registrar account. Attackers accomplish this by stealing registrar account credentials (via phishing or credential stuffing), social engineering the registrar's support team, or exploiting weak account security. Once in control, they can redirect all traffic, intercept email, and issue fraudulent SSL certificates.

## Key Details

- Social engineering attacks on registrar support staff ("I lost access to my account") can bypass technical controls.
- **Registry lock** (also called domain lock) prevents unauthorized transfers by requiring out-of-band verification—a key preventive control.
- Once hijacked, attackers can change **nameservers** to redirect all DNS, issue **fraudulent certificates**, and intercept email.
- High-profile examples: Fox News, New York Times, Twitter domains have been hijacked.
- Defenses: **strong MFA on registrar accounts**, **registry lock**, **WHOIS privacy protection**, **monitoring for unauthorized DNS changes**.

## Connections

- Parent: [[dns-attacks]] — domain hijacking as a DNS infrastructure attack
- See also: [[dns-hijacking]]
