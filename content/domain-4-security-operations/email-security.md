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

## Practice Questions

> [!qbank]- Q-Bank: Email Security (4 Questions)
>
> **Q1.** A company's employees are receiving emails that appear to come from the CEO requesting urgent wire transfers. The emails pass basic spam filters because they originate from a lookalike domain. Which combination of controls would BEST prevent these attacks?
>
> A. Installing full disk encryption on all workstations
> B. Implementing DMARC with a reject policy along with anti-phishing controls that detect impersonation
> C. Deploying a host-based firewall on the email server
> D. Requiring all employees to use S/MIME encryption
>
> > [!answer]- Show Answer
> > **B. Implementing DMARC with a reject policy along with anti-phishing controls that detect impersonation**
> >
> > [[dmarc-domain-based-message-authentication-reporting-conformance|DMARC]] with a reject policy prevents spoofed emails from being delivered, while [[anti-phishing-controls]] with impersonation detection can catch [[business-email-compromise-bec|BEC]] attacks from lookalike domains. Option A protects data at rest, not email delivery. Option C filters network traffic, not email content. Option D encrypts email content but does not prevent spoofing or impersonation.
>
> **Q2.** A security administrator is configuring DNS records to prevent email spoofing. Which record type specifies which mail servers are authorized to send email on behalf of the organization's domain?
>
> A. DKIM
> B. DMARC
> C. SPF
> D. MX
>
> > [!answer]- Show Answer
> > **C. SPF**
> >
> > [[spf-sender-policy-framework|SPF (Sender Policy Framework)]] is a DNS TXT record that lists the IP addresses and mail servers authorized to send email for a domain. Option A ([[dkim-domainkeys-identified-mail|DKIM]]) adds a digital signature for message integrity verification, not sender authorization. Option B ([[dmarc-domain-based-message-authentication-reporting-conformance|DMARC]]) defines the policy for handling SPF/DKIM failures. Option D (MX records) specifies where to deliver incoming mail, not who can send outgoing mail.
>
> **Q3.** An organization wants to ensure that the content of sensitive emails between its legal team and an external law firm cannot be read if intercepted in transit. Which technology BEST meets this requirement?
>
> A. SPF records
> B. DMARC policy
> C. S/MIME encryption
> D. Secure email gateway spam filtering
>
> > [!answer]- Show Answer
> > **C. S/MIME encryption**
> >
> > [[smime|S/MIME]] provides certificate-based end-to-end [[email-encryption]] that protects email content confidentiality both in transit and at rest. Option A verifies sender authorization but does not encrypt content. Option B defines spoofing policies but does not encrypt content. Option D filters malicious content but does not encrypt legitimate communications.
>
> **Q4.** A security analyst notices that outbound emails containing credit card numbers are being blocked by the email system before reaching external recipients. Which email security control is MOST likely responsible?
>
> A. DKIM signature verification
> B. Data Loss Prevention scanning
> C. SPF record validation
> D. Anti-malware attachment scanning
>
> > [!answer]- Show Answer
> > **B. Data Loss Prevention scanning**
> >
> > [[data-loss-prevention-dlp|DLP]] scans outbound email for patterns matching sensitive data such as credit card numbers, PII, and intellectual property, blocking or quarantining messages that violate policy. Option A verifies message integrity on inbound mail, not outbound content. Option C validates sender authorization, not message content. Option D scans for malware in attachments, not sensitive data patterns.

## Scenario

> See [[case-email-security]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [4.5 – Email Security](https://www.youtube.com/watch?v=v6ht9efsnRI)
