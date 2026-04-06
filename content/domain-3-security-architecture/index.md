---
title: "Domain 3: Security Architecture"
description: "Overview of Domain 3 topics for SY0-701"
draft: false
date: 2026-03-20
tags:
  - domain/3
---

## Overview

Domain 3 covers the design and implementation of secure network architectures, cryptographic solutions, and resilient infrastructure. At **18%** of the exam, it bridges the gap between theoretical concepts (Domain 1) and operational practices (Domain 4), focusing on *how* security is built into systems and networks.

## Exam Weight

**18%** — approximately 16-17 questions out of 90.

## Topics

| Topic | Note | Key Focus |
|---|---|---|
| Network Security Architecture | [[network-security-architecture]] | DMZ, screened subnet, east-west traffic |
| Firewalls | [[firewalls]] | NGFW, stateful/stateless, WAF, ACLs |
| IDS/IPS | [[ids-ips]] | Signature-based, anomaly-based, inline vs. passive |
| VPN | [[vpn]] | IPSec, SSL/TLS VPN, split vs. full tunnel |
| Network Segmentation | [[network-segmentation]] | VLANs, microsegmentation, air gaps |
| Load Balancers & Proxies | [[load-balancers-and-proxies]] | Reverse proxy, forward proxy, load balancing |
| NAC | [[nac]] | 802.1X, agent/agentless, posture assessment |
| Cloud Security | [[cloud-security]] | IaaS/PaaS/SaaS, shared responsibility, CASB |
| Virtualization Security | [[virtualization-security]] | VM sprawl, escape, hypervisor security |
| Serverless & Containers | [[serverless-and-containers]] | Container security, orchestration, FaaS |
| Infrastructure as Code | [[infrastructure-as-code]] | Terraform, Ansible, immutable infrastructure |
| Encryption | [[encryption]] | Symmetric, asymmetric, AES, RSA, ECC |
| PKI | [[pki]] | Certificate authorities, trust chains |
| Certificates | [[certificates]] | X.509, SAN, wildcard, certificate pinning |
| Hashing | [[hashing]] | SHA-256, MD5, HMAC, salting |
| Key Management | [[key-management]] | Key escrow, rotation, HSM, TPM |
| Data Protection | [[data-protection]] | Encryption at rest/in transit/in use, tokenization |
| DLP | [[dlp]] | Data loss prevention, endpoint/network/cloud DLP |
| Embedded Systems Security | [[embedded-systems-security]] | SCADA, IoT, RTOS, constraints |
| Resilience & Redundancy | [[resilience-and-redundancy]] | RAID, clustering, geographic dispersal, RPO/RTO |

## Cross-Domain Connections

- Implements [[zero-trust]] and [[defense-in-depth]] principles from Domain 1
- Defends against specific attacks from Domain 2: [[network-attacks]], [[cryptographic-attacks]], [[denial-of-service]]
- Architecture feeds telemetry to Domain 4's monitoring tools: [[siem]], [[network-monitoring]], [[log-management]]
- [[encryption]] and [[pki]] are foundational to [[authentication]] and [[data-classification]] across all domains
- Resilience designs support Domain 5's [[business-continuity]] and [[disaster-recovery]] planning
- Cloud security models connect to Domain 5's [[third-party-risk]] and [[compliance]] requirements

## Course Resources

- **Professor Messer's CompTIA SY0-701 Security+ Training Course**
  - [Full YouTube Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv)
