---
title: "Authentication"
description: "typically uses certificates, MFA, RADIUS, or LDAP for VPN user authentication"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

In the context of VPN security, authentication is the process of verifying the identity of users and devices before granting access to the VPN tunnel and corporate network resources. Strong authentication is critical for VPNs because they create pathways into internal networks from external, potentially hostile environments. Multiple authentication methods are often combined for defense in depth.

## Key Details

- **Certificate-based**: uses client certificates for device authentication; very strong
- **RADIUS**: centralized authentication server protocol commonly used with VPN concentrators
- **LDAP/Active Directory**: integrates VPN authentication with existing directory services
- **MFA**: combines passwords with a second factor (token, push notification) for stronger assurance
- Split-tunneling VPNs carry additional authentication risks as some traffic bypasses controls

## Connections

- Parent: [[vpn]] — authentication is a core security requirement for VPN implementations
- See also: [[always-on-vpn]]
