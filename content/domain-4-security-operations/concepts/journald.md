---
title: "journald"
description: "Linux systemd journal for structured logging"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

journald (systemd-journald) is the logging daemon included with systemd-based Linux distributions that collects, stores, and manages log data from the kernel, boot process, services, and applications. Unlike traditional syslog which stores plain text, journald stores log data in a structured binary format with rich metadata, enabling faster querying and indexed searching.

## Key Details

- Logs are stored in binary format in /var/log/journal/ — require `journalctl` to read
- Provides structured fields: unit name, timestamp, priority, PID, UID, and custom metadata
- Can forward logs to remote syslog servers for centralized collection
- `journalctl` provides powerful filtering: by time, unit, priority, user, and more
- Binary log format makes tampering detectable (checksum verification)

## Connections

- Parent: [[log-management]] — journald is a primary log source on modern Linux systems
- See also: [[syslog]]
