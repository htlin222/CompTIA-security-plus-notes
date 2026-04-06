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

> [!eli5] ELI5: What are Cross-Site Scripting and Cross-Site Request Forgery?
> These are two tricks that bad guys play on websites. Cross-site scripting is like someone taping a fake "Push this button for candy" sign on a school wall -- when kids push it, something bad happens. The website accidentally shows the attacker's trick to everyone who visits. Cross-site request forgery is different -- it's like someone secretly sending a letter to the principal with your name on it, asking to do something you never agreed to. Both attacks trick your web browser into doing things you didn't mean to do.
>
> > [!eli5] ELI5: XSS and CSRF (繁體中文版)
> > XSS 是壞人在網站上貼一段惡意腳本，讓去逛那個網站的人中招。CSRF 則是騙你在不知情的情況下，用你已經登入的身分去執行某些動作 (像是轉帳)。
> >
> > ```ascii
> > [壞人] --(貼惡意代碼)--> [網站] --(使用者造訪)--> [受害者]
> > ```

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

## Practice Questions

> [!qbank]- Q-Bank: Cross-Site Scripting and Cross-Site Request Forgery (4 Questions)
>
> **Q1.** An attacker posts a comment on a popular forum that contains a hidden JavaScript snippet. Every user who views the comment has their session cookie silently sent to the attacker's server. Which type of XSS attack is this?
>
> A. Reflected XSS
> B. Stored (Persistent) XSS
> C. DOM-based XSS
> D. CSRF
>
> > [!answer]- Show Answer
> > **B. Stored (Persistent) XSS**
> >
> > [[stored-persistent-xss|Stored XSS]] permanently saves the malicious script on the server (in this case, the forum post), affecting all users who view it. Reflected XSS (A) requires the victim to click a crafted URL — the script is not stored on the server. DOM-based XSS (C) modifies the DOM client-side without server involvement. CSRF (D) tricks browsers into making unwanted requests, not injecting scripts into pages.
>
> **Q2.** A user clicks a link in a phishing email that contains a malicious JavaScript payload in the URL parameter. The web application reflects this input back in the response page without sanitization, executing the script in the user's browser. Which attack type is this?
>
> A. Stored XSS
> B. Reflected XSS
> C. CSRF
> D. SQL injection
>
> > [!answer]- Show Answer
> > **B. Reflected XSS**
> >
> > [[reflected-xss|Reflected XSS]] includes the malicious script in a URL parameter that the server reflects back in the response without sanitization, requiring the victim to click a crafted link. Stored XSS (A) persists the script on the server permanently. CSRF (C) submits forged requests using the victim's session, not script injection. SQL injection (D) targets database queries, not client-side script execution.
>
> **Q3.** An attacker creates a webpage with a hidden form that automatically submits a fund transfer request to a banking site when visited. The attack works because the victim is currently logged into the banking site in another tab. Which attack is this?
>
> A. Reflected XSS
> B. DOM-based XSS
> C. Cross-Site Request Forgery (CSRF)
> D. Session replay
>
> > [!answer]- Show Answer
> > **C. Cross-Site Request Forgery (CSRF)**
> >
> > [[mechanism|CSRF]] tricks the victim's browser into making an authenticated request to a site where the user is already logged in, exploiting the site's trust in the user's session. Reflected XSS (A) injects script via URL parameters, not hidden form submissions. DOM-based XSS (B) modifies the client-side DOM, not forged cross-site requests. Session replay (D) retransmits captured authentication data, not browser-initiated forged requests.
>
> **Q4.** A developer wants to prevent session cookie theft through XSS attacks. Which defense MOST directly protects session cookies from JavaScript access?
>
> A. Anti-CSRF tokens
> B. Content Security Policy (CSP) headers
> C. HttpOnly cookie flag
> D. SameSite cookie attribute
>
> > [!answer]- Show Answer
> > **C. HttpOnly cookie flag**
> >
> > The HttpOnly flag prevents JavaScript from accessing session cookies via `document.cookie`, directly mitigating XSS-based cookie theft. Anti-CSRF tokens (A) protect against CSRF attacks, not XSS cookie theft. CSP headers (B) restrict which scripts can execute and help mitigate XSS broadly, but do not specifically prevent cookie access. The SameSite attribute (D) prevents cookies from being sent in cross-site requests (CSRF defense), not JavaScript access to cookies.

## Scenario

> See [[case-xss-and-csrf]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [2.3 – Cross-site Scripting](https://www.youtube.com/watch?v=PKgw0CLZIhE)
