---
title: "Case: The False Positive Cascade — SOAR Quarantine Failure"
description: "A SOAR playbook designed to auto-quarantine infected hosts triggers on a false positive from the EDR and isolates 85 production database servers during peak trading hours at a stock exchange. MTTR: 47 minutes."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

Velocity Trading operates a high-frequency trading platform for commodity futures, executing 50,000 trades per day with average trade latency requirements of <50 milliseconds. Their infrastructure runs on 150 servers: 85 database servers maintaining real-time market positions, 30 application servers handling trade execution, 20 analytics servers, and others.

In late January, they implemented a SOAR (Security Orchestration, Automation, and Response) platform integrated with their CrowdStrike EDR. The SOAR platform's primary playbook was designed to automatically quarantine any server that EDR flagged as potentially compromised: (1) isolate the server's network interface, (2) terminate all running processes, (3) create a snapshot for forensic analysis, (4) alert the incident response team.

The playbook had a documented threshold: any EDR alert with a threat score >80 would trigger automatic quarantine. This threshold was chosen to be sensitive (detecting most real threats) but with the assumption that false positives would be rare.

On January 14th at 2:37 PM Eastern Time, at the exact moment of peak trading volume (commodity prices were volatile due to weather reports affecting crop forecasts), a vulnerability in CrowdStrike's behavior analysis engine caused it to misidentify a legitimate system backup process as suspicious behavior. The backup process, running on all 85 database servers simultaneously, was flagged with a threat score of 87—above the 80-point threshold.

The SOAR playbook immediately triggered.

At 2:37:14 PM, the first database server's network interface was isolated. At 2:37:28 PM, the fifth database server went offline. By 2:37:45 PM, all 85 database servers had been quarantined. Velocity Trading's market connectivity suddenly died. The trading platform could no longer access the market data, couldn't read positions, couldn't execute trades.

Traders stared at blank screens. The exchange sent warning messages that Velocity Trading was not responding to trade confirmations. Pending trades were cancelled. Market positions became unknown. Within 60 seconds, Velocity had lost visibility into $400 million in open positions.

The incident response team, receiving alerts from the SOAR platform, immediately began investigating. They recognized the pattern—all 85 servers quarantined simultaneously—and suspected a false positive. But they couldn't quickly re-enable network access to 85 servers. The SOAR platform had to be overridden manually, each server restored individually, and each server's status verified before returning to service.

The recovery took 47 minutes:

- 0:00-5:00: Incident recognition and analysis
- 5:00-15:00: Manual override of SOAR playbook (required administrative action on each server)
- 15:00-47:00: Restoration of network connectivity and verification that services had recovered

During those 47 minutes, Velocity Trading lost approximately $2.1 million in trading revenue (based on their average daily P&L divided by trading hours and loss of 47 minutes of market access).

## What Went Right

- **Automatic detection and triage**: The SOAR platform detected the EDR alert and initiated response within seconds. If human analysts had needed to review the alert first, the detection would have taken minutes or hours.
- **Forensic snapshots captured**: Each quarantined server had a snapshot created at the exact moment of suspected compromise, preserving the system state for analysis.
- **Alert chain documentation**: The SOAR platform logged every action it took, every playbook execution, every override, enabling the incident response team to understand exactly what happened.

## What Could Go Wrong

- **No threshold for automatic quarantine**: Setting a 80-point EDR threshold for automatic isolation was too aggressive. A threshold of >95 would have been more conservative, requiring higher confidence before taking destructive action.
- **No blast radius limits**: The playbook was designed to quarantine servers globally. A better approach would have been to quarantine one server, wait 30 seconds to verify it was a real threat, then proceed with others.
- **No [[playbooksrunbooks]] testing for false positives**: The playbook was never tested with intentional false positive EDR alerts. A test run would have revealed the risk of mass quarantine.
- **No [[case-management]] workflow before destructive actions**: For high-impact systems, the SOAR platform should have created a case requiring human approval before executing destructive actions.
- **Missing business continuity context**: The SOAR platform didn't know that this was Velocity Trading's critical path—the database servers were the most critical systems. A more sophisticated [[orchestration]] would have prioritized less critical systems for automatic quarantine.

## Key Takeaways

- **Automatic destructive actions require extremely high confidence thresholds**: Automatic quarantine should only trigger at 95+ threat scores, not 80+. For critical systems, require human approval even at 95+.
- **Playbooksrunbooks must be tested extensively in staging**: Every [[orchestration]] playbook should be validated with: (1) real-world scenarios, (2) intentional false positives, (3) [[case-management]] workflow testing, and (4) disaster scenarios (what if the playbook itself fails?).
- **Blast-radius limits protect against cascading failures**: Instead of quarantining all servers matching criteria simultaneously, implement staged quarantine: (1) quarantine 1 server, (2) wait 30 seconds for validation, (3) quarantine the next batch of 5, (4) continue monitoring before escalating.
- **Business context must inform [[automation]] decisions**: A SOAR playbook for a trading platform should not operate the same way as a playbook for a development environment. Critical systems need more stringent approval workflows.
- **Case-management workflows should precede destructive actions**: Before quarantining servers, create an incident case that requires human approval. Automated quarantine should only follow approval unless in an active attack scenario.
- **Metrics-and-reporting on false positive rates should trigger playbook tuning**: If false positive rates exceed 1%, the threshold or rule logic needs adjustment. Velocity Trading's SOAR should have been monitoring false positive metrics daily.

## Related Cases

- [[case-siem]] — The SIEM can provide additional context (logs, network behavior) that helps validate EDR alerts before SOAR takes action.
- [[case-incident-response]] — SOAR orchestration works best as an acceleration tool for human incident response, not as a replacement for it. Humans provide judgment that automation lacks.
- [[case-automation-and-scripting]] — Automated scripts and playbooks must be tested with failure scenarios and false positive scenarios, not just happy-path scenarios.
