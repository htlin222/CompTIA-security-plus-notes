---
title: "Policy as code"
description: "defining security policies in code that automatically validates IaC templates before deployment"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Policy as code is the practice of expressing security and compliance policies as machine-readable code that can be automatically enforced during the infrastructure deployment process. Policy as code tools scan IaC templates (Terraform, CloudFormation) against defined security rules before deployment, blocking non-compliant configurations before they ever reach production.

## Key Details

- Tools: Open Policy Agent (OPA), Checkov, tfsec, Sentinel (HashiCorp), AWS Config Rules
- Policies are written in code (Rego for OPA, Python/YAML for Checkov) and version-controlled alongside IaC
- Catches security misconfigurations early — at development time rather than in production
- Common checks: public S3 buckets, missing encryption, open security groups, disabled MFA
- Enables "shift-left security" for infrastructure: security requirements validated before deployment

## Connections

- Parent: [[infrastructure-as-code]] — policy as code enforces security requirements within the IaC workflow
- See also: [[common-tools]]
