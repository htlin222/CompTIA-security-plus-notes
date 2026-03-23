---
title: "Virus"
description: "Requires a host file to execute; spreads when the infected file is opened or executed"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Virus?
> A computer virus is like a cold -- it hides inside a file, and when you open that file, it spreads to other files. It can't travel on its own; it needs you to pass the infected file along.

## Definition

A virus is a type of malware that requires a host file or program to function—it attaches itself to or inserts its code into an existing legitimate file (executable, document, script). Unlike worms, viruses do not spread independently; they propagate when the infected file is shared and executed by another user or system. When the infected file runs, the virus executes its payload and may infect additional files.

## Key Details

- **Key distinction from worms**: Viruses require user action to spread (sharing infected files); worms spread autonomously through networks.
- **Types**: File infectors (attach to executables), boot sector viruses (infect MBR), macro viruses (embedded in Office documents), multipartite (infect both files and boot sector).
- **Macro viruses**: Particularly relevant in enterprise environments—malicious macros in Word/Excel documents; delivered via email.
- **Polymorphic and metamorphic viruses**: Change their signature to evade antivirus detection.
- Detection: **signature-based scanning** (known patterns), **heuristic analysis** (suspicious code patterns), **behavioral monitoring**.

## Connections

- Parent: [[malware-types]] — a file-based malware that requires a host
- See also: [[worm]], [[trojan]]
