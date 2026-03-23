---
title: "HTML injection"
description: "Inserting HTML markup into web pages to alter content or redirect users"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is HTML Injection?
> It's like someone sneaking a fake poster onto the school bulletin board that looks official but sends students to the wrong room. The attacker adds fake content to a real website.

## Definition

HTML injection is a web application vulnerability where an attacker inserts malicious HTML code into a web page that is then rendered by other users' browsers. Unlike XSS (which injects scripts), HTML injection focuses on injecting markup to alter the visual appearance of a page, redirect users to phishing sites, display fake login forms to steal credentials, or insert malicious links.

## Key Details

- Less severe than XSS (no JavaScript execution) but still dangerous—can create convincing phishing content within legitimate sites.
- Common vectors: comment fields, user profiles, message boards, any field that accepts and displays user input in HTML context.
- **Stored HTML injection** persists on the server and affects all users who view the injected content.
- **Reflected HTML injection** is delivered via a crafted URL and affects users who click the link.
- Mitigation: **output encoding/escaping** HTML special characters (`<`, `>`, `"`, `&`) before rendering user input.

## Connections

- Parent: [[injection-attacks]] — a web application injection vulnerability
- See also: [[stored-persistent-xss]], [[reflected-xss]]
