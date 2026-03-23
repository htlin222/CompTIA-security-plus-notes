---
title: "Threat intelligence enrichment"
description: "Automatically querying threat feeds to add context to alerts before analysts review them"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Threat intelligence enrichment is an automated process in SOAR platforms that queries external threat intelligence sources to add contextual information to security alerts before human analysts review them. By automatically looking up IP addresses, domains, file hashes, and email addresses in threat intelligence feeds, enrichment provides analysts with valuable context that speeds triage and reduces investigation time.

## Key Details

- Enrichment queries: VirusTotal (file hash/URL reputation), Shodan (IP/port information), threat feed lookups, WHOIS data
- Adds context to raw alerts: "This IP is known to be associated with Emotet C2 infrastructure"
- Reduces analyst time spent on manual lookups by automating intelligence queries
- Enrichment data is included in the incident case for analyst review
- High-confidence threat intelligence can trigger automatic responses without analyst review

## Connections

- Parent: [[soar]] — threat intelligence enrichment is a key automated value-add provided by SOAR platforms
- See also: [[technical-intelligence]]
