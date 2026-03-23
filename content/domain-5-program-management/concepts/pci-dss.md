---
title: "PCI DSS"
description: "payment card industry standard; required for any organization handling cardholder data"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What is PCI DSS?
> Any store that takes credit cards must follow these safety rules to keep your card number from being stolen. It's like a set of locks and alarms specifically designed to protect payment information.

## Definition

The Payment Card Industry Data Security Standard (PCI DSS) is a set of security requirements created by the PCI Security Standards Council (founded by Visa, Mastercard, American Express, Discover, and JCB) to protect cardholder data (CHD) and sensitive authentication data (SAD). Compliance is mandatory for any organization that stores, processes, or transmits payment card data, enforced through card brand agreements rather than government regulation.

## Key Details

- 12 high-level requirements organized around 6 goals: build/maintain secure networks, protect cardholder data, manage vulnerabilities, implement access controls, monitor/test networks, maintain information security policies
- Compliance levels based on transaction volume: Level 1 (6M+ transactions/year) requires an annual QSA assessment; lower levels may use Self-Assessment Questionnaires (SAQs)
- Scope reduction through tokenization (replacing PANs with tokens) and network segmentation is a key compliance strategy
- PCI DSS v4.0 (effective March 2024) introduced customized implementation approach and enhanced multi-factor authentication requirements
- Non-compliance consequences: fines from card brands, increased transaction fees, and ultimately loss of card processing privileges

## Connections

- Parent: [[regulations-and-frameworks]] — PCI DSS is the mandatory payment card security standard
- See also: [[industry-standards]]
- See also: [[regulatory-audit]]
