---
title: "Serverless and Containers"
description: "Serverless computing and containers provide lightweight, scalable deployment models with unique security considerations."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/cloud
  - weight/medium
aliases:
  - "Serverless"
  - "Containers"
---

> [!eli5] ELI5: What are Serverless and Containers?
> Think of containers like lunchboxes -- each one has everything a meal needs, packed neatly so it does not mix with anyone else's food. You can stack many lunchboxes on one table. Serverless is even simpler: instead of packing your own lunch, you just tell the cafeteria what you want, and they make it for you on the spot. Both are ways to run programs on computers more efficiently, but each comes with its own safety rules to follow.

## Overview

Containers package applications with their dependencies into isolated units that share the host OS kernel, providing lightweight and consistent deployment. Serverless computing abstracts the infrastructure entirely, allowing developers to deploy functions that execute on demand without managing servers. Both models accelerate development but introduce security challenges around image integrity, runtime isolation, and supply chain risks.

## Key Concepts

- **Containers:**
  - Share the host OS kernel; lighter than VMs but weaker isolation
  - **Container images** — immutable templates; must be scanned for vulnerabilities before deployment
  - **Container registry** — repository for storing and distributing images; secure with access controls and signing
  - **Container orchestration (Kubernetes)** — manages deployment, scaling, and networking of containers
  - **Container escape** — breaking out of a container to access the host; similar to VM escape but more likely due to shared kernel
  - **Ephemeral nature** — containers are short-lived; logging and monitoring must capture data before termination
- **Serverless (Function as a Service / FaaS):**
  - Provider manages all infrastructure; customer only writes and deploys code
  - **Event-driven** — functions execute in response to triggers (API calls, messages, schedules)
  - **Cold starts** — latency when a function is invoked after being idle
  - **Execution time limits** — functions have maximum execution durations
  - **Security risks** — insecure function code, excessive permissions, dependency vulnerabilities, injection attacks
- **Shared security concerns:**
  - Supply chain attacks through compromised base images or dependencies
  - Secrets management for credentials and API keys
  - Least privilege for function/container permissions

## Exam Tips

> [!tip] Remember
> Containers share the host kernel = weaker isolation than VMs. Always scan container images for vulnerabilities. Serverless = provider manages infrastructure, customer manages code and permissions. Both are ephemeral, making logging challenging.

## Connections

- Runs within [[cloud-security]] environments and follows the shared responsibility model
- Image and dependency management relates to [[infrastructure-as-code]] practices for consistent, auditable deployments
- See also [[virtualization-security]] for comparing container isolation to VM isolation

## Practice Questions

> [!qbank]- Q-Bank: Serverless and Containers (4 Questions)
>
> **Q1.** A development team deploys microservices using containers. A security review reveals that a container image pulled from a public registry contains a known vulnerability. Which control should be implemented FIRST to prevent this in the future?
>
> A. Disable all container networking
> B. Scan container images for vulnerabilities before deployment
> C. Run all containers with root privileges for easier patching
> D. Use only serverless functions instead of containers
>
> > [!answer]- Show Answer
> > **B. Scan container images for vulnerabilities before deployment**
> >
> > [[serverless-and-containers|Container image scanning]] before deployment is the FIRST and most critical control to catch vulnerabilities in base images and dependencies. Disabling networking (A) would make the containers non-functional. Running as root (C) increases the attack surface and violates least privilege. Switching to serverless (D) may not be feasible and has its own security concerns.
>
> **Q2.** An attacker exploits a vulnerability in a container and gains access to the underlying host operating system. Which container-specific threat does this describe?
>
> A. Container sprawl
> B. Container escape
> C. Cold start latency
> D. Resource contention
>
> > [!answer]- Show Answer
> > **B. Container escape**
> >
> > [[serverless-and-containers|Container escape]] occurs when an attacker breaks out of the container's isolation boundary to access the host OS or other containers. This is possible because containers share the host kernel. Container sprawl is uncontrolled growth of container instances (A). Cold start latency (C) is a serverless performance issue. Resource contention (D) is containers competing for shared resources but not a breakout.
>
> **Q3.** A company uses serverless functions (FaaS) for processing customer orders. Which security concern is MOST unique to serverless environments compared to traditional server deployments?
>
> A. Operating system patch management
> B. Physical server security
> C. Excessive function permissions and dependency vulnerabilities
> D. Hypervisor hardening
>
> > [!answer]- Show Answer
> > **C. Excessive function permissions and dependency vulnerabilities**
> >
> > In [[serverless-and-containers|serverless environments]], the customer manages code and permissions, making excessive IAM permissions and vulnerable dependencies the primary security concern. OS patching (A), physical security (B), and hypervisor hardening (D) are all provider responsibilities in serverless, not customer concerns.
>
> **Q4.** A security team is comparing container isolation to virtual machine isolation for a multi-tenant environment. Which statement BEST describes the key difference?
>
> A. Containers provide stronger isolation because they are lighter weight
> B. VMs provide stronger isolation because each VM runs its own OS kernel
> C. Containers and VMs provide identical levels of isolation
> D. VMs share the host OS kernel just like containers
>
> > [!answer]- Show Answer
> > **B. VMs provide stronger isolation because each VM runs its own OS kernel**
> >
> > [[serverless-and-containers|Containers]] share the host OS kernel, which provides weaker isolation compared to [[virtualization-security|VMs]] that each run their own separate kernel. This makes container escape more feasible than VM escape. Containers are lighter but less isolated (A is incorrect reasoning). They do not provide identical isolation (C). VMs run their own kernels, they do not share the host kernel like containers (D).

## Scenario

> See [[case-serverless-and-containers]] for a practical DevOps scenario applying these concepts.
