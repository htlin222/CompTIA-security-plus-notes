---
title: "Attack Vectors"
description: "Pathways and methods that threat actors use to gain unauthorized access to systems"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/medium
aliases:
  - "Attack Surface"
---

> [!eli5] ELI5: What are Attack Vectors?
> Picture your house. A burglar could try the front door, climb through a window, sneak in through the garage, or even come down the chimney. Each of those paths into your house is like an attack vector. In the computer world, bad guys look for every possible way in -- emails, websites, USB drives, even tricking people on the phone. The more paths you leave open, the easier it is for someone to break in.

## Overview

An attack vector is the path or method a threat actor uses to gain unauthorized access to a target system or network. Understanding attack vectors is crucial for identifying vulnerabilities, implementing appropriate controls, and reducing the overall attack surface. The SY0-701 exam tests the ability to recognize common vectors and recommend appropriate mitigations.

## Key Concepts

- **Message-based vectors**
  - Email — phishing, spear phishing, malicious attachments (see [[social-engineering]])
  - SMS — smishing attacks targeting mobile users
  - Instant messaging — malicious links through chat platforms
- **Image-based vectors**
  - Steganography — hiding malicious code within images
  - Malicious image files — exploiting image parser vulnerabilities
- **File-based vectors**
  - Malicious documents (macros in Office files, PDF exploits)
  - Infected removable media (USB drives)
  - Malicious software packages and updates
- **Voice-based vectors**
  - Vishing — phone-based social engineering
  - Voice deepfakes — AI-generated impersonation
- **Removable device vectors**
  - USB drop attacks — leaving infected drives for targets to find
  - Rubber Ducky — USB device that emulates a keyboard and executes payloads
- **Vulnerable software vectors**
  - Unsupported/unpatched systems, client-based vs. agentless
  - Zero-day vulnerabilities — no patch available yet
- **[[open-service-ports|Open service ports]]** — unnecessary services listening on the network
- **Supply chain vectors**
  - Compromised hardware, software, or managed service providers
  - SolarWinds-style attacks through trusted update mechanisms
- **[[human-vectors|Human vectors]]** — social engineering exploiting human psychology
- **[[attack-surface-management|Attack surface management]]** — continuously identifying and reducing exposure across all vectors
- **Bluetooth-based vectors**
  - **Bluejacking** — sending unsolicited messages to Bluetooth-enabled devices (annoying, not data theft)
  - **Bluesnarfing** — unauthorized access to data on Bluetooth devices (contacts, emails, calendars)

## Exam Tips

> [!tip] Remember
> The exam categorizes vectors as: **message-based, image-based, file-based, voice-based, removable device, vulnerable software, unsecure network, open service ports, default credentials, and supply chain**. Be able to identify each from a scenario.

> [!tip] Supply Chain Attacks
> These are high-weight on the SY0-701. A supply chain attack compromises a trusted vendor or software to reach the ultimate target. Think SolarWinds, Kaseya, or compromised npm packages.

## Connections

- Exploited by [[threat-actors]] based on their capabilities and motivations
- Social engineering is a major human-based attack vector (see [[social-engineering]])
- Mitigated through [[vulnerability-management]] and regular patching
- Network-based vectors defended by [[firewalls]], [[ids-ips]], and [[network-segmentation]]
- Supply chain vectors addressed through [[third-party-risk]] management programs

## Practice Questions

> [!qbank]- Q-Bank: Attack Vectors (4 Questions)
>
> **Q1.** A security team discovers that a widely used open-source library included in their application was compromised at the source repository, and malicious code was distributed through the normal update process. Which attack vector does this BEST describe?
>
> A. Vulnerable software vector
> B. File-based vector
> C. Supply chain vector
> D. Open service port vector
>
> > [!answer]- Show Answer
> > **C. Supply chain vector**
> >
> > A [[attack-vectors|supply chain attack]] compromises a trusted vendor, library, or update mechanism to reach the ultimate target — exactly what happened with the compromised open-source library distributed through normal updates (similar to SolarWinds or compromised npm packages). A vulnerable software vector involves exploiting unpatched or unsupported software, not a compromised trusted source. File-based vectors involve malicious documents or media, not poisoned software repositories. Open service port vectors involve unnecessary services listening on the network.
>
> **Q2.** An employee finds a USB flash drive labeled "Payroll Q4" in the company parking lot and plugs it into a workstation. The drive immediately executes a keystroke injection payload. Which type of attack vector and tool is MOST likely involved?
>
> A. File-based vector using a malicious macro
> B. Removable device vector using a Rubber Ducky
> C. Message-based vector using a phishing attachment
> D. Human vector using social engineering
>
> > [!answer]- Show Answer
> > **B. Removable device vector using a Rubber Ducky**
> >
> > A [[attack-vectors|Rubber Ducky]] is a USB device that emulates a keyboard and executes keystroke injection payloads automatically when plugged in — this is a classic removable device vector combined with a USB drop attack. A malicious macro requires the user to open a file and enable macros, not automatic keystroke injection. A message-based vector uses email or messaging, not physical media. While social engineering enticed the employee to plug in the drive, the attack vector itself is the removable device, not the human element.
>
> **Q3.** A penetration tester identifies that a target organization has multiple internet-facing servers running Telnet, FTP, and an outdated web server on non-standard ports. Which attack vector category should the tester's report PRIMARILY highlight?
>
> A. Vulnerable software vectors
> B. Supply chain vectors
> C. Open service ports
> D. Image-based vectors
>
> > [!answer]- Show Answer
> > **C. Open service ports**
> >
> > [[open-service-ports|Open service ports]] with unnecessary services (Telnet, FTP) listening on the network increase the attack surface and provide entry points for attackers. While the outdated web server also represents a vulnerable software vector, the primary finding described is unnecessary services exposed on the network. Supply chain vectors involve compromised third-party software or hardware, which is not described here. Image-based vectors involve steganography or exploiting image parsers, which is unrelated.
>
> **Q4.** A threat intelligence analyst observes that attackers are hiding command-and-control instructions within the metadata of JPEG images posted on a public website. Which attack vector is this technique MOST closely associated with?
>
> A. Message-based vector
> B. File-based vector
> C. Image-based vector
> D. Voice-based vector
>
> > [!answer]- Show Answer
> > **C. Image-based vector**
> >
> > Hiding data within images (steganography) is the defining characteristic of [[attack-vectors|image-based vectors]], which exploit image files to conceal malicious code or communication channels. Message-based vectors involve email, SMS, or instant messaging as the delivery mechanism, not embedded image data. File-based vectors typically involve malicious documents like Office macros or PDFs, not steganographic techniques in images. Voice-based vectors use phone calls or voice deepfakes for social engineering.

## Scenario

> See [[case-attack-vectors]] for a practical DevOps scenario applying these concepts.
