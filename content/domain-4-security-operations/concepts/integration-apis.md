---
title: "Integration APIs"
description: "SOAR platforms connect to dozens of security tools to take coordinated action"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Integration APIs in the context of SOAR platforms are the programmatic interfaces used to connect SOAR solutions to the diverse ecosystem of security tools they need to orchestrate. SOAR platforms use APIs to query data from SIEMs, trigger actions on firewalls, create tickets in ITSM systems, and communicate with dozens of other security tools — all within a single automated workflow.

## Key Details

- SOAR platforms maintain libraries of pre-built integrations (connectors) for common security tools
- REST APIs are the most common integration method; some tools use proprietary protocols
- Integration depth varies: some tools support full bidirectional control; others are read-only
- API authentication must be secured: API keys should be stored in secrets management systems
- The breadth of integrations is a key differentiator when evaluating SOAR platforms

## Connections

- Parent: [[soar]] — integration APIs are what enable SOAR platforms to orchestrate the security tool ecosystem
- See also: [[orchestration]]
