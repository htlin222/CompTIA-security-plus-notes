---
title: "Cloud Security"
description: "Cloud security encompasses the controls, policies, and technologies that protect cloud-based infrastructure, applications, and data."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cloud
  - weight/high
aliases:
  - "Cloud Security"
---

## Overview

Cloud security addresses the unique risks and shared responsibilities of deploying resources in cloud environments. As organizations move workloads to IaaS, PaaS, and SaaS platforms, they must understand which security controls they manage versus what the cloud provider handles. Cloud security requires adapting traditional security practices to dynamic, API-driven, multi-tenant environments.

## Key Concepts

- **Cloud service models and shared responsibility:**
  - **IaaS** — provider manages physical infrastructure; customer manages OS, apps, data (most customer responsibility)
  - **PaaS** — provider manages infrastructure + runtime; customer manages apps and data
  - **SaaS** — provider manages nearly everything; customer manages data and access (least customer responsibility)
- **[[cloud-deployment-models|Cloud deployment models:]]** public, private, hybrid, community, multi-cloud
- **[[shared-responsibility-model|Shared responsibility model]]** — security "of" the cloud (provider) vs. security "in" the cloud (customer)
- **Cloud security controls:**
  - **CASB (Cloud Access Security Broker)** — enforces security policies between users and cloud services
  - **CSPM (Cloud Security Posture Management)** — monitors cloud configurations for misconfigurations
  - **CWPP (Cloud Workload Protection Platform)** — protects workloads across cloud environments
- **[[identity-and-access-management|Identity and access management]]** — federated identity, SSO, and strong IAM policies for cloud resources
- **[[data-sovereignty|Data sovereignty]]** — data stored in the cloud is subject to the laws of its physical location
- **[[multitenancy-risks|Multitenancy risks]]** — data isolation between tenants; side-channel attacks; resource contention
- **[[api-security|API security]]** — cloud services are API-driven; securing APIs is critical to cloud security
- **[[secrets-management|Secrets management]]** — storing credentials, keys, and tokens securely in cloud environments

## Exam Tips

> [!tip] Remember
> Shared responsibility: IaaS = customer manages the most; SaaS = provider manages the most. CASB = policy enforcement between users and cloud. CSPM = finds misconfigurations. The exam loves testing the shared responsibility model.

## Connections

- Extends [[network-security-architecture]] principles into cloud environments where traditional perimeters do not exist
- Related to [[virtualization-security]] as cloud platforms are built on virtualization technology
- See also [[serverless-and-containers]] for securing modern cloud-native deployment models
- Data protection in the cloud depends on [[encryption]] for data at rest and in transit

## Scenario

> See [[case-cloud-security]] for a practical DevOps scenario applying these concepts.
