---
title: "Case: The MD5 Reckoning — Upgrading Legacy Password Storage for 8 Million Gamers"
description: "A security audit uncovers 8 million user accounts with passwords stored in unsalted MD5 hashing—a deprecated algorithm from 2006. The database was breached in 2018 and posted to the dark web. The company must migrate without triggering a mass password reset."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

Apex Legends is a global multiplayer online game with 8.2 million monthly active players. The game launched in 2009 with a PHP-based authentication system that stored user passwords using MD5 hashing. At the time, MD5 was considered acceptable for password storage (it wasn't, but it was common). Nobody had updated the authentication system in 15 years.

In March 2018, the player database was compromised—145 million account records including hashed passwords were exfiltrated. The breach went undetected for three months until a security researcher noticed the data appearing on dark web markets. By that time, the database had been distributed across thousands of paste sites and underground forums.

The company issued a mandatory password reset for all players. But not all players complied. Many accounts were inactive. Many were alt-accounts (backup characters) that the player didn't care about. Of the 8.2 million accounts, only 4.1 million players reset their passwords within 30 days. Another 1.8 million reset within 90 days. The remaining 2.3 million accounts retained their original MD5-hashed passwords.

Fast forward to October 2024 (six years later). Marcus Rodriguez, the company's Chief Information Security Officer, commissioned a password storage audit as part of their post-merger integration. The audit firm conducted a simple check: What [[hashing]] algorithm was used for password storage?

The answer shocked everyone. The authentication system had never been upgraded from MD5. All 8 million password hashes, including those from the 2018 breach that were still circulating on the dark web, were stored using unsalted MD5.

Marcus convened an emergency meeting with the Engineering Director, Jennifer Park, and the company's legal team. The implications were dire:

1. **MD5 is cryptographically broken**: Collisions can be computed in seconds on modern hardware. While MD5 password hashes aren't directly reversible, the algorithm is weak enough that rainbow tables (precomputed hash-value pairs) for MD5-hashed passwords have been published for over a billion common passwords.

2. **Passwords are unsalted**: Each password hash was computed as MD5(password)—no random salt added. This meant that two users with the same password would have identical hashes. More importantly, if a password appeared in any public rainbow table, it could be cracked immediately.

3. **The old breach data is public**: 145 million MD5 hashes from 2018 are already in threat feeds, dark web collections, and academic datasets. Attackers have six years to crack passwords using precomputed tables.

4. **Alternative algorithms were never implemented**: While the industry had moved to bcrypt (2006), scrypt (2009), and Argon2 (2015), this company was still using MD5.

Jennifer explained the technical challenge: Forcing a mass password reset to bcrypt would be operationally disastrous. Many players hadn't logged in for years. If they suddenly had to reset their password to play, they'd simply abandon their accounts. The company would lose monthly active users and revenue. Yet leaving 8 million accounts in MD5 was an unacceptable security liability.

Marcus and Jennifer developed a two-phase upgrade strategy:

**Phase 1: Upgrade on Login (Silent Migration)**
- Deploy a new authentication system that still accepts MD5-hashed passwords but generates [[digital-signatures|HMAC]] signatures of those hashes using a [[key-management|server-side secret]] key stored in an [[hardware-security-module|HSM]]
- When a user logs in with MD5 hash, the system would verify the old hash, then immediately upgrade the password to bcrypt using Argon2 as the [[hashing|password hashing]] algorithm
- The new bcrypt hash would be stored in a separate table, replacing the old MD5 hash
- This way, players wouldn't notice any difference, but their passwords would be upgraded to a modern [[hashing]] algorithm upon next login

**Phase 2: Deadline-Based Reset (Forced for Non-Logins)**
- Set a deadline (24 months) for any account still using MD5 to reset the password
- Accounts that hadn't logged in by the deadline would be transitioned to bcrypt hashes with random [[key-splitting-secret-sharing|shared secrets]] (requiring a password reset on next login)

The implementation required careful [[key-management]]:

1. **HSM Integration**: The [[hashing|HMAC signing key]] was generated inside an HSM and never exported. All signing operations would happen inside the HSM, ensuring the key never touched application servers.

2. **Key Rotation**: The signing key would be rotated quarterly. Old keys would be retained to support verification of old hashes, but new passwords would only use the current key.

3. **[[Digital-signatures|HMAC-Based]] Verification**: The system would compute HMAC-SHA256 of each MD5 hash using the HSM key, preventing attackers who gained database access from forging new hashes without the key.

4. **Argon2 Configuration**: New passwords would use Argon2id with memory cost of 64MB, time cost of 3 iterations, and parallelism of 4—providing strong resistance against brute-force attacks while keeping login latency under 100ms.

The team also discovered a secondary problem: password reset emails. Many players had outdated email addresses on file. If they tried to reset their password, the reset link would go to an email they no longer monitored. The team had to implement account recovery via security questions and SMS verification.

The upgrade was deployed in January 2025. Over 18 months, the silent migration upgraded 6.4 million passwords to bcrypt on login. Another 800,000 accounts were automatically reset to bcrypt with randomized temporary passwords sent via SMS (since emails were outdated). The remaining 1.4 million accounts were either permanently disabled (they hadn't logged in for over 24 months) or were reset when the players returned.

By September 2025, fewer than 50,000 accounts still used MD5 hashing—all of them inactive. The company decided to leave those accounts as-is rather than force a reset for players who may never return.

## What Went Right

- **Proactive audit caught the problem**: The company didn't wait for a second breach. An objective assessment identified the weakness.
- **Silent migration didn't disrupt players**: By upgrading passwords on login rather than forcing a reset, the company avoided user friction.
- **[[Key-management|HSM-based]] signing protected the upgrade process**: The [[digital-signatures|HMAC signing key]] was never exposed to attackers, preventing forgery of new password hashes.
- **Fallback mechanisms existed**: SMS-based password reset and security questions provided recovery options for users with outdated email addresses.
- **Clear timeline provided accountability**: The 24-month deadline meant that any remaining MD5 accounts were explicitly accepted as a legacy risk, not an oversight.

## What Could Go Wrong

- **MD5 passwords in circulation**: The 2018 breach data is public and searchable. MD5 password hashes can be cracked in minutes using online tools and precomputed tables.
- **Mass password reset would cause player churn**: Forcing 8 million players to reset passwords would alienate users and reduce monthly active users significantly—a business-ending scenario.
- **Weak [[hashing]] algorithm (MD5) allowed crackers years of access**: Between 2018 and 2024, any attacker with the breached database could have cracked a significant percentage of passwords offline.
- **Unsalted hashes meant identical passwords left identical hashes**: An attacker analyzing the 2018 breach database could identify accounts sharing the same password, revealing patterns or shared credentials.
- **Missing [[key-rotation]]**: If the HSM signing key had never been rotated, compromise of the key would have compromised the entire upgrade process.

## Key Takeaways

- **MD5 for passwords has been deprecated for 20+ years**: There is no excuse for MD5 in any modern system. Use Argon2id (preferred), bcrypt, or scrypt. Never use MD5, SHA1, or unsalted hashing.
- **[[Hashing|Password hashing]] should be computationally expensive**: Modern [[hashing|password hashing]] algorithms (Argon2id, bcrypt) are deliberately slow to resist brute-force attacks. Fast algorithms (MD5, SHA256) should only be used for integrity checking, not password storage.
- **Salting is mandatory, not optional**: Every password hash must include a cryptographically random salt. This prevents rainbow table attacks and makes crack time proportional to the number of unique passwords, not accounts.
- **Silent migration via login is the best approach for large user bases**: Forcing a mass password reset is operationally damaging. Upgrading passwords on next login is seamless and achieves 95%+ coverage without user friction.
- **[[Key-management|HSM-based]] secrets protect the upgrade process**: If the system uses a signing key or secret during password migration, that key must be protected in an HSM. Never store such keys in application code or environment variables.
- **Long-tail accounts are acceptable risk**: Some inactive accounts will retain weak passwords indefinitely. Setting a deadline (24 months) and then accepting the risk is reasonable governance—better than forcing a reset that will break dormant accounts.

## Related Cases

- [[case-encryption]] — Cryptographic principles underlying [[hashing|password hashing]]
- [[case-key-management]] — The HSM and key rotation strategies that protect password upgrade systems
- [[case-pki]] — Digital certificates and their hashing-based integrity mechanisms

