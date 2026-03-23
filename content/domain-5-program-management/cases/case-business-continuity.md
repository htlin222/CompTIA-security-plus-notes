---
title: "Case: The Silent Failure — Business Continuity in Crisis"
description: "A ransomware attack exposes a regional hospital chain's dangerously outdated BCP, forcing clinicians to resort to paper records while the security team races to restore systems in unprioritized order."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/case
---

## The Scenario

St. Catherine's Health Network operates five hospitals and 47 clinics across upstate New York and Vermont. On a gray Tuesday in February, during peak flu season with occupancy at 94%, their Electronic Health Records system went dark at 3:17 AM. A sophisticated LockBit ransomware variant had encrypted their primary Windows domain controllers, file servers, and the EHR database backup appliance in a coordinated strike that exploited an unpatched SQL Server vulnerability on an internet-facing management portal.

The incident commander—Angela Torres, the network's Chief Information Security Officer—reached for the Business Continuity Plan document on her shelf. It was bound and printed. It was last updated in August 2024—18 months ago. The contact list included five people who no longer worked there. The communication tree referenced a crisis team structure that had been reorganized twice since the plan was written. The [[business-continuity-vs-disaster-recovery]] section listed manual recovery steps that assumed someone could log into servers that were currently bricked and encrypted.

By sunrise, ICU nurses were handwriting patient vital signs on printed forms. The lab was unable to process blood work. The pharmacy had manually filled prescriptions since midnight using index cards—an error rate that terrified everyone. The hospital administration was fielding calls from referring physicians asking where their patients' records were. Angela's team was trying to determine what needed to be restored first, but the [[order-of-restoration]] in the BCP was alphabetical by system name, not by [[critical-business-functions]].

The real nightmare unfolded in the incident command center. The [[communication-plan]] referenced phone numbers that were disconnected. The vendor contact list for the EHR system was stale; the primary contact had been promoted to a regional role and had changed phone numbers. The [[disaster-recovery]] site in Boston, which was supposed to have current database replicas, had never been tested in a live failover scenario. When they finally reached the DR coordinator at 10 AM, he admitted the replication had been "having sync issues" for weeks but nobody had escalated it because it "usually resolves on its own."

The [[succession-planning]] problems became obvious when the Director of Technology couldn't be reached—he was at a conference without cell service—and nobody else had override privileges for the DR site's network configuration. The operations team that was supposed to execute the [[business-continuity]] plan included a contractor who was on medical leave and two staff members who had no hands-on experience with the actual recovery procedures because they'd joined the organization after the last (failed) BCP test.

Angela realized they weren't going to recover using the outdated plan. She pivoted to a manual recovery approach based on what the team could actually do: manually copying encrypted backups to external drives, hand-decrypting what they could from unencrypted backups, and restoring critical data to new hardware one patient module at a time. It took 72 hours to restore the main EHR functionality, during which patient care quality degraded significantly and the hospital operated at reduced capacity.

## What Went Right

- **Documented fallback procedures**: Despite the outdated plan, having _any_ [[business-continuity]] documentation allowed the team to at least attempt a systematic recovery rather than complete chaos.
- **Preserved backups in multiple locations**: The encrypted ransomware couldn't reach backups on physically isolated external drives, enabling eventual data recovery without paying ransom.
- **Incident escalation**: Angela recognized early that the outdated plan wasn't viable and pivoted to adaptive recovery rather than wasting time trying to follow incorrect procedures.
- **Staff commitment**: Despite the failures, clinicians, nurses, and IT staff worked together to maintain patient safety through manual processes during the crisis.

## What Could Go Wrong

- **Plan never updated after reorganizations**: This is the most preventable failure. The [[communication-plan]] must be refreshed whenever organizational structure changes, at minimum annually.
- **No regular [[testing-the-drp]] exercises**: If the team had executed even a tabletop exercise in 2025, they would have discovered the communication failures, stale contacts, and untrained staff members before the real incident.
- **Recovery procedures not actually tested**: The assumption that systems "could" be recovered without proof is catastrophic. The [[disaster-recovery]] site should have been validated with a full failover test at least quarterly.
- **No [[critical-business-functions]] prioritization**: Alphabetical ordering is not a [[business-impact-analysis]]. Without a clear prioritization based on patient safety and clinical dependencies, recovery became ad hoc.
- **Missing [[after-action-review]] culture**: If previous BCP tests had been documented and reviewed, lessons learned would have prevented these gaps from persisting.

## Key Takeaways

- **Business-continuity-vs-disaster-recovery requires active maintenance**: Plans age. Update contact lists immediately when staff changes occur. Refresh [[communication-plan]] content annually at minimum.
- **Order-of-restoration must be driven by [[critical-business-functions]] impact, not alphabetical convenience**: Conduct a [[business-impact-analysis]] to determine which systems must be recovered first based on organizational mission, not IT convenience.
- **Disaster-recovery sites need live validation**: Never assume replication is working or that failover will succeed. Test failover procedures quarterly with a documented recovery time and data loss measurement against your [[recovery-time-objective-rto]] and [[recovery-point-objective-rpo]].
- **Succession-planning must include DR site access and procedure authority**: Ensure multiple people can execute recovery steps and have necessary system access documented and tested.
- **After-action-review from previous tests must inform plan updates**: Every test failure is a gift—document it and fix the plan before a real incident.

## Related Cases

- [[case-disaster-recovery]] — Deeper dive into backup strategies and recovery validation
- [[case-business-impact-analysis]] — Understanding how to prioritize critical functions in the first place
- [[case-resilience-and-redundancy]] — Designing systems that prevent single-point-of-failure scenarios
- [[case-incident-response]] — Handling the crisis when plans fail
