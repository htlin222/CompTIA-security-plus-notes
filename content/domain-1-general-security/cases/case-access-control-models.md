---
title: "Case: The Classified Leak — DAC vs. MAC in 90 Days"
description: "After a defense contractor leaks classified aeronautics schematics through a carelessly inherited folder permission, the CISO mandates a shift from discretionary to mandatory access controls. A security architect faces 90 days to redesign access models across 12 business units."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

Apex Aerospace Systems manufactures avionics components and flight control systems for military and civilian aircraft. The company operates across 12 geographically dispersed engineering centers with approximately 3,200 employees. In February 2024, Elena Rodriguez, the Chief Information Security Officer, inherited a patchwork of access control systems that had accumulated over 20 years of mergers and acquisitions. Some divisions used Windows NTFS ACLs, some used traditional Linux POSIX permissions, and the legacy manufacturing division still relied on basic group-based access inherited from 2003-era systems.

At 4:15 PM on a Thursday in late February 2026, Alex Patel, a junior systems engineer at the Connecticut engineering facility, copied a dataset labeled "UNCLASSIFIED - For Internal Use Only - F-35 Flight Control Algorithm Variants" from a secure shared drive into his personal OneDrive folder. He was consolidating files before a team reorganization and wanted to keep a "working copy." The problem: his OneDrive was configured with overly permissive settings inherited from a previous role in the sales department. His folder's NTFS ACL allowed "Connecticut Engineering Staff" and "All Employees With Contractor Access" full read/write permissions. Three other engineers immediately downloaded the 47 MB dataset. Within two hours, one of them shared it via Slack with a colleague at another facility. By 6:30 PM, the dataset had been downloaded nine times across the company.

By 9:15 PM that night, someone who should not have had access—a contractor in the IT support team stationed at the Phoenix facility—noticed the unusual file activity in the storage logs and flagged it. The contractor, a former engineer, immediately recognized that the 47 MB file labeled with flight control algorithm variants was highly sensitive. The CISO was contacted. Elena reviewed the access logs and her stomach dropped: the file had been accessed from IP addresses in three states, including at least two that appeared to be residential ISPs (potentially unsecured home networks where employees were working).

The core problem was this: Apex Aerospace had never fully transitioned from discretionary-access-control (DAC) to mandatory-access-control (MAC) models. In a DAC system like Windows or traditional Linux, the file owner decides who can access the file. This is convenient for employees but catastrophic for classified information—a junior engineer can casually move sensitive data to a permissive folder without triggering any controls. In contrast, a MAC system like the [[bell-lapadula-model]] enforces information flow rules at the operating system level: a user with clearance level "Secret" can never move a "Top Secret" document into a folder accessible to users with "Confidential" clearance, period. The system blocks it regardless of what the file owner wants.

Elena pulled together a rapid assessment team and discovered the nightmare: there was no consistent [[data-classification]] enforcement anywhere in the company. Some divisions had classification metadata in SharePoint, but it was not bound to actual access control decisions. The [[bell-lapadula-model]] principle—"no write down" (you cannot write to a lower classification level)—had never been implemented. An "Unclassified" user could not read "Secret" documents, but a "Secret" user could freely write to "Unclassified" storage, which meant classified information could be demoted through careless sharing.

The [[authorization]] model was equally broken. A contractor who had been hired for a three-month IT support role five years ago still had "engineer" group membership because the access review process was ad-hoc. Alex's own permissions were the result of five role transitions over seven years: he had accumulated permissions from Sales (OneDrive permissiveness), Engineering (read access to design files), Manufacturing (legacy group membership), and Integration (access to integration test data). When he was finally moved to his actual role in Connecticut Engineering, nobody revoked the previous permissions—they just added new ones. The [[principle-of-least-privilege]] had been violated so thoroughly that nobody could accurately say what Alex was actually supposed to be able to access.

Elena made a decision on Friday morning: the company would implement a complete access control model redesign, moving from legacy DAC to a mandatory control framework aligned with the [[bell-lapadula-model]] and the [[biba-model]] (which prevents lower-integrity users from modifying high-integrity data). She gave the security architecture team 90 days.

By Monday, Elena's team had secured the immediate exposure: the dataset was classified as "Controlled Unclassified Information" (CUI) and added to a government list of disclosed items. A mandatory disclosure was made to the customer's contracting officer. The customer's audit team arrived Tuesday morning. The good news: the data contained algorithm variants, not the actual proprietary core code. The bad news: it confirmed that Apex Aerospace had inadequate information flow controls.

The real reckoning began. Elena's team spent week 1 conducting a baseline access review using automated tools. The results were horrifying: 1,247 user accounts had excessive permissions that didn't match their current job description. A network technician in Phoenix had inherited "Vault_Admin" group membership from a role 11 years ago. A receptionist at the Connecticut facility had read access to classified vendor contracts. An intern in HR had write access to the payroll database. The principle of least privilege had been aspirational at best.

Week 2-4: The team built a new role taxonomy. Instead of the existing sprawl of 347 distinct permissions combinations, they defined 23 job-based roles:

