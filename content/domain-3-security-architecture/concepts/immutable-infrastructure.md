---
title: "Immutable infrastructure"
description: "servers are never modified after deployment; updates create new instances that replace old ones"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Immutable infrastructure?
> Instead of fixing a broken toy, you throw it away and get a brand-new identical one from the box. Immutable infrastructure means servers are never patched in place -- you replace them with fresh, clean copies every time an update is needed.

## Definition

Immutable infrastructure is a deployment philosophy in which servers and other infrastructure components are never modified after they are deployed. Instead of patching or updating a running server, a new server image is built with the required changes and deployed to replace the old one. The old server is then decommissioned. This approach eliminates configuration drift and ensures every running server is in a known, validated state.

## Key Details

- Once deployed, immutable servers are never changed — they are replaced, not modified
- Enables rapid rollback: if a new version has problems, simply redeploy the previous image
- Eliminates configuration drift because there is no opportunity for manual changes to accumulate
- Strongly aligned with containerization and microservices architectures
- Security benefit: a compromised immutable server is replaced, not remediated, ensuring a clean state

## Connections

- Parent: [[infrastructure-as-code]] — immutable infrastructure is a key IaC deployment pattern
- See also: [[configuration-drift]]
