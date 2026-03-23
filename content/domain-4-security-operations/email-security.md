---
title: "Email Security"
description: "Controls and technologies to protect email communications from phishing, spoofing, and data loss"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/network
  - weight/medium
aliases:
  - "Email Protection"
---

> [!eli5] ELI5: What is Email Security?
> Your mailbox at home sometimes gets junk mail or letters pretending to be from someone they are not. Email security is like having a really smart mail sorter who checks every letter before it reaches you. They look at the return address to make sure it is real, scan for anything dangerous inside, and toss out the fakes. Without this protection, bad people could trick you into opening something harmful just by sending a convincing-looking message.

## Overview

Email security encompasses the techniques and technologies used to protect email accounts, content, and communications from unauthorized access, loss, or compromise. Email remains the primary attack vector for phishing, malware delivery, and business email compromise (BEC). Effective email security requires multiple layers of technical controls and user awareness.

## Key Concepts

- **[[spf-sender-policy-framework|SPF (Sender Policy Framework)]]**: DNS TXT record that specifies which mail servers are authorized to send email for a domain
- **[[dkim-domainkeys-identified-mail|DKIM (DomainKeys Identified Mail)]]**: Adds a digital signature to outgoing emails to verify the message was not altered in transit
- **[[dmarc-domain-based-message-authentication-reporting-conformance|DMARC (Domain-based Message Authentication, Reporting & Conformance)]]**: Policy that tells receiving servers what to do when SPF/DKIM fail (none, quarantine, reject)
- **[[secure-email-gateway|Secure email gateway]]**: Filters inbound and outbound email for spam, phishing, malware, and DLP violations
- **[[smime|S/MIME]]**: Certificate-based encryption and digital signing of email content
- **[[email-encryption|Email encryption]]**: Protects email content in transit and at rest; can be gateway-based or end-to-end
- **[[anti-phishing-controls|Anti-phishing controls]]**: URL rewriting, sandbox analysis of attachments, impersonation detection
- **[[business-email-compromise-bec|Business Email Compromise (BEC)]]**: Social engineering attacks where attackers impersonate executives to request wire transfers or sensitive data
- **[[data-loss-prevention-dlp|Data Loss Prevention (DLP)]]**: Scanning outbound email for sensitive data (PII, credit cards, intellectual property)

## Exam Tips

> [!tip] Remember
> SPF = who CAN send (IP allowlist in DNS). DKIM = message INTEGRITY (digital signature). DMARC = what to DO when checks fail (policy). All three together provide strong anti-spoofing protection.

- BEC attacks do not use malware — they rely purely on social engineering and urgency
- S/MIME requires PKI infrastructure with certificates for both sender and recipient
- Know that SPF, DKIM, and DMARC are all DNS-based records

## Connections

- Primary defense against [[social-engineering]] attacks delivered via phishing emails
- Works alongside [[security-awareness-training]] to reduce user susceptibility to email threats
- [[encryption]] technologies (S/MIME, TLS) protect email content confidentiality
- Phishing emails are a common delivery mechanism for [[malware-types]] and [[ransomware]]

## Scenario

> See [[case-email-security]] for a practical DevOps scenario applying these concepts.
