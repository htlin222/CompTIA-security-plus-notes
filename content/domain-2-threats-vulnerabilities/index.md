---
title: "Domain 2: Threats, Vulnerabilities & Mitigations"
description: "Overview of Domain 2 topics for SY0-701"
draft: false
date: 2026-03-20
tags:
  - domain/2
---

## Overview

Domain 2 focuses on identifying and understanding the threats and vulnerabilities that affect organizations and the techniques used to mitigate them. At **22%** of the exam, it is the second-heaviest domain and requires deep familiarity with specific attack types, vulnerability categories, and mitigation strategies.

## Exam Weight

**22%** — approximately 19-20 questions out of 90.

## Topics

| Topic | Note | Key Focus |
|---|---|---|
| Malware Types | [[malware-types]] | Viruses, worms, trojans, rootkits, spyware |
| Ransomware | [[ransomware]] | Encryption, double extortion, recovery |
| Password Attacks | [[password-attacks]] | Brute force, dictionary, rainbow tables, spraying |
| Cryptographic Attacks | [[cryptographic-attacks]] | Birthday, downgrade, collision |
| Application Attacks | [[application-attacks]] | Buffer overflow, race condition, SSRF |
| Injection Attacks | [[injection-attacks]] | SQL injection, LDAP injection, command injection |
| XSS and CSRF | [[xss-and-csrf]] | Reflected, stored, DOM-based XSS; CSRF tokens |
| Network Attacks | [[network-attacks]] | ARP poisoning, VLAN hopping, rogue devices |
| Denial of Service | [[denial-of-service]] | DDoS, amplification, SYN flood |
| DNS Attacks | [[dns-attacks]] | DNS poisoning, zone transfer, typosquatting |
| Wireless Attacks | [[wireless-attacks]] | Evil twin, deauthentication, WPS attacks |
| On-Path Attacks | [[on-path-attacks]] | MITM, SSL stripping, session hijacking |
| Indicators of Compromise | [[indicators-of-compromise]] | IOCs, anomalous activity, STIX/TAXII |
| Vulnerability Types | [[vulnerability-types]] | Zero-day, misconfiguration, default credentials |
| Mitigation Techniques | [[mitigation-techniques]] | Patching, segmentation, hardening |

## Cross-Domain Connections

- Attacks in this domain target systems defended by Domain 3's architecture: [[firewalls]], [[ids-ips]], [[encryption]]
- Detection of these threats relies on Domain 4's operational tools: [[siem]], [[edr-xdr]], [[threat-intelligence]]
- [[threat-actors]] from Domain 1 are the adversaries executing these attacks
- [[social-engineering]] from Domain 1 is a primary delivery mechanism for many Domain 2 attacks
- Vulnerability management and mitigation connect to Domain 4's [[vulnerability-management]] and [[penetration-testing]]
- Compliance frameworks in Domain 5 ([[regulations-and-frameworks]]) mandate protections against these threats
