---
title: "Software-defined perimeter (SDP)"
description: "Creates one-to-one encrypted connections between users and resources; hides infrastructure"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
aliases:
  - SDP
---

## Definition

A Software-Defined Perimeter (SDP) is a security framework that creates dynamic, one-to-one encrypted network connections between authenticated and authorized users and the specific resources they need to access—while keeping the existence of other resources completely hidden. Unlike traditional VPNs (which grant broad network access), SDP exposes only specific resources to specific users, treating every access request with zero-trust principles.

## Key Details

- **Dark cloud**: Infrastructure is invisible to the internet and to unauthorized users—only authenticated users can see what they're authorized to access.
- Based on **"authenticate first, then connect"** rather than "connect, then authenticate" (as with traditional VPN).
- Implements **microsegmentation** automatically—each user gets a narrowly scoped connection, not broad network access.
- Often referred to as **Zero Trust Network Access (ZTNA)** in modern terminology—the successor to VPN for remote access.
- Vendors: **Zscaler Private Access (ZPA)**, **Cloudflare Access**, **Palo Alto Prisma Access**, **Google BeyondCorp**.

## Connections

- Parent: [[zero-trust]] — an implementation approach for Zero Trust access
- See also: [[policy-enforcement-point-pep]]
