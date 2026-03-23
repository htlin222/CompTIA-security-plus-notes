---
title: "Principle of least privilege"
description: "Grant only the minimum access necessary for a role or task"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is the Principle of Least Privilege?
> Give people only the access they truly need, nothing extra. If your job is to water the garden, you get the garden key -- not the key to every room in the house.

## Definition

The principle of least privilege (PoLP) is a foundational security concept specifying that every user, process, service, or system component should be granted only the minimum permissions necessary to accomplish its intended task—and nothing more. It limits the blast radius of security incidents by ensuring that compromised accounts, exploited processes, or malicious insiders have constrained access to sensitive resources.

## Key Details

- Applied at all levels: **user accounts** (no admin for daily tasks), **service accounts** (only the permissions needed by the service), **network access** (only reach required systems), **file permissions** (only read/write files needed).
- **Privilege creep**: Users accumulate permissions over time as roles change—regular access reviews are needed to combat this.
- **Just-in-time (JIT) access**: Grant elevated permissions only when needed, for a defined period—then automatically revoke.
- Implemented via: **RBAC**, **ABAC**, **PAM (Privileged Access Management)** solutions.
- Reduces risk of **insider threats**, **malware lateral movement**, and **privilege escalation** attacks.

## Connections

- Parent: [[authorization]] — implementation of least privilege through authorization controls
- See also: [[least-privilege]], [[separation-of-duties]]
