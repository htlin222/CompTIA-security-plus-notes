---
title: "Honeytokens"
description: "Fake data (credentials, database records, API keys) that alert when used"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What are Honeytokens?
> Picture a fake password hidden in a file. Nobody real would ever try to use it. If someone does, you instantly know a thief stole that file and is trying to use what's inside.

## Definition

Honeytokens are decoy digital artifacts—such as fake credentials, database records, API keys, or email addresses—that appear to be legitimate but are monitored and trigger alerts when anyone attempts to use them. Unlike honeypots (which simulate systems), honeytokens are specific pieces of data that can be embedded throughout an environment to detect unauthorized access or data theft.

## Key Details

- **Fake credentials**: A username/password combination that, if used, triggers an immediate alert—indicates credential theft.
- **Fake API keys**: API tokens that will never legitimately be called—any API call using them signals theft of developer credentials or secrets.
- **Canary tokens**: A widely used free tool (canarytokens.org) that generates web bugs, documents, and URLs that alert when accessed.
- **Fake database records**: A row in a customer database with a monitoring email address—if spammers or attackers use that address, the organization knows their database was exfiltrated.
- Excellent for detecting **insider threats** and **data exfiltration** after a breach.

## Connections

- Parent: [[deception-technologies]] — a data-level deception technique
- See also: [[honeyfiles]], [[honeypots]]
