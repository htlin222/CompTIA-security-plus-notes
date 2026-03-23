---
title: "Session replay"
description: "Capturing and retransmitting a valid authentication exchange to gain unauthorized access"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Session Replay?
> The attacker records your login conversation and plays it back to the server later. The server thinks it's you logging in again, but it's actually the attacker using your old recording.

## Definition

Session replay is an attack where an attacker captures a valid authentication exchange or session token and replays it at a later time to gain unauthorized access. Unlike relay attacks (which are real-time), session replay uses previously captured data. It is closely related to replay attacks but specifically focuses on authentication sessions rather than individual packets or transactions.

## Key Details

- Captured via: **network sniffing** (unencrypted sessions), **MitM attacks**, **XSS** (stealing session cookies from browsers).
- **Mitigation**: Session tokens must have **short lifetimes** and **proper expiration**; tokens should be invalidated upon logout.
- **One-time tokens**: Authentication systems that use tokens valid for only one request (nonces) defeat session replay.
- **Token rotation**: Re-issue new session tokens periodically or after privilege changes—limits the window of a captured token's usefulness.
- Modern web frameworks using **HTTPS** and properly flagged cookies significantly reduce session replay risk.

## Connections

- Parent: [[application-attacks]] — a session-based authentication attack
- See also: [[session-hijacking]], [[replay-attack]]
