---
title: "Implicit deny"
description: "If no rule explicitly grants access, access is denied by default"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Implicit Deny?
> It's like a club with a guest list: if your name isn't on the list, you don't get in. The default answer is always "no" unless there's a specific rule that says "yes."

## Definition

Implicit deny is a fundamental security principle stating that any access not explicitly permitted by a rule or policy is automatically denied. It establishes a "default deny" security posture—the system blocks everything unless a specific rule allows it. This is the opposite of "default allow" (which permits everything not explicitly blocked) and is considered a more secure baseline.

## Key Details

- Applied in: **ACLs** (firewall rules end with an implicit deny), **file system permissions** (no permission = no access), **network security policies**.
- The final (often invisible) rule in firewall ACLs is **"deny all"**—traffic not matching a permit rule is dropped.
- Supports the **principle of least privilege**—users and systems start with no access and must be explicitly granted what they need.
- Contrasts with **default allow**: If no rule matches, traffic/access is permitted—far less secure.
- Important in **Zero Trust**: every request is denied by default until evaluated and explicitly approved.

## Connections

- Parent: [[authorization]] — a core authorization principle
- See also: [[access-control-lists-acls]]