- Manufacturing_Technician (limited read on legacy systems, no cloud access)
- Product_Engineer_L1 (read access to engineering documents, no classified access)
- Product_Engineer_L2 (read/write on current-generation designs, no classified)
- Security_Clearance_Engineer (read "Controlled Unclassified" documents, write only to classified storage)
- Contracting_Officer (read access to contracts, write access to procurement documents)
- IT_Support (system access limited to support functions, audited logging)

Week 5-8: Implementation of mandatory access controls. The team selected CentOS systems with SELinux for the most sensitive workloads (design databases, classified document repositories). For Windows domains, they implemented AppLocker to enforce application-level restrictions and configured NTFS ACLs to deny "Everyone" by default, then grant permissions explicitly per role. They also deployed Azure Identity Governance to enforce annual access reviews—users who hadn't explicitly confirmed their need for access every 365 days were automatically revoked.

Week 9: The critical test. A simulated scenario: an engineer in the "Product_Engineer_L1" role attempted to move a classified document to their shared folder. The [[bell-lapadula-model]] policy rejected it at the file system level—the operation failed with a clear error message: "Cannot downgrade classification level. Contact security@apexaero.com." The same engineer tried to open a classified document they didn't have clearance for. The mandatory access control (SELinux enforced at the kernel level) denied the read operation.

By Day 90, the migration was complete. Every user had been remapped to exactly one primary role, with explicit approval from their manager. Access to classified documents now required documented security clearance. Every file server enforced the [[bell-lapadula-model]] through mandatory controls, not discretionary settings that employees could accidentally override.

The final audit found zero discrepancies in the new access control model. More importantly, a post-implementation security test showed that a junior engineer could no longer casually move classified data—the system itself enforced the boundary.

## What Went Right

- **Rapid detection and escalation**: The contractor who noticed the unusual file activity had the security awareness to flag it immediately. The escalation chain worked—the CISO was engaged within 2 hours of discovery.
- **Comprehensive forensics and scope assessment**: The team used storage logs, network flow analysis, and file timestamps to determine exactly who accessed what and when. They identified the nine download events and traced them to specific users.
- **Executive commitment to remediation**: Elena secured budget, staff, and timeline to completely overhaul the access control model. This wasn't a "quick fix" mentality—this was a fundamental redesign.
- **Mandatory access control enforcement**: The implementation of [[bell-lapadula-model]] and [[biba-model]] made it technically impossible to bypass the controls through carelessness. The system enforced policy rather than trusting humans.
- **Role-based structure eliminated accumulated permissions**: By consolidating 347 permission combinations into 23 well-defined roles, the team made the access model auditable and maintainable going forward.
- **Automated access review processes**: The enforcement of annual attestation eliminated the "fire and forget" problem where former employees retained access for years.

## What Could Go Wrong

- **No [[data-classification]] enforcement at the storage layer**: The dataset was labeled "Unclassified" in metadata, but that label had no connection to actual file system permissions. A user could read it and move it freely.
- **Absence of [[bell-lapadula-model]] controls**: The "no write down" principle was never implemented. Anyone could write classified information into lower-classification storage, demoting it through carelessness or malice.
- **Discretionary-access-control was the default everywhere**: File owners (employees) decided access levels individually. This works for personal folders but is catastrophic for classified or sensitive data.
- **Permission accumulation and drift**: Employees kept permissions from old roles because the access review process was ad-hoc and manual. Five year old permissions coexisted with current ones.
- **No [[principle-of-least-privilege]] enforcement**: Every employee had at least 4-6 permissions aggregated from past roles. Nobody was regularly challenged to justify why they needed each one.
- **Lack of [[zero-trust]] model**: The system assumed that "being logged in to the domain" meant you were trustworthy and should have broad access. There was no verification at the resource level.
- **No incident response playbook for data exposure**: When the file was found in multiple locations, there was no clear procedure for containing it, notifying affected parties, or preventing replication.

## Key Takeaways

- **Bell-lapadula-model and [[biba-model]] are not optional for classified or sensitive data**: Implement mandatory access controls that enforce information flow rules at the operating system or file system level, not just in application logic.
- **Discretionary-access-control must be eliminated for sensitive data**: Replace ad-hoc file owner decisions with centralized, role-based access policies enforced by the system.
- **Data-classification must be enforced technically, not just in metadata**: A file labeled "Classified" is worthless if the file system allows anyone to read it. Bind classification to actual access controls.
- **Principle-of-least-privilege requires automation**: Manual access reviews fail. Implement automated systems that revoke access older than 365 days unless explicitly renewed, or that flag permission combinations that exceed the role baseline.
- **Role-based access control simplifies everything**: Moving from 347 permission combinations to 23 well-defined roles made the system auditable, maintainable, and enforceable.
- **Authorization models must be regularly tested**: Use red team exercises to verify that a user cannot accidentally or intentionally access data outside their clearance level.

## Related Cases

- [[case-authorization]] — Deep dive into role-based authorization and privilege management
- [[case-identity-management]] — Automating access reviews and preventing permission drift
- [[case-data-classification]] — Establishing and enforcing classification systems
- [[case-zero-trust]] — Implementing verification at every resource boundary, not just at login
