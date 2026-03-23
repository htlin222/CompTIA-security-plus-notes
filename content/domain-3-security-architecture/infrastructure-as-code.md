---
title: "Infrastructure as Code"
description: "Infrastructure as Code manages and provisions computing resources through machine-readable configuration files rather than manual processes."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cloud
  - weight/medium
aliases:
  - "IaC"
---

> [!eli5] ELI5: What is Infrastructure as Code?
> Remember how LEGO instructions let you rebuild the same model perfectly every time? Infrastructure as Code works the same way for computers. Instead of setting up servers by hand (and maybe making mistakes), you write a set of instructions that a computer follows automatically. If something breaks, you just run the instructions again and get a perfect copy. This makes it much easier to keep everything safe and consistent.

## Overview

Infrastructure as Code (IaC) is the practice of defining and managing infrastructure (servers, networks, storage) through code and automation rather than manual configuration. IaC enables consistent, repeatable, and auditable deployments. From a security perspective, IaC allows organizations to enforce security baselines, detect configuration drift, and rapidly rebuild compromised systems from known-good templates.

## Key Concepts

- **Declarative vs. imperative:**
  - **Declarative** — defines the desired end state; the tool determines how to achieve it (Terraform, CloudFormation)
  - **Imperative** — defines the exact steps to execute (Ansible playbooks, scripts)
- **Key benefits for security:**
  - **Consistency** — every deployment matches the approved template; eliminates configuration drift
  - **Version control** — infrastructure definitions stored in Git; changes are tracked, reviewed, and auditable
  - **Rapid recovery** — rebuild infrastructure from code after a breach or failure
  - **Security baselines** — embed hardening configurations directly into templates
- **[[configuration-drift|Configuration drift]]** — when running infrastructure diverges from its defined state; IaC detects and corrects this
- **[[immutable-infrastructure|Immutable infrastructure]]** — servers are never modified after deployment; updates create new instances that replace old ones
- **[[common-tools|Common tools:]]** Terraform, AWS CloudFormation, Azure ARM/Bicep, Ansible, Puppet, Chef
- **Security risks:**
  - Secrets hardcoded in templates (credentials, API keys)
  - Misconfigured templates that deploy insecure resources
  - Supply chain risks from third-party modules
- **[[policy-as-code|Policy as code]]** — defining security policies in code that automatically validates IaC templates before deployment

## Exam Tips

> [!tip] Remember
> IaC = consistent, auditable, repeatable infrastructure. Immutable infrastructure = replace, never patch in place. The biggest IaC security risk is hardcoded secrets in templates. Version control provides audit trails.

## Connections

- Enables secure deployments in [[cloud-security]] by automating consistent, policy-compliant infrastructure
- Used to deploy and manage [[serverless-and-containers]] workloads in a repeatable manner
- See also [[resilience-and-redundancy]] for how IaC supports rapid recovery and consistent rebuilds

## Scenario

> See [[case-infrastructure-as-code]] for a practical DevOps scenario applying these concepts.
