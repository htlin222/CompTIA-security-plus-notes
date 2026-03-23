---
title: "Race condition / TOCTOU"
description: "Exploiting the timing gap between checking a condition and using the result"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A TOCTOU (Time of Check to Time of Use) race condition is a vulnerability that arises when a program checks the state of a resource (e.g., file permissions, object state) and then uses that resource, but the state can be changed between the check and the use. An attacker who can modify the resource during this window can cause the program to act on false assumptions—bypassing security checks or corrupting program logic.

## Key Details

- Classic example: **File system TOCTOU**—check if a file is safe to open (time of check), then symlink the file to /etc/shadow (time of use)—program opens the sensitive file instead.
- **Symlink attacks**: The classic file system exploitation of TOCTOU conditions.
- Also relevant in: **database transactions** (check then update without a lock), **multi-threaded applications** (shared state modified by another thread), **setuid programs** (Unix privilege escalation vector).
- Mitigation: **atomic operations** (check and use in a single uninterruptible step), **file descriptor security** (open the file once and use the descriptor), **proper locking**.
- Category: **concurrency vulnerability**—timing-dependent and often difficult to reliably reproduce.

## Connections

- Parent: [[application-attacks]] — a concurrency-based application vulnerability
- See also: [[race-conditions]]
