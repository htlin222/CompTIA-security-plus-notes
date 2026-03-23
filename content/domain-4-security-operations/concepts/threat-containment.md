---
title: "Threat containment"
description: "Ability to isolate a compromised endpoint from the network in real time"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Threat containment in EDR/XDR is the ability to immediately isolate a compromised endpoint from the network — blocking all network communications except those required for the EDR agent to continue communicating with the management platform — with a single click or automated trigger. This limits lateral movement and data exfiltration while preserving the ability to investigate the endpoint.

## Key Details

- EDR agent on the endpoint enforces network isolation even if the endpoint is not on the corporate network
- Agent continues to communicate with the EDR management console during isolation for ongoing investigation
- Can be triggered manually by an analyst or automatically by EDR detection rules
- Isolation is reversible: once investigation is complete, the endpoint can be released from isolation
- Network containment should be documented as part of the chain of custody in forensic investigations

## Connections

- Parent: [[edr-xdr]] — threat containment is a key response capability of EDR platforms
- See also: [[automated-response]]
