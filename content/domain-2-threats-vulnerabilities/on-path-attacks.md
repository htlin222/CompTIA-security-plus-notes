---
title: "On-Path Attacks"
description: "Attacks where the adversary positions themselves between two communicating parties to intercept or alter traffic"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/medium
aliases:
  - "Man-in-the-Middle"
  - "MitM"
---

> [!eli5] ELI5: What are On-Path Attacks?
> Say you're passing notes to a friend in class, but someone sitting between you secretly reads each note, maybe even changes what it says, then passes it along. Neither you nor your friend realizes anyone is in the middle. That's an on-path attack -- the attacker sits between two people (or computers) who are talking, secretly reading or changing messages as they pass through. Both sides think they're talking directly to each other, but everything goes through the attacker first.

## Overview

On-path attacks (formerly called man-in-the-middle attacks) occur when an attacker secretly positions themselves between two communicating parties, intercepting and potentially altering the data in transit. The attacker can eavesdrop on sensitive communications, steal credentials, inject malicious content, or modify transactions — all while both parties believe they are communicating directly with each other.

## Key Concepts

- **[[arp-spoofingpoisoning|ARP spoofing/poisoning]]**: The most common technique on local networks — redirects traffic through the attacker's machine by poisoning ARP caches
- **[[ssltls-stripping|SSL/TLS stripping]]**: Downgrading an HTTPS connection to HTTP so the attacker can read traffic in plaintext
- **[[ssltls-interception-ssl-proxy|SSL/TLS interception (SSL proxy)]]**: Using a trusted certificate to decrypt, inspect, and re-encrypt TLS traffic (used legitimately in corporate environments)
- **[[dns-spoofing|DNS spoofing]]**: Redirecting DNS responses to send users to attacker-controlled servers
- **[[https-spoofing|HTTPS spoofing]]**: Presenting a fraudulent certificate to intercept encrypted web traffic
- **[[session-hijacking|Session hijacking]]**: Stealing session tokens from intercepted traffic to impersonate authenticated users
- **[[man-in-the-browser-mitb|Man-in-the-Browser (MitB)]]**: Malware in the browser modifies transactions in real time (e.g., changing bank account numbers)
- **[[relay-attacks|Relay attacks]]**: Forwarding authentication exchanges between a victim and a legitimate service (common with NFC/RFID)
- **[[defenses|Defenses]]**: HTTPS everywhere, HSTS (HTTP Strict Transport Security), certificate pinning, mutual TLS, encrypted protocols

## Exam Tips

> [!tip] Remember
> On-path = attacker is BETWEEN two parties. ARP poisoning = Layer 2 on-path setup. SSL stripping = HTTPS downgraded to HTTP. Defense: use encrypted protocols (HTTPS, SSH), HSTS headers, and certificate validation.

- CompTIA now uses "on-path" instead of "man-in-the-middle" — know both terms
- HSTS tells browsers to ALWAYS use HTTPS, preventing SSL stripping
- Certificate pinning prevents acceptance of fraudulent certificates

## Connections

- Uses techniques from [[network-attacks]] like ARP poisoning and DNS spoofing to position the attacker
- Can intercept credentials vulnerable to [[password-attacks]] when encryption is stripped or absent
- [[wireless-attacks]] like evil twin APs are a common setup for on-path attacks
- [[encryption]] and proper certificate validation are the primary defenses against interception

## Practice Questions

> [!qbank]- Q-Bank: On-Path Attacks (4 Questions)
>
> **Q1.** A user connects to their bank's website over HTTPS, but an attacker on the same network has performed ARP poisoning and is intercepting traffic. The attacker downgrades the connection to HTTP so they can read the traffic in plaintext. Which on-path technique is being used?
>
> A. DNS spoofing
> B. Session hijacking
> C. SSL/TLS stripping
> D. Man-in-the-Browser
>
> > [!answer]- Show Answer
> > **C. SSL/TLS stripping**
> >
> > [[ssltls-stripping|SSL/TLS stripping]] downgrades an HTTPS connection to HTTP, allowing the on-path attacker to read plaintext traffic. DNS spoofing (A) redirects DNS responses to malicious servers but does not downgrade HTTPS to HTTP. Session hijacking (B) steals session tokens but does not describe the HTTPS-to-HTTP downgrade mechanism. Man-in-the-Browser (D) is browser malware that modifies transactions locally, not a network-level downgrade attack.
>
> **Q2.** A corporate security team wants to prevent on-path attackers from successfully performing SSL stripping attacks against employee web browsing. Which defense is MOST effective?
>
> A. Deploying a network IDS
> B. Configuring HSTS (HTTP Strict Transport Security) headers
> C. Installing antivirus software
> D. Using longer SSL certificate key lengths
>
> > [!answer]- Show Answer
> > **B. Configuring HSTS (HTTP Strict Transport Security) headers**
> >
> > HSTS instructs browsers to always use HTTPS, preventing the downgrade to HTTP that [[ssltls-stripping|SSL stripping]] requires. Network IDS (A) can detect but not prevent SSL stripping in real time. Antivirus (C) protects against malware, not network-level protocol downgrade attacks. Longer certificate key lengths (D) strengthen encryption but do not prevent the connection from being downgraded to unencrypted HTTP.
>
> **Q3.** An attacker compromises a user's browser with malware that silently modifies the destination account number during an online banking transfer, while the user sees the correct account number on screen. Which on-path attack variant is this?
>
> A. ARP spoofing
> B. SSL/TLS interception
> C. Relay attack
> D. Man-in-the-Browser (MitB)
>
> > [!answer]- Show Answer
> > **D. Man-in-the-Browser (MitB)**
> >
> > [[man-in-the-browser-mitb|MitB]] is browser-resident malware that modifies transactions in real time while displaying the original values to the user. ARP spoofing (A) is a network-level technique for positioning between hosts, not modifying browser content. SSL/TLS interception (B) decrypts and re-encrypts traffic at the network level, not within the browser. Relay attacks (C) forward authentication exchanges, typically in NFC/RFID contexts, not web banking transactions.
>
> **Q4.** CompTIA's SY0-701 exam uses the term "on-path attack" instead of the older terminology. Which attack description BEST matches the core concept of an on-path attack?
>
> A. An attacker floods a target with traffic to exhaust its resources
> B. An attacker positions themselves between two communicating parties to intercept or alter data
> C. An attacker guesses passwords through repeated login attempts
> D. An attacker exploits a software vulnerability to execute arbitrary code
>
> > [!answer]- Show Answer
> > **B. An attacker positions themselves between two communicating parties to intercept or alter data**
> >
> > The defining characteristic of an on-path attack (formerly man-in-the-middle) is the attacker's position between two communicating parties, enabling interception or modification of traffic while both sides believe they are communicating directly. Flooding with traffic (A) describes a [[denial-of-service]] attack. Guessing passwords (B) describes [[password-attacks]]. Exploiting software vulnerabilities (D) describes [[application-attacks]], not traffic interception.

## Scenario

> See [[case-on-path-attacks]] for a practical DevOps scenario applying these concepts.
