---
title: "Race conditions"
description: "Timing-dependent flaws where concurrent processes can interfere with each other"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Race Conditions?
> When two people try to grab the last cookie at the same time, weird things happen. Race conditions are when two computer tasks bump into each other because they're running at the same time and nobody took turns.

## Definition

Race conditions are security vulnerabilities that arise when the security behavior of a system depends on the timing and sequence of multiple concurrent operations—and attackers can influence that timing. When two or more threads or processes access shared resources without proper synchronization, an attacker who can manipulate the ordering of operations can cause unexpected or malicious outcomes.

## Key Details

- Occur in **multi-threaded** and **multi-process** environments where shared state is not properly protected.
- **TOCTOU** (Time of Check to Time of Use) is the most well-known security-relevant race condition.
- Common in: **operating system kernels** (privileged code paths), **web applications** (session management), **database transactions** (unprotected concurrent updates), **file systems**.
- **Mitigation**: Proper use of **mutexes, semaphores, and locks**; **atomic operations**; **database transactions** with appropriate isolation levels.
- Detection: **static analysis** tools for concurrency issues, **fuzzing** with timing manipulation, **code review** focusing on shared state access.

## Connections

- Parent: [[vulnerability-types]] — a concurrency-based vulnerability category
- See also: [[race-condition-toctou]]
