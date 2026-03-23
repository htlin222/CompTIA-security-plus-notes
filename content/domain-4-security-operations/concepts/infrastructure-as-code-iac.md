---
title: "Infrastructure as Code (IaC)"
description: "Managing and provisioning infrastructure through code (Terraform, Ansible, Puppet)"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - IaC
  - IAC
---

> [!eli5] ELI5: What is Infrastructure as Code?
> Instead of clicking buttons to set up a server, you write instructions in a file. It is like building with LEGO instructions -- you get the same result every single time.

## Definition

Infrastructure as Code (IaC) is the practice of managing and provisioning computing infrastructure using machine-readable configuration files rather than manual processes or interactive tools. IaC enables consistent, repeatable, and auditable infrastructure deployments while embedding security policies and hardening configurations directly into the deployment process.

## Key Details

- Infrastructure defined in code can be version-controlled, reviewed, and audited like application code
- Enables rapid, consistent deployment of security-hardened infrastructure
- Security scanning of IaC templates (Checkov, tfsec) can identify misconfigurations before deployment
- Common tools: Terraform (multi-cloud), AWS CloudFormation, Azure Bicep, Ansible, Puppet
- Reducing manual configuration reduces human error and configuration drift

## Connections

- Parent: [[automation-and-scripting]] — IaC is a key application of automation in security operations
- See also: [[continuous-integrationdeployment-cicd-security]]
