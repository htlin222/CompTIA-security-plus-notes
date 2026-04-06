---
title: "Privileged Access Management"
description: "Controls and monitoring for accounts with elevated permissions to critical systems"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/identity
  - weight/high
aliases:
  - "PAM"
---

> [!eli5] ELI5: What is Privileged Access Management?
> In a school, the principal has a master key that opens every room. If that key gets lost, someone could go anywhere -- the office, the supply room, everywhere. Privileged access management is about keeping those master keys in a locked safe, only handing them out when absolutely needed, watching what people do with them, and taking them back as soon as possible. The fewer people holding master keys, the safer the building.

## Overview

Privileged Access Management (PAM) is a set of strategies and technologies for controlling, monitoring, and auditing elevated access to critical systems and data. Privileged accounts (admin, root, service accounts) are prime targets for attackers because they provide broad access. PAM solutions enforce least privilege and provide accountability for privileged actions.

## Key Concepts

- **[[password-vaulting|Password vaulting]]**: Storing privileged credentials in an encrypted vault; users check out passwords for time-limited sessions
- **[[just-in-time-jit-access|Just-in-time (JIT) access]]**: Granting privileged access only when needed and automatically revoking it after a set period
- **[[session-recording|Session recording]]**: Recording all actions taken during privileged sessions for audit and forensic purposes
- **[[credential-rotation|Credential rotation]]**: Automatically changing privileged passwords on a schedule or after each use
- **[[break-glass-accounts|Break-glass accounts]]**: Emergency access accounts with heightened monitoring for use when normal access paths fail
- **[[service-account-management|Service account management]]**: Tracking and securing non-human accounts used by applications and scripts
- **[[least-privilege-enforcement|Least privilege enforcement]]**: Ensuring even administrators only have access to what their role requires
- **[[separation-of-duties|Separation of duties]]**: Requiring multiple privileged users to complete sensitive operations
- **[[pap|PAP (Password Authentication Protocol)]]**: Sends passwords in cleartext; insecure, should be avoided
- **[[chap|CHAP (Challenge-Handshake Authentication Protocol)]]**: Uses challenge/response with hashing; more secure than PAP
- **[[ms-chapv2|MS-CHAPv2]]**: Microsoft's enhanced CHAP with mutual authentication

## Exam Tips

> [!tip] Remember
> PAM focuses on the "keys to the kingdom" — admin and root accounts. Key controls: vault credentials, limit time, record sessions, rotate passwords. If a scenario mentions admin access, think PAM.

- Service accounts are frequently overlooked — they often have excessive permissions and rarely rotate passwords
- Know the difference between PAM (managing privileged accounts) and general IAM (managing all accounts)
- Break-glass procedures should be documented and heavily monitored

## Connections

- Critical extension of [[identity-management]] for high-risk accounts
- Must be protected with [[mfa]] — privileged accounts should always require multi-factor authentication
- Helps detect compromises through [[log-management]] by recording privileged session activity
- [[hardening]] includes restricting and monitoring privileged access as a key security baseline

## Practice Questions

> [!qbank]- Q-Bank: Privileged Access Management (4 Questions)
>
> **Q1.** An organization's database administrators currently share a single root password that has not been changed in over a year. A security audit recommends implementing PAM controls. Which action should be taken FIRST?
>
> A. Deploy session recording software on all endpoints
> B. Store the root credential in an encrypted password vault with individual checkout and automatic rotation
> C. Disable the root account entirely
> D. Require all DBAs to use personal laptops for database access
>
> > [!answer]- Show Answer
> > **B. Store the root credential in an encrypted password vault with individual checkout and automatic rotation**
> >
> > [[password-vaulting]] with individual checkout provides accountability (who used the credential and when) and [[credential-rotation]] eliminates the risk of a stale, shared password. Option A adds monitoring but does not fix the shared credential problem. Option C would disrupt operations if no alternative privileged access method is in place. Option D introduces BYOD risks and does not address the credential management issue.
>
> **Q2.** A cloud administrator needs emergency access to a production system during a critical outage, but the normal PAM approval workflow is unavailable because the approval server is also down. Which PAM mechanism is designed for this situation?
>
> A. Just-in-time access provisioning
> B. Break-glass account
> C. Credential rotation policy
> D. Role-based access control
>
> > [!answer]- Show Answer
> > **B. Break-glass account**
> >
> > [[break-glass-accounts]] are emergency access accounts specifically designed for situations when normal access paths fail. They come with heightened monitoring and audit requirements. Option A ([[just-in-time-jit-access|JIT access]]) requires the approval workflow to be functioning. Option C is a scheduled credential management process, not an emergency access method. Option D defines access based on roles but does not provide emergency access mechanisms.
>
> **Q3.** A security team discovers that a service account used by an automated backup application has domain administrator privileges and its password has never been changed. What is the MOST significant risk?
>
> A. The backup application may run slower with a domain admin account
> B. If compromised, the service account provides an attacker full control over the entire domain
> C. The service account will generate excessive log entries
> D. The backup application license may not support privileged accounts
>
> > [!answer]- Show Answer
> > **B. If compromised, the service account provides an attacker full control over the entire domain**
> >
> > [[service-account-management]] is critical because service accounts often have excessive privileges and rarely rotate passwords, making them high-value targets. A domain admin service account with a static password is an extreme [[least-privilege-enforcement|least privilege]] violation. Option A is incorrect — privilege level does not affect performance. Option C may generate some additional audit events but is not the primary risk. Option D is a licensing concern, not a security risk.
>
> **Q4.** An organization implements a PAM solution that grants administrators elevated access only when a ticket is approved, and automatically revokes access after 4 hours. All actions during the session are recorded. Which PAM capability does the time-limited access represent?
>
> A. Password vaulting
> B. Session recording
> C. Just-in-time access
> D. Separation of duties
>
> > [!answer]- Show Answer
> > **C. Just-in-time access**
> >
> > [[just-in-time-jit-access|Just-in-time (JIT) access]] grants privileged access only when needed and automatically revokes it after a set period, minimizing the window of exposure. Option A ([[password-vaulting]]) stores credentials securely but does not inherently limit access duration. Option B ([[session-recording]]) is also described in the scenario but the question asks specifically about the time-limited access. Option D requires multiple people for sensitive operations, which is a separate control.

## Scenario

> See [[case-privileged-access-management]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [4.6 – Access Controls](https://www.youtube.com/watch?v=9ANHcZwJfdQ)
