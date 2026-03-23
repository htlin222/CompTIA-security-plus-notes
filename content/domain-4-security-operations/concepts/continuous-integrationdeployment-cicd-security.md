---
title: "Continuous integration/deployment (CI/CD) security"
description: "Embedding security checks into automated build and deployment pipelines"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

CI/CD security, also called DevSecOps, involves integrating security testing, scanning, and policy checks directly into the automated software build and deployment pipeline. Rather than performing security assessments as a separate, post-development step, security controls are embedded at each stage of the CI/CD pipeline to catch vulnerabilities early when they are cheapest to fix.

## Key Details

- Security gates in CI/CD pipelines can block deployments that fail security checks
- Common security checks: SAST (static application security testing), DAST (dynamic testing), dependency scanning, container image scanning
- Infrastructure as Code templates can be scanned for misconfigurations before deployment
- Secrets must not be hardcoded in source code — use secrets management tools instead
- Shift-left security: finding vulnerabilities earlier in the development lifecycle reduces cost and risk

## Connections

- Parent: [[automation-and-scripting]] — CI/CD security is a key application of security automation
- See also: [[infrastructure-as-code-iac]]
