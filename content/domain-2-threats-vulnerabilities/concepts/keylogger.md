---
title: "Keylogger"
description: "Records keystrokes to capture passwords, credit card numbers, and other sensitive input"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A keylogger is a type of malware (or legitimate monitoring software) that records keystrokes entered on a keyboard, capturing sensitive information such as passwords, credit card numbers, private messages, and other credentials. Keyloggers can be implemented in software (kernel-level drivers, API hooks, form grabbers) or hardware (physical devices inserted between keyboard and computer).

## Key Details

- **Software keyloggers**: Installed as malware; can be kernel-level (difficult to detect), user-level (easier to detect), or form-grabbing (captures data before encryption).
- **Hardware keyloggers**: Physical devices between keyboard and USB/PS2 port—not detectable by software security tools.
- **Form grabbers**: Browser-based keyloggers that capture form data before it's submitted—often used by banking trojans.
- Detection: **EDR solutions**, **behavioral analysis** (keylogging is detectable via API monitoring), physical inspection of computers in high-security environments.
- Mitigation: **MFA** (stolen password alone isn't enough), **on-screen keyboards** (partial mitigation), **antimalware**, **physical security**.

## Connections

- Parent: [[malware-types]] — a specific malware category focused on credential theft
- See also: [[keylogging]]
