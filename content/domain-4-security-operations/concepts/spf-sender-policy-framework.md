---
title: "SPF (Sender Policy Framework)"
description: "DNS TXT record that specifies which mail servers are authorized to send email for a domain"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - SPF
---

## Definition

SPF (Sender Policy Framework) is an email authentication mechanism that allows domain owners to specify which mail servers are authorized to send email on behalf of their domain. The list is published as a DNS TXT record. Receiving mail servers query the DNS record and compare the sending server's IP address against the authorized list, flagging or rejecting messages from unauthorized senders.

## Key Details

- SPF record published in DNS specifies authorized IP addresses and mail servers for a domain
- Receiving server checks the SPF record of the domain in the Return-Path (envelope from) address
- SPF can only protect against spoofing of the envelope sender — not the From header displayed to users
- Results: Pass, Fail, SoftFail, Neutral, None, TemperError, PermError
- SPF alone is insufficient — must be used with DKIM and DMARC for complete email authentication

## Connections

- Parent: [[email-security]] — SPF is one of three email authentication protocols (with DKIM and DMARC)
- See also: [[dmarc-domain-based-message-authentication-reporting-conformance]]
