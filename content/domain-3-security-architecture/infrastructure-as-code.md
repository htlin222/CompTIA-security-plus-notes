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

## Practice Questions

> [!qbank]- Q-Bank: Infrastructure as Code (4 Questions)
>
> **Q1.** A security audit reveals that production servers have configurations that differ from the approved baseline templates. Which IaC concept directly addresses this problem?
>
> A. Key escrow
> B. Configuration drift detection and correction
> C. Data masking
> D. Network segmentation
>
> > [!answer]- Show Answer
> > **B. Configuration drift detection and correction**
> >
> > [[configuration-drift|Configuration drift]] occurs when running infrastructure diverges from its defined state. IaC tools detect and correct this automatically by comparing actual state to the template. Key escrow (A) relates to cryptographic key recovery. Data masking (C) is a data protection technique. Network segmentation (D) divides networks into zones but does not address server configuration consistency.
>
> **Q2.** A DevOps team discovers that AWS access keys have been committed to a Terraform template in their Git repository. What is the PRIMARY security risk?
>
> A. The Terraform template will fail to execute
> B. Credentials are exposed in version control history and can be exploited
> C. The infrastructure will experience configuration drift
> D. The template will create immutable infrastructure by default
>
> > [!answer]- Show Answer
> > **B. Credentials are exposed in version control history and can be exploited**
> >
> > Hardcoded secrets in [[infrastructure-as-code|IaC templates]] are a major security risk because version control systems retain the full history, meaning the credentials remain accessible even after removal. Template execution failure (A) is unlikely since the credentials would work. Configuration drift (C) is unrelated to hardcoded secrets. Immutable infrastructure (D) is a deployment strategy, not a consequence of exposed credentials.
>
> **Q3.** An organization wants to ensure that no IaC template can deploy resources with overly permissive security group rules (e.g., allowing 0.0.0.0/0 on port 22). Which approach BEST enforces this?
>
> A. Manual code review of all templates before deployment
> B. Policy as code that automatically validates templates before deployment
> C. Deploying all infrastructure manually instead of using IaC
> D. Using imperative scripts instead of declarative templates
>
> > [!answer]- Show Answer
> > **B. Policy as code that automatically validates templates before deployment**
> >
> > [[policy-as-code|Policy as code]] defines security rules in code that automatically validates IaC templates, blocking non-compliant resources before deployment. Manual review (A) does not scale and is error-prone. Abandoning IaC (C) loses all benefits of consistency and auditability. Imperative vs. declarative (D) is a style choice that does not address security policy enforcement.
>
> **Q4.** After a ransomware attack encrypts several production servers, the incident response team needs to rebuild the environment quickly. Which IaC benefit is MOST valuable in this situation?
>
> A. The ability to track who made changes via version control
> B. The ability to rapidly rebuild infrastructure from known-good templates
> C. The ability to use declarative syntax instead of imperative
> D. The ability to deploy across multiple cloud providers
>
> > [!answer]- Show Answer
> > **B. The ability to rapidly rebuild infrastructure from known-good templates**
> >
> > [[infrastructure-as-code|IaC]] enables rapid recovery by rebuilding infrastructure from code, which is critical after a destructive attack like ransomware. Version control auditing (A) is valuable for investigation but does not help with immediate recovery. Declarative syntax (C) is a development preference, not a recovery capability. Multi-cloud deployment (D) provides vendor diversity but does not directly address rapid post-incident rebuilding.

## Scenario

> See [[case-infrastructure-as-code]] for a practical DevOps scenario applying these concepts.
