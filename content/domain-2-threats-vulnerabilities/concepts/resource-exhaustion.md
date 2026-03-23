---
title: "Resource exhaustion"
description: "Consuming all available memory, CPU, disk, or connections to cause denial of service"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Resource exhaustion is an attack or vulnerability condition where the consumption of finite system resources (memory, CPU, disk space, network connections, file handles, threads) reaches capacity, causing the application or system to degrade or become completely unavailable. It can result from deliberate attacks (DoS), malicious application bugs, or uncontrolled resource allocation in application code.

## Key Details

- **Memory exhaustion**: Allocating memory faster than it can be freed—causes OOM (Out of Memory) conditions and crashes.
- **CPU exhaustion**: CPU-intensive operations triggered by user input (algorithmic complexity attacks, e.g., ReDoS using malicious regex input).
- **Connection pool exhaustion**: Consuming all available database or HTTP connections—Slowloris and similar attacks do this.
- **Disk exhaustion**: Filling disk with log files or uploaded content—prevents normal operations requiring disk writes.
- Mitigation: **rate limiting**, **resource quotas**, **connection timeouts**, **memory limits**, **input validation** to prevent algorithmic complexity attacks.

## Connections

- Parent: [[application-attacks]] — a resource-based application denial of service
- See also: [[application-layer-attacks]]
