---
title: "Keylogging"
description: "Capturing passwords as users type them using hardware or software keyloggers"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Keylogging?
> Instead of cracking your password after the fact, this attack records it the moment you type it. The attacker gets your exact password in plain text, no guessing needed.

## Definition

Keylogging as a password attack technique involves capturing user credentials by recording keystrokes at the time of entry. This technique bypasses the need to crack hashed passwords—instead, credentials are captured in plaintext as the user types them. Keylogging can be performed via software malware installed on the target system or via physical hardware devices covertly attached to a computer.

## Key Details

- **Software approach**: Malware intercepts OS keyboard API calls to capture keystrokes—highly effective, remotely deployable.
- **Hardware approach**: Physical keyloggers plug between keyboard and computer; undetectable by software tools; require physical access for retrieval.
- **Form-grabbing** variant: Captures data from web forms before it's sent—even works against HTTPS because capture happens before encryption.
- Keylogging is a component of many **banking trojans** (Zeus, SpyEye) targeting online banking credentials.
- **MFA** is the most effective defense—a stolen password is useless without the second factor.

## Connections

- Parent: [[password-attacks]] — an alternative to cracking that captures passwords in plaintext
- See also: [[keylogger]]
