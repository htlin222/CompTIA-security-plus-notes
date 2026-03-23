---
title: "Live forensics vs. dead forensics"
description: "Live = analyzing a running system (captures volatile data); dead = analyzing powered-off media"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Live vs. Dead Forensics?
> Live forensics examines a running computer -- like watching a movie while it plays. Dead forensics examines a powered-off computer -- like studying a paused screenshot.

## Definition

Live forensics involves collecting and analyzing evidence from a system while it is still running, enabling capture of volatile data (RAM contents, running processes, network connections) that would be lost if the system were powered off. Dead forensics (or post-mortem forensics) involves analysis of storage media from a powered-off system, following the traditional acquire-then-analyze model.

## Key Details

- **Live forensics captures**: RAM contents, running processes, open network connections, logged-in users, decrypted content (if FDE is in use)
- **Dead forensics captures**: disk contents, file system metadata, deleted files, unallocated space
- Order of volatility dictates that live (volatile) evidence should be collected first
- Full disk encryption makes dead forensics less effective — drive is unreadable without the key
- Live forensics tools: WinPmem (RAM capture), Volatility (RAM analysis), netstat, procexp

## Connections

- Parent: [[digital-forensics]] — understanding when to use live vs. dead forensics is a key forensic skill
- See also: [[order-of-volatility]]
