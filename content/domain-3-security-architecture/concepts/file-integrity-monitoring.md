---
title: "File integrity monitoring"
description: "comparing current file hashes to known-good baselines to detect tampering"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

File Integrity Monitoring (FIM) is a security technology that detects changes to files and directories by computing cryptographic hash values (MD5, SHA-256) of files and comparing them against a known-good baseline. When a file's hash changes unexpectedly, an alert is triggered, indicating potential tampering, malware infection, or unauthorized modification.

## Key Details

- Creates a baseline hash database of all monitored files at a known-good state
- Continuously or periodically recomputes hashes and alerts on changes
- Commonly monitors system binaries, configuration files, security tools, and application executables
- Required by compliance frameworks such as PCI DSS for cardholder data environments
- Tools include Tripwire, AIDE (Linux), and Windows built-in monitoring; SIEM can centralize FIM alerts

## Connections

- Parent: [[hashing]] — file integrity monitoring relies on cryptographic hashing for tamper detection
- See also: [[digital-signatures]]
