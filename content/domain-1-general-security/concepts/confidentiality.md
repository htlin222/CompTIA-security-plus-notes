---
title: "Confidentiality"
description: "Protecting data from unauthorized access or disclosure"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Confidentiality?
> Confidentiality means keeping secrets secret. Only the people who are supposed to read your diary get to read it -- everyone else is locked out.

## Definition

Confidentiality is the first pillar of the CIA Triad, focused on ensuring that sensitive information is accessible only to authorized individuals and protected from unauthorized disclosure. Threats to confidentiality include eavesdropping, data breaches, insider threats, and unencrypted data transmission. Controls include encryption, access controls, data classification, and need-to-know policies.

## Key Details

- Achieved through: **encryption** (at rest and in transit), **access controls**, **data classification**, **DLP (Data Loss Prevention)**.
- **Data at rest**: Encrypted with AES; protected by file/disk encryption (BitLocker, FileVault).
- **Data in transit**: Protected by TLS/HTTPS, VPNs, and encrypted protocols (SSH, SFTP).
- The DAD Triad counterpart to confidentiality is **Disclosure**.
- Confidentiality must be balanced with availability—overly restrictive controls can prevent legitimate access.

## Connections

- Parent: [[cia-triad]] — the "C" in CIA Triad
- See also: [[integrity]], [[availability]]
