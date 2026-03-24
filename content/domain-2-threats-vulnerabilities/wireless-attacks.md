---
title: "Wireless Attacks"
description: "Attacks targeting wireless networks and protocols including Wi-Fi, Bluetooth, and RFID"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/medium
aliases:
  - "Wi-Fi Attacks"
---

> [!eli5] ELI5: What are Wireless Attacks?
> Wi-Fi is like an invisible conversation happening through the air between your device and a router. Since it's traveling through open air instead of a wire, anyone nearby can try to listen in or interfere. Wireless attacks are when someone sets up a fake Wi-Fi network that looks real (like a fake lemonade stand), jams the signal so you can't connect, or eavesdrops on what you're sending. It's like someone with a walkie-talkie tuned to your channel, hearing everything you say.

## Overview

Wireless attacks exploit the inherent vulnerability of data transmitted over radio frequencies — anyone within range can potentially intercept or interfere with wireless communications. Wi-Fi, Bluetooth, NFC, and RFID each present unique attack surfaces. The Security+ exam tests knowledge of wireless attack techniques and the protocols and configurations that defend against them.

## Key Concepts

- **[[evil-twin|Evil twin]]**: Rogue access point that mimics a legitimate network's SSID to trick users into connecting
- **[[rogue-access-point|Rogue access point]]**: Unauthorized AP connected to the corporate network, creating a backdoor past perimeter security
- **[[deauthentication-attack|Deauthentication attack]]**: Sending forged 802.11 deauth frames to disconnect clients, often preceding an evil twin or handshake capture
- **[[wpawpa2-handshake-capture|WPA/WPA2 handshake capture]]**: Capturing the 4-way handshake to perform offline brute-force password cracking
- **[[wps-attacks|WPS attacks]]**: Exploiting Wi-Fi Protected Setup PIN vulnerability to recover the WPA key
- **[[krack-key-reinstallation-attack|KRACK (Key Reinstallation Attack)]]**: Exploiting a flaw in WPA2's 4-way handshake to decrypt traffic
- **[[bluetooth-attacks|Bluetooth attacks]]**: Bluejacking (unsolicited messages), Bluesnarfing (data theft), Bluebugging (full device control)
- **[[rfid-cloning|RFID cloning]]**: Copying RFID badge data to create unauthorized duplicate access cards
- **[[nfc-attacks|NFC attacks]]**: Eavesdropping on or manipulating Near Field Communication transactions
- **[[jamming|Jamming]]**: Flooding the wireless spectrum with noise to prevent legitimate communication (DoS)
- **[[war-driving|War driving]]**: Scanning for wireless networks while moving through an area to map vulnerable APs

## Exam Tips

> [!tip] Remember
> WPA3 fixes KRACK and adds SAE (Simultaneous Authentication of Equals) replacing PSK. Evil twin = fake AP, rogue AP = unauthorized AP on network. Always disable WPS. Use WPA3-Enterprise with 802.1X for maximum security.

- WEP is completely broken — never use it. WPA2-Enterprise with AES is minimum acceptable
- Deauth attacks work because management frames in 802.11 are not authenticated (fixed in 802.11w/WPA3)
- Bluetooth: disable when not in use, set to non-discoverable mode

## Connections

- Evil twin and deauth attacks are specific types of [[network-attacks]] in the wireless domain
- Wireless interception enables [[on-path-attacks]] between the victim and the access point
- Rogue APs and evil twins bypass controls that [[network-monitoring]] should detect through wireless IDS
- Wireless vulnerabilities are a category covered under [[vulnerability-types]]

## Practice Questions

> [!qbank]- Q-Bank: Wireless Attacks (4 Questions)
>
> **Q1.** An attacker sets up a Wi-Fi access point in a coffee shop with the same SSID as the legitimate free Wi-Fi network. Unsuspecting customers connect to the attacker's AP, allowing all their traffic to be intercepted. Which wireless attack is this?
>
> A. Rogue access point
> B. Evil twin
> C. Deauthentication attack
> D. War driving
>
> > [!answer]- Show Answer
> > **B. Evil twin**
> >
> > An [[evil-twin]] mimics a legitimate network's SSID to trick users into connecting, enabling traffic interception. A rogue access point (A) is an unauthorized AP connected to the corporate network, creating a backdoor — it does not necessarily mimic an existing SSID. A deauthentication attack (C) disconnects clients from a network but does not set up a fake AP. War driving (D) scans for wireless networks while moving through an area but does not involve setting up a fake AP.
>
> **Q2.** A security team notices that wireless clients are repeatedly being disconnected from the corporate Wi-Fi. Packet analysis reveals forged 802.11 deauthentication frames being broadcast. Which attack is occurring, and which protocol improvement addresses it?
>
> A. RFID cloning; WPA2-Enterprise
> B. Evil twin; DNSSEC
> C. Deauthentication attack; 802.11w / WPA3
> D. Jamming; frequency hopping
>
> > [!answer]- Show Answer
> > **C. Deauthentication attack; 802.11w / WPA3**
> >
> > A [[deauthentication-attack]] sends forged deauth frames to disconnect clients. 802.11w (Protected Management Frames), incorporated into WPA3, authenticates management frames to prevent this. RFID cloning (A) involves duplicating access badges, not Wi-Fi disconnections. Evil twin (B) is a fake AP, not forged deauth frames, and DNSSEC protects DNS, not Wi-Fi. Jamming (D) floods the RF spectrum with noise rather than sending specific deauth frames.
>
> **Q3.** An attacker captures the WPA2 4-way handshake between a client and access point, then performs offline brute-force cracking to recover the pre-shared key. Which defense BEST prevents this attack from succeeding?
>
> A. Disabling SSID broadcast
> B. Using a long, complex passphrase
> C. Enabling WPS for easier connection
> D. Reducing wireless transmit power
>
> > [!answer]- Show Answer
> > **B. Using a long, complex passphrase**
> >
> > A strong passphrase makes offline brute-force cracking of a captured [[wpawpa2-handshake-capture|WPA2 handshake]] computationally infeasible. Disabling SSID broadcast (A) provides minimal security through obscurity and does not prevent handshake capture. Enabling WPS (C) actually introduces additional vulnerabilities through its PIN-based authentication. Reducing transmit power (D) limits range but does not prevent an attacker within range from capturing handshakes.
>
> **Q4.** An employee copies the RFID data from a coworker's building access badge using a portable reader, then programs a blank card with the copied data to gain physical access. Which wireless attack is this?
>
> A. Bluesnarfing
> B. NFC eavesdropping
> C. RFID cloning
> D. Evil twin
>
> > [!answer]- Show Answer
> > **C. RFID cloning**
> >
> > [[rfid-cloning]] involves copying RFID badge data to create unauthorized duplicate access cards, enabling physical access bypass. Bluesnarfing (A) is a Bluetooth attack for stealing data from a device, not duplicating RFID badges. NFC eavesdropping (B) involves intercepting NFC communications, not cloning access cards. Evil twin (D) is a Wi-Fi attack using a fake access point, not a physical access card duplication.

## Scenario

> See [[case-wireless-attacks]] for a practical DevOps scenario applying these concepts.
