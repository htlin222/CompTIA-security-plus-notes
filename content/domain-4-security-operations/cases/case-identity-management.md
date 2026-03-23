---
title: "Case: The Orphaned Accounts Nightmare — Identity Lifecycle Failures"
description: "An identity governance review at a 10,000-employee energy company discovers 1,800 orphaned accounts from employees who left up to five years ago. Fourteen of those accounts have active VPN sessions in the last 30 days."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

Pinnacle Energy Corporation operates power generation facilities across 12 states, employing 10,200 people across generation, transmission, distribution, and corporate functions. In October, the CISO initiated a comprehensive [[identity-governance]] review as part of the annual audit cycle. The task was simple: reconcile the employee database (HRIS system) with active accounts in all systems and identify any accounts where the employee no longer worked there.

What the forensics team discovered was alarming. Of the 10,200 people listed in the current HRIS database, there were 11,847 active accounts across all systems (Active Directory, email, VPN, Jenkins CI/CD, AWS, Salesforce, time-tracking systems, badge access, etc.). That meant 1,647 accounts were "orphaned"—belonging to people who were no longer employed at Pinnacle.

When the team dug deeper, the situation was worse. The 1,647 orphaned accounts dated back years:

- 340 accounts from 2023 (people who left more than a year ago)
- 520 accounts from 2022
- 510 accounts from 2021
- 210 accounts from 2020
- 67 accounts from 2019 or earlier

But the truly alarming finding came from correlating the orphaned accounts with VPN access logs. Fourteen of the 1,647 orphaned accounts had active VPN sessions within the last 30 days. Someone was using credentials from employees who no longer worked there to access the company VPN and, by extension, critical industrial control systems (ICS) that managed power generation.

The investigation that followed revealed:

1. **Incomplete offboarding processes**: When employees left, their managers were supposed to submit a termination request that would trigger a checklist of account removals: AD account disable, email deactivation, VPN revocation, etc. But the checklist was manual—a PDF form that was often incomplete or lost. There was no automated enforcement, no system of record tracking which items had been completed.

2. **Decentralized account management**: Every system (AWS, Salesforce, Jenkins, etc.) had its own user management interface and account database. There was no centralized [[directory-services]] or [[provisioning-and-deprovisioning]] system that could revoke access across all systems simultaneously. Revoking a user required manual requests to 8-12 different system administrators.

3. **Lack of periodic [[identity-lifecycle-management]] reviews**: There was no regular reconciliation between the HRIS database and actual accounts in systems. Once an account was created, it persisted indefinitely unless someone noticed.

4. **No [[role-based-access-control-rbac]] framework**: Access was granted ad-hoc based on requests, with no clear [[provisioning-and-deprovisioning]] criteria. When an employee left, nobody knew exactly what access they had or what needed to be revoked.

5. **Weak audit logging**: The VPN logs showed that someone was using a terminated employee's credentials to access the VPN, but the logs didn't show what resources were accessed after authentication, what commands were executed, or where the authentication came from.

The most concerning case: a transmission operations engineer named David Torres had left Pinnacle in January 2020 to take a job at another utility company. His account should have been disabled on his last day. Instead, the offboarding checklist was filled out incompletely—his email and badge were deactivated, but his AD account, VPN access, and Jenkins access were never revoked. In late September 2024, someone accessed the company VPN using David Torres's credentials (which apparently David had recorded/saved somewhere) and, once on the network, accessed the ICS environment to monitor power generation schedules and transmission loads.

The investigation couldn't definitively determine if this was David Torres himself (accessing his former employer's systems, which would be a criminal offense), a competitor trying to steal operational information, or some other threat actor who had obtained David's credentials. But the fact that 1,647 orphaned accounts existed—and 14 had active usage—meant this was a widespread vulnerability.

## What Went Right

- **Comprehensive audit discovered the problem**: The decision to do a full identity governance review across all systems revealed the orphaned account epidemic.
- **VPN logging enabled detection**: Even though the VPN logs didn't show the full activity after authentication, they did show that someone was using terminated employees' credentials.
- **Rapid containment**: Once orphaned accounts were identified, the security team immediately revoked access to 1,200 of the 1,647 accounts.
- **Audit trail exists**: Because Pinnacle did maintain access logs (even if incomplete), the forensics team could document which accounts had been used and when.

## What Could Go Wrong

- **No centralized provisioning system**: If every system manages users independently, offboarding becomes impossible to enforce consistently. A centralized [[directory-services]] system (like Active Directory federation) would have made mass revocation possible.
- **Manual checklists without enforcement**: The PDF offboarding form had no workflow engine, no notification system, no escalation if items weren't completed. Without automation, human error is guaranteed.
- **No periodic access reviews**: If Pinnacle had conducted monthly reconciliation between HRIS and active accounts, the 1,800-account gap would have been caught within weeks, not years.
- **Missing [[attribute-based-access-control-abac]] rules**: If access rules were tied to HRIS attributes ("termination_date"), accounts could be automatically disabled when that attribute was set.
- **Incomplete audit logging**: The VPN logs showed authentication but not subsequent activity. If the ICS environment had full session recording, the investigation would know exactly what the attacker accessed.

## Key Takeaways

- **Identity-lifecycle-management must be automated from provisioning through deprovisioning**: When an employee is hired in HRIS, an automated workflow should provision accounts in all systems. When terminated, an automated workflow should revoke access in all systems.
- **Implement centralized [[directory-services]]**: Use a central identity source (Active Directory, Azure AD) as the system of record. All other systems should integrate with this directory so revocation is immediate and consistent.
- **Provisioning-and-deprovisioning must enforce completion**: Use workflow automation with approval gates and audit trails. Don't use manual PDF checklists.
- **Conduct monthly [[identity-governance]] audits**: Reconcile active accounts in each system against the HRIS database monthly. Alert on any accounts that don't match an active employee.
- **Implement [[attribute-based-access-control-abac]] rules**: Allow access only if an HRIS attribute (department, termination_date, etc.) meets certain criteria. Automatically revoke when attributes change.
- **Session recording for sensitive systems**: For systems like VPN and ICS access, implement [[session-recording]] to capture not just authentication, but all activity within the session.
- **Implement [[mfa]] for critical systems**: Even if credentials are compromised, MFA prevents unauthorized access. A terminated employee's password alone shouldn't grant access to the VPN.

## Related Cases

- [[case-privileged-access-management]] — Privileged accounts like service accounts require even more stringent deprovisioning processes to prevent long-term persistence.
- [[case-sso]] — A [[sso]] system can enable centralized authentication across all systems, making authentication centralized; but user provisioning/deprovisioning still requires a process.
- [[case-mfa]] — MFA prevents someone from using a compromised password to authenticate even if the account wasn't deprovisioned.
