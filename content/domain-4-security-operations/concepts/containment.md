---
title: "Containment"
description: "Short-term (isolate the system) and long-term (apply temporary fixes while building permanent solutions)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Containment?
> When someone spills juice on the table, you put towels around it so it does not drip onto the floor. Containment in security means stopping a problem from spreading to other computers.

## Definition

Containment is the third phase of the NIST incident response lifecycle, occurring after detection and analysis, in which the incident response team takes action to limit the spread and impact of the incident. Containment can be short-term (immediate isolation to stop active damage) or long-term (temporary measures applied to keep systems operational while permanent fixes are developed).

## Key Details

- **Short-term containment**: immediately isolate affected systems from the network; disconnect from internet
- **Long-term containment**: apply temporary patches, enhanced monitoring, or restrictions while building permanent fix
- Preservation of evidence must be balanced against urgency to contain
- Network isolation via EDR console, VLAN changes, or firewall rules
- Containment decisions depend on business impact — sometimes affected systems must stay online temporarily

## Connections

- Parent: [[incident-response]] — containment is a core phase in the incident response lifecycle
- See also: [[eradication]]
