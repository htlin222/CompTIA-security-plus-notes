---
title: "Single point of failure risk"
description: "If SSO is compromised, all linked applications are at risk"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Single point of failure risk in SSO refers to the critical security concern that because SSO centralizes authentication for all linked applications through a single identity provider, a compromise of the SSO system or an SSO credential can provide an attacker with access to all applications in the SSO ecosystem simultaneously. This concentration of authentication risk is the primary downside of SSO implementations.

## Key Details

- A compromised SSO credential or session token can be used to access all federated applications
- If the IdP is unavailable, users cannot authenticate to any SSO-enabled application
- Strong authentication (MFA) on the SSO login is critical to mitigate the authentication risk
- Conditional access policies (device compliance, location, risk score) provide additional protection layers
- SSO platforms must be highly available and hardened as critical infrastructure

## Connections

- Parent: [[sso]] — single point of failure is the primary risk that SSO implementations must mitigate
- See also: [[mfa-fatigue-attacks]]
