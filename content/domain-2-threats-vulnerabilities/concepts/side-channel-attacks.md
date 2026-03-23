---
title: "Side-channel attacks"
description: "Exploiting physical characteristics (timing, power, EM emissions) rather than algorithmic weaknesses"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Side-channel attacks extract secret information by analyzing the physical characteristics of a cryptographic system's operation—such as execution timing, power consumption, electromagnetic radiation, or even acoustic emanations—rather than breaking the underlying algorithm. These attacks can recover cryptographic keys from hardware devices that correctly implement mathematically sound algorithms, by observing how the implementation behaves physically.

## Key Details

- **Timing attacks**: Measure the time an operation takes—operations that vary based on key bits reveal information about the key (e.g., RSA decryption time).
- **Power analysis**: Measure power consumption during cryptographic operations; **SPA** (Simple Power Analysis) and **DPA** (Differential Power Analysis).
- **Electromagnetic (EM) attacks**: Measure EM emissions from ICs—similar to power analysis but more versatile.
- **Acoustic cryptanalysis**: Capture sounds made by hardware during computation—demonstrated against RSA-4096.
- **Spectre/Meltdown**: CPU cache timing side-channels in modern processors—allow user-space code to read kernel memory.

## Connections

- Parent: [[cryptographic-attacks]] — attacks on cryptographic implementations rather than algorithms
- See also: [[hardware-vulnerabilities]]
