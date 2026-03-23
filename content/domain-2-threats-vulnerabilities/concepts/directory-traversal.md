---
title: "Directory traversal"
description: "Using \"../\" sequences to access files outside the intended directory"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Directory traversal (also called path traversal) is a web application vulnerability where an attacker uses `../` sequences (or encoded equivalents) in file path inputs to navigate outside the web root and access sensitive files on the server's filesystem. Successful exploitation can expose configuration files, password files, private keys, and application source code.

## Key Details

- Classic payload: `../../etc/passwd` (Linux) or `..\..\..\windows\system32\` (Windows).
- URL encoding bypass: `%2e%2e%2f` is the URL-encoded form of `../`—used to bypass naive input filters.
- Can also be used to **read source code**, **private keys**, and **application configuration files** containing database credentials.
- Mitigation: **canonicalize file paths** before checking them, **validate that the resolved path starts with the expected base directory**, avoid building file paths from user input.
- Closely related to **Local File Inclusion (LFI)** in web applications.

## Connections

- Parent: [[application-attacks]] — a file access vulnerability in web applications
- See also: [[server-side-request-forgery-ssrf]]
