---
title: "Shared responsibility model"
description: "security \"of\" the cloud (provider) vs. security \"in\" the cloud (customer)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

The shared responsibility model defines the division of security responsibilities between a cloud service provider and their customers. The cloud provider is responsible for securing the underlying infrastructure (the cloud itself), while the customer is responsible for securing what they deploy and configure within the cloud. The exact boundary between provider and customer responsibility shifts depending on the service model (IaaS, PaaS, SaaS).

## Key Details

- **IaaS**: customer manages OS, applications, data, network controls; provider manages physical hardware and hypervisor
- **PaaS**: customer manages applications and data; provider manages OS, runtime, and infrastructure
- **SaaS**: customer manages data and user access; provider manages everything else
- Security "of" the cloud: physical security, hypervisor security, network infrastructure — provider's responsibility
- Security "in" the cloud: data classification, access management, configuration, network rules — customer's responsibility

## Connections

- Parent: [[cloud-security]] — the shared responsibility model is the foundational framework for cloud security
- See also: [[cloud-deployment-models]]
