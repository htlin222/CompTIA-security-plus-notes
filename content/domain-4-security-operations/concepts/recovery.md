---
title: "Recovery"
description: "Restoring systems to normal operations, monitoring for re-infection"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Recovery is the incident response phase in which affected systems are restored to normal, verified-clean operations after successful eradication of the threat. Recovery must be done carefully to ensure the threat has been fully eliminated before systems return to production, and enhanced monitoring should remain in place to detect any signs of re-infection or incomplete eradication.

## Key Details

- Restore from known-good backups if system integrity is uncertain (preferred over cleaning an infected system)
- Verify restored systems are patched and hardened before returning to production
- Credential reset for all potentially compromised accounts must be completed before recovery
- Enhanced monitoring: increased logging, SIEM alerts, and threat hunting on recovered systems for 30-90 days
- Prioritize recovery of business-critical systems; document the recovery process for future reference

## Connections

- Parent: [[incident-response]] — recovery is a key phase in the NIST IR lifecycle
- See also: [[eradication]]
