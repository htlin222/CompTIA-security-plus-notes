---
title: "DOM-based XSS"
description: "Script executes by modifying the DOM in the victim's browser without server involvement"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is DOM-based XSS?
> The bad code runs entirely inside your own browser without even talking to the website's server. It's like a trick that makes your own notebook write something harmful without the teacher ever seeing it.

## Definition

DOM-based Cross-Site Scripting (DOM XSS) is a type of XSS attack where the vulnerability exists in client-side JavaScript code that unsafely processes data from attacker-controllable sources (like the URL fragment or `document.location`) and writes it to dangerous DOM sinks (like `innerHTML` or `eval()`). Unlike reflected or stored XSS, the malicious payload never touches the server—it executes entirely within the victim's browser.

## Key Details

- **Sources**: URL hash (`#fragment`), `document.location`, `document.referrer`, `window.name`, `localStorage`.
- **Sinks**: `innerHTML`, `document.write()`, `eval()`, `setTimeout()` with string input, jQuery `$()` with string.
- Does not appear in server-side logs—makes it harder to detect through server-level monitoring.
- Mitigation: use safe DOM APIs (`textContent` instead of `innerHTML`), **avoid `eval()`**, implement **Content Security Policy (CSP)**.
- Can be found using static analysis of JavaScript code and dynamic scanning tools.

## Connections

- Parent: [[xss-and-csrf]] — a client-side variant of XSS
- See also: [[reflected-xss]], [[stored-persistent-xss]]
