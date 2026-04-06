---
title: "Indicators of Compromise"
description: "Observable artifacts or behaviors that indicate a system or network has been breached"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/incident
  - weight/high
aliases:
  - "IoC"
---

> [!eli5] ELI5: What are Indicators of Compromise?
> After a burglar breaks into a house, they leave clues behind -- a broken window, muddy footprints, things moved around. Indicators of compromise are the digital clues that tell you a computer or network has been broken into. Maybe there are strange files that shouldn't be there, or a program is running at 3 AM when nobody's working. Security teams look for these clues the same way detectives look for evidence, so they can figure out what happened and stop it from getting worse.
>
> > [!eli5] ELI5: Indicators of Compromise (繁體中文版)
> > 入侵指標 (IoC) 就像是小偷闖進家裡後留下的腳印或指紋。在電腦世界裡，這可能是奇怪的檔案、陌生的連線紀錄或是系統變慢。
> >
> > ```ascii
> > [系統] --(異常跡象)--> [腳印/指紋] --(發現入侵者)
> > ```

## Overview

Indicators of Compromise (IoCs) are pieces of forensic evidence — such as file hashes, IP addresses, domain names, or behavioral patterns — that suggest a system or network has been compromised. IoCs are used by security tools and analysts to detect, investigate, and respond to security incidents. They represent the "breadcrumbs" left behind by attackers and are critical for threat detection and intelligence sharing.

## Key Concepts

- **[[file-based-indicators|File-based indicators]]**: Malicious file hashes (MD5, SHA-256), suspicious file names, unexpected file locations
- **[[network-based-indicators|Network-based indicators]]**: Known malicious IP addresses, suspicious domains, unusual outbound connections, C2 (command and control) traffic patterns
- **[[host-based-indicators|Host-based indicators]]**: Unexpected processes, registry changes, scheduled tasks, unauthorized user accounts, modified system files
- **[[behavioral-indicators|Behavioral indicators]]**: Unusual login times, impossible travel (logins from distant locations in short timeframes), lateral movement patterns
- **[[email-indicators|Email indicators]]**: Phishing sender addresses, malicious attachment hashes, suspicious URLs in email bodies
- **[[account-indicators|Account indicators]]**: Multiple failed logins, privilege escalation attempts, account lockouts, new admin accounts
- **[[indicators-of-attack-ioa|Indicators of Attack (IoA)]]**: Proactive behavioral signals suggesting an attack is in progress (more real-time than IoCs)
- **[[stixtaxii|STIX/TAXII]]**: Standards for formatting (STIX) and sharing (TAXII) IoC data between organizations
- **[[threat-feeds|Threat feeds]]**: Automated IoC data streams from commercial and open-source providers
- **[[false-positives|False positives]]**: Legitimate activity that matches IoC patterns — tuning is essential

## Exam Tips

> [!tip] Remember
> IoCs = evidence of past compromise (reactive). IoAs = signs of active attack (proactive). Common IoCs: unexpected outbound traffic, unusual process execution, beaconing (regular interval C2 communication), new accounts.

- Beaconing (regular interval outbound connections) is a classic C2 indicator
- Data exfiltration indicators: large outbound transfers, DNS tunneling, encrypted traffic to unusual destinations
- IoCs have a shelf life — sophisticated attackers change infrastructure frequently

## Connections

- Fed into [[siem]] to create correlation rules and automated detection alerts
- Drives the detection phase of [[incident-response]] by identifying potential security events
- [[threat-intelligence]] provides IoCs from external sources to enhance organizational detection
- May reveal specific [[malware-types]] through file hashes and behavioral patterns

## Practice Questions

> [!qbank]- Q-Bank: Indicators of Compromise (4 Questions)
>
> **Q1.** A SOC analyst notices that a workstation makes HTTPS connections to the same external IP address every 60 seconds, regardless of user activity. Which indicator of compromise does this BEST represent?
>
> A. Impossible travel
> B. Beaconing
> C. Data exfiltration via DNS
> D. Credential stuffing
>
> > [!answer]- Show Answer
> > **B. Beaconing**
> >
> > Regular-interval outbound connections are classic beaconing behavior, indicating [[network-based-indicators|C2 (command and control) communication]] from malware checking in with its controller. Impossible travel (A) refers to logins from geographically distant locations in short timeframes. DNS exfiltration (C) uses DNS queries, not HTTPS connections. Credential stuffing (D) is a [[password-attacks|password attack]], not a network traffic pattern.
>
> **Q2.** An incident response team receives a threat intelligence feed containing SHA-256 file hashes, malicious IP addresses, and domain names associated with a new malware campaign. These are distributed using STIX format over TAXII protocol. What category of security data is this?
>
> A. Indicators of Attack (IoA)
> B. Vulnerability disclosures
> C. Indicators of Compromise (IoC)
> D. Penetration testing results
>
> > [!answer]- Show Answer
> > **C. Indicators of Compromise (IoC)**
> >
> > File hashes, malicious IPs, and domain names shared via [[stixtaxii|STIX/TAXII]] are classic IoCs — forensic artifacts used to detect known threats. IoAs (A) are behavioral signals indicating an active attack in progress, not static artifacts like hashes. Vulnerability disclosures (B) describe software weaknesses, not threat artifacts. Penetration testing results (D) are assessment findings, not threat intelligence data.
>
> **Q3.** A security team discovers a new administrator account that no one in IT created, along with several scheduled tasks running PowerShell scripts at 2 AM. Which type of indicators are these?
>
> A. Network-based indicators
> B. Email indicators
> C. Host-based indicators
> D. Behavioral indicators
>
> > [!answer]- Show Answer
> > **C. Host-based indicators**
> >
> > Unauthorized user accounts and suspicious scheduled tasks are [[host-based-indicators]] — evidence found on the compromised system itself. Network-based indicators (A) involve traffic patterns, IPs, and domains. Email indicators (B) relate to phishing addresses and malicious attachments. Behavioral indicators (D) describe user activity patterns like unusual login times, though the scheduled tasks overlap somewhat — the unauthorized account and system-level artifacts make host-based the BEST answer.
>
> **Q4.** After deploying new IoC signatures from a threat feed, a company's SIEM generates hundreds of alerts for legitimate software updates being flagged as malicious. What is this situation BEST described as?
>
> A. True positive
> B. False positive
> C. Indicator of Attack
> D. Beaconing
>
> > [!answer]- Show Answer
> > **B. False positive**
> >
> > Legitimate activity matching IoC patterns is a [[false-positives|false positive]], requiring tuning to reduce alert fatigue. A true positive (A) would mean the alerts correctly identified actual malicious activity. An Indicator of Attack (C) describes behavioral signals of an active attack, not a detection accuracy issue. Beaconing (D) is a specific C2 communication pattern, not a term for detection errors.

## Scenario

> See [[case-indicators-of-compromise]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [2.4 – Indicators of Compromise](https://www.youtube.com/watch?v=x72hG9GvkaQ)
