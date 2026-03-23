---
title: "Blind SQL injection"
description: "Application does not return data directly; attacker infers information through true/false responses or time delays"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Blind SQL injection is a form of SQL injection in which the application does not return database error messages or query results directly to the attacker. Instead, the attacker infers information by observing how the application behaves differently based on true or false queries (Boolean-based blind SQLi) or by measuring response time delays triggered by conditional SQL statements (Time-based blind SQLi).

## Key Details

- **Boolean-based blind SQLi**: Attacker sends queries that change the page response (e.g., returns different content or length) based on true/false conditions.
- **Time-based blind SQLi**: Uses database functions like `SLEEP()` (MySQL) or `WAITFOR DELAY` (SQL Server) to infer data bit by bit via response timing.
- Much slower than error-based SQLi but equally dangerous—automated tools (sqlmap) can extract entire databases.
- Mitigation: **parameterized queries**, **stored procedures**, **input validation**, **WAF**.
- The blind nature makes it harder to detect in logs but still leaves SQL-like patterns in request parameters.

## Connections

- Parent: [[injection-attacks]] — a variant of SQL injection
- See also: [[sql-injection-sqli]], [[parameterized-queries-prepared-statements]]
