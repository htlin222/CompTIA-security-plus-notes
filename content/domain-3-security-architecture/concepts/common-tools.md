---
title: "Common IaC tools"
description: "Terraform, AWS CloudFormation, Azure ARM/Bicep, Ansible, Puppet, Chef"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Infrastructure as Code (IaC) tools are software platforms that enable administrators and developers to define, provision, and manage infrastructure through code rather than manual processes. These tools enable consistent, repeatable infrastructure deployment with version control, automated testing, and security policy validation built into the deployment pipeline.

## Key Details

- **Terraform**: cloud-agnostic IaC tool using HashiCorp Configuration Language (HCL); most widely used
- **AWS CloudFormation**: AWS-native IaC using JSON or YAML templates
- **Azure ARM/Bicep**: Azure-native IaC; Bicep is a domain-specific language that compiles to ARM JSON
- **Ansible**: agentless configuration management using YAML playbooks; also used for IaC
- **Puppet/Chef**: agent-based configuration management tools commonly used for server hardening at scale

## Connections

- Parent: [[infrastructure-as-code]] — these are the primary tools used to implement IaC
- See also: [[policy-as-code]]
