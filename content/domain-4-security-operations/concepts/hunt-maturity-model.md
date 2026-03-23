---
title: "Hunt maturity model"
description: "Levels from HM0 (initial, relies on automated alerts) to HM4 (leading, creates new detection content)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is the Hunt Maturity Model?
> This measures how good a team is at hunting for threats, from beginners who just follow basic steps all the way to experts who create their own clever strategies.

## Definition

The Hunt Maturity Model (HMM) is a framework that describes an organization's capability and sophistication in performing proactive threat hunting. Developed by David Bianco, the model defines five levels (HM0-HM4) that describe progression from reactive, alert-driven security operations to proactive, hypothesis-driven hunting that generates new detection content.

## Key Details

- **HM0 (Initial)**: relies entirely on automated alerts; no proactive hunting
- **HM1 (Minimal)**: incorporates threat intelligence; hunts based on known IoCs
- **HM2 (Procedural)**: follows established hunt procedures and checklists
- **HM3 (Innovative)**: creates novel hunt hypotheses based on TTP analysis
- **HM4 (Leading)**: hunts generate new automated detection content fed back into SIEM/EDR

## Connections

- Parent: [[threat-hunting]] — the maturity model helps organizations assess and improve their hunting capability
- See also: [[hypothesis-driven-hunting]]
