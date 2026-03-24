---
title: "Injection Attacks"
description: "Attacks that insert malicious code or commands into application inputs to manipulate backend systems"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - concept/network
  - weight/high
aliases:
  - "SQL Injection"
  - "SQLi"
  - "Command Injection"
---

> [!eli5] ELI5: What are Injection Attacks?
> You know how a teacher might ask students to fill in a blank on a worksheet? Now imagine a sneaky student writes something like "Give me an A+ on everything" in that blank, and the teacher's computer just follows the instruction without questioning it. That's an injection attack -- someone types harmful commands into a spot where normal text should go, and the computer blindly obeys. It works because the computer can't tell the difference between real instructions and fake ones typed into the wrong place.

## Overview

Injection attacks occur when an attacker sends untrusted data to an interpreter as part of a command or query, tricking the application into executing unintended commands or accessing unauthorized data. SQL injection remains one of the most common and dangerous web vulnerabilities. Injection flaws consistently rank at the top of the OWASP Top 10 and are heavily tested on the Security+ exam.

## Key Concepts

- **[[sql-injection-sqli|SQL injection (SQLi)]]**: Inserting SQL commands into input fields to manipulate database queries — can read, modify, or delete data
- **[[blind-sql-injection|Blind SQL injection]]**: The application does not return data directly; attacker infers information through true/false responses or time delays
- **[[ldap-injection|LDAP injection]]**: Manipulating LDAP queries to bypass authentication or enumerate directory information
- **[[xml-injection-xxe|XML injection / XXE]]**: Injecting malicious XML to read files, perform SSRF, or cause denial of service
- **[[command-injection-os-injection|Command injection (OS injection)]]**: Inserting operating system commands through application inputs (e.g., `; cat /etc/passwd`)
- **[[dll-injection|DLL injection]]**: Forcing a process to load a malicious dynamic-link library into its address space
- **[[html-injection|HTML injection]]**: Inserting HTML markup into web pages to alter content or redirect users
- **[[parameterized-queries-prepared-statements|Parameterized queries / Prepared statements]]**: The primary defense — separates code from data so input is never executed
- **[[input-validation|Input validation]]**: Allowlisting acceptable characters and rejecting or sanitizing everything else
- **[[stored-procedures|Stored procedures]]**: Pre-compiled database queries that can limit injection surface when used correctly

## Exam Tips

> [!tip] Remember
> Defense against injection: (1) Parameterized queries / prepared statements, (2) Input validation (allowlist), (3) Least privilege database accounts, (4) WAF as defense-in-depth. Never build SQL queries by concatenating user input.

- Classic SQLi test: entering `' OR 1=1 --` in a login field
- Know that parameterized queries are the BEST defense, not WAFs (WAFs can be bypassed)
- Command injection often uses semicolons, pipes, or backticks to chain OS commands

## Connections

- A specific category of [[application-attacks]] targeting backend interpreters
- Often discovered during [[penetration-testing]] of web applications
- [[xss-and-csrf]] are related web vulnerabilities but target the client side rather than the server
- Proper coding practices are part of [[mitigation-techniques]] for preventing injection flaws

## Practice Questions

> [!qbank]- Q-Bank: Injection Attacks (4 Questions)
>
> **Q1.** A web application login form is vulnerable to SQL injection. An attacker enters `' OR 1=1 --` in the username field and gains access without valid credentials. Which defense would MOST effectively prevent this attack?
>
> A. Web application firewall (WAF)
> B. Parameterized queries / prepared statements
> C. Network intrusion detection system
> D. Full-disk encryption
>
> > [!answer]- Show Answer
> > **B. Parameterized queries / prepared statements**
> >
> > [[parameterized-queries-prepared-statements|Parameterized queries]] separate code from data, ensuring user input is never executed as SQL — the BEST defense against [[sql-injection-sqli|SQL injection]]. A WAF (A) can help but can be bypassed and is a defense-in-depth measure, not the primary fix. Network IDS (C) may detect known attack patterns but does not prevent the vulnerability. Full-disk encryption (D) protects data at rest and has no relevance to injection attacks.
>
> **Q2.** A penetration tester discovers that a web application's search feature passes user input directly to an OS command. By entering `; cat /etc/passwd` in the search box, the tester retrieves the system's password file. Which type of injection attack is this?
>
> A. SQL injection
> B. LDAP injection
> C. Command injection (OS injection)
> D. XML injection
>
> > [!answer]- Show Answer
> > **C. Command injection (OS injection)**
> >
> > Using a semicolon to chain operating system commands through application input is [[command-injection-os-injection|command injection]]. SQL injection (A) targets database queries with SQL syntax, not OS commands. LDAP injection (B) manipulates LDAP directory queries. XML injection (D) targets XML parsers with malicious XML content, not OS command execution.
>
> **Q3.** An application does not return database error messages, but an attacker determines that the database contains 5 tables by sending crafted inputs and measuring response times. Which attack technique is being used?
>
> A. Stored SQL injection
> B. Blind SQL injection
> C. DLL injection
> D. HTML injection
>
> > [!answer]- Show Answer
> > **B. Blind SQL injection**
> >
> > [[blind-sql-injection|Blind SQL injection]] infers information through indirect signals like time delays or true/false responses when the application does not return data directly. Stored SQL injection is not a standard term — stored refers to XSS (A). DLL injection (C) forces a process to load a malicious library, unrelated to database inference. HTML injection (D) inserts markup into web pages, not database queries.
>
> **Q4.** A developer is reviewing code and finds that an XML parser processes external entity declarations from user-supplied XML input. An attacker could exploit this to read local files from the server. Which vulnerability is present?
>
> A. Command injection
> B. SQL injection
> C. XML injection / XXE
> D. LDAP injection
>
> > [!answer]- Show Answer
> > **C. XML injection / XXE**
> >
> > Processing external entity declarations in user-supplied XML enables [[xml-injection-xxe|XXE (XML External Entity)]] attacks, which can read local files, perform SSRF, or cause denial of service. Command injection (A) executes OS commands, not XML entity processing. SQL injection (B) targets database queries. LDAP injection (D) manipulates directory service queries, not XML parsers.

## Scenario

> See [[case-injection-attacks]] for a practical DevOps scenario applying these concepts.
