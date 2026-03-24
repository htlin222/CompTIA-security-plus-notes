---
title: "Application Attacks"
description: "Attacks targeting software applications through input manipulation, logic flaws, and misconfigurations"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/high
aliases:
  - "Web Application Attacks"
---

> [!eli5] ELI5: What are Application Attacks?
> You know how some apps on your phone ask you to type things in, like your name or a search? Application attacks are when a bad person types in sneaky, harmful instructions instead of normal words. It's like someone slipping a fake note into a suggestion box that tricks the person reading it into doing something wrong. These attacks work because the app trusts what you type without double-checking, so the bad instructions get followed just like real ones. That's why apps need to carefully check everything people type in.

## Overview

Application attacks exploit vulnerabilities in software applications — particularly web applications — through techniques like input manipulation, session hijacking, and exploiting logic flaws. As organizations expose more applications to the internet, the application layer has become a primary attack vector. The Security+ exam covers both attack techniques and the defenses that mitigate them.

## Key Concepts

- **[[buffer-overflow|Buffer overflow]]**: Sending more data than a buffer can hold, overwriting adjacent memory to execute arbitrary code
- **[[integer-overflow|Integer overflow]]**: Exceeding the maximum value of an integer variable, causing unexpected behavior
- **[[race-condition-toctou|Race condition / TOCTOU]]**: Exploiting the timing gap between checking a condition and using the result
- **[[directory-traversal|Directory traversal]]**: Using "../" sequences to access files outside the intended directory (e.g., `../../etc/passwd`)
- **[[session-hijacking|Session hijacking]]**: Stealing or predicting a valid session token to impersonate an authenticated user
- **[[session-replay|Session replay]]**: Capturing and retransmitting a valid authentication exchange
- **[[api-attacks|API attacks]]**: Exploiting insecure APIs through broken authentication, excessive data exposure, or lack of rate limiting
- **[[privilege-escalation|Privilege escalation]]**: Exploiting flaws to gain higher-level access than authorized (vertical) or access other users' data (horizontal)
- **[[resource-exhaustion|Resource exhaustion]]**: Consuming all available memory, CPU, disk, or connections to cause denial of service
- **Injection attacks**: Inserting malicious input into application commands — covered in detail in [[injection-attacks]]
- **[[server-side-request-forgery-ssrf|Server-Side Request Forgery (SSRF)]]**: Tricking the server into making requests to internal resources on behalf of the attacker

## Exam Tips

> [!tip] Remember
> Input validation is the #1 defense against application attacks. Buffer overflows = memory safety issue. Directory traversal = path validation issue. SSRF = the server becomes the attacker's proxy to internal systems.

- Memory-safe languages (Rust, Go, Java) prevent buffer overflows; C/C++ are vulnerable
- API security: always authenticate, authorize, rate-limit, and validate input
- TOCTOU: the gap between "check" and "use" can be exploited in concurrent environments

## Connections

- [[injection-attacks]] and [[xss-and-csrf]] are specific subcategories of application attacks
- [[penetration-testing]] actively exploits these vulnerabilities to demonstrate real-world impact
- Application-level weaknesses are categorized under [[vulnerability-types]]
- Web Application Firewalls (WAFs) as part of [[hardening]] mitigate many application attacks

## Practice Questions

> [!qbank]- Q-Bank: Application Attacks (4 Questions)
>
> **Q1.** A developer discovers that an attacker submitted a username field containing `../../../../etc/shadow` through the application's file download feature. Which type of application attack is MOST likely being attempted?
>
> A. Buffer overflow
> B. SQL injection
> C. Directory traversal
> D. Server-side request forgery
>
> > [!answer]- Show Answer
> > **C. Directory traversal**
> >
> > The `../` sequences are the hallmark of a [[directory-traversal]] attack, where the attacker navigates outside the intended directory to access sensitive system files. Buffer overflow (A) involves exceeding memory boundaries, not path manipulation. SQL injection (B) targets database queries with SQL syntax, not file paths. SSRF (D) tricks the server into making requests to internal resources, but the `../` pattern specifically indicates directory traversal.
>
> **Q2.** A web application checks whether a temporary file exists, then reads it a few milliseconds later. An attacker exploits the gap between the check and the read to swap the file with a malicious one. What type of vulnerability is this?
>
> A. Race condition / TOCTOU
> B. Integer overflow
> C. Session replay
> D. Resource exhaustion
>
> > [!answer]- Show Answer
> > **A. Race condition / TOCTOU**
> >
> > This describes a classic [[race-condition-toctou]] (Time-of-Check to Time-of-Use) vulnerability, where the attacker exploits the timing gap between verifying a condition and acting on it. Integer overflow (B) involves exceeding the maximum value of a numeric variable. Session replay (C) involves retransmitting captured authentication data. Resource exhaustion (D) involves consuming system resources to cause denial of service.
>
> **Q3.** An organization's REST API has no rate limiting and returns full user objects including passwords hashes when queried. Which BEST describes this vulnerability category?
>
> A. Privilege escalation
> B. API attack surface
> C. Buffer overflow
> D. Session hijacking
>
> > [!answer]- Show Answer
> > **B. API attack surface**
> >
> > The combination of no rate limiting and excessive data exposure are classic [[api-attacks]] vulnerabilities from the OWASP API Security Top 10. Privilege escalation (A) involves gaining higher access than authorized, not data overexposure. Buffer overflow (C) is a memory safety issue unrelated to API design. Session hijacking (D) involves stealing session tokens, not exploiting API design flaws.
>
> **Q4.** A penetration tester gains access to a standard user account and then exploits a vulnerable SUID binary to obtain root shell access. Which type of application attack does this BEST represent?
>
> A. Horizontal privilege escalation
> B. Vertical privilege escalation
> C. Server-side request forgery
> D. Resource exhaustion
>
> > [!answer]- Show Answer
> > **B. Vertical privilege escalation**
> >
> > Moving from a standard user account to root represents [[privilege-escalation]] in the vertical direction — gaining higher-level access than originally authorized. Horizontal privilege escalation (A) involves accessing another user's data at the same privilege level, not moving to root. SSRF (C) involves tricking the server into making internal requests. Resource exhaustion (D) involves consuming system resources to cause denial of service.

## Scenario

> See [[case-application-attacks]] for a practical DevOps scenario applying these concepts.
