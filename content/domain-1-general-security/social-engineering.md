---
title: "Social Engineering"
description: "Psychological manipulation techniques used to trick people into compromising security"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/high
aliases:
  - "Social Engineering Attacks"
---

> [!eli5] ELI5: What is Social Engineering?
> Instead of picking a lock, what if a burglar just tricked you into handing over the key? That's social engineering. Bad guys use lies, fake stories, and pressure to get people to give up passwords, open dangerous files, or let strangers into secure places. They play on feelings like trust, fear, and helpfulness. It works because even the strongest computer security can be beaten when a person gets fooled.

## Overview

Social engineering is the art of manipulating people into performing actions or divulging confidential information. Rather than exploiting technical vulnerabilities, these attacks target human psychology — trust, fear, urgency, and curiosity. Social engineering is consistently one of the most effective attack methods and is heavily tested on the SY0-701 exam.

## Key Concepts

- **[[phishing|Phishing]]** — fraudulent emails impersonating legitimate entities to steal credentials or deliver malware
  - **Spear phishing** — targeted at specific individuals or organizations
  - **Whaling** — targets high-level executives (C-suite)
  - **Business Email Compromise (BEC)** — impersonating or compromising business email accounts
- **[[vishing|Vishing]]** — voice-based phishing via phone calls
- **[[smishing|Smishing]]** — SMS-based phishing via text messages
- **[[pretexting|Pretexting]]** — creating a fabricated scenario to gain trust and extract information
- **[[baiting|Baiting]]** — offering something enticing (USB drive, free download) to lure victims
- **[[tailgatingpiggybacking|Tailgating/Piggybacking]]** — following an authorized person through a secured door
  - Tailgating = without their knowledge; Piggybacking = with their consent
- **[[watering-hole-attack|Watering hole attack]]** — compromising a website frequently visited by the target group
- **[[typosquatting|Typosquatting]]** — registering domains similar to legitimate ones to capture mistyped URLs
- **[[brand-impersonation|Brand impersonation]]** — creating fake websites, emails, or social media profiles mimicking trusted brands
- **[[influence-campaigns|Influence campaigns]]** — large-scale disinformation operations to manipulate public opinion
- **Psychological principles exploited**:
  - Authority, urgency, scarcity, social proof, likability, fear, intimidation, consensus

## Exam Tips

> [!tip] Remember
> **Phishing family**: Email = Phishing, Phone = Vishing, SMS = Smishing, Targeted = Spear phishing, Executive = Whaling. The exam will describe a scenario and expect you to identify the specific type.

> [!tip] Tailgating vs. Piggybacking
> **Tailgating** = victim is unaware someone followed them through the door. **Piggybacking** = victim knowingly allows it (e.g., holds door open out of politeness).

## Connections

- Best countered by [[security-awareness-training]] to educate users on recognizing these attacks
- Phishing attacks mitigated by [[email-security]] controls like DMARC, DKIM, and SPF
- A primary method used by [[threat-actors]] of all sophistication levels
- Physical social engineering (tailgating) addressed through [[physical-security]] controls
- Credential theft from social engineering feeds into [[password-attacks]]

## Scenario

> See [[case-social-engineering]] for a practical DevOps scenario applying these concepts.
