---
title: "Intelligence-driven hunting"
description: "Using threat intelligence reports, IoCs, or known TTPs as starting points"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Intelligence-driven Hunting?
> This means using real reports about real bad guys to guide your search. If you know a thief targets red bikes, you go check on all the red bikes in the neighborhood first.

## Definition

Intelligence-driven hunting is a threat hunting methodology that uses external and internal threat intelligence as the starting point for hunting activities. Rather than forming original hypotheses, hunters begin with specific threat intelligence — such as a vendor report about a new threat actor, recently published IoCs, or MITRE ATT&CK-documented TTPs — and search for matching activity in the organization's environment.

## Key Details

- Starting point is threat intelligence: APT reports, threat feeds, industry alerts, government advisories
- Hunters search for specific IoCs (IP addresses, domains, file hashes) or behavioral patterns from threat intel
- More tactical and reactive than hypothesis-driven hunting; still more proactive than waiting for alerts
- Good entry point for organizations building a threat hunting capability (HM1-HM2 maturity)
- Results can update defensive controls: new detections, firewall blocks, or EDR rules

## Connections

- Parent: [[threat-hunting]] — intelligence-driven hunting is a key hunting methodology
- See also: [[threat-intelligence-integration]]
