---
title: "DLL injection"
description: "Forcing a process to load a malicious dynamic-link library into its address space"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

DLL injection is a technique used by malware and attackers to execute malicious code within the context of a running process by loading a malicious Dynamic-Link Library (DLL) into that process's memory space. Since the malicious code runs inside a trusted process, it can evade process-based security controls, inherit the process's privileges, and access its resources and memory.

## Key Details

- Common injection methods: **LoadLibrary injection**, **reflective DLL injection** (loads DLL from memory without touching disk), **process hollowing**.
- Malicious DLLs can **hook API calls**, steal data, establish persistence, or escalate privileges.
- Used extensively in **malware** (banking trojans, RATs) and in legitimate security tools (AV engines, DRM).
- **DLL search order hijacking**: Placing a malicious DLL in a location that's searched before the legitimate one—a common privilege escalation technique.
- Detection: monitoring for unexpected DLL loads, process behavior analysis (EDR).

## Connections

- Parent: [[injection-attacks]] — a code injection technique targeting Windows processes
- See also: [[fileless-malware]]
