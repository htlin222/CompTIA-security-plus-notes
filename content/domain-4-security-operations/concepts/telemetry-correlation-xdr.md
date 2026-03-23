---
title: "Telemetry correlation (XDR)"
description: "Combines data from endpoints, network, cloud, and email to detect multi-vector attacks"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - XDR
---

## Definition

Telemetry correlation in XDR (Extended Detection and Response) refers to the capability of XDR platforms to ingest and correlate security telemetry from multiple different security domains — endpoints, network, cloud infrastructure, identity, and email — to detect complex, multi-stage attacks that span across these domains. This cross-domain correlation is the key differentiator of XDR over traditional EDR.

## Key Details

- XDR correlates: endpoint process data + network connections + cloud API calls + email click events + identity logs
- Detects attacks that span multiple domains: initial email phishing → endpoint execution → lateral network movement → cloud exfiltration
- Reduces mean time to detect (MTTD) by correlating signals that would appear unrelated in isolated tools
- Reduces alert fatigue: correlated incidents surface as single, rich incident rather than multiple unrelated alerts
- XDR platforms include Palo Alto Cortex XDR, Microsoft Defender XDR, CrowdStrike Falcon XDR

## Connections

- Parent: [[edr-xdr]] — telemetry correlation is the defining capability of XDR platforms
- See also: [[behavioral-analysis]]
