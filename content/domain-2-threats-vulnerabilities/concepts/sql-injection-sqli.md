---
title: "SQL injection (SQLi)"
description: "Inserting SQL commands into input fields to manipulate database queries — can read, modify, or delete data"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - SQLi
  - SQLI
---

## Definition

SQL injection is one of the most critical and common web application vulnerabilities, occurring when attacker-supplied SQL code is inserted into application queries without proper sanitization, causing the database to execute unintended commands. Successful SQL injection can allow attackers to read sensitive data, modify or delete records, bypass authentication, and in some cases, execute operating system commands.

## Key Details

- **Classic bypass**: `' OR '1'='1` in a login form causes the WHERE clause to always evaluate true—bypasses authentication.
- **UNION-based**: `' UNION SELECT username, password FROM users--` appends additional query results to the response.
- **Error-based**: Forces database error messages that reveal schema and data.
- **Primary mitigation**: **Parameterized queries / prepared statements**—separates SQL code from user data; input is treated as data, never executed as SQL.
- Consistently in the **OWASP Top 10**; automated scanners (sqlmap) can exploit SQLi automatically.

## Connections

- Parent: [[injection-attacks]] — the most prevalent injection attack type
- See also: [[blind-sql-injection]], [[parameterized-queries-prepared-statements]]
