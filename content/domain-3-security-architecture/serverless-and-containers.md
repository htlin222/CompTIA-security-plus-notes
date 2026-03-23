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

## Scenario

> See [[case-serverless-and-containers]] for a practical DevOps scenario applying these concepts.
