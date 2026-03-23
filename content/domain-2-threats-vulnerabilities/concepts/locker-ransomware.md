---
title: "Locker ransomware"
description: "Locks the user out of the system entirely without necessarily encrypting files"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Locker Ransomware?
> Instead of scrambling your files, this type just locks your whole screen with a big scary message. Your stuff is usually still there -- you just can't get to it until you get past the lock.

## Definition

Locker ransomware prevents users from accessing their systems by locking the desktop, displaying a full-screen ransom message, and disabling normal user interaction—without necessarily encrypting files. Unlike encryption-based ransomware, locker ransomware typically targets the operating system interface rather than individual files, making it somewhat less severe since files often remain intact on disk.

## Key Details

- Often targets the **Windows login process** or **desktop shell** to prevent normal OS operation.
- May masquerade as law enforcement messages ("Your computer has been locked by the FBI") to intimidate victims.
- Early ransomware families (e.g., Police Trojan, Reveton) were primarily lockers.
- Less destructive than encryption ransomware—files are not encrypted, so system restore or boot from external media may allow recovery.
- Modern ransomware is predominantly encryption-based; locker ransomware is now less common but still encountered.

## Connections

- Parent: [[ransomware]] — a type of ransomware that restricts access through locking
- See also: [[encryption-based-ransomware]]
