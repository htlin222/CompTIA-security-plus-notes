---
title: "Brute force"
description: "Trying all possible keys or password combinations until the correct one is found"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A brute-force attack systematically tries every possible combination of characters (for password attacks) or every possible key value (for cryptographic attacks) until the correct one is found. The feasibility of a brute-force attack depends entirely on the size of the search space—determined by key length or password complexity—and available computational resources.

## Key Details

- Time to crack grows **exponentially** with key/password length: doubling key length squares the search space.
- **128-bit AES** is computationally infeasible to brute-force with current technology.
- For passwords, mitigated by **account lockout policies**, **CAPTCHA**, **rate limiting**, and **MFA**.
- For cryptographic keys, mitigated by using **sufficiently long keys** (AES-128+, RSA-2048+).
- **GPU clusters** and cloud computing have dramatically reduced brute-force times for short passwords.

## Connections

- Parent: [[password-attacks]] — the most fundamental password attack method
- Parent: [[cryptographic-attacks]] — brute-force against encryption keys
- See also: [[dictionary-attack]], [[key-stretching]]
