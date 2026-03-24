---
title: "Zero Trust"
description: "Security model that assumes no implicit trust and verifies every access request continuously"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/network
  - weight/high
aliases:
  - "Zero Trust Architecture"
  - "ZTA"
---

> [!eli5] ELI5: What is Zero Trust?
> Most buildings work like this: once you're past the front door, everyone trusts you. Zero Trust says "no way." Even if you're already inside the building, you still have to show your badge every time you open a new door, and someone checks whether you should really be there right now. It doesn't matter if you're the CEO or a new employee -- everyone gets checked, every time, for every request. No free passes.

## Overview

Zero Trust is a security model built on the principle of "never trust, always verify." Unlike traditional perimeter-based security, Zero Trust assumes that threats exist both inside and outside the network and requires continuous verification of every user, device, and connection before granting access. It has become a major focus of the SY0-701 exam due to its growing adoption across industries.

## Key Concepts

- **Core principles**:
  - Verify explicitly — authenticate and authorize based on all available data points
  - Use least-privilege access — limit access with just-in-time and just-enough-access (JIT/JEA)
  - Assume breach — minimize blast radius and segment access; verify end-to-end encryption
- **Control plane vs. Data plane**
  - **Control plane** — policy engine and policy administrator that make access decisions
  - **Data plane** — policy enforcement points that allow or deny traffic based on control plane decisions
- **[[policy-engine|Policy engine]]** — evaluates access requests against defined policies, risk signals, and threat intelligence
- **[[policy-administrator|Policy administrator]]** — establishes and removes communication paths based on policy engine decisions
- **[[policy-enforcement-point-pep|Policy enforcement point (PEP)]]** — gateway that enforces access decisions at the data plane level
- **[[adaptive-identity|Adaptive identity]]** — authentication and authorization that adjust based on real-time risk assessment
- **[[implicit-trust-zones|Implicit trust zones]]** — Zero Trust aims to eliminate these; every zone is treated as untrusted
- **Microsegmentation** — breaking the network into small zones to contain lateral movement (see [[network-segmentation]])
- **[[software-defined-perimeter-sdp|Software-defined perimeter (SDP)]]** — creates one-to-one connections between users and resources; hides infrastructure

## Exam Tips

> [!tip] Remember
> Zero Trust = **Control Plane** (decisions) + **Data Plane** (enforcement). Know the three components: Policy Engine, Policy Administrator, Policy Enforcement Point. The exam specifically tests the plane architecture.

> [!tip] Key Distinction
> Zero Trust is NOT just about the network — it covers identity, devices, applications, data, and infrastructure. If a question mentions "eliminating implicit trust," the answer is Zero Trust.

## Connections

- Relies heavily on [[mfa]] for continuous identity verification at every access request
- Implemented through [[network-segmentation]] and microsegmentation to limit lateral movement
- Requires robust [[authentication]] that goes beyond simple credentials
- Complements [[defense-in-depth]] by adding verification layers within each security tier
- Supported by [[endpoint-security]] to validate device posture before granting access

## Practice Questions

> [!qbank]- Q-Bank: Zero Trust (4 Questions)
>
> **Q1.** An organization redesigns its network so that every access request — whether from inside the corporate office or from a remote location — must be authenticated and authorized before any resource is accessible. No user or device is automatically trusted based on network location. Which security model does this BEST describe?
>
> A. Defense in depth
> B. Perimeter-based security
> C. Zero Trust
> D. Network segmentation
>
> > [!answer]- Show Answer
> > **C. Zero Trust**
> >
> > [[zero-trust|Zero Trust]] operates on the principle of "never trust, always verify" — every access request is authenticated and authorized regardless of network location, eliminating implicit trust. Defense in depth uses multiple layers of controls but does not specifically require that internal traffic be continuously verified. Perimeter-based security is the opposite approach, trusting traffic once it passes the perimeter. Network segmentation is a technique used within Zero Trust but is not the overarching model described.
>
> **Q2.** In a Zero Trust architecture, which component is responsible for evaluating access requests against defined policies, risk signals, and threat intelligence to make allow/deny decisions?
>
> A. Policy enforcement point (PEP)
> B. Policy engine
> C. Policy administrator
> D. Data plane gateway
>
> > [!answer]- Show Answer
> > **B. Policy engine**
> >
> > The [[policy-engine|policy engine]] evaluates access requests against defined policies, risk signals, and threat intelligence to make access decisions in the control plane. The [[policy-enforcement-point-pep|PEP]] enforces those decisions at the data plane level but does not make the decisions itself. The [[policy-administrator|policy administrator]] establishes and removes communication paths based on the policy engine's decisions but does not evaluate requests. The data plane is where enforcement occurs, not where decisions are made.
>
> **Q3.** A security architect is implementing Zero Trust and needs to limit an attacker's ability to move laterally after compromising a single workstation. Which technique MOST directly supports this goal?
>
> A. Multi-factor authentication
> B. Microsegmentation
> C. Full disk encryption
> D. Security awareness training
>
> > [!answer]- Show Answer
> > **B. Microsegmentation**
> >
> > [[network-segmentation|Microsegmentation]] breaks the network into small zones with individual access controls, directly containing lateral movement by limiting what a compromised host can reach. MFA strengthens identity verification but does not restrict network movement after a host is compromised. Full disk encryption protects data at rest on the device but does not prevent network-based lateral movement. Security awareness training is a preventive administrative control targeting human behavior, not network containment.
>
> **Q4.** A Zero Trust implementation requires that a user's access level automatically adjusts when they connect from a new device or an unusual location, potentially requiring additional verification steps. Which Zero Trust concept does this BEST illustrate?
>
> A. Implicit trust zones
> B. Software-defined perimeter
> C. Adaptive identity
> D. Policy enforcement point
>
> > [!answer]- Show Answer
> > **C. Adaptive identity**
> >
> > [[adaptive-identity|Adaptive identity]] adjusts authentication and authorization requirements based on real-time risk assessment — new devices or unusual locations increase risk signals, triggering additional verification. [[implicit-trust-zones|Implicit trust zones]] are what Zero Trust aims to eliminate, not a feature it implements. A [[software-defined-perimeter-sdp|software-defined perimeter]] creates one-to-one connections between users and resources but does not dynamically adjust authentication requirements. The [[policy-enforcement-point-pep|PEP]] enforces access decisions but does not determine the adaptive risk-based adjustments.

## Scenario

> See [[case-zero-trust]] for a practical DevOps scenario applying these concepts.
