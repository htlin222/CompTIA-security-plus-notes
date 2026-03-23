---
title: "Case: The Forgotten VPN Key — Credential Revocation at 2:47 AM"
description: "A SOC analyst's careful eye catches suspicious RADIUS logs at midnight, revealing a former contractor's credentials still active three months after termination. The incident exposes critical gaps in the AAA framework's accounting layer."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

MediTech Ventures, a Series B healthcare tech startup in Boston, operates a patient monitoring platform that hospitals depend on for real-time cardiac data streaming. The company employs 45 people spread across engineering, sales, and operations. In July 2025, they hired Marcus Chen, a highly skilled DevOps contractor, on a six-month project to architect their cloud infrastructure migration. By January 15, 2026, the project was complete and Marcus's contract ended. The offboarding checklist was standard: laptop returned, Slack revoked, GitHub access removed. What wasn't on the checklist was the VPN credential tied to his name.

At 2:47 AM on a Tuesday in March, the on-call SOC analyst, Priya Patel, was running her routine threat hunt when an unusual pattern appeared in the RADIUS authentication logs streaming into their Splunk instance. The logs showed seven failed authentication attempts from IP address 203.104.88.224 (geolocated to a VPN exit node in Hanoi, Vietnam) using the account "mchen_vpn_contractor." The attempts were methodical: each credential attempt was spaced exactly 3 minutes apart, suggesting automated dictionary attacks. After four failures, the account was temporarily locked by the RADIUS server. At 2:53 AM, a fifth attempt succeeded using a slightly different password variant—"mchen_vpn_contractor2021."

Priya's pulse quickened. She immediately checked the Active Directory notes and discovered Marcus Chen had been offboarded 53 days ago. The RADIUS server, which handles [[authentication]] for the VPN, had never received a credential revocation for this account. She escalated to the senior architect, David Kowalski, who was asleep but received an urgent call at 3:02 AM. By 3:15 AM, David was online examining the incident with a cup of cold brew coffee.

What they found was worse than expected. The [[accounting]] logs in the RADIUS system showed that "mchen_vpn_contractor" had made seven successful VPN connections in the past four days. Each session lasted 2–4 hours, and during each session, the attacker had enumerated network shares, attempted to connect to their CloudSQL databases, and made repeated queries to their LDAP server. The accounting layer showed exactly this data: who (username: mchen_vpn_contractor), what (resources accessed and commands executed), where (IP addresses and geolocation: Vietnam), and how long they stayed (2–4 hours per session). But nobody was reading these logs—they were being generated and discarded after 30 days of retention.

The [[authorization]] controls had also failed spectacularly. Once the attacker breached the VPN using the old credential, the RADIUS-to-LDAP mapping granted the account permissions that were still tied to Marcus's original contractor profile: full read access to the "engineering-shared" folder containing architecture diagrams, and read access to the development database backups that contained three months of patient device records. The [[authentication]] (you are who you say you are) succeeded, the [[authorization]] (you are allowed to access these resources) succeeded, but the [[access-control-models]] assumed credentials would be revoked promptly upon offboarding.

By 5:30 AM, David had revoked the account across all systems using their centralized Active Directory system—a button that had been added only six weeks earlier after a previous identity management incident. The forensic analysis was grim: the attacker had exfiltrated three months' worth of database snapshots containing anonymized but complete patient device records, heart rate variability data, and medication schedules. The [[siem]] hadn't triggered any alerting because the account's baseline behavior from July 2025 was old enough that the machine learning models didn't recognize the sudden login from Vietnam and late-night database queries as anomalous. Worse, Priya later discovered that the [[tacacs]] server (a backup authentication system for network device access) still had the contractor's credentials active.

## What Went Right

