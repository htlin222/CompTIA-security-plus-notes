---
title: "Man-in-the-Browser (MitB)"
description: "Malware in the browser modifies transactions in real time (e.g., changing bank account numbers)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - MitB
  - MITB
---

> [!eli5] ELI5: What is Man-in-the-Browser?
> Bad software hides inside your web browser and secretly changes what you see or send. You think you're transferring $10, but it quietly changes it to $1,000 going to the attacker.

## Definition

Man-in-the-Browser (MitB) is a sophisticated attack where malware is installed as a browser extension or plugin that intercepts and modifies web transactions in real time—after the user initiates them but before they are submitted to the server. Unlike traditional MitM attacks, MitB bypasses HTTPS because the interception occurs within the browser after decryption, before the user sees or submits the data.

## Key Details

- The malware sits **inside the browser** (as an extension or hooked DLL)—can read and modify any page content and form data.
- Classic use case: banking fraud—attacker changes the destination account number and amount in a wire transfer without the user's knowledge; the user sees the intended transaction but the bank processes the modified one.
- Bypasses **HTTPS** completely—encryption doesn't help because the interception is post-decryption.
- **Out-of-band transaction verification**: The bank sends the actual transaction details via SMS or a separate app for verification—detects MitB modifications.
- Famous examples: **Zeus** and **SpyEye** banking trojans used MitB techniques extensively.

## Connections

- Parent: [[on-path-attacks]] — a browser-based variant of MitM attacks
- See also: [[session-hijacking]]
