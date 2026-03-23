---
title: "RAT (Remote Access Trojan)"
description: "Gives attackers full remote control of a compromised system"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - RAT
---

## Definition

A Remote Access Trojan (RAT) is a type of malware that provides the attacker with full remote control capabilities over a compromised system—including file system access, process management, screen viewing, keylogging, webcam/microphone activation, and command execution. RATs are often disguised as legitimate software and establish persistent, covert connections back to the attacker's C2 server.

## Key Details

- Gives attackers **complete remote control**—equivalent to sitting at the keyboard of the infected system.
- Common features: **file browser and transfer**, **shell/command execution**, **screenshot capture**, **keylogging**, **webcam/microphone access**.
- Communicates with attacker via **C2 (Command and Control)** channels—often over HTTP/HTTPS to blend with normal traffic.
- Commonly delivered via **phishing emails** with malicious attachments (Word macros, ISO files) or drive-by downloads.
- Famous RATs: **DarkComet**, **njRAT**, **Poison Ivy**, **Quasar RAT**, **AsyncRAT**.

## Connections

- Parent: [[malware-types]] — a comprehensive remote control malware category
- See also: [[trojan]]
