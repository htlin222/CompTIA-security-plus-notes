---
title: "Bell-LaPadula Model"
description: "\"No read up, no write down\" — protects confidentiality"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

The Bell-LaPadula Model is a formal access control model designed to protect the confidentiality of classified information in hierarchical security environments (e.g., government/military). It defines two key properties: the Simple Security Property ("no read up"—a subject cannot read data at a higher classification) and the *-property (star property, "no write down"—a subject cannot write data to a lower classification level).

## Key Details

- **Simple Security Property (SS Property)**: "No read up" — users cannot read files classified above their clearance.
- **Star Property (*-Property)**: "No write down" — users cannot write to files at a lower classification (prevents data leakage).
- Designed for **confidentiality**—it does not address integrity (that's Biba's role).
- Uses **mandatory access control (MAC)** with security labels (Unclassified, Secret, Top Secret).
- The model allows users to read at their level or below, and write at their level or above.

## Connections

- Parent: [[access-control-models]] — a formal access control model
- See also: [[biba-model]]
