---
title: "Cryptographic Attacks"
description: "Attacks targeting cryptographic implementations to break encryption, forge signatures, or bypass protections"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/cryptography
  - weight/medium
aliases:
  - "Crypto Attacks"
---

> [!eli5] ELI5: What are Cryptographic Attacks?
> Think of a secret code you and your best friend use to pass notes in class. Cryptographic attacks are when someone figures out how to crack your code and read your private messages. Maybe they notice patterns, or maybe your code is too simple. Some attackers even trick you into using an easier code that's simpler to break. This is why computers need really strong codes (called encryption) to keep secrets safe, and why old, weak codes need to be replaced with better ones.
>
> > [!eli5] ELI5: Cryptographic Attacks (繁體中文版)
> > 加密攻擊是想辦法破解被鎖起來的訊息。壞人可能會利用數學上的弱點，或是在你加密的過程中偷看一些線索。
> >
> > ```ascii
> > [加密後的訊息] --(破解/攻擊)--> [原始訊息]
> > ```

## Overview

Cryptographic attacks target weaknesses in cryptographic algorithms, implementations, or key management practices to decrypt protected data, forge digital signatures, or bypass security controls. While modern algorithms are generally secure when properly implemented, flaws in implementation, key management, or the use of deprecated algorithms create exploitable vulnerabilities. The exam focuses on understanding attack types and knowing which algorithms are considered secure.

## Key Concepts

- **[[brute-force|Brute force]]**: Trying all possible keys until the correct one is found — feasibility depends on key length
- **[[birthday-attack|Birthday attack]]**: Exploits the mathematics of hash collisions; finding two inputs that produce the same hash output
- **[[collision-attack|Collision attack]]**: Specifically crafting two different inputs that produce an identical hash — compromises integrity verification
- **[[downgrade-attack|Downgrade attack]]**: Forcing a system to use a weaker, vulnerable cryptographic protocol or cipher (e.g., POODLE forcing SSL 3.0)
- **[[known-plaintext-attack|Known plaintext attack]]**: Attacker has both plaintext and corresponding ciphertext and uses them to derive the key
- **[[chosen-plaintextciphertext-attack|Chosen plaintext/ciphertext attack]]**: Attacker can encrypt or decrypt chosen data to extract information about the key
- **[[side-channel-attacks|Side-channel attacks]]**: Exploiting physical characteristics (timing, power consumption, electromagnetic emissions) rather than algorithmic weaknesses
- **[[key-stretching|Key stretching]]**: Techniques (PBKDF2, bcrypt, scrypt) that make brute force against passwords computationally expensive
- **[[deprecated-algorithms|Deprecated algorithms]]**: MD5 and SHA-1 (collision-vulnerable), DES (56-bit key too short), RC4 (biases in keystream)
- **[[quantum-computing-threat|Quantum computing threat]]**: Shor's algorithm could break RSA and ECC; post-quantum cryptography is being standardized

## Exam Tips

> [!tip] Remember
> MD5 and SHA-1 = broken (collisions found). DES = too short (56-bit). Use SHA-256+ for hashing, AES-256 for symmetric encryption. Downgrade attacks force weaker crypto — disable legacy protocols to prevent them.

- Birthday attack effectiveness: a 128-bit hash only provides 64 bits of collision resistance
- Key stretching (bcrypt, PBKDF2) is the defense for password hashing — NOT plain SHA-256
- Know that quantum computing threatens asymmetric crypto (RSA, ECC) more than symmetric (AES)

## Connections

- Targets [[encryption]] implementations and protocols — understanding these attacks informs proper crypto choices
- [[password-attacks]] overlap with brute-force attacks on cryptographic keys and hashed passwords
- Downgrade attacks can undermine [[vpn]] and TLS connections by forcing weak cipher suites
- Understanding these attacks is essential for [[vulnerability-types]] assessment in cryptographic systems

## Practice Questions

> [!qbank]- Q-Bank: Cryptographic Attacks (4 Questions)
>
> **Q1.** During a TLS negotiation, an attacker intercepts the handshake and manipulates it so the client and server agree to use SSL 3.0 instead of TLS 1.3. Which type of cryptographic attack is this?
>
> A. Birthday attack
> B. Brute force attack
> C. Downgrade attack
> D. Known plaintext attack
>
> > [!answer]- Show Answer
> > **C. Downgrade attack**
> >
> > Forcing a system to negotiate a weaker protocol version is a [[downgrade-attack]], such as the POODLE attack which forced SSL 3.0. A birthday attack (A) exploits hash collision probability. Brute force (B) tries all possible keys. Known plaintext (D) requires having both plaintext and ciphertext pairs to derive the key.
>
> **Q2.** A security analyst finds that an application stores user passwords using unsalted MD5 hashes. An attacker with access to the database could MOST efficiently recover passwords using which technique?
>
> A. Brute force attack
> B. Rainbow table attack
> C. Side-channel attack
> D. Chosen ciphertext attack
>
> > [!answer]- Show Answer
> > **B. Rainbow table attack**
> >
> > Unsalted hashes are vulnerable to [[rainbow-table-attack]]s, which use precomputed hash-to-password lookup tables for rapid cracking. MD5 is a [[deprecated-algorithms|deprecated algorithm]] with widely available rainbow tables. Brute force (A) would work but is far slower than precomputed tables. Side-channel attacks (C) exploit physical characteristics, not hash weaknesses. Chosen ciphertext (D) applies to encryption schemes, not password hash cracking.
>
> **Q3.** A researcher generates two different PDF documents that produce the same SHA-1 hash value. Which cryptographic attack has been demonstrated?
>
> A. Known plaintext attack
> B. Brute force attack
> C. Collision attack
> D. Replay attack
>
> > [!answer]- Show Answer
> > **C. Collision attack**
> >
> > Creating two different inputs with an identical hash output is a [[collision-attack]], which compromises integrity verification. This is why SHA-1 is considered a [[deprecated-algorithms|deprecated algorithm]]. Known plaintext (A) requires matching plaintext-ciphertext pairs to derive a key. Brute force (B) tries all possible inputs rather than crafting specific collisions. Replay attack (D) involves retransmitting captured data, not hash manipulation.
>
> **Q4.** An organization is concerned about future quantum computing threats to its current RSA-2048 encryption. Which statement BEST describes the quantum computing risk to cryptography?
>
> A. Quantum computers threaten symmetric encryption more than asymmetric encryption
> B. Quantum computers can break AES-256 in polynomial time using Grover's algorithm
> C. Quantum computers threaten asymmetric encryption (RSA, ECC) more than symmetric encryption
> D. Quantum computers make all current encryption immediately obsolete
>
> > [!answer]- Show Answer
> > **C. Quantum computers threaten asymmetric encryption (RSA, ECC) more than symmetric encryption**
> >
> > Shor's algorithm on a quantum computer could break RSA and ECC, while symmetric algorithms like AES are less affected — the [[quantum-computing-threat]] primarily targets asymmetric cryptography. Option A is backwards. Option B is incorrect because Grover's algorithm only halves the effective key length of symmetric encryption (AES-256 becomes AES-128 equivalent), not polynomial-time breakage. Option D overstates the threat — symmetric encryption remains viable with sufficient key lengths.

## Scenario

> See [[case-cryptographic-attacks]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [2.4 – Cryptographic Attacks](https://www.youtube.com/watch?v=7aJaEQy6Yoc)
