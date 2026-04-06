---
title: "AAA Framework"
description: "Authentication, Authorization, and Accounting — the three pillars of access management"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/identity
  - weight/high
aliases:
  - "AAA"
---

> [!eli5] ELI5: What is the AAA Framework?
> Think of going to a theme park. First, they check your ticket to make sure you're really a guest (that's authentication). Then, the ticket says which rides you're allowed on -- maybe you have a VIP pass or a basic pass (that's authorization). Finally, the park keeps track of which rides you went on and when (that's accounting). Computers use these same three steps to keep track of who's using them and what they're doing.
>
> > [!eli5] ELI5: AAA Framework (繁體中文版)
> > AAA 就像是進入管制區的流程。1. 認證 (Authentication)：確認「你是誰」 (檢查證件)；2. 授權 (Authorization)：確認「你能做什麼」 (你有哪裡的鑰匙)；3. 紀錄 (Accounting)：記下「你做了什麼」 (攝影機紀錄)。
> >
> > ```ascii
> > [使用者] --1.身分驗證--> [管理系統] --2.權限控制--> [資源]
> >            ^                       |
> >            |----------3.行為紀錄-------|
> > ```

## Overview

The AAA (Authentication, Authorization, and Accounting) framework defines how users are identified, what they are permitted to do, and how their actions are tracked. AAA is implemented through protocols like RADIUS, TACACS+, and Kerberos and underpins identity and access management across enterprise environments.

## Key Concepts

- **Authentication** — verifying the identity of a user, device, or service (see [[authentication]])
  - Something you know (password), something you have (token), something you are (biometric)
- **Authorization** — determining what an authenticated entity is allowed to do (see [[authorization]])
  - Enforced through access control models (RBAC, ABAC, MAC, DAC)
- **[[accounting|Accounting]]** — logging and tracking user activities for audit and forensic purposes
  - Includes session duration, commands executed, data accessed, and resource usage
- **[[radius|RADIUS]]** (Remote Authentication Dial-In User Service) — UDP-based, encrypts only the password, commonly used for network access (Wi-Fi, VPN)
  - Combines authentication and authorization in a single step
- **[[tacacs|TACACS+]]** (Terminal Access Controller Access-Control System Plus) — TCP-based, encrypts the entire payload, separates AAA functions independently
  - Preferred for device administration (switches, routers, firewalls)
- **[[kerberos|Kerberos]]** — ticket-based authentication protocol used in Active Directory environments; uses port 88

## Exam Tips

> [!tip] RADIUS vs. TACACS+
> | Feature | RADIUS | TACACS+ |
> |---|---|---|
> | Protocol | UDP (1812/1813) | TCP (49) |
> | Encryption | Password only | Full packet |
> | AAA Separation | Combined auth/authz | Separate |
> | Best for | Network access | Device admin |

> [!tip] Remember
> "RADIUS for Remote users, TACACS+ for Terminal/device administration." The exam loves comparing these two.

## Connections

- Authentication component detailed in [[authentication]] with methods like [[mfa]] and [[sso]]
- Authorization component detailed in [[authorization]] and implemented via [[access-control-models]]
- Accounting feeds into [[log-management]] and [[siem]] for monitoring and incident detection
- Essential for [[identity-management]] in security operations

## Practice Questions

> [!qbank]- Q-Bank: AAA Framework (4 Questions)
>
> **Q1.** A network administrator wants to centrally manage login access for all 200 switches and routers in the enterprise. The solution must encrypt the entire authentication session and allow granular control over which commands each admin can execute. Which protocol is BEST suited for this requirement?
>
> A. RADIUS
> B. TACACS+
> C. Kerberos
> D. LDAP
>
> > [!answer]- Show Answer
> > **B. TACACS+**
> >
> > [[tacacs|TACACS+]] encrypts the entire payload (not just the password) and separates authentication, authorization, and accounting, making it ideal for device administration with granular command-level control. RADIUS only encrypts the password and combines authentication/authorization, making it less suitable for device admin. Kerberos is a ticket-based protocol used primarily in Active Directory environments, not for network device management. LDAP is a directory service protocol, not an AAA protocol.
>
> **Q2.** A company deploys a wireless network and needs to authenticate employees connecting via Wi-Fi and VPN. The chosen protocol should use UDP and handle large volumes of remote user connections efficiently. Which AAA protocol MOST likely meets this need?
>
> A. TACACS+
> B. RADIUS
> C. Kerberos
> D. SAML
>
> > [!answer]- Show Answer
> > **B. RADIUS**
> >
> > [[radius|RADIUS]] uses UDP (ports 1812/1813), combines authentication and authorization in a single step, and is the standard protocol for network access scenarios like Wi-Fi and VPN. TACACS+ uses TCP and is preferred for device administration rather than network access. Kerberos is used in Active Directory environments for domain authentication, not typically for Wi-Fi/VPN. SAML is a federation protocol for web-based single sign-on, not a network access protocol.
>
> **Q3.** After a data breach, an incident response team needs to determine exactly which files a compromised user account accessed and when. Which component of the AAA framework PRIMARILY provides this information?
>
> A. Authentication
> B. Authorization
> C. Accounting
> D. Access control
>
> > [!answer]- Show Answer
> > **C. Accounting**
> >
> > [[accounting|Accounting]] is the AAA component responsible for logging and tracking user activities, including session duration, commands executed, data accessed, and timestamps — exactly what investigators need for forensic analysis. Authentication only verifies identity at login time. Authorization defines permissions but does not track what was actually accessed. Access control is a broader concept that encompasses authorization models but does not specifically refer to activity logging.
>
> **Q4.** An organization uses RADIUS for VPN authentication and TACACS+ for switch management. A security auditor notes that RADIUS only encrypts the password field during transmission. Which security risk does this PRIMARILY introduce?
>
> A. Unauthorized command execution on network devices
> B. Exposure of usernames and accounting data in transit
> C. Inability to separate authentication from authorization
> D. Incompatibility with multi-factor authentication
>
> > [!answer]- Show Answer
> > **B. Exposure of usernames and accounting data in transit**
> >
> > [[radius|RADIUS]] encrypts only the password, leaving usernames, accounting data, and other attributes visible in transit, which could be captured through network sniffing. Unauthorized command execution relates to authorization controls, not encryption scope. While RADIUS does combine authentication and authorization, that is a design characteristic rather than a risk introduced by partial encryption. RADIUS fully supports MFA — the encryption limitation does not affect MFA compatibility.

## Scenario

> See [[case-aaa-framework]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [1.2 – Authentication, Authorization, and Accounting](https://www.youtube.com/watch?v=AhaZtj5P2a8)
