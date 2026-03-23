---
title: "Hash verification"
description: "Using MD5/SHA-256 hashes to prove the forensic copy is identical to the original"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Hash verification in digital forensics is the process of computing a cryptographic hash value of both the original evidence and the forensic copy (image) and comparing them to verify that the copy is identical to the original, bit-for-bit. A matching hash proves that the forensic copy has not been altered and accurately represents the original evidence, supporting its admissibility in legal proceedings.

## Key Details

- Hash is calculated before and after imaging — must match exactly to prove integrity
- Common algorithms used: MD5 (faster, 128-bit), SHA-256 (stronger, 256-bit), or both
- Hash values are recorded in the chain of custody documentation
- Hash verification must also be performed each time evidence is accessed or transferred
- A non-matching hash indicates the evidence has been modified and its integrity is compromised

## Connections

- Parent: [[digital-forensics]] — hash verification is fundamental to maintaining evidence integrity
- See also: [[chain-of-custody]]
