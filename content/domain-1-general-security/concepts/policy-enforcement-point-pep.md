---
title: "Policy enforcement point (PEP)"
description: "Gateway that enforces access decisions at the data plane level in Zero Trust"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
aliases:
  - PEP
---

> [!eli5] ELI5: What is a Policy Enforcement Point (PEP)?
> The PEP is the actual gate or door that opens or stays shut. The brain (policy engine) decides yes or no, but the PEP is the one physically blocking or allowing you through.

## Definition

The Policy Enforcement Point (PEP) is the Zero Trust Architecture component that sits in the data path and enforces access control decisions made by the policy engine. It acts as the gatekeeper—blocking, allowing, or conditionally permitting resource access based on the access decisions it receives. The PEP is what actually controls traffic flow and access at the network or application level.

## Key Details

- Sits between the **subject** (user/device) and the **resource** (application/data) being accessed.
- Receives access decisions from the **policy administrator** (which relays them from the policy engine).
- Implemented as: **API gateways**, **proxies**, **SDN controllers**, **VPN concentrators**, **identity-aware proxies** (Google BeyondCorp, Zscaler ZPA).
- Enforces **micro-segmentation** by controlling traffic flows at a granular level.
- If the policy engine denies access, the PEP blocks the connection—even if the request appears to come from the "trusted" internal network.

## Connections

- Parent: [[zero-trust]] — the enforcement mechanism in Zero Trust Architecture
- See also: [[policy-engine]], [[policy-administrator]]
