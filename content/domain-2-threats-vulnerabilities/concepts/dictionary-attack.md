---
title: "Dictionary attack"
description: "Using a wordlist of common passwords and variations to guess credentials"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Dictionary Attack?
> Instead of trying every possible combination, this attack tries common words people actually use as passwords -- like "password," "sunshine," or "football123." It's faster because most people pick predictable passwords.

## Definition

A dictionary attack uses a predefined wordlist of common passwords, words, phrases, and their variations to systematically attempt to guess a user's password. Unlike pure brute-force attacks that try all possible combinations, dictionary attacks leverage the fact that most people choose passwords based on recognizable words or predictable patterns, making them far more efficient.

## Key Details

- Common wordlists: **RockYou** (14 million passwords from a 2009 breach), **SecLists**, **CrackStation**.
- Tools include: **Hashcat** (offline hash cracking), **John the Ripper**, **Hydra** (online attack).
- Effective against users with **weak, predictable passwords** (password, 123456, qwerty, company name + year).
- Defeated by: **account lockout policies** (online attacks), **key stretching/salting** (offline attacks), **passphrases**, **MFA**.
- Precursor to **hybrid attacks** that apply rule-based mutations to wordlist entries.

## Connections

- Parent: [[password-attacks]] — a common password attack technique
- See also: [[brute-force]], [[hybrid-attack]], [[rainbow-table-attack]]
