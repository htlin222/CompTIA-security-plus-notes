---
title: "Password Attacks"
description: "Techniques used to discover, crack, or bypass password-based authentication"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/identity
  - weight/high
aliases:
  - "Credential Attacks"
---

> [!eli5] ELI5: What are Password Attacks?
> Your password is like the combination to your locker. Password attacks are all the different ways someone might try to figure out that combination. They could try every single number one by one (brute force), guess common ones like "1234" (dictionary attack), or find a list of combinations that leaked from another school (credential stuffing). Some attackers don't even try to guess -- they just watch you type it in. That's why using long, unique passwords and not reusing them matters so much.

## Overview

Password attacks target the most common authentication mechanism — passwords — using various techniques to discover, guess, or steal credentials. Despite advances in authentication, passwords remain widespread, making password attacks a persistent and high-priority threat. The Security+ exam tests knowledge of attack methods, defenses, and the relationship between password attacks and other security controls.

## Key Concepts

- **[[brute-force|Brute force]]**: Systematically trying every possible combination until the correct password is found
- **[[dictionary-attack|Dictionary attack]]**: Using a wordlist of common passwords and variations to guess credentials
- **[[password-spraying|Password spraying]]**: Trying a small number of common passwords against many accounts to avoid lockout thresholds
- **[[credential-stuffing|Credential stuffing]]**: Using stolen username/password pairs from breached databases to log into other services
- **[[rainbow-table-attack|Rainbow table attack]]**: Using precomputed hash-to-password lookup tables to crack hashed passwords quickly
- **[[salting|Salting]]**: Adding random data to passwords before hashing to defeat rainbow table attacks
- **[[hybrid-attack|Hybrid attack]]**: Combining dictionary words with brute-force modifications (e.g., "Password1!", "Summer2026!")
- **[[pass-the-hash|Pass-the-hash]]**: Using a captured NTLM hash to authenticate without knowing the actual password
- **[[kerberoasting|Kerberoasting]]**: Extracting and cracking service account ticket hashes from Active Directory
- **[[keylogging|Keylogging]]**: Capturing passwords as users type them using hardware or software keyloggers
- **[[shoulder-surfing|Shoulder surfing]]**: Physically observing someone entering their password

## Exam Tips

> [!tip] Remember
> Password spraying avoids lockout (few passwords, many accounts). Credential stuffing exploits password reuse. Rainbow tables are defeated by SALTING. Pass-the-hash works without knowing the plaintext password.

- Account lockout policies defend against brute force but NOT password spraying
- Salting makes each hash unique even for identical passwords — renders rainbow tables useless
- Longer passwords (passphrases) are more secure than complex short passwords

## Connections

- [[mfa]] is the strongest defense — even if a password is compromised, a second factor is required
- [[authentication]] systems must implement lockout, complexity, and history policies to resist these attacks
- Credential stuffing exploits reuse across services, highlighting the value of [[sso]] reducing password count
- Password hashes may be obtained through [[network-attacks]] or compromised databases

## Scenario

> See [[case-password-attacks]] for a practical DevOps scenario applying these concepts.
