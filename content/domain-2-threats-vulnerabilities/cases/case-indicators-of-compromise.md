---
title: "Case: IOC Correlation Across Subsidiaries — Finding the Needle in 1,200 Alerts"
description: "A SIEM generates 1,200 correlated alerts overnight linking unusual DNS queries to known C2 domains in a CISA advisory. A Tier 2 analyst must determine if this is a coordinated APT campaign across European subsidiaries or false positives."
draft: false
date: 2026-03-21
tags:
  - domain/2
  - type/case
---

## The Scenario

GlobalTech Holdings operates 14 subsidiaries across Europe, Asia, and North America. In March 2026, CISA published a flash alert warning about a coordinated campaign by the Wizard Spider APT group, including a list of 47 command-and-control (C2) domains they were using.

GlobalTech's SIEM immediately began correlating network traffic against these [[indicators-of-compromise|IOCs]]. The correlation produced 1,200 alerts overnight. The alerts indicated that workstations and servers across multiple European subsidiaries were attempting connections to the C2 domains.

Tier 2 analyst Maria Garcia was tasked with triage. Her first actions:

1. **Validate the IOCs**: Were the C2 domains definitely malicious, or were they false positives? (CISA's advisory was authoritative; the domains were confirmed malicious)
2. **Determine the scope**: Which specific systems were affected?
3. **Determine the timeline**: When did the connections start?
4. **Determine if it was actual compromise or just blocked attempts**: Had the malware exfiltrated data or just attempted to communicate?

Investigation revealed:
- 47 workstations across 4 subsidiaries had attempted connections to the C2 domains
- The attempts were blocked by the firewall (the company had previously configured rules to block known APT C2 domains)
- The [[behavioral-indicators|behavioral patterns]] suggested malware was running on these systems (periodic connection attempts, consistent timing patterns)
- The malware had likely been installed weeks prior but had just been flagged once the IOCs were published

Maria escalated to the incident response team. The determination: this was a real compromise, not false positives. The systems had been infected with Wizard Spider malware, likely through a phishing campaign.

The remediation:
1. Isolate affected systems
2. Conduct forensic analysis to determine malware entry point
3. Identify all affected users and reset their credentials
4. Rebuild all compromised systems from clean backups
5. Sweep remaining systems for similar indicators

The forensic investigation identified that the malware had been delivered through a targeted phishing email impersonating IT support. The email included an attachment claiming to be a security update. Victims who opened the attachment were infected.

The investigation also revealed 12 additional systems with the same malware, for a total of 59 compromised systems across 4 subsidiaries.

## What Went Right

- **IOCs from CISA were actionable**: CISA's published list of C2 domains provided concrete indicators for threat hunting
- **SIEM was configured to correlate against IOCs**: Automatic correlation meant no manual searching was required
- **Firewall had already blocked the C2 connections**: This prevented data exfiltration
- **Forensic analysis identified the entry vector**: Phishing email with malware attachment
- **Rapid response prevented further spread**: Lateral movement attempts were detected and stopped

## What Could Go Wrong

- **1,200 alerts required triage and analysis**: Alert fatigue could have caused analysts to miss the real compromises
- **Blocked connections might be missed**: The malware was blocked by the firewall, but discovery only happened because of IOC correlation; it wouldn't have been detected through normal monitoring
- **Phishing continued to work**: 47 employees fell for the spear-phishing email despite security awareness training

## Key Takeaways

- **[[Indicators-of-compromise|IOCs]] from threat intelligence feeds should be ingested into SIEM**: Automatic correlation against known malicious domains/IPs/hashes enables rapid threat hunting
- **[[Behavioral-indicators]] (periodic connection attempts, consistent timing) suggest active compromise**: IOCs aren't perfect; behavioral analysis provides additional confirmation
- **Firewall-blocked connections should still trigger alerts**: Even if the firewall stopped the attack, the attempt indicates a compromised endpoint
- **CISA flash alerts warrant immediate investigation**: When CISA publishes IOCs about targeted campaigns, assume your organization might be affected
- **Phishing remains the most effective attack vector**: 47 employees clicking malicious attachments led to 59 compromised systems

## Related Cases

- [[case-siem]] — Configuring SIEM for IOC correlation and alert generation
- [[case-threat-intelligence]] — Obtaining and operationalizing threat intelligence IOCs
- [[case-incident-response]] — Triage and response procedures for widespread compromises
