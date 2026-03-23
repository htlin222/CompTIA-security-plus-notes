---
title: "DNS amplification"
description: "Using open DNS resolvers to amplify DDoS attacks — small queries generate large responses"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

DNS amplification is a DDoS attack that exploits open DNS resolvers to generate a large volume of response traffic directed at a victim. The attacker sends small DNS queries (spoofing the victim's IP as the source) for records with large responses (such as DNSSEC-signed zones or ANY queries), causing resolvers to flood the victim with traffic many times larger than the original query.

## Key Details

- **Amplification factor**: DNS can amplify traffic 50-100x—a 60-byte query can generate a 3,000-byte response.
- **ANY queries** return all DNS records for a domain—maximizing amplification.
- The victim receives traffic from thousands of legitimate DNS resolvers, making source-based blocking ineffective.
- Mitigation: **disable ANY queries** on authoritative servers, **configure DNS resolvers to respond only to authorized clients** (not open resolvers), **BCP38 ingress filtering**.
- **DNSSEC** inadvertently worsens amplification by creating larger signed responses.

## Connections

- Parent: [[dns-attacks]] — a DNS-based DDoS amplification technique
- See also: [[amplification-attack]], [[amplificationreflection]]
