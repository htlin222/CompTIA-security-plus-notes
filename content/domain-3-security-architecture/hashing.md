---
title: "Hashing"
description: "Hashing produces a fixed-length digest from input data to verify integrity, authenticate messages, and securely store passwords."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cryptography
  - weight/high
aliases:
  - "Hashing"
  - "Hash Functions"
---

> [!eli5] ELI5: What is Hashing?
> Think of hashing like a fingerprint for data. Just like every person has a unique fingerprint, hashing takes any piece of information and creates a unique code for it. If even one tiny thing changes in the original data, the fingerprint looks completely different. This makes it easy to check if something has been tampered with. Unlike encryption, you cannot turn the fingerprint back into the original -- it is a one-way process.
>
> > [!eli5] ELI5: Hashing (繁體中文版)
> > 雜湊就像是資料的指紋。即便是超大的檔案，經過雜湊運算後都會得到一段簡短且唯一的字串，只要檔案改動一點點，指紋就會完全不同。
> >
> > ```ascii
> > [大檔案] --(雜湊運算)--> [唯一的指紋]
> > ```

## Overview

Hashing is a one-way cryptographic function that converts input data of any size into a fixed-length output (hash, digest, or fingerprint). Unlike encryption, hashing is irreversible. Hashing is used to verify data integrity, authenticate messages (HMAC), store passwords securely, and create digital signatures. Any change to the input produces a completely different hash.

## Key Concepts

- **Properties of a good hash function:**
  - **Deterministic** — same input always produces the same output
  - **Fixed output length** — regardless of input size
  - **Avalanche effect** — small input change produces drastically different output
  - **Pre-image resistance** — cannot derive the input from the hash
  - **Collision resistance** — computationally infeasible to find two inputs with the same hash
- **Common hash algorithms:**
  - **MD5** — 128-bit; broken, vulnerable to collisions; do not use for security
  - **SHA-1** — 160-bit; deprecated due to collision vulnerabilities
  - **SHA-2 family** — SHA-256, SHA-384, SHA-512; current standard; widely used
  - **SHA-3** — newest standard; based on Keccak algorithm; alternative to SHA-2
- **[[hmac-hash-based-message-authentication-code|HMAC (Hash-based Message Authentication Code)]]** — combines a hash with a secret key to provide integrity AND authentication
- **[[password-hashing|Password hashing]]** — uses salting and key stretching to protect stored passwords
  - **Salt** — random value added to each password before hashing; prevents rainbow table attacks
  - **Key stretching** — intentionally slow hashing (bcrypt, scrypt, PBKDF2, Argon2) to resist brute force
  - **Rainbow table** — precomputed table of hashes; defeated by salting
- **[[digital-signatures|Digital signatures]]** — hash the message, then encrypt the hash with the sender's private key
- **[[file-integrity-monitoring|File integrity monitoring]]** — comparing current file hashes to known-good baselines to detect tampering

## Exam Tips

> [!tip] Remember
> MD5 and SHA-1 are deprecated. SHA-256 is the current standard. Hashing is one-way; encryption is two-way. HMAC = hash + key = integrity + authentication. Salt defeats rainbow tables. Bcrypt/Argon2 defeat brute force on passwords.

## Connections

- Provides the integrity component that [[encryption]] does not (encryption = confidentiality, hashing = integrity)
- Used within [[pki]] for digital signatures — the message hash is signed with the private key
- See also [[key-management]] for HMAC key handling and password hashing salt management

## Practice Questions

> [!qbank]- Q-Bank: Hashing (4 Questions)
>
> **Q1.** A forensic investigator needs to verify that a disk image has not been altered since it was collected as evidence. Which technique is MOST appropriate?
>
> A. Encrypt the disk image with AES-256
> B. Compare the current SHA-256 hash against the original hash
> C. Compress the disk image to reduce file size
> D. Store the disk image on a RAID 5 array
>
> > [!answer]- Show Answer
> > **B. Compare the current SHA-256 hash against the original hash**
> >
> > [[hashing|Hashing]] with SHA-256 provides integrity verification — if the hash matches the original, the data has not been altered. This is the standard method for [[file-integrity-monitoring|file integrity monitoring]] in forensics. Encryption (A) provides confidentiality but does not verify integrity. Compression (C) reduces size but does not detect tampering. RAID 5 (D) provides storage redundancy, not integrity verification.
>
> **Q2.** A security administrator discovers that a password database uses MD5 hashes without salting. Which attack is this system MOST vulnerable to?
>
> A. Brute force attack against the MD5 algorithm itself
> B. Rainbow table attack using precomputed MD5 hashes
> C. Man-in-the-middle attack on the authentication protocol
> D. Denial-of-service attack against the database
>
> > [!answer]- Show Answer
> > **B. Rainbow table attack using precomputed MD5 hashes**
> >
> > Without salting, identical passwords produce identical hashes, making the system vulnerable to [[hashing|rainbow table]] attacks that use precomputed hash-to-password mappings. MD5 is also deprecated and collision-prone. Brute force (A) is possible but slower than rainbow tables when salts are absent. MITM (C) targets network communication, not stored password hashes. DoS (D) targets availability, not password confidentiality.
>
> **Q3.** A developer needs to store user passwords securely. Which approach is BEST?
>
> A. Encrypt passwords with AES-256 and store the key alongside the database
> B. Hash passwords with SHA-256 without any salt
> C. Hash passwords with bcrypt using a unique salt per password
> D. Store passwords in plaintext in an access-controlled database
>
> > [!answer]- Show Answer
> > **C. Hash passwords with bcrypt using a unique salt per password**
> >
> > [[password-hashing|Bcrypt]] is a key-stretching algorithm designed for password hashing — it is intentionally slow to resist brute force and uses a unique salt per password to defeat rainbow tables. Encrypting passwords (A) means they can be decrypted if the key is compromised. SHA-256 without salt (B) is vulnerable to rainbow tables and is too fast for password hashing. Plaintext storage (D) is the worst possible approach regardless of access controls.
>
> **Q4.** A web application needs to verify both the integrity and authenticity of messages received from a partner API. Which mechanism BEST provides both?
>
> A. SHA-256 hash of the message
> B. HMAC using a shared secret key
> C. MD5 checksum
> D. CRC32 error detection
>
> > [!answer]- Show Answer
> > **B. HMAC using a shared secret key**
> >
> > [[hmac-hash-based-message-authentication-code|HMAC]] combines a hash function with a secret key, providing both integrity (the message was not altered) and authentication (it came from someone who knows the key). SHA-256 alone (A) provides integrity but not authentication since anyone can compute a hash. MD5 (C) is deprecated and also provides only integrity. CRC32 (D) is an error-detection code, not a cryptographic function, and provides neither security integrity nor authentication.

## Scenario

> See [[case-hashing]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [1.4 – Hashing and Digital Signatures](https://www.youtube.com/watch?v=EcGmQjl6XEo)
