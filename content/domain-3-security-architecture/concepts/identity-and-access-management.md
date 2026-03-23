---
title: "Identity and access management"
description: "federated identity, SSO, and strong IAM policies for cloud resources"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Identity and Access Management (IAM) in cloud environments encompasses the policies, processes, and technologies used to manage digital identities and control what cloud resources each identity can access. Cloud IAM is a shared responsibility — cloud providers offer IAM services (AWS IAM, Azure AD, Google Cloud IAM), but customers are responsible for configuring policies correctly.

## Key Details

- **Federated identity**: connecting on-premises identity (Active Directory) with cloud IAM using SAML or OIDC
- **SSO**: users authenticate once and access multiple cloud services without re-authenticating
- **Least privilege**: IAM policies should grant only the minimum permissions required for each role
- Overly permissive IAM policies are a leading cause of cloud data breaches
- Multi-factor authentication should be enforced for all privileged cloud IAM accounts

## Connections

- Parent: [[cloud-security]] — IAM is a critical component of cloud security architecture
- See also: [[secrets-management]]
