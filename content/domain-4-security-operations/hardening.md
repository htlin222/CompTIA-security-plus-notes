---
title: "Hardening"
description: "Reducing the attack surface of systems by eliminating unnecessary services, applying patches, and enforcing secure configurations"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - concept/endpoint
  - weight/high
aliases:
  - "System Hardening"
  - "OS Hardening"
---

> [!eli5] ELI5: What is Hardening?
> When you move into a new house, you lock the doors, close the windows, and maybe remove the spare key from under the mat. Hardening a computer is the same idea -- you turn off features you do not need, remove programs that came pre-installed, and change all the default passwords. The fewer unlocked doors and open windows a system has, the harder it is for a bad guy to sneak in.

## Overview

Hardening is the process of securing a system by reducing its attack surface through removing unnecessary software, disabling unused services, applying patches, and configuring security settings according to established benchmarks. Every system should be hardened before deployment and maintained through ongoing configuration management. Hardening applies to operating systems, applications, network devices, and firmware.

## Key Concepts

- **[[cis-benchmarks|CIS Benchmarks]]**: Industry-standard security configuration guidelines from the Center for Internet Security
- **[[stig-security-technical-implementation-guide|STIG (Security Technical Implementation Guide)]]**: DoD-specific hardening standards for government systems
- **[[disable-unnecessary-services-and-ports|Disable unnecessary services and ports]]**: Reduce potential entry points by turning off what is not needed
- **[[remove-default-accounts-and-passwords|Remove default accounts and passwords]]**: Default credentials are publicly known and easily exploited
- **[[patch-management|Patch management]]**: Applying security updates promptly to close known vulnerabilities
- **[[least-functionality-principle|Least functionality principle]]**: Systems should only have the minimum capabilities needed for their role
- **[[application-allowlisting|Application allowlisting]]**: Only permit approved executables to run
- **[[registry-and-gpo-hardening|Registry and GPO hardening]]**: Windows Group Policy Objects enforce security settings across domains
- **[[firmware-updates|Firmware updates]]**: BIOS/UEFI and device firmware must be kept current
- **[[secure-baseline-images|Secure baseline images]]**: Golden images with pre-hardened configurations for consistent deployment
- **[[file-system-permissions|File system permissions]]**: Restricting access to sensitive files and directories

## Exam Tips

> [!tip] Remember
> Hardening = reduce attack surface. Steps: remove defaults, disable services, patch, configure securely, monitor for drift. CIS Benchmarks are the go-to reference for "how should I configure this?"

- Hardening is NOT a one-time activity — drift detection ensures systems stay in compliance
- Know that hardening applies to ALL layers: OS, apps, network devices, firmware, cloud services
- Default configurations are NEVER secure — always customize security settings

## Connections

- Implements findings from [[vulnerability-management]] by closing identified weaknesses
- Strengthens [[endpoint-security]] by establishing secure baselines before deploying systems
- Supports [[compliance]] requirements by following recognized security standards (CIS, STIG)
- [[automation-and-scripting]] ensures hardening configurations are applied consistently at scale

## Practice Questions

> [!qbank]- Q-Bank: Hardening (4 Questions)
>
> **Q1.** A security auditor discovers that several production servers are running with default administrator credentials and have unnecessary services such as FTP and Telnet enabled. Which hardening step should be performed FIRST?
>
> A. Install an EDR agent on all servers
> B. Change default credentials and disable unnecessary services
> C. Implement full disk encryption
> D. Deploy a SIEM to monitor the servers
>
> > [!answer]- Show Answer
> > **B. Change default credentials and disable unnecessary services**
> >
> > [[remove-default-accounts-and-passwords|Removing default credentials]] and [[disable-unnecessary-services-and-ports|disabling unnecessary services]] are fundamental hardening steps that directly eliminate known attack vectors. Default credentials are publicly documented and easily exploited. Option A adds detection but does not fix the root vulnerability. Option C protects data at rest but does not address the exposed services. Option D provides monitoring but does not remediate the immediate risk.
>
> **Q2.** An organization needs to ensure that all Windows workstations across its 50 branch offices enforce the same security settings, including password policies, screen lock timers, and disabled USB storage. What is the BEST approach?
>
> A. Sending a policy document to each branch office manager for manual implementation
> B. Configuring Group Policy Objects (GPOs) through Active Directory
> C. Installing third-party antivirus software on all workstations
> D. Enabling BitLocker on all workstations
>
> > [!answer]- Show Answer
> > **B. Configuring Group Policy Objects (GPOs) through Active Directory**
> >
> > [[registry-and-gpo-hardening|GPO hardening]] through Active Directory centrally enforces security settings consistently across all domain-joined workstations regardless of location. Option A relies on manual compliance and is error-prone at scale. Option C addresses malware but not configuration enforcement. Option D provides encryption but does not enforce the specific security policies mentioned.
>
> **Q3.** A security team is building golden images for deploying new servers. They want to ensure every server starts with a secure configuration aligned with industry standards. Which resource should they PRIMARILY reference for configuration guidelines?
>
> A. The server vendor's default installation documentation
> B. CIS Benchmarks for the specific operating system
> C. The organization's acceptable use policy
> D. OWASP Top 10 vulnerability list
>
> > [!answer]- Show Answer
> > **B. CIS Benchmarks for the specific operating system**
> >
> > [[cis-benchmarks|CIS Benchmarks]] provide industry-standard, detailed security configuration guidelines for specific operating systems and applications, making them the ideal reference for building [[secure-baseline-images|secure baseline images]]. Option A provides default settings which are never considered secure. Option C governs user behavior, not technical configurations. Option D focuses on web application vulnerabilities, not OS hardening.
>
> **Q4.** Six months after deploying hardened server images, a security scan reveals that several servers have drifted from their original secure configurations — new services have been enabled and firewall rules relaxed. What control would BEST prevent this issue?
>
> A. Conducting annual penetration tests
> B. Implementing automated configuration management with drift detection
> C. Requiring administrators to sign an acceptable use agreement
> D. Increasing the frequency of vulnerability scans to daily
>
> > [!answer]- Show Answer
> > **B. Implementing automated configuration management with drift detection**
> >
> > Hardening is not a one-time activity. Automated [[configuration-management]] with drift detection continuously monitors systems and can alert on or automatically remediate configuration changes that deviate from the [[secure-baseline-images|secure baseline]]. Option A is periodic and would not catch drift between tests. Option C is a policy control that does not technically enforce configurations. Option D identifies vulnerabilities but does not enforce configuration compliance.

## Scenario

> See [[case-hardening]] for a practical DevOps scenario applying these concepts.
