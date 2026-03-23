---
title: "Self-service capabilities"
description: "Password resets and profile updates reduce helpdesk burden while maintaining security"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Self-service identity capabilities allow end users to perform certain identity management tasks themselves — such as resetting their own passwords, updating contact information, or managing MFA devices — without requiring helpdesk intervention. These capabilities improve the user experience and reduce IT support burden while maintaining security through appropriate verification controls.

## Key Details

- **Self-service password reset (SSPR)**: users reset their own passwords after verifying identity via email, phone, or authenticator app
- Dramatically reduces helpdesk password reset tickets (often 30-50% of all helpdesk calls)
- Must be secured: verification method must be strong enough to prevent social engineering attacks
- Microsoft Entra ID (Azure AD), Okta, and other IAM platforms provide built-in SSPR capabilities
- Audit logging of self-service actions is essential for security monitoring

## Connections

- Parent: [[identity-management]] — self-service capabilities reduce operational burden while maintaining identity security
- See also: [[provisioning-and-deprovisioning]]
