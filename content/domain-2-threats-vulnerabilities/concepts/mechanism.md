---
title: "CSRF Mechanism"
description: "Attacker crafts a request using hidden forms or image tags that perform actions using the victim's authenticated session"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is the CSRF Mechanism?
> Your browser automatically sends your login cookie with every request to a website. The attacker hides a request on their page, and when you visit it, your browser sends that request to the real site as if you asked for it.

## Definition

The CSRF attack mechanism works by exploiting the fact that browsers automatically include cookies (including session cookies) with every request to a domain, regardless of the origin of the request. An attacker crafts a malicious request—embedded in a hidden form, an image tag, or a JavaScript fetch call on their own website—that performs a state-changing action on a target site. When the victim visits the attacker's page while logged into the target, the browser sends the forged request with valid authentication.

## Key Details

- The key technical requirement: the target site uses **session cookies for authentication** and doesn't verify request origin.
- **GET-based CSRF**: Simple—`<img src="https://target.com/action?param=evil">` triggers a GET request automatically.
- **POST-based CSRF**: Requires a hidden form with JavaScript auto-submission—more powerful for state-changing actions.
- The attack requires the **victim to be authenticated** to the target site at the time of visiting the attacker's page.
- **SameSite cookie attribute** (Strict or Lax): Instructs the browser not to send cookies on cross-site requests—one of the most effective modern defenses.

## Connections

- Parent: [[xss-and-csrf]] — the technical mechanism of CSRF attacks
- See also: [[example]]
