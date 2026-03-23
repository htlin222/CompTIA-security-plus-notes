---
title: "Secure email gateway"
description: "Filters inbound and outbound email for spam, phishing, malware, and DLP violations"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

A secure email gateway (SEG) is a security appliance or cloud service that sits in the mail flow path and inspects all inbound and outbound email messages for threats, policy violations, and unwanted content. It combines multiple security capabilities — spam filtering, anti-phishing, malware scanning, DLP, and email authentication enforcement — into a single email security solution.

## Key Details

- **Inbound**: blocks spam, phishing attempts, malware-laden attachments, and impersonation attempts
- **Outbound**: enforces DLP policies, applies email encryption, and prevents data leakage via email
- Enforces SPF, DKIM, and DMARC authentication checks on inbound messages
- URL rewriting changes links in emails to be proxied through a security service
- Sandboxing of attachments detects zero-day malware not caught by signature scanning
- Common SEG products: Proofpoint, Mimecast, Cisco Email Security, Microsoft Defender for Office 365

## Connections

- Parent: [[email-security]] — the secure email gateway is the primary email security enforcement point
- See also: [[anti-phishing-controls]]
