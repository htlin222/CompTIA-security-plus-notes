---
title: "Biometric authentication"
description: "FAR vs. FRR; CER (Crossover Error Rate) measures biometric system accuracy"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Biometric authentication uses physiological or behavioral characteristics (fingerprints, retina/iris scans, facial recognition, voice patterns) to verify identity. Biometric systems are evaluated using two error rates: the False Acceptance Rate (FAR)—the rate at which unauthorized users are incorrectly granted access—and the False Rejection Rate (FRR)—the rate at which authorized users are incorrectly denied access. These rates trade off against each other as the system's sensitivity is adjusted.

## Key Details

- **FAR (False Acceptance Rate)**: Incorrectly accepts an unauthorized user—a security risk.
- **FRR (False Rejection Rate)**: Incorrectly rejects an authorized user—a usability problem.
- **CER (Crossover Error Rate)**: The point where FAR = FRR; a lower CER means a more accurate system.
- Biometrics represent the "**something you are**" authentication factor.
- Biometric data cannot be changed if compromised—unlike passwords or tokens.

## Connections

- Parent: [[authentication]] — biometrics as an authentication factor
- See also: [[single-factor-authentication-sfa]]
