---
title: "Digital Forensics"
description: "Collection, preservation, and analysis of digital evidence following security incidents or legal matters"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/incident
  - weight/medium
aliases:
  - "Computer Forensics"
---

> [!eli5] ELI5: What is Digital Forensics?
> Think of a detective investigating a crime scene -- they take photos, dust for fingerprints, and put evidence in sealed bags so nothing gets contaminated. Digital forensics is the same thing, but for computers. When something bad happens on a computer or network, investigators carefully collect clues like files, messages, and activity logs. They have to be super careful so the evidence can be trusted later, just like a real crime scene.

## Overview

Digital forensics is the process of identifying, preserving, collecting, analyzing, and presenting digital evidence in a manner that is legally admissible. It plays a critical role during and after security incidents to determine what happened, how it happened, and who was responsible. Forensic principles ensure evidence integrity so findings can support legal proceedings or internal investigations.

## Key Concepts

- **[[order-of-volatility|Order of volatility]]**: Collect the most volatile evidence first — CPU registers → RAM → swap → disk → logs → network → archival media
- **[[chain-of-custody|Chain of custody]]**: Documented record of who handled the evidence, when, and what was done — breaks invalidate evidence
- **[[disk-imaging|Disk imaging]]**: Creating a bit-for-bit copy of storage media for analysis without altering the original
- **[[write-blockers|Write blockers]]**: Hardware or software tools that prevent accidental modification of evidence during acquisition
- **[[hash-verification|Hash verification]]**: Using MD5/SHA-256 hashes to prove the forensic copy is identical to the original
- **[[legal-hold|Legal hold]]**: Directive to preserve all relevant data when litigation is anticipated
- **[[timeline-analysis|Timeline analysis]]**: Reconstructing the sequence of events using file timestamps, logs, and artifacts
- **[[live-forensics-vs-dead-forensics|Live forensics vs. dead forensics]]**: Live = analyzing a running system (captures volatile data); dead = analyzing powered-off media
- **[[e-discovery|E-discovery]]**: Legal process of identifying and collecting electronically stored information (ESI) for litigation
- **[[anti-forensics|Anti-forensics]]**: Techniques attackers use to hinder forensic analysis (encryption, log wiping, timestomping)
- **[[rfc-3227|RFC 3227]]**: Guidelines for evidence collection and archiving; establishes order of volatility
- **[[time-offsets|Time offsets]]**: Accounting for time zone differences and clock drift when correlating forensic evidence
- **[[ftk-imager|FTK Imager]]**: Forensic imaging tool for creating bit-for-bit disk copies
- **[[autopsy|Autopsy]]**: Open-source digital forensics platform for analyzing disk images
- **[[dd|dd]]**: Unix command for creating raw disk images (`dd if=/dev/sda of=image.dd`)
- **[[memdump|memdump]]**: Tool for capturing volatile memory (RAM) contents for analysis

## Exam Tips

> [!tip] Remember
> Order of volatility (most to least): Registers → Cache → RAM → Disk → Remote logs → Archive. ALWAYS image first, analyze the copy. Never work on original evidence.

- If a system is ON, capture RAM before powering off — you lose volatile data otherwise
- Chain of custody must be maintained at ALL times; one gap can invalidate all evidence
- Know the difference between legal hold (preserve data) and e-discovery (produce data)

## Connections

- Core skill used during [[incident-response]] to determine scope and attribution of attacks
- [[log-management]] provides crucial evidence sources for forensic timeline reconstruction
- Evidence may reveal [[indicators-of-compromise]] that inform broader organizational defense
- Findings feed into [[threat-intelligence]] to improve detection of similar future attacks

## Practice Questions

> [!qbank]- Q-Bank: Digital Forensics (4 Questions)
>
> **Q1.** A forensic investigator arrives at a scene where a suspected compromised server is still powered on and connected to the network. What should the investigator do FIRST?
>
> A. Unplug the server to prevent further damage
> B. Capture the contents of RAM before taking any other action
> C. Create a disk image of the hard drive
> D. Review the server's firewall logs
>
> > [!answer]- Show Answer
> > **B. Capture the contents of RAM before taking any other action**
> >
> > According to the [[order-of-volatility]], the most volatile evidence must be collected first. RAM contents are lost when the system is powered off, making them the highest priority. Option A would destroy volatile data in memory. Option C is important but disk data is less volatile than RAM. Option D is useful for analysis but logs are less volatile than memory contents.
>
> **Q2.** During a forensic investigation, an analyst creates a bit-for-bit copy of a suspect's hard drive. Before beginning analysis, the analyst generates a SHA-256 hash of both the original and the copy. What is the PRIMARY purpose of this step?
>
> A. To encrypt the forensic copy for secure storage
> B. To compress the disk image for faster analysis
> C. To prove the forensic copy is identical to the original and has not been altered
> D. To scan the disk image for known malware signatures
>
> > [!answer]- Show Answer
> > **C. To prove the forensic copy is identical to the original and has not been altered**
> >
> > [[hash-verification]] using SHA-256 ensures the integrity of the forensic copy by proving it matches the original bit-for-bit. This is essential for maintaining the [[chain-of-custody]] and ensuring evidence is admissible in court. Option A describes encryption, not hashing. Option B describes compression, which is unrelated. Option D describes malware scanning, which is a separate analysis step.
>
> **Q3.** A company receives notification that it may be subject to a lawsuit. The legal department sends a directive to the IT team requiring preservation of all employee emails and documents related to a specific project. What is this directive called?
>
> A. Chain of custody
> B. E-discovery
> C. Legal hold
> D. Data loss prevention
>
> > [!answer]- Show Answer
> > **C. Legal hold**
> >
> > A [[legal-hold]] is a directive to preserve all relevant data when litigation is anticipated. It prevents routine deletion of potentially relevant information. Option A refers to documenting evidence handling, not data preservation directives. Option B ([[e-discovery]]) is the broader process of identifying and producing electronically stored information — legal hold is a step within that process. Option D is a technology for preventing data leakage, not a legal preservation directive.
>
> **Q4.** An incident responder is analyzing a compromised workstation and discovers that all system log files have timestamps modified to the same date, and several event logs have been cleared. Which anti-forensics technique is the attacker MOST likely using?
>
> A. Steganography
> B. Timestomping and log wiping
> C. Full disk encryption
> D. Network tunneling
>
> > [!answer]- Show Answer
> > **B. Timestomping and log wiping**
> >
> > [[anti-forensics]] techniques like timestomping (modifying file timestamps) and log wiping are used by attackers to hinder [[timeline-analysis]] and forensic reconstruction. Option A hides data within other files but does not alter timestamps. Option C protects data confidentiality but does not modify timestamps. Option D is a data exfiltration method, not a forensic evasion technique.

## Scenario

> See [[case-digital-forensics]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [4.8 – Digital Forensics](https://www.youtube.com/watch?v=KiEptGbnEBc&list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv&index=103)
