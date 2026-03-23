---
title: "Credential stuffing"
description: "Using stolen username/password pairs from breached databases to log into other services"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Credential stuffing is an automated attack that takes advantage of the widespread practice of password reuse. Attackers use large databases of username/password pairs leaked in previous data breaches and systematically attempt to log in to other web services with those same credentials. Because many users reuse passwords across multiple sites, even a small percentage success rate yields thousands of compromised accounts.

## Key Details

- Relies on **password reuse**—the same password used on multiple sites is the key enabling factor.
- Uses automated tools and **botnets** to distribute login attempts, evading rate limiting and IP blocking.
- Defenses: **MFA** (most effective—credentials alone aren't enough), **password managers** (encourage unique passwords), **CAPTCHA**, **IP reputation checks**, **rate limiting**.
- Breach notification services (HaveIBeenPwned) help users identify if their credentials have been exposed.
- Organizations can monitor for **credential stuffing** by detecting unusual login patterns from many different IPs.

## Connections

- Parent: [[password-attacks]] — a large-scale automated password attack
- See also: [[password-spraying]], [[brute-force]]
