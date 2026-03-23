---
title: "Reconnaissance"
description: "Passive (OSINT, DNS lookups) and active (port scanning, service enumeration) information gathering"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Reconnaissance is the first active phase of penetration testing in which testers gather information about the target organization and its systems to identify potential attack vectors. Reconnaissance can be passive (using publicly available information without directly interacting with target systems) or active (directly probing target systems, which may be detected by the target's security monitoring).

## Key Details

- **Passive reconnaissance**: OSINT (open-source intelligence), Google dorking, Shodan, DNS lookups, WHOIS, social media, job postings, LinkedIn
- **Active reconnaissance**: port scanning (nmap), service enumeration, banner grabbing, vulnerability scanning
- Active reconnaissance generates network traffic that may be detected by IDS/IPS and SIEM
- Information gathered: IP ranges, domain names, email formats, employee names, technologies in use, potential vulnerabilities
- Rules of engagement define the scope — only systems explicitly in scope may be actively scanned

## Connections

- Parent: [[penetration-testing]] — reconnaissance is the information gathering phase of penetration testing
- See also: [[phases]]
