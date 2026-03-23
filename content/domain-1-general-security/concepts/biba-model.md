---
title: "Biba Model"
description: "\"No read down, no write up\" — protects integrity"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

The Biba Model is a formal access control model that is the integrity-focused counterpart to Bell-LaPadula. It defines two key rules: the Simple Integrity Property ("no read down"—a subject cannot read data at a lower integrity level) and the *-Integrity Property ("no write up"—a subject cannot write to a higher integrity level). This prevents lower-integrity data from contaminating higher-integrity data.

## Key Details

- **Simple Integrity Property**: "No read down" — a high-integrity subject cannot read low-integrity data (prevents corruption by untrusted input).
- **Integrity *-Property**: "No write up" — a low-integrity subject cannot write to high-integrity objects (prevents contamination).
- Designed for **integrity**—the opposite concern of Bell-LaPadula (confidentiality).
- Commonly used as a mental model for understanding integrity controls in systems handling critical data.
- Think of it as: "don't let dirty data pollute clean systems."

## Connections

- Parent: [[access-control-models]] — a formal access control model
- See also: [[bell-lapadula-model]]
