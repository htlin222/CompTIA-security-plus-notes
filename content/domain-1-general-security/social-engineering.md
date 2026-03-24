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

## Practice Questions

> [!qbank]- Q-Bank: Social Engineering (4 Questions)
>
> **Q1.** A CFO receives an email that appears to come from the company's external auditor, requesting an urgent wire transfer to a new account before end of business. The email uses the auditor's name, signature block, and references a real ongoing audit. Which type of social engineering attack is this MOST likely?
>
> A. Phishing
> B. Spear phishing
> C. Whaling
> D. Vishing
>
> > [!answer]- Show Answer
> > **C. Whaling**
> >
> > [[social-engineering|Whaling]] is a form of phishing that specifically targets high-level executives (C-suite), using highly personalized content and often involving financial requests — the CFO being targeted with an urgent wire transfer request is a classic whaling scenario. Spear phishing is targeted at specific individuals but the term "whaling" more precisely describes targeting executives. Generic phishing is untargeted mass email campaigns without personalization. [[vishing|Vishing]] uses voice calls, not email.
>
> **Q2.** A security team discovers that a popular industry forum frequently visited by their developers was compromised with a drive-by download exploit. Several developer workstations were infected after visiting the site. Which social engineering technique does this BEST describe?
>
> A. Baiting
> B. Pretexting
> C. Watering hole attack
> D. Typosquatting
>
> > [!answer]- Show Answer
> > **C. Watering hole attack**
> >
> > A [[watering-hole-attack|watering hole attack]] compromises a website frequently visited by the target group, exploiting the trust users place in familiar sites — the compromised industry forum targeting developers is a textbook example. [[baiting|Baiting]] offers something enticing like a USB drive or free download to lure victims, not compromising a trusted website. [[pretexting|Pretexting]] involves creating a fabricated scenario to extract information through direct interaction. [[typosquatting|Typosquatting]] registers domains similar to legitimate ones to capture mistyped URLs, not compromising legitimate sites.
>
> **Q3.** An employee holds the door open for a person carrying a large box who claims to be a delivery driver. The person is actually an unauthorized individual who gains access to the server room. Which physical social engineering technique was used?
>
> A. Tailgating
> B. Piggybacking
> C. Pretexting
> D. Shoulder surfing
>
> > [!answer]- Show Answer
> > **B. Piggybacking**
> >
> > [[tailgatingpiggybacking|Piggybacking]] occurs when an authorized person knowingly allows someone to follow them through a secured door — the employee intentionally held the door open. Tailgating occurs when someone follows through without the authorized person's knowledge or consent. While pretexting was used as part of the attack (claiming to be a delivery driver), the physical access technique itself is piggybacking. Shoulder surfing involves observing someone's screen or keyboard to steal information, not gaining physical access to a building.
>
> **Q4.** An attacker sends text messages to hundreds of employees claiming their corporate benefits enrollment will expire in 24 hours, with a link to a fake enrollment portal that harvests credentials. Which attack type and psychological principle are MOST involved?
>
> A. Phishing exploiting authority
> B. Smishing exploiting urgency
> C. Vishing exploiting fear
> D. Spear phishing exploiting scarcity
>
> > [!answer]- Show Answer
> > **B. Smishing exploiting urgency**
> >
> > [[smishing|Smishing]] is SMS-based phishing, and the 24-hour deadline creates urgency — a psychological principle that pressures victims into acting quickly without thinking critically. Phishing uses email, not text messages. [[vishing|Vishing]] uses voice calls, not text messages. Spear phishing is targeted at specific individuals, but this attack was sent to hundreds of employees indiscriminately, making it a mass smishing campaign rather than targeted spear phishing.

## Scenario

> See [[case-social-engineering]] for a practical DevOps scenario applying these concepts.
