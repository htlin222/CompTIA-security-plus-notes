---
title: "Privilege escalation"
description: "Exploiting flaws to gain higher-level access (vertical) or access other users' data (horizontal)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Privilege Escalation?
> A regular student finds a trick to give themselves teacher-level access to the school computer. Now they can change grades, see private files, and do things they were never supposed to do.

## Definition

Privilege escalation is the act of exploiting vulnerabilities, misconfigurations, or weaknesses to gain more access rights than were originally granted. Vertical privilege escalation involves elevating from a lower privilege level to a higher one (e.g., from a regular user to an administrator or root). Horizontal privilege escalation involves accessing resources or data belonging to other users at the same privilege level.

## Key Details

- **Vertical (privilege elevation)**: Regular user → administrator; standard user → SYSTEM/root; local user → domain admin.
- **Horizontal**: Accessing another user's files, email, or resources without elevated privileges—IDOR (Insecure Direct Object Reference) is a common web application example.
- Common techniques: **unquoted service paths**, **DLL hijacking**, **SUID/GUID binaries** (Linux), **kernel exploits**, **token impersonation** (Windows).
- A critical post-exploitation step: attackers almost always seek to escalate privileges after gaining initial access.
- Defenses: **least privilege**, **regular patching**, **application hardening**, **EDR behavioral detection**.

## Connections

- Parent: [[application-attacks]] — a post-exploitation attack technique
- See also: [[least-privilege]]
