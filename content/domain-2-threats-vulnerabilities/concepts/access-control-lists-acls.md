---
title: "Access control lists (ACLs)"
description: "Defining explicit allow/deny rules for network traffic and resource access"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
aliases:
  - ACLs
  - ACLS
---

> [!eli5] ELI5: What are Access Control Lists (ACLs)?
> It's like a guest list at a party -- only people whose names are on the list get in, and everyone else gets turned away at the door.

## Definition

Access Control Lists (ACLs) are ordered sets of permit and deny rules applied to network interfaces, firewalls, or file systems to control what traffic or users are allowed. In network security, ACLs filter packets based on attributes such as source/destination IP, port, and protocol. They are a fundamental tool for enforcing network segmentation and the principle of least privilege.

## Key Details

- ACLs are **processed top-to-bottom**; the first matching rule is applied and processing stops.
- An **implicit deny** at the end of every ACL means unmatched traffic is blocked by default.
- **Standard ACLs** filter by source IP only; **Extended ACLs** filter by source/destination IP, port, and protocol.
- ACLs can be applied to inbound or outbound interfaces on routers and switches.
- File system ACLs (Windows NTFS, Linux) control which users/groups can read, write, or execute files.

## Connections

- Parent: [[mitigation-techniques]] — used as a mitigation technique to restrict traffic
- See also: [[network-segmentation]]
