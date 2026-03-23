---
title: "DNSSEC (DNS Security Extensions)"
description: "Adds digital signatures to DNS records to verify authenticity and integrity"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - DNSSEC
---

## Definition

DNSSEC (DNS Security Extensions) is a suite of extensions to the DNS protocol that adds cryptographic authentication to DNS responses. DNSSEC signs DNS records with digital signatures using public-key cryptography, allowing resolvers to verify that the records they receive are authentic and have not been tampered with. It protects against DNS spoofing and cache poisoning attacks.

## Key Details

- Does **not** encrypt DNS data—only provides **authentication and integrity verification**.
- Uses a **chain of trust** from the root DNS zone down to individual domains—each level signs the keys of the next level.
- Key records: **DNSKEY** (public key), **RRSIG** (record signature), **DS** (delegation signer—links parent to child zone), **NSEC/NSEC3** (authenticated denial of existence).
- Inadvertently increases **amplification attack** potential due to larger signed responses.
- Adoption has been slow due to complexity; **DoH/DoT** are increasingly used as complementary protections.

## Connections

- Parent: [[dns-attacks]] — the primary defense against DNS spoofing and poisoning
- See also: [[dns-poisoning-dns-cache-poisoning]], [[dns-over-https-doh-dns-over-tls-dot]]
