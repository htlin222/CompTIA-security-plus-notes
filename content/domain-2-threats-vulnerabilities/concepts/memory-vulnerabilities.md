---
title: "Memory vulnerabilities"
description: "Buffer overflows, use-after-free, memory leaks that can be exploited for code execution"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Memory vulnerabilities are a class of security flaws arising from improper handling of computer memory—including insufficient bounds checking, improper memory deallocation, and memory state management errors. These vulnerabilities can lead to crashes, information disclosure, or remote code execution. They are most prevalent in programs written in languages like C and C++ that provide direct memory management without built-in safety checks.

## Key Details

- **Buffer overflow**: Writing past the end of a buffer, overwriting adjacent memory—can redirect execution to malicious code.
- **Use-after-free**: Accessing memory after it has been deallocated—the freed memory may be reallocated for another purpose, leading to type confusion or code execution.
- **Memory leak**: Failure to release allocated memory—causes resource exhaustion (availability impact) rather than direct code execution.
- **Heap spray**: Filling heap memory with shellcode to increase the probability of landing in a predictable location after a memory vulnerability is exploited.
- Mitigations: **ASLR** (randomizes memory layout), **DEP/NX** (marks memory as non-executable), **safe languages** (Java, Rust, C# manage memory safely).

## Connections

- Parent: [[vulnerability-types]] — a category of application-level vulnerability
- See also: [[buffer-overflow]], [[integer-overflow]]
