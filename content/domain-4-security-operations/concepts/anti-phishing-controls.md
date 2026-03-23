---
title: "Anti-phishing controls"
description: "URL rewriting, sandbox analysis of attachments, impersonation detection"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What are Anti-phishing Controls?
> These are like a spam filter for trick messages. They catch fake emails pretending to be from someone you trust before those emails can fool you into clicking something bad.

## Definition

Anti-phishing controls are security measures implemented primarily in email security gateways and web filtering systems to detect, block, and mitigate phishing attacks. These controls work by analyzing email content, links, attachments, and sender information to identify and quarantine messages designed to deceive users into revealing credentials or downloading malware.

## Key Details

- **URL rewriting**: rewrites URLs in emails so clicks are proxied through a security service for real-time analysis
- **Sandbox analysis**: detonates attachments in isolated environments to detect malicious behavior
- **Impersonation detection**: identifies emails spoofing executives, vendors, or trusted domains
- Works in conjunction with SPF, DKIM, and DMARC for sender authentication
- User security awareness training complements technical controls

## Connections

- Parent: [[email-security]] — anti-phishing controls are a core component of email security
- See also: [[business-email-compromise-bec]]
