---
title: "Logic bomb"
description: "Malicious code that triggers when specific conditions are met (date, user action, system event)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Logic Bomb?
> It's hidden bad code that sleeps inside a program until something specific happens -- like a certain date arrives or someone gets fired. Then BOOM, it goes off and causes damage.

## Definition

A logic bomb is malicious code deliberately inserted into a software system or application that remains dormant until specific triggering conditions are met—such as a particular date/time, a user action, or a system event. When triggered, it executes its payload, which can include deleting files, encrypting data, creating backdoors, or disrupting operations. Logic bombs are particularly dangerous because they are often planted by insiders with legitimate access.

## Key Details

- **Common triggers**: Specific date/time (time bomb), login attempt by a specific user, file deletion, reaching a record count threshold.
- Frequently used by **disgruntled employees** as a sabotage mechanism—planted before termination to execute after they leave.
- The "dead man's switch" variant: executes if the insider doesn't perform a regular action (e.g., doesn't log in weekly), designed to fire upon termination.
- Detection is difficult because the code is dormant—**code review**, **change management**, and **separation of duties** are key mitigations.
- Famous cases: UBS PaineWebber (2002) bank network attack; Roger Duronio case.

## Connections

- Parent: [[malware-types]] — a malware type often associated with insider threats
- See also: [[rootkit]]
