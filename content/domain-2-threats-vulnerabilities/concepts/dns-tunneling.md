---
title: "DNS tunneling"
description: "Encoding data within DNS queries and responses to exfiltrate data or establish C2 channels"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

DNS tunneling is a covert communication technique that encodes data (command-and-control traffic or exfiltrated data) within DNS query and response packets. Since DNS traffic is rarely blocked or deeply inspected by firewalls, attackers can establish persistent communication channels through DNS even in highly restricted network environments. Tools like iodine, dnscat2, and DNScat enable this technique.

## Key Details

- DNS queries are limited in size, so data must be **encoded in subdomains** (e.g., `BASE64-DATA.attacker.com`).
- The attacker controls the authoritative DNS server for their domain, receiving the encoded data as DNS queries.
- **Indicators**: unusually high volume of DNS queries, queries for randomly-appearing long subdomains, DNS queries from unusual sources.
- Detection: **DNS analytics** tools, monitoring query rates, inspecting query content length and entropy.
- Mitigation: **DNS security monitoring**, **blocking DNS to external resolvers** (force internal DNS), **DNS filtering** solutions.

## Connections

- Parent: [[dns-attacks]] — covert use of DNS for data exfiltration and C2
- See also: [[network-based-indicators]]
