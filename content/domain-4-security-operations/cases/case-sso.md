---
title: "Case: The Identity Provider Cascading Failure — SSO System Down"
description: "The identity provider for a 4,000-person consulting firm goes down during a Kerberos ticket renewal storm, locking every employee out of every application for 90 minutes on the last day of the fiscal quarter."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

Stratton Consulting employs 4,000 people across 12 offices managing technology transformation projects for Fortune 500 companies. Their entire infrastructure is built on [[single-point-of-failure-risk]] mitigation, with one critical exception: their identity provider. They use Azure AD as their [[identity-provider-idp]] for SSO across 47 different applications: Office 365, Salesforce, Jira, GitHub, AWS accounts, time tracking, expense reporting, and dozens more. All of these applications are configured to [[federation]] with Azure AD.

On March 31st at 3:47 PM Eastern Time—the last business day of Q1, historically the busiest day for financial reconciliation, expense reporting, and deal closing—the Azure AD service in Microsoft's data center experienced an outage in the US East region. The outage lasted 47 minutes.

The cascading failure was catastrophic:

**Phase 1: Authentication Failure (0:00-5:00)**
All employees attempting to authenticate to any of the 47 federated applications received error messages: "Cannot validate your identity. Please try again later." New browser sessions couldn't authenticate. Applications tried to re-authenticate users via Azure AD and failed.

**Phase 2: Kerberos Ticket Renewal Storm (5:00-20:00)**
Employees who were already logged into their Windows workstations experienced a different problem. Windows uses Kerberos tickets (granted by the domain controller, which uses Azure AD as the identity source) that expire every 10 hours. During the outage, existing tickets continued to work (Kerberos doesn't require constant validation), but as tickets expired, Windows tried to renew them by contacting the domain controller. The domain controller tried to refresh the ticket with Azure AD and received an error.

As more users' Kerberos tickets expired—creating a "ticket renewal storm"—the domain controller was flooded with failed renewal attempts, consuming all available resources. New workstations booting up couldn't authenticate at all. Existing sessions began degrading as tickets expired and couldn't be renewed.

**Phase 3: Business Impact (20:00-47:00)**
By 4:12 PM (25 minutes after the outage began):

- 3,800 of 4,000 employees had lost access to at least one critical application
- 1,200 employees couldn't access Salesforce (critical for customer-facing project teams)
- 2,100 employees couldn't access their Office 365 email
- All financial reconciliation work (supposed to close Q1 by end-of-day) ground to a halt
- Deal teams trying to finalize contracts worth $40 million couldn't access documents in SharePoint

The incident occurred at exactly the worst time: hours before the fiscal quarter close, when reconciliation, deal closing, and financial reporting all happen simultaneously. Stratton's accounting team couldn't close the books on Q1. Deal teams couldn't send final contracts to customers.

The consulting firm had an [[sso]] architecture with no [[single-point-of-failure-risk]] mitigation for the identity provider itself. If Azure AD was down, every application was inaccessible. There was no local caching of Kerberos tickets beyond the standard 10-hour lifetime. There was no offline authentication mode. There was no secondary identity provider.

Microsoft's Azure AD service returned to normal 47 minutes later, and access gradually restored as users reconnected and re-authenticated. But the damage was done. Stratton Consulting missed their Q1 fiscal close by 4 hours (unusual for public companies, raising questions with auditors). Deal teams missed their contractual close deadlines, delaying revenue recognition. The company reported the outage to customers as a service disruption, damaging their consulting reputation.

The incident forced a painful architectural review. Stratton realized they had designed their entire authentication infrastructure around a single {{[[single-point-of-failure-risk]]}}: the Azure AD [[identity-provider-idp]]. If Microsoft's service had an outage, the entire organization was paralyzed.

## What Went Right

- **Rapid [[federation]] failover**: When Azure AD came back online, [[token-based-authentication]] was quickly restored because no local state needed to be rebuilt.
- **Kerberos as a backup**: Existing Kerberos tickets continued working even when the identity provider was unavailable, allowing some users to maintain access for up to 10 hours.
- **Incident notification**: Microsoft immediately notified Stratton that the outage was on their infrastructure, not Stratton's, enabling rapid troubleshooting.

## What Could Go Wrong

- **No {{[[single-point-of-failure-risk]]}} mitigation for identity**: The entire 4,000-person organization depended on a single Azure AD tenant with no redundancy, no secondary provider, no fallback authentication mechanism.
- **No local identity cache**: Kerberos tickets expire within 10 hours. There was no mechanism to cache authorization decisions locally so applications could make limited-capability access decisions if the identity provider was offline.
- **No [[oauth-20]] token refresh logic in applications**: Applications were configured to immediately fail if token validation against Azure AD failed. Better applications would cache the last-known-good token state and allow limited access (read-only) while the identity provider recovered.
- **No multi-region Azure AD redundancy**: Although Azure AD is a Microsoft managed service, Stratton could have configured regional failover or a secondary authentication mechanism for critical applications.
- **Missing [[openid-connect-oidc]] offline token strategy**: Some of Stratton's applications could have been configured to issue long-lived tokens that don't require immediate [[identity-provider-idp]] validation, allowing continued operation during outages.

## Key Takeaways

- **Single-point-of-failure-risk is inherent in SSO architectures**: [[federation]] and [[sso]] by definition create centralized authentication. Organizations must implement redundancy at the identity provider level (geo-redundant instances, secondary providers) and in applications (local token caching, offline modes).
- **Token-based-authentication lifetimes should balance security and resilience**: Extremely short token lifetimes (5 minutes) mean the identity provider must be always available. Longer lifetimes (hours) increase security risk if tokens are compromised. Balance security requirements with availability requirements.
- **Applications should implement graceful degradation when identity provider is offline**: Instead of immediately failing, applications should cache the last-known-good authorization state and allow read-only access or limited functionality until the identity provider recovers.
- **Kerberos provides valuable resilience**: Unlike OAuth/OIDC tokens, Kerberos tickets are valid for 10 hours even if the authentication server is offline. This provides natural resilience that should be leveraged.
- **Critical business operations should not depend entirely on online authentication**: For applications involved in fiscal close, deal finalization, or other critical-path business processes, implement offline authentication modes or require biannual testing of offline access procedures.
- **Mfa adds complexity to [[single-point-of-failure-risk]] mitigation**: If MFA is required, authenticating offline becomes more complex. [[passwordless-authentication]] with hardware keys is more resilient than push-notification MFA during provider outages.

## Related Cases

- [[case-federation]] — Federation architectures create [[single-point-of-failure-risk]] at the identity provider level; redundancy strategies must be built into the architecture.
- [[case-identity-management]] — Identity governance processes should include contingency planning for identity provider failures.
- [[case-mfa]] — MFA systems should have offline fallback mechanisms for critical business operations.
