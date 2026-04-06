---
title: "Ransomware"
description: "Malware that encrypts victim data and demands payment for the decryption key"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/endpoint
  - weight/high
aliases:
  - "Crypto-Malware"
---

> [!eli5] ELI5: What is Ransomware?
> Picture someone sneaking into your room, putting all your favorite toys and books into a locked safe, and then saying "Pay me $50 or you'll never see them again." That's ransomware. It's a type of bad software that scrambles all your computer files so you can't open them, then demands money to unlock them. Sometimes the attacker also threatens to show your private stuff to everyone if you don't pay. It's one of the scariest computer threats because people can lose everything important to them.

> [!eli5] ELI5: 勒索軟體 (繁體中文版)
> 勒索軟體就是「電腦綁匪」。它會把你所有的檔案鎖起來，然後叫你付錢才給你鑰匙。有時還會威脅你不付錢就把你的秘密公開。
>
> ```ascii
> [資料夾] --(加密)--> [🔒 勒索信]
> ```

## Overview

Ransomware is a type of malware that encrypts a victim's files or locks system access, then demands a ransom payment (typically in cryptocurrency) in exchange for the decryption key. Modern ransomware operations have evolved into sophisticated criminal enterprises using double and triple extortion tactics. Ransomware is one of the most impactful and heavily tested threat types on the SY0-701 exam.

## Key Concepts

- **[[encryption-based-ransomware|Encryption-based ransomware]]**: Encrypts files using strong cryptographic algorithms; data is unrecoverable without the key
- **[[locker-ransomware|Locker ransomware]]**: Locks the user out of the system entirely without necessarily encrypting files
- **[[double-extortion|Double extortion]]**: Attackers exfiltrate data before encrypting — threaten to publish it if ransom is not paid
- **[[triple-extortion|Triple extortion]]**: Adds DDoS attacks or contacting victims' customers/partners as additional pressure
- **[[ransomware-as-a-service-raas|Ransomware-as-a-Service (RaaS)]]**: Criminal developers provide ransomware tools to affiliates in exchange for a cut of profits
- **[[common-delivery-methods|Common delivery methods]]**: Phishing emails, exploited vulnerabilities (especially RDP), drive-by downloads, supply chain compromise
- **[[lateral-movement|Lateral movement]]**: Ransomware spreads across the network before detonating to maximize impact
- **[[cryptocurrency-payment|Cryptocurrency payment]]**: Bitcoin or Monero used to make payments difficult to trace
- **[[notable-examples|Notable examples]]**: WannaCry (EternalBlue exploit), NotPetya (supply chain), LockBit, BlackCat/ALPHV

## Exam Tips

> [!tip] Remember
> Best defense against ransomware: offline/immutable backups + network segmentation + patching + user training. Never rely solely on paying the ransom — there is no guarantee of decryption, and it funds criminal operations.

- The 3-2-1 backup rule: 3 copies, 2 different media types, 1 offsite (ideally air-gapped or immutable)
- Network segmentation limits blast radius when ransomware detonates
- Know that paying ransom may violate OFAC sanctions if the threat actor is in a sanctioned country

## Connections

- Triggers [[incident-response]] procedures — ransomware events are major security incidents
- Impacts [[business-continuity]] — recovery depends on backup availability and tested restore procedures
- Uses [[encryption]] algorithms against the victim — strong crypto makes recovery without keys virtually impossible
- Delivered through phishing ([[email-security]]) and exploits of [[vulnerability-types]]

## Practice Questions

> [!qbank]- Q-Bank: Ransomware (4 Questions)
>
> **Q1.** A ransomware group exfiltrates 500 GB of sensitive customer data before encrypting the victim's servers. They demand payment both for the decryption key and to prevent public release of the stolen data. Which ransomware tactic does this BEST describe?
>
> A. Locker ransomware
> B. Single extortion
> C. Double extortion
> D. Ransomware-as-a-Service
>
> > [!answer]- Show Answer
> > **C. Double extortion**
> >
> > [[double-extortion]] involves both encrypting data and threatening to publish exfiltrated data, creating two separate pressure points for payment. Locker ransomware (A) locks system access but does not exfiltrate data. Single extortion would only involve the encryption demand. Ransomware-as-a-Service (D) is a business model for distributing ransomware, not an extortion tactic.
>
> **Q2.** An organization's BEST defense against ransomware rendering their data unrecoverable is which of the following?
>
> A. Paying the ransom promptly to receive the decryption key
> B. Maintaining offline, immutable backups following the 3-2-1 rule
> C. Installing a host-based firewall on all endpoints
> D. Deploying full-disk encryption on all servers
>
> > [!answer]- Show Answer
> > **B. Maintaining offline, immutable backups following the 3-2-1 rule**
> >
> > Offline/immutable backups ensure data recovery without paying the ransom. The 3-2-1 rule (3 copies, 2 media types, 1 offsite) provides resilience against ransomware destroying accessible backups. Paying the ransom (A) is never recommended — there is no guarantee of decryption, and it funds criminal operations. Host-based firewalls (C) help prevent initial access but do not ensure data recovery. Full-disk encryption (D) protects data confidentiality but does not prevent ransomware from encrypting files on top of it.
>
> **Q3.** A criminal organization provides ransomware tools, infrastructure, and payment processing to affiliates who carry out the actual attacks, taking a percentage of each ransom collected. Which model does this describe?
>
> A. Double extortion
> B. Triple extortion
> C. Ransomware-as-a-Service (RaaS)
> D. Advanced persistent threat (APT)
>
> > [!answer]- Show Answer
> > **C. Ransomware-as-a-Service (RaaS)**
> >
> > [[ransomware-as-a-service-raas|RaaS]] is a criminal business model where developers provide ransomware tools to affiliates for a share of profits. Double extortion (A) and triple extortion (B) are attack tactics, not business models for distributing ransomware. APT (D) refers to sophisticated state-sponsored or organized threat groups, not specifically a ransomware distribution model.
>
> **Q4.** During a ransomware incident, investigators discover the malware spread across the entire flat network within minutes before detonating simultaneously on all systems. Which mitigation would have MOST reduced the blast radius of this attack?
>
> A. Security awareness training
> B. Endpoint antivirus
> C. Network segmentation
> D. Email filtering
>
> > [!answer]- Show Answer
> > **C. Network segmentation**
> >
> > [[network-segmentation]] divides the network into isolated zones, directly limiting [[lateral-movement]] and reducing the blast radius when ransomware detonates. Security awareness training (A) helps prevent initial infection but does not limit spread once malware is inside. Endpoint antivirus (B) may detect ransomware but failed in this scenario, and does not architecturally limit spread. Email filtering (D) blocks phishing delivery but does not prevent lateral movement across a flat network.

## Scenario

> See [[case-ransomware]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [2.4 – Other Malware Types](https://www.youtube.com/watch?v=nu27ovJ5rqw)
