---
title: "Anti-forensics"
description: "Techniques attackers use to hinder forensic analysis (encryption, log wiping, timestomping)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Anti-forensics?
> When a kid draws on the wall and then tries to wipe it off before Mom sees -- that is anti-forensics. Attackers try to erase their footprints so investigators cannot figure out what happened.

## Definition

Anti-forensics refers to a collection of techniques used by attackers to destroy, hide, or alter digital evidence in order to prevent or impede forensic investigation. These techniques are designed to cover an attacker's tracks and make it difficult or impossible for investigators to reconstruct what happened during a security incident.

## Key Details

- **Timestomping**: modifying file timestamps to hide when files were created or modified
- **Log wiping**: deleting or corrupting system, application, and security logs
- **Encryption**: encrypting malicious tools or stolen data to prevent analysis
- **Steganography**: hiding data within legitimate-looking files (images, audio)
- Investigators must account for anti-forensic activity when analyzing evidence and maintain chain of custody

## Connections

- Parent: [[digital-forensics]] — anti-forensics is a key challenge in forensic investigations
- See also: [[timeline-analysis]]
