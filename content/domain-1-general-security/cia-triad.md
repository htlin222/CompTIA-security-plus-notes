---
title: "CIA Triad"
description: "The three pillars of information security: Confidentiality, Integrity, and Availability"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/high
aliases:
  - "CIA Triad"
  - "Confidentiality Integrity Availability"
---

> [!eli5] ELI5: What is the CIA Triad?
> The CIA Triad is the three big promises of keeping information safe. Confidentiality means only the right people can see your secret diary. Integrity means nobody can sneak in and change what you wrote. Availability means you can always open your diary when you need it. Every security rule and tool exists to protect at least one of these three things. If any one of them breaks, your information is in trouble.

> [!eli5] ELI5: CIA 三要素 (繁體中文版)
> 想像你有一個秘密寶盒：
> 1. **機密性 (Confidentiality)**：只有你有鑰匙能打開看裡面的東西，別人看不到。
> 2. **完整性 (Integrity)**：沒人能偷偷換掉或弄壞裡面的東西，內容保證正確。
> 3. **可用性 (Availability)**：當你想看的時候，寶盒隨時都在那裡讓你打開。
> 任何安全規則都是為了保護這三件事。
>
> ```ascii
>       [機密性 Confidentiality]
>              / \
>             /   \
>            / CIA \
>           / 三要素 \
>          /_________\
> [完整性 Integrity] [可用性 Availability]
> ```

## Overview

The CIA Triad is the foundational model in information security that defines three core objectives: Confidentiality (preventing unauthorized disclosure), Integrity (preventing unauthorized modification), and Availability (ensuring authorized access when needed). Every security control, policy, and architecture decision can be mapped back to protecting one or more of these three properties.

## Key Concepts

- **[[confidentiality|Confidentiality]]** — protecting data from unauthorized access or disclosure
  - Controls: encryption, access controls, data masking, DLP
  - Threats: eavesdropping, data breaches, shoulder surfing, social engineering
- **[[integrity|Integrity]]** — ensuring data is accurate, complete, and unaltered by unauthorized parties
  - Controls: hashing, digital signatures, checksums, version control
  - Threats: man-in-the-middle attacks, malware, unauthorized modification
- **[[availability|Availability]]** — ensuring systems and data are accessible to authorized users when needed
  - Controls: redundancy, backups, load balancing, failover clusters
  - Threats: DDoS attacks, hardware failure, ransomware, natural disasters
- **[[dad-triad|DAD Triad]]** (opposite) — Disclosure, Alteration, Destruction; represents what attackers aim to achieve
- **[[non-repudiation|Non-repudiation]]** — often considered the fourth pillar; ensures actions cannot be denied after the fact

## Exam Tips

> [!tip] Remember
> **CIA vs. DAD**: Confidentiality opposes Disclosure, Integrity opposes Alteration, Availability opposes Destruction. Scenario questions often describe an attack — identify which CIA element is compromised.

> [!tip] Ransomware and CIA
> Ransomware primarily attacks **Availability** (locks you out of data) and **Confidentiality** (threatens to leak data in double-extortion schemes).

## Connections

- Core framework for all [[security-concepts]] and foundational to every exam domain
- Encryption technologies protect confidentiality (see [[encryption]])
- Hashing algorithms verify integrity (see [[hashing]])
- Redundancy and disaster recovery ensure availability (see [[resilience-and-redundancy]], [[disaster-recovery]])
- [[defense-in-depth]] layers controls to protect all three CIA properties simultaneously

## Practice Questions

> [!qbank]- Q-Bank: CIA Triad (4 Questions)
>
> **Q1.** A hospital's electronic health records system is hit by a ransomware attack that encrypts all patient data and threatens to publish it unless a ransom is paid. Which elements of the CIA triad are PRIMARILY compromised?
>
> A. Confidentiality and Integrity
> B. Integrity and Availability
> C. Confidentiality and Availability
> D. Confidentiality, Integrity, and Availability
>
> > [!answer]- Show Answer
> > **C. Confidentiality and Availability**
> >
> > Ransomware primarily attacks [[availability|Availability]] by locking users out of their data, and in double-extortion schemes threatens [[confidentiality|Confidentiality]] by publishing stolen data. While data integrity could be affected if files are corrupted, the primary attack targets are access denial (Availability) and data exposure threats (Confidentiality). Option A misses Availability, which is the most direct impact of encryption-based ransomware. Option B misses Confidentiality, which is threatened by the data leak extortion. Option D overstates the impact — Integrity is not the primary target.
>
> **Q2.** A security engineer implements SHA-256 checksums on all software packages before deployment to ensure they have not been tampered with during transfer. Which CIA triad element does this control PRIMARILY protect?
>
> A. Confidentiality
> B. Integrity
> C. Availability
> D. Non-repudiation
>
> > [!answer]- Show Answer
> > **B. Integrity**
> >
> > [[hashing|Hashing]] algorithms like SHA-256 verify that data has not been altered — this directly protects [[integrity|Integrity]] by detecting unauthorized modifications during transfer. Confidentiality would require encryption to prevent unauthorized viewing, not hashing. Availability ensures systems are accessible when needed, which checksums do not address. Non-repudiation proves who performed an action (typically via digital signatures), and while related to hashing, the primary purpose of checksums is integrity verification.
>
> **Q3.** A financial services company deploys redundant servers across two data centers with automatic failover, ensuring their trading platform remains operational even if one site goes offline. Which CIA triad element is this architecture PRIMARILY designed to protect?
>
> A. Confidentiality
> B. Integrity
> C. Availability
> D. Non-repudiation
>
> > [!answer]- Show Answer
> > **C. Availability**
> >
> > Redundancy, failover clusters, and geographically distributed data centers are classic [[availability|Availability]] controls that ensure authorized users can access systems when needed. Confidentiality controls prevent unauthorized disclosure (encryption, access controls), not service continuity. Integrity controls prevent unauthorized data modification (hashing, digital signatures), not infrastructure redundancy. Non-repudiation ensures actions cannot be denied and is achieved through logging and digital signatures, not redundant infrastructure.
>
> **Q4.** An attacker intercepts and modifies a wire transfer instruction between a bank and a payment processor, changing the destination account number. Which element of the CIA triad is MOST directly attacked, and what is the corresponding DAD triad term?
>
> A. Confidentiality — Disclosure
> B. Integrity — Alteration
> C. Availability — Destruction
> D. Integrity — Disclosure
>
> > [!answer]- Show Answer
> > **B. Integrity — Alteration**
> >
> > Modifying data in transit (changing the account number) is a direct attack on [[integrity|Integrity]], and the corresponding [[dad-triad|DAD triad]] opposite is Alteration. Confidentiality/Disclosure would apply if the attacker viewed the data without modifying it. Availability/Destruction would apply if the attacker prevented the transaction from being processed at all. Integrity/Disclosure is an incorrect pairing — Integrity's opposite in the DAD triad is Alteration, not Disclosure.

## Scenario

> See [[case-cia-triad]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [1.2 – The CIA Triad](https://www.youtube.com/watch?v=SBcDGb9l6yo)
