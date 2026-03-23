---
title: "Impact"
description: "Session cookie theft, account hijacking, defacement, keylogging, phishing via injected forms; unauthorized actions as authenticated user"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is the Impact of XSS and CSRF?
> With XSS, the attacker can steal your login session and pretend to be you on a website. With CSRF, they can make your browser do things on websites you're logged into -- like transferring money -- without you knowing.

## Definition

This concept covers the impacts of XSS (Cross-Site Scripting) and CSRF (Cross-Site Request Forgery) attacks. XSS enables attackers to steal session cookies, hijack accounts, deface pages, log keystrokes, and inject phishing forms into trusted sites. CSRF causes unauthorized actions—such as fund transfers, password changes, or data modifications—to be executed using the victim's authenticated session without their knowledge.

## Key Details

- **XSS impact**: **Session cookie theft** (using `document.cookie`)—enables account hijacking; **defacement**; **keylogging** via injected scripts; **phishing** by injecting fake login forms on real domains.
- **CSRF impact**: **Unauthorized transactions** (bank transfers, purchases), **account modifications** (password/email changes), **data deletion/modification**—all performed with the victim's identity.
- XSS impact is **wider** (affects all victims who view the page) in stored/persistent XSS scenarios.
- **HttpOnly cookie flag** prevents JavaScript from accessing session cookies—mitigates XSS-based cookie theft.
- CSRF impact is limited to what the victim is **authorized to do**—but that can be very significant for privileged users.

## Connections

- Parent: [[xss-and-csrf]] — the consequences of XSS and CSRF attacks
- See also: [[session-hijacking]]
