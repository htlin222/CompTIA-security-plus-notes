---
title: "Data states"
description: "data at rest, data in transit, data in use; each requires appropriate protection"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What are Data States?
> Data can be sitting still (saved on a hard drive), moving (being sent over the internet), or being used right now (open on your screen). Each state needs its own kind of protection, like how you guard a parked bike differently than one you're riding.

## Definition

Data exists in three states, each requiring distinct protection controls: **data at rest** (stored on disk, tape, or other persistent storage), **data in transit** (moving across a network), and **data in use** (actively being processed in memory or a CPU). Classification level drives the protection requirements for each state. Sensitive data must be protected in all three states to prevent unauthorized access or disclosure.

## Key Details

- **Data at rest**: protected by encryption (AES-256), access controls, and physical security; full-disk encryption (FDE) and file-level encryption are common
- **Data in transit**: protected by TLS/SSL, VPNs, and IPsec; plaintext protocols (HTTP, FTP, Telnet) are prohibited for sensitive data
- **Data in use**: most difficult to protect; techniques include Trusted Execution Environments (TEEs), memory encryption, and application-level controls
- Classification labels determine which encryption and access control requirements apply at each state
- Exam tip: questions about "data in transit" protection → think TLS, VPN; "data at rest" → think encryption at rest, FDE

## Connections

- Parent: [[data-classification]] — data state determines the appropriate protection mechanisms per classification level
- See also: [[handling-procedures]]
- See also: [[labeling-and-marking]]
