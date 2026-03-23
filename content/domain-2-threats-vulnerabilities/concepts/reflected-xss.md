---
title: "Reflected XSS"
description: "Malicious script in a URL parameter is reflected back in the server's response — requires victim to click a crafted link"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Reflected Cross-Site Scripting (Reflected XSS) occurs when malicious script code included in a URL parameter or form input is immediately "reflected" back in the server's HTTP response without being stored. The script executes in the victim's browser when they click a crafted link containing the payload. It requires victim interaction (clicking the malicious link) but can be combined with phishing or social engineering to deliver the link.

## Key Details

- **Non-persistent**: The payload is not stored on the server—each victim must click the malicious link.
- Typically delivered via **phishing emails** or **malicious links** on websites.
- Common attack scenario: URL like `https://legitimate.com/search?q=<script>steal(document.cookie)</script>`.
- The server reflects the search term back in the response: `"Searching for: <script>steal(document.cookie)</script>"` — which executes in the browser.
- **Defense**: Output encoding/escaping before rendering user-supplied content in HTML context; **Content Security Policy (CSP)**.

## Connections

- Parent: [[xss-and-csrf]] — one of the three XSS variants
- See also: [[stored-persistent-xss]], [[dom-based-xss]]
