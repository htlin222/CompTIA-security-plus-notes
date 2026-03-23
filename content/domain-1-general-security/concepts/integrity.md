---
title: "Integrity"
description: "Ensuring data is accurate, complete, and unaltered by unauthorized parties"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Integrity?
> Integrity means your information stays exactly the way you left it. Nobody sneaks in and changes your answers on a test, swaps numbers in a report, or messes with your files.

## Definition

Integrity is the second pillar of the CIA Triad, ensuring that data and systems remain accurate, complete, and unmodified by unauthorized parties. Threats to integrity include data tampering, unauthorized modifications, man-in-the-middle attacks that alter data in transit, and malware that corrupts files. Controls that protect integrity include hashing, digital signatures, access controls, and checksums.

## Key Details

- **Hashing** (SHA-256, SHA-3): Produces a fixed-length fingerprint of data—any modification changes the hash, revealing tampering.
- **Digital signatures**: Combine hashing and asymmetric cryptography to prove both integrity and authenticity.
- **File integrity monitoring (FIM)**: Tools like Tripwire detect unauthorized changes to critical system files.
- The DAD Triad counterpart to integrity is **Alteration**.
- **Code signing**: Software signed by its developer allows users to verify the code hasn't been modified after signing.

## Connections

- Parent: [[cia-triad]] — the "I" in CIA Triad
- See also: [[confidentiality]], [[availability]]
