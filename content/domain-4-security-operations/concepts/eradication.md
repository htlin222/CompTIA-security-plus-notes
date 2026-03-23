---
title: "Eradication"
description: "Removing the threat — deleting malware, closing vulnerabilities, resetting compromised credentials"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

> [!eli5] ELI5: What is Eradication?
> After you contain a problem, eradication is removing it completely -- like pulling a weed out by the roots so it does not grow back.

## Definition

Eradication is the incident response phase in which all components of the threat are completely removed from the environment. This occurs after containment and involves not just removing the immediate malware or attacker tools, but also closing the initial vulnerability that was exploited, removing persistence mechanisms, and resetting any compromised credentials to prevent re-infection.

## Key Details

- Remove all malware, backdoors, web shells, and attacker-created accounts
- Patch or remediate the vulnerability used for initial access to prevent re-exploitation
- Reset passwords for all accounts that may have been compromised or accessed
- Rebuild systems from known-good backups or images if the integrity of the system is uncertain
- Verify eradication is complete before moving to recovery — rushing to recovery may leave remnants

## Connections

- Parent: [[incident-response]] — eradication is a critical phase in the IR lifecycle after containment
- See also: [[recovery]]
