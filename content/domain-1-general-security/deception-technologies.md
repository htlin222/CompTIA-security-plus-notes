---
title: "Deception Technologies"
description: "Decoy systems and techniques designed to detect, deflect, and study attackers"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/medium
aliases:
  - "Honeypots"
  - "Honeynets"
---

> [!eli5] ELI5: What are Deception Technologies?
> It's like setting up a fake treasure chest in your room. If someone sneaks in and opens it, an alarm goes off -- and now you know someone was snooping. Security teams do the same thing with computers: they create fake files, fake passwords, and even fake computers that look real. No normal person would ever touch them, so if anyone does, it means a bad guy is in the system. It's a clever trap that catches intruders early.
>
> > [!eli5] ELI5: Deception Technologies (繁體中文版)
> > 欺敵技術就像是「假錢包」或「誘餌」。放一個假的系統在那裡讓壞人去攻擊，這樣你就能發現他們，同時保護真的系統。
> >
> > ```ascii
> > [攻擊者] ----> [真系統 (隱藏)]
> >            \--> [誘餌系統 (蜜罐)]
> > ```

## Overview

Deception technologies are security tools and techniques that use decoy systems, files, and credentials to detect, deflect, and analyze attacker behavior. By creating fake targets that appear legitimate, organizations can identify unauthorized activity early, slow down attackers, and gather intelligence about their tactics, techniques, and procedures (TTPs).

## Key Concepts

- **[[honeypots|Honeypots]]** — decoy systems designed to attract and trap attackers
  - **Low-interaction** — simulates limited services; easy to deploy, less intelligence gathered
  - **High-interaction** — fully functional system; riskier but captures detailed attacker behavior
- **[[honeynets|Honeynets]]** — networks of honeypots simulating an entire environment
- **[[honeyfiles|Honeyfiles]]** — fake files (e.g., "passwords.xlsx") placed on systems to trigger alerts when accessed
- **[[honeytokens|Honeytokens]]** — fake data (credentials, database records, API keys) that alert when used
- **[[dns-sinkholes|DNS sinkholes]]** — redirect malicious domain requests to a controlled server; disrupts botnet communication and detects infected hosts
- **[[fake-telemetry|Fake telemetry]]** — generating false network data to confuse attackers performing reconnaissance
- **[[deception-platforms|Deception platforms]]** — enterprise solutions that automate deployment and management of decoys across the network
- **Benefits**:
  - Early detection of lateral movement and insider threats
  - Low false-positive rate — legitimate users have no reason to access decoys
  - Intelligence gathering on attacker methods
  - Slows attackers by wasting their time on fake targets
- **Risks**:
  - Maintenance overhead; decoys must appear realistic
  - High-interaction honeypots can be co-opted if not properly isolated

## Exam Tips

> [!tip] Remember
> **Honeypot** = decoy system. **Honeynet** = network of honeypots. **Honeyfile** = decoy file. **Honeytoken** = decoy credential/data. **DNS sinkhole** = redirects malicious DNS to controlled IP. Know the distinctions — the exam tests each term specifically.

> [!tip] Key Advantage
> Deception technologies have a very low false-positive rate because legitimate users and processes should never interact with decoy resources. Any interaction is suspicious by definition.

## Connections

- Provides intelligence about [[threat-actors]] and their tactics, techniques, and procedures
- Complements [[ids-ips]] by offering an additional detection mechanism with fewer false positives
- Supports [[threat-intelligence]] and [[threat-hunting]] by gathering data on active adversaries
- Works within a [[defense-in-depth]] strategy as a detective control layer
- DNS sinkholes aid [[network-monitoring]] in identifying compromised internal hosts

## Practice Questions

> [!qbank]- Q-Bank: Deception Technologies (4 Questions)
>
> **Q1.** A security team places a file named "employee-salaries-2026.xlsx" on a file server with an alert configured to trigger whenever the file is accessed. No legitimate employee has any reason to open this file. Which deception technology is this an example of?
>
> A. Honeypot
> B. Honeynet
> C. Honeyfile
> D. DNS sinkhole
>
> > [!answer]- Show Answer
> > **C. Honeyfile**
> >
> > A [[honeyfiles|honeyfile]] is a fake file placed on systems specifically to trigger alerts when accessed — the decoy salary spreadsheet is a textbook example. A [[honeypots|honeypot]] is a decoy system, not a single file. A [[honeynets|honeynet]] is a network of honeypots simulating an entire environment. A [[dns-sinkholes|DNS sinkhole]] redirects malicious domain requests to a controlled server and is unrelated to file-based deception.
>
> **Q2.** A SOC analyst notices that several internal workstations are sending DNS queries to a known malicious command-and-control domain. The security team wants to redirect these queries to a controlled internal server to disrupt the botnet communication and identify all infected hosts. Which technology should they deploy?
>
> A. High-interaction honeypot
> B. Honeytoken
> C. DNS sinkhole
> D. Deception platform
>
> > [!answer]- Show Answer
> > **C. DNS sinkhole**
> >
> > A [[dns-sinkholes|DNS sinkhole]] redirects malicious domain requests to a controlled server, disrupting botnet communication and helping identify infected internal hosts — precisely the described use case. A high-interaction honeypot simulates a full system to study attacker behavior, not redirect DNS traffic. A [[honeytokens|honeytoken]] is fake data like credentials or API keys that alerts when used, not a DNS redirection tool. A deception platform manages multiple decoy types but the specific requirement is DNS redirection, making a sinkhole the direct answer.
>
> **Q3.** A security architect argues that deception technologies have a significant advantage over traditional IDS in terms of alert accuracy. What is the PRIMARY reason for this claim?
>
> A. Deception technologies use more advanced signature databases
> B. Legitimate users and processes should never interact with decoy resources
> C. Deception technologies analyze full packet payloads unlike IDS
> D. Deception technologies are placed outside the network perimeter
>
> > [!answer]- Show Answer
> > **B. Legitimate users and processes should never interact with decoy resources**
> >
> > [[deception-technologies|Deception technologies]] have an inherently low false-positive rate because no legitimate user or process has any reason to access decoy systems, files, or credentials — any interaction is suspicious by definition. Deception technologies do not rely on signature databases; they rely on the principle that decoys should never be touched. IDS can also perform deep packet inspection, so this is not a unique deception advantage. Deception technologies are typically deployed inside the network to detect lateral movement, not outside the perimeter.
>
> **Q4.** A penetration tester discovers what appears to be a fully functional web server with realistic data during an internal assessment. After spending several hours exploring it, they realize it was an intentional decoy that logged all their activities. Which type of deception technology was MOST likely deployed?
>
> A. Low-interaction honeypot
> B. High-interaction honeypot
> C. Honeytoken
> D. Fake telemetry
>
> > [!answer]- Show Answer
> > **B. High-interaction honeypot**
> >
> > A high-interaction [[honeypots|honeypot]] is a fully functional system that appears realistic and captures detailed attacker behavior over extended periods — matching the description of a realistic web server the tester spent hours exploring. A low-interaction honeypot simulates only limited services and would not sustain hours of realistic interaction. A [[honeytokens|honeytoken]] is fake data (credentials, records), not a full system. [[fake-telemetry|Fake telemetry]] generates false network data to confuse reconnaissance but does not present as an interactive system.

## Scenario

> See [[case-deception-technologies]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [1.2 – Deception and Disruption](https://www.youtube.com/watch?v=X_qfMVty4ts)
