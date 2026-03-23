---
title: "Insecure protocols"
description: "Using unencrypted protocols (Telnet, FTP, HTTP, SNMPv1/v2) that expose data in transit"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Insecure Protocols?
> Some older ways computers talk to each other are like sending postcards -- anyone who handles them can read what's written. Insecure protocols don't scramble messages, so snoopers can see everything.

## Definition

Insecure protocols are network communication protocols that transmit data in plaintext without encryption, allowing anyone with network access to capture credentials, session data, and sensitive information using a packet sniffer. These protocols were designed before encryption was a priority and have secure alternatives that should replace them in all security-conscious environments.

## Key Details

- **Telnet** → replace with **SSH** (port 22); Telnet sends all data including passwords in cleartext.
- **FTP** → replace with **SFTP or FTPS**; FTP credentials and file contents are transmitted in cleartext.
- **HTTP** → replace with **HTTPS**; HTTP transmits all web traffic unencrypted.
- **SNMPv1/v2** → replace with **SNMPv3** (adds authentication and encryption); older versions transmit community strings in cleartext.
- **TFTP (Trivial FTP)**: Unauthenticated file transfer with no encryption—only acceptable on isolated lab networks.

## Connections

- Parent: [[vulnerability-types]] — a common network-level vulnerability
- See also: [[weak-encryption]]