- **[[Radius]] and [[sso]] logging was comprehensive**: The [[accounting]] layer captured every successful and failed authentication attempt with full context (IP address, timestamp, session duration, LDAP queries, resource access). This created an audit trail that made discovery possible.
- **Priya's vigilance caught the attack early**: The analyst was actively threat hunting using Splunk, not just waiting for alerts. She recognized the pattern of seven failed attempts followed by a successful login as a classic brute-force attack signature.
- **Multi-factor evidence**: The combination of failed RADIUS attempts, successful logins from an anomalous location (Vietnam), database access patterns, and follow-up LDAP enumeration made the incident undeniable and impossible to dismiss as false positives.
- **Quick escalation and centralized revocation**: Once alerted, David knew exactly how to revoke the credential system-wide across RADIUS, LDAP, and SSO simultaneously because of the Active Directory integration implemented six weeks prior. Revocation took 3 minutes instead of the usual 4 hours per system.
- **Network segmentation limited blast radius**: The attacker could read data but couldn't execute code or modify systems—this was later attributed to the firewall rules limiting the contractor VLAN to read-only access on databases.

## What Could Go Wrong

- **Credential revocation processes were largely manual**: No automated workflow existed to revoke VPN credentials when an employee offboarded. The contractor checklist was a spreadsheet with no synchronization to RADIUS, LDAP, or [[tacacs]].
- **No [[mfa]] on the VPN**: The VPN only required a username and password—no second factor. A brute-force attack with a leaked credential list would be trivial. If Marcus had reused his password across personal accounts, the attacker would have had success with just the credential pair.
- **Lack of [[authentication]] baseline expectations and alerting**: The RADIUS logs existed but weren't being monitored for anomalies. A baseline rule like "flag logins from countries outside North America" would have caught this in minutes instead of after four successful sessions over four days.
- **No [[log-management]] integration with [[incident-response]]**: Splunk had the data, but nobody had set up alerting rules for geographically impossible logins, failed-then-successful authentication patterns, or after-hours VPN access from contractors.
- **[[Identity-management]] system drift**: The authorizations granted to Marcus's account were never re-evaluated after his contract ended. He should have been moved to a "contractor-offboarded" role with zero permissions to everything, but the access list was manually maintained and nobody triggered that transition.
- **No periodic access review process**: A quarterly attestation process where managers review who still needs access would have caught this in 90 days maximum.

## Key Takeaways

- **[[Aaa-framework]] requires three operational layers maintained continuously**: [[Authentication]] (do you have valid credentials?), [[Authorization]] (are you allowed to access these resources?), and [[Accounting]] (what did you actually do?) must all work together and be actively monitored throughout the credential's lifecycle.
- **Offboarding must be automated and verified across all systems**: Create a deprovisioning workflow that simultaneously revokes credentials across VPN, [[radius]], [[tacacs]], SSO, LDAP, and application-level access. Test this workflow quarterly with real data.
- **[[Mfa]] is non-negotiable for remote access**: Every credential-based authentication should require a second factor—a hardware security key, TOTP app, or SMS. This is true for VPN, for SSH, for admin portals, for everything. A single compromised password becomes worthless.
- **Accounting logs must have real-time alerting rules**: Implement [[siem]] rules that flag failed authentication followed by success (brute-force detection), authentication from new geographies (impossible travel), and concurrent sessions from the same account in different countries.
- **Baseline and anomaly detection matter more than signature matching**: A baseline rule like "VPN logins only from North America during business hours, flag all after-hours access from new countries" catches advanced attacks that don't match any known IOCs but violate normal behavior patterns.
- **Centralize identity management**: Every credential revocation should trigger immediately everywhere. LDAP, RADIUS, TACACS, SSO—these must be synchronized so that a single revocation in Active Directory cascades everywhere in under 60 seconds.

## Related Cases

- [[case-authentication]] — Deep dive into credential-based authentication systems, their vulnerabilities, and how to defend them
- [[case-identity-management]] — Understanding role lifecycle, automated deprovisioning, and access review processes across systems
- [[case-sso]] — How centralized single sign-on systems improve visibility and control across all [[accounting]] layers
- [[case-log-management]] — Building alerting rules and response workflows from raw authentication logs and SIEM data
