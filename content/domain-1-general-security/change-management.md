---
title: "Change Management"
description: "Structured process for managing changes to IT systems while minimizing security risk"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/compliance
  - weight/medium
aliases:
  - "Change Control"
---

> [!eli5] ELI5: What is Change Management?
> Before your school repaints the cafeteria or moves all the desks around, they don't just do it randomly. Someone writes a plan, the principal approves it, they pick a time when students aren't there, and they make sure they can put things back if it goes wrong. Change management for computers works the same way -- every change gets planned, approved, and tested so nothing accidentally breaks.

## Overview

Change management is a structured process for proposing, evaluating, approving, implementing, and reviewing changes to IT systems and infrastructure. It ensures that modifications do not introduce security vulnerabilities, cause service disruptions, or violate compliance requirements. The SY0-701 exam emphasizes change management as a critical governance control.

## Key Concepts

- **[[change-advisory-board-cab|Change Advisory Board (CAB)]]** — group of stakeholders who review and approve/deny change requests
- **Change management process**:
  1. **Request** — formal proposal documenting the change, rationale, and impact
  2. **Impact analysis** — assess risk, scope, affected systems, and rollback plan
  3. **Approval** — CAB or designated authority reviews and authorizes
  4. **Implementation** — execute the change during an approved maintenance window
  5. **Documentation** — record what was changed, when, and by whom
  6. **Verification/Testing** — confirm the change works as intended without side effects
- **Types of changes**:
  - **Standard** — pre-approved, low-risk, routine changes (e.g., password resets)
  - **Normal** — requires full CAB review and approval
  - **Emergency** — expedited process for critical issues; documented retroactively
- **[[backoutrollback-plan|Backout/Rollback plan]]** — predefined steps to reverse a change if it causes problems
- **[[maintenance-windows|Maintenance windows]]** — scheduled periods for implementing changes with minimal user impact
- **[[version-control|Version control]]** — tracking changes to configurations, code, and documentation
- **[[configuration-management|Configuration management]]** — maintaining a baseline of system configurations
- **Technical implications of changes**:
  - Allow/deny lists, firewall rules, downtime requirements
  - Service restarts, legacy application compatibility
  - Dependencies between systems

## Exam Tips

> [!tip] Remember
> Every change must have: **documentation, approval, testing, and a rollback plan**. If a scenario describes skipping any of these steps, that is the security concern. The exam loves testing "what went wrong" in a change management failure.

> [!tip] Emergency Changes
> Emergency changes bypass normal approval but still require **retroactive documentation and review**. They are not exempt from the process — just expedited.

## Connections

- Supports [[governance]] by enforcing structured oversight of system modifications
- Prevents unauthorized changes that could undermine [[security-policies]]
- Integrates with [[infrastructure-as-code]] for automated and auditable deployments
- Part of [[compliance]] requirements in frameworks like ITIL, SOC 2, and ISO 27001
- Change failures may trigger [[incident-response]] if they cause security incidents

## Practice Questions

> [!qbank]- Q-Bank: Change Management (4 Questions)
>
> **Q1.** A system administrator applies a firewall rule change during business hours without documenting the change or obtaining approval. The next day, several business-critical applications are unreachable. Which change management failure is the PRIMARY cause of this issue?
>
> A. Lack of a backout/rollback plan
> B. Missing impact analysis and approval process
> C. Failure to use version control
> D. Not scheduling a maintenance window
>
> > [!answer]- Show Answer
> > **B. Missing impact analysis and approval process**
> >
> > The [[change-management|change management]] process requires impact analysis to assess risk and scope, followed by CAB or authority approval before implementation. Skipping these steps directly caused the outage because the effects were not evaluated. While a rollback plan is important, it addresses recovery rather than prevention. Version control tracks changes but would not have prevented the unapproved modification. Scheduling a maintenance window reduces user impact but does not replace the need for impact analysis and approval.
>
> **Q2.** During a major security incident, the security team needs to immediately patch a critical vulnerability on production servers. There is no time for a full CAB review. Which type of change process should they follow?
>
> A. Standard change
> B. Normal change
> C. Emergency change
> D. Unauthorized change
>
> > [!answer]- Show Answer
> > **C. Emergency change**
> >
> > An [[change-management|emergency change]] follows an expedited process for critical issues that cannot wait for normal CAB review, but still requires retroactive documentation and review afterward. A standard change is pre-approved and routine (like password resets), not applicable to critical emergency patching. A normal change requires full CAB review and approval, which the scenario states there is no time for. An unauthorized change bypasses the process entirely without any intent to document — emergency changes are still within the process framework.
>
> **Q3.** A company's change management policy requires four elements for every system modification. A junior technician completed a server upgrade with proper documentation, testing, and approval but did not prepare a rollback plan. Which essential element was MOST critically missing?
>
> A. Maintenance window scheduling
> B. Backout/rollback plan
> C. CAB notification
> D. Version control commit
>
> > [!answer]- Show Answer
> > **B. Backout/rollback plan**
> >
> > Every change must have documentation, approval, testing, and a [[backoutrollback-plan|backout/rollback plan]]. The rollback plan provides predefined steps to reverse a change if problems occur — without it, recovery from a failed change becomes ad hoc and risky. Maintenance window scheduling is important but is part of implementation planning, not one of the four essential elements. CAB notification falls under the approval process, which was already completed. Version control is a supporting tool, not one of the four core requirements.
>
> **Q4.** An IT manager needs to categorize a routine weekly antivirus definition update that has been performed identically for the past year. Which change type BEST applies to this modification?
>
> A. Emergency change
> B. Normal change
> C. Standard change
> D. Critical change
>
> > [!answer]- Show Answer
> > **C. Standard change**
> >
> > A [[change-management|standard change]] is pre-approved, low-risk, and routine — exactly matching a weekly antivirus update performed identically over time. An emergency change is for critical, time-sensitive issues that bypass normal review, not routine updates. A normal change requires full CAB review and approval, which is unnecessary overhead for a well-established routine task. "Critical change" is not a standard change management classification used in the SY0-701 exam framework.

## Scenario

> See [[case-change-management]] for a practical DevOps scenario applying these concepts.
