---
title: "Zero trust architecture"
description: "never trust, always verify; authenticate and authorize every access request regardless of network location"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Zero trust architecture (ZTA) is a security model based on the principle of "never trust, always verify" — eliminating the concept of implicit trust based on network location (e.g., being inside the corporate perimeter). Every access request, whether from inside or outside the network, must be authenticated, authorized, and continuously validated based on identity, device health, and context before access is granted to any resource.

## Key Details

- Core principle: no user, device, or network segment is inherently trusted; trust must be earned and continuously verified
- Identity-centric: strong authentication (MFA) and identity verification for every resource access
- Least privilege access: users and systems granted only the minimum permissions required for specific tasks
- Microsegmentation limits lateral movement by dividing the network into small, isolated segments
- Continuous validation: posture checks and behavioral analytics re-evaluate trust during sessions
- NIST SP 800-207 provides the official Zero Trust Architecture guidance

## Connections

- Parent: [[network-security-architecture]] — zero trust is the dominant modern approach to network security design
- See also: [[micro-segmentation]], [[secure-access-service-edge-sase]], [[identity-and-access-management]], [[defense-in-depth]]
