---
title: "Chain of custody"
description: "Documented record of who handled the evidence, when, and what was done — breaks invalidate evidence"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Chain of Custody?
> It is like a sign-out sheet for library books. Every time evidence changes hands, someone writes down who had it and when, so you can prove nobody tampered with it.

## Definition

Chain of custody is a documented and unbroken record of the chronological transfer, handling, and storage of digital or physical evidence from the time of collection through presentation in legal proceedings. Any break or gap in the chain of custody can render evidence inadmissible in court and undermine criminal prosecutions or civil litigation.

## Key Details

- Documents who collected the evidence, when, how, and what was done with it at each step
- Each person who handles evidence must sign and date the chain of custody form
- Evidence containers must be sealed and tamper-evident
- Hash values (MD5, SHA-256) verify evidence integrity — hash must match at each transfer point
- A broken chain of custody does not necessarily mean evidence is wrong, but it loses legal admissibility

## Connections

- Parent: [[digital-forensics]] — chain of custody is fundamental to forensically sound investigations
- Parent: [[incident-response]] — maintaining evidence integrity during incident response
- See also: [[hash-verification]]
