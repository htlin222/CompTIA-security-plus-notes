---
title: "DNS sinkholes"
description: "Redirect malicious domain requests to a controlled server to disrupt botnets and detect infected hosts"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What are DNS Sinkholes?
> When a bad program on your computer tries to call home to the bad guys, a DNS sinkhole redirects that call to a dead end. The bad program can't talk to anyone, and the security team knows which computer is infected.

## Definition

DNS sinkholes are a defensive deception technique where known malicious domains (used for botnet command-and-control, malware distribution, or phishing) are redirected to a controlled "sinkhole" server rather than their actual malicious destination. This disrupts attacker communications and, critically, reveals which internal hosts are attempting to reach those malicious domains—identifying infected or compromised systems.

## Key Details

- Operate by configuring DNS resolvers to return the sinkhole server's IP for blacklisted domains.
- **Botnet disruption**: Infected hosts cannot reach C2 servers, breaking the attacker's control.
- **Detection capability**: Any host that queries a sinkholes domain is flagged as potentially infected—high-fidelity indicator.
- Threat intelligence feeds provide lists of known malicious domains for sinkholing.
- Government and industry organizations (CISA, ISACs) often operate sinkholes and notify organizations of infected hosts.

## Connections

- Parent: [[deception-technologies]] — a DNS-based deception and detection technique
- See also: [[honeypots]], [[dns-hijacking]]
