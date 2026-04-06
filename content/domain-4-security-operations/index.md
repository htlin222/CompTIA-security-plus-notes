---
title: "Domain 4: Security Operations"
description: "Overview of Domain 4 topics for SY0-701"
draft: false
date: 2026-03-20
tags:
  - domain/4
---

## Overview

Domain 4 is the **largest domain** on the SY0-701 exam at **28%**, covering the day-to-day operational activities that keep an organization secure. This includes identity management, monitoring, incident response, vulnerability management, and security tooling. Expect the most questions from this domain.

## Exam Weight

**28%** — approximately 25-26 questions out of 90.

## Topics

| Topic | Note | Key Focus |
|---|---|---|
| Identity Management | [[identity-management]] | Provisioning, deprovisioning, directory services |
| Single Sign-On | [[sso]] | SAML, OAuth, OIDC, federation |
| Multi-Factor Authentication | [[mfa]] | Factor types, push notifications, TOTP, FIDO2 |
| Federation | [[federation]] | Cross-organization trust, SAML assertions |
| Privileged Access Management | [[privileged-access-management]] | PAM, just-in-time access, credential vaulting |
| Endpoint Security | [[endpoint-security]] | Antivirus, HIDS, application control, boot integrity |
| EDR/XDR | [[edr-xdr]] | Endpoint/extended detection and response |
| SIEM | [[siem]] | Log aggregation, correlation, alerting, dashboards |
| SOAR | [[soar]] | Security orchestration, automation, playbooks |
| Vulnerability Management | [[vulnerability-management]] | Scanning, CVE, CVSS, remediation prioritization |
| Penetration Testing | [[penetration-testing]] | Rules of engagement, methodologies, reporting |
| Incident Response | [[incident-response]] | Phases, containment, eradication, lessons learned |
| Digital Forensics | [[digital-forensics]] | Chain of custody, imaging, volatility order |
| Threat Hunting | [[threat-hunting]] | Proactive search, hypothesis-driven, IOC analysis |
| Threat Intelligence | [[threat-intelligence]] | OSINT, STIX/TAXII, TTP, threat feeds |
| Log Management | [[log-management]] | Syslog, centralized logging, retention, NTP |
| Network Monitoring | [[network-monitoring]] | NetFlow, packet capture, SNMP, baseline |
| Email Security | [[email-security]] | SPF, DKIM, DMARC, gateway filtering |
| Automation & Scripting | [[automation-and-scripting]] | Python, PowerShell, Bash, API integration |
| Hardening | [[hardening]] | Benchmarks, CIS, STIG, removing unnecessary services |

## Cross-Domain Connections

- Operationalizes identity concepts from Domain 1: [[authentication]], [[authorization]], [[aaa-framework]]
- Uses Domain 3 infrastructure for monitoring and defense: [[firewalls]], [[ids-ips]], [[network-segmentation]]
- Detects and responds to Domain 2 threats: [[malware-types]], [[ransomware]], [[network-attacks]]
- [[incident-response]] and [[digital-forensics]] connect to Domain 5's [[governance]] and [[compliance]] reporting
- [[vulnerability-management]] informs Domain 5's [[risk-management]] and [[risk-assessment]] processes
- [[email-security]] directly counters Domain 1's [[social-engineering]] attacks
- [[security-awareness-training]] in Domain 5 reduces the operational burden documented here

## Course Resources

- **Professor Messer's CompTIA SY0-701 Security+ Training Course**
  - [Full YouTube Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv)
