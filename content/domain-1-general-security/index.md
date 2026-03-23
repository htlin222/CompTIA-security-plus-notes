---
title: "Domain 1: General Security Concepts"
description: "Overview of Domain 1 topics for SY0-701"
draft: false
date: 2026-03-20
tags:
  - domain/1
---

## Overview

Domain 1 covers the foundational security concepts that underpin all other domains. It accounts for **12%** of the SY0-701 exam and focuses on core security principles, identity and access management frameworks, and the threat landscape. While it is the smallest domain by weight, the concepts here are referenced throughout every other domain.

## Exam Weight

**12%** — approximately 10-11 questions out of 90.

## Topics

| Topic | Note | Key Focus |
|---|---|---|
| Security Fundamentals | [[security-concepts]] | CIA, least privilege, separation of duties |
| CIA Triad | [[cia-triad]] | Confidentiality, Integrity, Availability |
| AAA Framework | [[aaa-framework]] | RADIUS, TACACS+, Kerberos |
| Authentication | [[authentication]] | Factors, biometrics, passwordless |
| Authorization | [[authorization]] | OAuth, implicit deny, permissions |
| Access Control Models | [[access-control-models]] | DAC, MAC, RBAC, ABAC |
| Zero Trust | [[zero-trust]] | Control/data plane, policy engine |
| Defense in Depth | [[defense-in-depth]] | Layered security, control types |
| Threat Actors | [[threat-actors]] | APT, insider, hacktivists, organized crime |
| Attack Vectors | [[attack-vectors]] | Supply chain, message-based, removable device |
| Social Engineering | [[social-engineering]] | Phishing, pretexting, tailgating |
| Physical Security | [[physical-security]] | Mantraps, bollards, surveillance |
| Deception Technologies | [[deception-technologies]] | Honeypots, DNS sinkholes, honeytokens |
| Change Management | [[change-management]] | CAB, rollback plans, maintenance windows |

## Cross-Domain Connections

Domain 1 concepts appear throughout the exam in applied contexts:

- **Authentication and Identity** connect to Domain 4's [[identity-management]], [[mfa]], [[sso]], and [[privileged-access-management]]
- **Threat Actors and Vectors** inform Domain 2's specific attack types like [[malware-types]], [[password-attacks]], and [[network-attacks]]
- **Zero Trust and Defense in Depth** are implemented through Domain 3's [[network-segmentation]], [[firewalls]], and [[cloud-security]]
- **Social Engineering** is countered by Domain 5's [[security-awareness-training]] and [[security-policies]]
- **Change Management** aligns with Domain 5's [[governance]] and [[compliance]] requirements
