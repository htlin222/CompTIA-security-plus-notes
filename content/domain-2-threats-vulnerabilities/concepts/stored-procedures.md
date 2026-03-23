---
title: "Stored procedures"
description: "Pre-compiled database queries that can limit injection surface when used correctly"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Stored procedures are pre-compiled database routines stored within the database server that encapsulate SQL logic. When used with parameterized input (rather than string concatenation), they can help protect against SQL injection by preventing user-supplied data from being interpreted as SQL syntax. However, stored procedures that build SQL dynamically with string concatenation internally are still vulnerable to SQLi.

## Key Details

- When used correctly with **parameterized calls**: User input is passed as parameters, not concatenated into SQL—provides injection protection similar to prepared statements.
- **Critical caveat**: A stored procedure that internally uses `EXEC('SELECT ... WHERE name = ''' + @name + '''')` is still vulnerable to SQLi.
- Provides **security through encapsulation**: Application code doesn't need raw table access—only permission to execute specific procedures.
- **Performance benefit**: Pre-compiled and cached—faster than dynamically parsed queries.
- **Defense in depth**: Combining stored procedures + parameterized parameters + least-privilege database users provides strong SQLi protection.

## Connections

- Parent: [[injection-attacks]] — an additional defense mechanism against SQL injection
- See also: [[parameterized-queries-prepared-statements]]
