---
title: "Cross-Site Scripting and Cross-Site Request Forgery"
description: "Client-side web attacks that exploit trust between users, browsers, and web applications"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/high
aliases:
  - "XSS"
  - "CSRF"
---

## Overview

Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) are client-side web vulnerabilities that exploit the trust relationship between users and web applications. XSS injects malicious scripts into web pages viewed by other users. CSRF tricks authenticated users into performing unintended actions on a web application. Both are critical topics on the Security+ exam and appear in the OWASP Top 10.

## Key Concepts

### XSS (Cross-Site Scripting)

- **[[reflected-xss|Reflected XSS]]**: Malicious script is included in a URL parameter and reflected back in the server's response — requires victim to click a crafted link
- **[[stored-persistent-xss|Stored (Persistent) XSS]]**: Malicious script is permanently stored on the target server (e.g., in a forum post) — affects all users who view the content
- **[[dom-based-xss|DOM-based XSS]]**: Script executes by modifying the DOM in the victim's browser without server involvement
- **[[impact|Impact]]**: Session cookie theft, account hijacking, defacement, keylogging, phishing via injected forms
- **[[defenses|Defenses]]**: Output encoding/escaping, Content Security Policy (CSP) headers, input validation, HttpOnly cookie flag

### CSRF (Cross-Site Request Forgery)

- **[[mechanism|Mechanism]]**: Attacker crafts a request (e.g., hidden form or image tag) that performs an action using the victim's authenticated session
- **[[example|Example]]**: A hidden image tag that triggers a bank transfer while the victim is logged into their banking site
- **[[impact|Impact]]**: Unauthorized actions performed as the authenticated user — fund transfers, password changes, data modification
- **[[defenses|Defenses]]**: Anti-CSRF tokens (unique per-session or per-request), SameSite cookie attribute, requiring re-authentication for sensitive actions

## Exam Tips

> [!tip] Remember
> XSS = attacker injects script into a page that OTHER USERS see (exploits user trust in the site). CSRF = attacker tricks the user's BROWSER into making requests (exploits site trust in the user). XSS steals data; CSRF performs actions.

- Stored XSS is more dangerous than reflected XSS because it affects all visitors
- HttpOnly cookies prevent JavaScript from accessing session cookies (mitigates XSS cookie theft)
- CSRF tokens must be unique and validated server-side for every state-changing request

## Connections

- Subcategory of [[application-attacks]] targeting the client side of web applications
- Related to [[injection-attacks]] — XSS is essentially JavaScript injection into HTML pages
- Discovered during [[penetration-testing]] web application assessments
- [[mitigation-techniques]] include CSP headers, token-based defenses, and secure cookie attributes

## Scenario

> See [[case-xss-and-csrf]] for a practical DevOps scenario applying these concepts.
