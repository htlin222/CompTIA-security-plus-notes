---
title: "API integration"
description: "Connecting security tools through REST APIs for orchestrated workflows"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is API Integration?
> APIs are like waiters in a restaurant -- they carry messages between the kitchen and your table. API integration connects security tools so they can share information and work together automatically.

## Definition

API integration in security operations refers to the use of REST APIs and other programmatic interfaces to connect disparate security tools so they can share data and trigger actions automatically. This is the foundation of security automation and orchestration — tools like SIEM, firewalls, EDR, and ticketing systems expose APIs that allow SOAR platforms and scripts to coordinate responses without manual intervention.

## Key Details

- REST APIs use HTTP methods (GET, POST, PUT, DELETE) and JSON data formats
- Enables bidirectional communication: pulling data from tools and pushing actions to them
- Authentication to APIs typically uses API keys, OAuth tokens, or certificates
- Essential for SOAR playbooks that automate multi-tool incident response workflows
- Common integrations: SIEM → ticketing systems, threat feeds → firewall blocklists

## Connections

- Parent: [[automation-and-scripting]] — API integration is a core mechanism for automation
- See also: [[orchestration]]
