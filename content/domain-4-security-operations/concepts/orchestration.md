---
title: "Orchestration"
description: "Connecting and coordinating multiple security tools (SIEM, firewalls, EDR, ticketing) through APIs"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Security orchestration is the process of connecting and coordinating multiple security tools and systems through APIs and automated workflows to enable them to work together as a unified, coordinated response capability. It is a core component of SOAR (Security Orchestration, Automation, and Response) and allows disparate tools to share data and trigger actions in sequence without manual human intervention between steps.

## Key Details

- Connects tools: SIEM sends alert → SOAR enriches with threat intel → SOAR blocks IP at firewall → SOAR creates ticket
- Eliminates manual "swivel chair" work where analysts switch between multiple tool consoles
- Enables playbooks to span multiple tools and data sources in a single automated workflow
- Requires robust API integrations with each tool in the security ecosystem
- Orchestration without automation still provides value by streamlining multi-tool workflows

## Connections

- Parent: [[soar]] — orchestration is one of the three pillars of SOAR
- See also: [[integration-apis]]
