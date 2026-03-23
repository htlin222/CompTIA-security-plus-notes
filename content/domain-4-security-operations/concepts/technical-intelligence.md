---
title: "Technical intelligence"
description: "Specific IoCs — IP addresses, file hashes, domain names — fed into security tools"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Technical threat intelligence consists of specific, machine-readable Indicators of Compromise (IoCs) that can be directly consumed by security tools to detect or block known threats. These atomic indicators include IP addresses, domain names, URLs, file hashes (MD5/SHA256), email addresses, and other concrete observables that can be matched against network traffic, logs, and endpoint activity.

## Key Details

- Examples: malicious IP addresses for firewall blocklists, file hashes for EDR/AV signatures, malicious domains for DNS filtering
- Most immediately actionable of the three intelligence levels — can be automated into defenses
- Short shelf life: IP addresses and domains change frequently; file hashes change with each malware variant
- Fed into: firewall block rules, EDR/AV signature databases, SIEM watchlists, DNS sinkholes, proxy URL filters
- Quantity is less important than quality — a few high-confidence IoCs are more valuable than thousands of low-confidence ones

## Connections

- Parent: [[threat-intelligence]] — technical intelligence is the most operationally immediate type of threat intelligence
- See also: [[confidence-levels]]
