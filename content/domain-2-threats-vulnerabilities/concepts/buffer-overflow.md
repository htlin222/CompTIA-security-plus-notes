---
title: "Buffer overflow"
description: "Sending more data than a buffer can hold, overwriting adjacent memory to execute arbitrary code"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Buffer Overflow?
> You know how pouring too much water into a glass makes it spill onto the table? A buffer overflow is when a program gets more data than it can hold, and the extra spills into places it shouldn't, letting attackers take over.

## Definition

A buffer overflow occurs when a program writes more data to a buffer (a fixed-size memory block) than it can hold, causing the excess data to overwrite adjacent memory regions. Attackers craft this overflow to overwrite the return address on the stack, redirecting program execution to attacker-controlled shellcode. Buffer overflows are a classic and historically significant vulnerability, particularly in C and C++ programs that do not perform bounds checking.

## Key Details

- **Stack-based buffer overflow**: Overwrites the stack return address—most classic and common type.
- **Heap-based buffer overflow**: Overwrites heap memory, more complex to exploit.
- Mitigations include: **ASLR** (Address Space Layout Randomization), **DEP/NX** (Data Execution Prevention/No-Execute), **stack canaries**, **safe C functions** (e.g., `strncpy` instead of `strcpy`).
- Languages like **Java, Python, and C#** perform automatic bounds checking, preventing buffer overflows.
- Famous examples: **Morris Worm (1988)**, **Code Red (2001)**, many early Windows exploits.

## Connections

- Parent: [[application-attacks]] — a fundamental application vulnerability
- See also: [[memory-vulnerabilities]], [[integer-overflow]]
