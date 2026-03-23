---
title: "Birthday attack"
description: "Exploits the mathematics of hash collisions; finding two inputs that produce the same hash output"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A birthday attack is a cryptographic attack that exploits the birthday paradox—a probability phenomenon showing that in a group of only 23 people, there's a 50% chance two share a birthday. Applied to cryptography, it means that finding any two inputs that produce the same hash output (a collision) requires far fewer attempts than finding a specific hash. This is the basis for attacking hash functions used in digital signatures and integrity verification.

## Key Details

- Based on the **birthday paradox**: collision probability grows much faster than expected due to combinatorial mathematics.
- For a hash with an n-bit output, a birthday attack requires only ~2^(n/2) operations (not 2^n) to find a collision.
- **SHA-1** (160-bit) is vulnerable—collisions have been demonstrated (e.g., Google's SHAttered attack, 2017).
- **MD5** is fully broken for collision resistance—do not use for integrity verification.
- Defense: use modern hash functions with large outputs (**SHA-256** or **SHA-3**).

## Connections

- Parent: [[cryptographic-attacks]] — a fundamental type of cryptographic attack
- See also: [[collision-attack]], [[deprecated-algorithms]]
