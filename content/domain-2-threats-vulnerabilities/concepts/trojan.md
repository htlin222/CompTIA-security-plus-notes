---
title: "Trojan"
description: "Malware disguised as legitimate software; provides backdoor access or delivers additional payloads"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A Trojan (Trojan horse) is malware that disguises itself as or is bundled with legitimate, desirable software to trick users into installing it. Unlike viruses or worms, Trojans do not self-replicate—they rely on user action to install them. Once installed, they can create backdoors, steal data, download additional malware, or give attackers remote control of the compromised system.

## Key Details

- Named after the Greek myth: appears beneficial on the outside, delivers malicious payload once inside.
- **Does not self-replicate**: Unlike viruses (which infect files) or worms (which spread through networks)—Trojans rely on social engineering for installation.
- Common delivery: **pirated software**, **malicious email attachments**, **fake software updates**, **drive-by downloads**, **phishing links**.
- Types: **banking Trojans** (Zeus, Emotet), **downloader Trojans** (download and install other malware), **backdoor Trojans**, **RATs** (Remote Access Trojans).
- **Dropper**: A Trojan variant that installs other malware and then may remove itself.

## Connections

- Parent: [[malware-types]] — a fundamental malware delivery mechanism
- See also: [[rat-remote-access-trojan]]
