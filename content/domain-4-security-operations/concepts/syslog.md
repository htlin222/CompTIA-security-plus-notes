---
title: "Syslog"
description: "Standard protocol (UDP 514, TCP 514, or TLS 6514) for transmitting log data to a centralized server"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Syslog?
> Syslog is one of the oldest ways computers send their diary entries to a central server. It is like a postal service that delivers log messages from many devices to one mailbox.

## Definition

Syslog is the most widely used standard protocol for transmitting log messages from network devices, servers, and applications to a centralized log collection server. Originally designed for Unix systems, syslog has been adopted by virtually all network devices and many applications, making it the universal log forwarding protocol in most enterprise environments.

## Key Details

- **UDP 514**: traditional syslog; connectionless; fast but unreliable — logs can be lost if network is congested
- **TCP 514**: reliable delivery but no encryption — logs transmitted in plaintext
- **TLS 6514** (syslog over TLS): encrypted, authenticated syslog transport — preferred for sensitive environments
- Syslog messages include a severity level (0=Emergency to 7=Debug) and a facility code
- SIEM platforms and log servers (rsyslog, syslog-ng) receive and process syslog messages

## Connections

- Parent: [[log-management]] — syslog is the primary log transmission protocol in enterprise environments
- See also: [[log-forwarding-agents]]
