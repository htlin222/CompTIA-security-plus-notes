---
title: "Stored (Persistent) XSS"
description: "Malicious script permanently stored on the server — affects all users who view the infected content"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Stored (Persistent) Cross-Site Scripting is the most dangerous form of XSS, where malicious script code is permanently saved on the target server—typically in a database, comment field, forum post, or user profile—and then served to all users who view that content. Unlike reflected XSS (which requires the victim to click a link), stored XSS automatically executes in every visitor's browser without any additional attacker action.

## Key Details

- **Persistence**: The payload is stored on the server and served to all subsequent users automatically—maximum blast radius.
- Common injection points: **comment fields**, **user profiles**, **forum posts**, **product reviews**, **chat messages**, **form fields stored in databases**.
- Attacker injects once; the stored script executes for **every visitor** to the affected page—potentially thousands of victims.
- **Impact**: Session cookie theft, account hijacking at scale, browser-based malware distribution, defacement, phishing via injected forms.
- **Mitigation**: **Output encoding** before rendering stored user content in HTML; **Content Security Policy (CSP)** to restrict script execution; **input validation** and sanitization on storage.

## Connections

- Parent: [[xss-and-csrf]] — the most severe XSS variant
- See also: [[reflected-xss]], [[dom-based-xss]]
