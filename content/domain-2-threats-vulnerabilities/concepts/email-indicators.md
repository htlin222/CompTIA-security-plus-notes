---
title: "Email indicators"
description: "Phishing sender addresses, malicious attachment hashes, suspicious URLs in email bodies"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Email Indicators?
> These are the red flags in an email that tell you something is wrong -- like a weird sender address, a suspicious link, or an attachment you weren't expecting. They're clues that someone is trying to trick you.

## Definition

Email indicators of compromise are artifacts found in email messages that indicate malicious activity—such as phishing campaigns, malware delivery, or business email compromise (BEC). Analysts extract these indicators from suspicious emails and use them to block future messages, search historical mail logs for related activity, and share with threat intelligence platforms.

## Key Details

- **Sender addresses**: Look-alike domains (microsoft-security@microsofl.com), spoofed display names, recently registered domains.
- **Attachment hashes**: MD5/SHA-256 hashes of malicious attachments used to search across mail logs and endpoints for the same file.
- **Suspicious URLs**: Links to known phishing kits, lookalike domains, URL shorteners that hide the actual destination.
- **Email headers**: Reveal the true sending infrastructure—`X-Originating-IP`, `Received` chain—can expose attacker infrastructure.
- Email authentication failures (**SPF fail**, **DKIM fail**, **DMARC fail**) are strong indicators of spoofed or fraudulent email.

## Connections

- Parent: [[indicators-of-compromise]] — email-specific IoC category
- See also: [[phishing]]
