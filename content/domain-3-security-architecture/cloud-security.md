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

> [!eli5] ELI5: What is Cloud Security?
> You know how you might store your toys at a friend's house? You trust your friend to keep them safe, but you still want to make sure the door is locked and nobody else can take them. Cloud security is the same idea -- when companies store their data on someone else's computers (the cloud), they need rules and locks to keep that data safe, even though they do not own the building where it lives.
>
> > [!eli5] ELI5: Cloud Security (繁體中文版)
> > 雲端安全就是保護放在別人電腦裡的資料。你需要搞清楚哪些是你的責任 (資料和存取控制)，哪些是雲端公司的責任 (實體伺服器)。
> >
> > ```ascii
> > [雲端公司 (基礎設施)] <--> [你 (資料/權限)]
> > ```

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
- **Edge computing** — processing data near the source rather than in a centralized cloud data center
- **Fog computing** — extends cloud computing to the network edge, providing local processing and storage
- **VPC (Virtual Private Cloud)** — isolated virtual network within a public cloud provider
- **Transit gateway** — centralized hub connecting multiple VPCs and on-premises networks
- **Availability zones** — physically separate data centers within a cloud region for redundancy
- **SWG (Secure Web Gateway)** — filters unwanted software and enforces corporate policy for web traffic

## Exam Tips

> [!tip] Remember
> Shared responsibility: IaaS = customer manages the most; SaaS = provider manages the most. CASB = policy enforcement between users and cloud. CSPM = finds misconfigurations. The exam loves testing the shared responsibility model.

## Connections

- Extends [[network-security-architecture]] principles into cloud environments where traditional perimeters do not exist
- Related to [[virtualization-security]] as cloud platforms are built on virtualization technology
- See also [[serverless-and-containers]] for securing modern cloud-native deployment models
- Data protection in the cloud depends on [[encryption]] for data at rest and in transit

## Practice Questions

> [!qbank]- Q-Bank: Cloud Security (4 Questions)
>
> **Q1.** A company migrates its email system to a SaaS provider. Under the shared responsibility model, which of the following is the customer MOST responsible for?
>
> A. Patching the email server operating system
> B. Managing physical data center security
> C. Controlling user access and data classification
> D. Maintaining the hypervisor infrastructure
>
> > [!answer]- Show Answer
> > **C. Controlling user access and data classification**
> >
> > In the [[shared-responsibility-model|shared responsibility model]] for SaaS, the provider manages nearly everything including infrastructure, OS, and application. The customer remains responsible for their data and access management. Patching the OS (A), physical security (B), and hypervisor maintenance (D) are all provider responsibilities in a SaaS model.
>
> **Q2.** A security team discovers that several cloud storage buckets have been left publicly accessible due to misconfigurations. Which cloud security tool is BEST suited to detect this type of issue?
>
> A. CASB (Cloud Access Security Broker)
> B. CSPM (Cloud Security Posture Management)
> C. CWPP (Cloud Workload Protection Platform)
> D. DLP (Data Loss Prevention)
>
> > [!answer]- Show Answer
> > **B. CSPM (Cloud Security Posture Management)**
> >
> > [[cloud-security|CSPM]] specifically monitors cloud environments for misconfigurations such as publicly exposed storage buckets. CASB (A) enforces security policies between users and cloud services but focuses on access control and shadow IT. CWPP (C) protects running workloads, not configuration posture. DLP (D) detects unauthorized data transfers but does not identify infrastructure misconfigurations.
>
> **Q3.** An organization uses multiple cloud providers to avoid vendor lock-in and increase resilience. Which cloud deployment model does this describe?
>
> A. Hybrid cloud
> B. Community cloud
> C. Private cloud
> D. Multi-cloud
>
> > [!answer]- Show Answer
> > **D. Multi-cloud**
> >
> > [[cloud-deployment-models|Multi-cloud]] involves using services from multiple cloud providers, which reduces vendor lock-in and increases availability. Hybrid cloud (A) combines on-premises infrastructure with a public cloud, not multiple public providers. Community cloud (B) is shared among organizations with common interests. Private cloud (C) is dedicated to a single organization.
>
> **Q4.** A development team stores API keys and database passwords in environment variables within their cloud platform. A security architect recommends a more secure approach. Which solution BEST addresses this concern?
>
> A. Encrypting the environment variables with a symmetric key stored in the same environment
> B. Using a dedicated secrets management service with access controls and audit logging
> C. Hardcoding the credentials in the application source code
> D. Sharing credentials via encrypted email to team members
>
> > [!answer]- Show Answer
> > **B. Using a dedicated secrets management service with access controls and audit logging**
> >
> > A [[secrets-management|secrets management]] service (such as AWS Secrets Manager or HashiCorp Vault) provides centralized, access-controlled, auditable storage for credentials. Encrypting variables with a key in the same environment (A) still exposes the key alongside the secrets. Hardcoding credentials in source code (C) is the worst practice and risks exposure through version control. Sharing via email (D) creates uncontrolled copies and is not scalable.

## Scenario

> See [[case-cloud-security]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [3.1 – Cloud Infrastructures](https://www.youtube.com/watch?v=8qpQ8Q6xxiU)
