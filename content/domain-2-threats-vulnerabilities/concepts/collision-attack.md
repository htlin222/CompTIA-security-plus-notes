---
title: "Collision attack"
description: "Specifically crafting two different inputs that produce an identical hash — compromises integrity verification"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A collision attack targets hash functions by finding two distinct inputs that produce the same hash output (a collision). Unlike birthday attacks (which find any collision), practical collision attacks often focus on crafting meaningful documents or data that collide. A successful collision attack against a hash function used in digital signatures allows an attacker to substitute fraudulent data while maintaining a valid signature.

## Key Details

- **MD5** collisions can be computed in seconds on modern hardware—completely broken for security use.
- **SHA-1** was practically broken in 2017 (Google's SHAttered attack)—two different PDF files with the same SHA-1 hash.
- Used to attack **certificate authorities**—a rogue certificate with the same hash as a legitimate one could be signed.
- **SHA-256** and **SHA-3** are currently collision-resistant and recommended for security applications.
- Collision resistance is critical for **digital signatures**, **software integrity verification**, and **certificate validation**.

## Connections

- Parent: [[cryptographic-attacks]] — a direct attack on hash function security
- See also: [[birthday-attack]], [[deprecated-algorithms]]
