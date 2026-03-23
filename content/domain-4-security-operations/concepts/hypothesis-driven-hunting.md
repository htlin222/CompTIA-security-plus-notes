---
title: "Hypothesis-driven hunting"
description: "Starting with an educated guess about attacker behavior and searching for evidence to confirm or deny it"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Hypothesis-driven Hunting?
> It is like being a scientist who says "I bet the attacker came in through the side door" and then goes looking for evidence to prove or disprove that guess.

## Definition

Hypothesis-driven hunting is a threat hunting methodology that begins with a structured hypothesis about how an attacker might be operating in the environment, then systematically searches for evidence to confirm or refute the hypothesis. The hypothesis is formed based on threat intelligence, knowledge of the environment, attacker TTPs, and analytical reasoning.

## Key Details

- Example hypothesis: "A threat actor using PowerShell for lateral movement would exhibit encoded command execution and unusual WMI activity"
- Hypothesis quality determines hunt effectiveness — should be specific, testable, and based on real attacker behavior
- MITRE ATT&CK provides a library of TTPs to form hypotheses from
- Results in either confirmed hypothesis (investigation) or refuted hypothesis (improved knowledge of normal baseline)
- Mature hunting programs feed refuted hypotheses back as new detection rules

## Connections

- Parent: [[threat-hunting]] — hypothesis-driven hunting is the primary advanced hunting methodology
- See also: [[mitre-attck-framework]]
