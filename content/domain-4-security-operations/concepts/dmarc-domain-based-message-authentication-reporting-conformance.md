---
title: "DMARC (Domain-based Message Authentication, Reporting & Conformance)"
description: "Policy that tells receiving servers what to do when SPF/DKIM fail (none, quarantine, reject)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - DMARC
---

> [!eli5] ELI5: What is DMARC?
> DMARC is the boss that tells email servers what to do when a message fails its identity checks -- reject it, flag it, or let it through. It also sends reports so you know who is faking your address.

## Definition

DMARC (Domain-based Message Authentication, Reporting & Conformance) is an email authentication protocol that builds on SPF and DKIM by adding a policy layer that instructs receiving mail servers what to do when incoming messages fail SPF or DKIM checks. DMARC also provides reporting mechanisms that allow domain owners to monitor authentication failures and detect spoofing attempts.

## Key Details

- Policy published in DNS TXT record; three policy options: none (monitor only), quarantine (spam folder), reject (block message)
- Requires alignment: the domain in the From header must align with the domain that passed SPF or DKIM
- Reporting: aggregate (rua) and forensic (ruf) reports show authentication results from receiving servers
- Widely recommended to start with policy=none to monitor, then progress to quarantine and reject
- Organizations without DMARC are highly susceptible to spoofing of their domain

## Connections

- Parent: [[email-security]] — DMARC is the policy enforcement layer for email authentication
- See also: [[dkim-domainkeys-identified-mail]]
