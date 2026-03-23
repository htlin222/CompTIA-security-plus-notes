---
title: "Integer overflow"
description: "Exceeding the maximum value of an integer variable, causing unexpected behavior"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is an Integer Overflow?
> Remember when a car odometer hits 999,999 and rolls back to 000,000? That's what happens when a number in a program gets too big -- it wraps around and causes weird, exploitable behavior.

## Definition

An integer overflow occurs when an arithmetic operation produces a value that exceeds the maximum size that the integer data type can hold, causing the value to "wrap around" to a small or negative number. In security contexts, this unexpected behavior can be exploited to bypass security checks, cause buffer overflows (by making an allocation size smaller than expected), or corrupt application logic.

## Key Details

- An 8-bit unsigned integer can hold 0–255; adding 1 to 255 wraps to 0—unexpected for most program logic.
- **Security impact**: If an integer overflow reduces an expected buffer size, the subsequent allocation is too small—leading to a buffer overflow when data is written.
- Can be exploited to **bypass size checks**: `if (user_input + 10 < MAX_SIZE)` can be fooled if `user_input + 10` overflows.
- Relevant in: image parsers, cryptographic implementations, network packet parsing, and any code handling untrusted size values.
- Mitigation: use **safe integer libraries**, enable compiler flags (`-fsanitize=integer`), validate size calculations explicitly.

## Connections

- Parent: [[application-attacks]] — a numeric vulnerability in application code
- See also: [[buffer-overflow]]
