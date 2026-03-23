---
title: "Scripting languages"
description: "Bash, PowerShell, Python are the most common in security operations"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Scripting Languages?
> Scripting languages like Python and Bash are tools for writing quick instructions that computers follow. They are like giving your computer a to-do list it can work through on its own.

## Definition

Scripting languages are programming languages used in security operations to automate tasks, process large data sets, interact with APIs, and build security tools. Unlike compiled languages, scripting languages are interpreted and allow rapid development and iteration, making them ideal for security automation and tooling.

## Key Details

- **Bash**: essential for Linux/Unix automation; system administration, log processing, pipeline chaining
- **PowerShell**: dominant for Windows security automation; Active Directory management, WMI, .NET integration; also used by attackers (LOLbins)
- **Python**: cross-platform; rich ecosystem of security libraries (Scapy, Impacket, Requests, Paramiko); used for tool development and automation
- Security professionals should be comfortable reading and writing basic scripts in all three
- PowerShell execution policy, script block logging, and AMSI (Antimalware Scan Interface) are key defenses against malicious PowerShell

## Connections

- Parent: [[automation-and-scripting]] — scripting languages are the tools used to implement security automation
- See also: [[api-integration]]
