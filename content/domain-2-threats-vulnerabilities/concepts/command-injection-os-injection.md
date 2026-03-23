---
title: "Command injection (OS injection)"
description: "Inserting operating system commands through application inputs to execute on the host system"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Command injection (also called OS injection) occurs when an attacker inserts malicious operating system commands into an application's input fields that are then executed by the underlying host system. This typically happens when an application passes user input to a system shell (e.g., `exec()`, `system()`, `popen()`) without proper sanitization, allowing the attacker to run arbitrary commands with the application's privileges.

## Key Details

- Classic payload: appending commands with shell separators: `; cat /etc/passwd`, `&& whoami`, `| ls -la`.
- Severity: **Critical**—can lead to complete server compromise, data exfiltration, or lateral movement.
- Unlike SQLi (which targets databases), command injection targets the **OS shell**.
- Mitigations: **avoid calling OS commands from user input**, use language-native libraries instead, implement strict **input validation** and allowlisting, run applications with **least privilege**.
- Common in **IoT devices**, **web applications**, and **network device management interfaces**.

## Connections

- Parent: [[injection-attacks]] — a category of injection vulnerability
- See also: [[sql-injection-sqli]], [[input-validation]]
