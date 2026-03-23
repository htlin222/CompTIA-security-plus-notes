---
title: "Password spraying"
description: "Trying a small number of common passwords against many accounts to avoid lockout thresholds"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Password spraying is an attack technique that inverts traditional brute-force: instead of trying many passwords against one account (which triggers lockout), the attacker tries a very small number of commonly used passwords (often just one or two) against a large number of different accounts. This stays below lockout thresholds per account while still achieving successful logins for accounts with weak passwords.

## Key Details

- **Lockout evasion**: Tries only 1-3 passwords per account per time period—stays below the lockout threshold (typically 5-10 failures).
- Common spray passwords: `SeasonYear!` (Summer2024!), `CompanyName1`, `Password1`, `Welcome1`.
- Highly effective in environments with **weak password policies** or no MFA.
- Detection: many accounts receiving exactly 1-2 failed login attempts within a short window—unusual pattern.
- **MFA** is the most effective defense—a correct password is insufficient without the second factor.

## Connections

- Parent: [[password-attacks]] — a stealthy alternative to traditional brute-force
- See also: [[brute-force]], [[credential-stuffing]]
