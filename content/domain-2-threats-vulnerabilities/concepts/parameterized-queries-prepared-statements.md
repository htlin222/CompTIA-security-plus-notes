---
title: "Parameterized queries / Prepared statements"
description: "The primary defense against SQL injection — separates code from data so input is never executed as SQL"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Parameterized queries (also called prepared statements) are the primary and most effective defense against SQL injection. They separate the SQL code structure (the query template) from the user-supplied data (the parameters). The database compiles the query structure first, then treats all user input as literal data—not executable code—making it impossible for injected SQL syntax to alter the query structure.

## Key Details

- **How it works**: SQL query is pre-compiled with placeholders (`?` or named parameters); user input is bound separately and treated as data, never parsed as SQL.
- Example (safe): `SELECT * FROM users WHERE username = ? AND password = ?` with bound parameters.
- Example (vulnerable): `"SELECT * FROM users WHERE username = '" + username + "'"` — string concatenation allows injection.
- Works in virtually all programming languages and database platforms: Java PreparedStatement, Python `%s` with parameterized queries, PHP PDO.
- **Stored procedures** can also be parameterized—provides a similar defense when used correctly.

## Connections

- Parent: [[injection-attacks]] — the most effective defense against SQL injection
- See also: [[input-validation]], [[stored-procedures]]
