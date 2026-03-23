---
title: "File system permissions"
description: "Restricting access to sensitive files and directories"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are File System Permissions?
> Permissions decide who can read, change, or run each file. It is like putting name labels on folders: "Only Mom can open this drawer."

## Definition

File system permissions are access control mechanisms at the operating system level that determine which users and processes can read, write, execute, or modify files and directories. Properly configured file system permissions enforce the principle of least privilege by ensuring users and processes can only access the files they legitimately need for their roles.

## Key Details

- UNIX/Linux: permissions use owner/group/other model with read (r), write (w), execute (x) bits; setuid/setgid can be dangerous
- Windows: uses Access Control Lists (ACLs) with NTFS permissions including read, write, modify, full control, and special permissions
- Service accounts should have minimum necessary file system access
- Misconfigured permissions (world-writable system files) are a common privilege escalation path
- Regular permission audits are recommended to detect unnecessary access accumulation

## Connections

- Parent: [[hardening]] — proper file system permissions are a fundamental hardening control
- See also: [[least-functionality-principle]]
