---
title: "Patch management"
description: "Keeping OS and applications up to date to close known vulnerabilities"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Patch management is the systematic process of identifying, testing, approving, deploying, and verifying security patches and updates for operating systems, applications, firmware, and other software components. It is the most common and effective vulnerability remediation method, directly addressing the root cause of known vulnerabilities by applying vendor-supplied fixes.

## Key Details

- Patch lifecycle: identify available patches → assess and prioritize → test in non-production → approve and deploy → verify deployment
- Critical/high-severity patches should be deployed rapidly (24-72 hours for critical); lower severity on regular cycles
- Patch deployment tools: Windows Server Update Services (WSUS), SCCM/Intune, Red Hat Satellite, Ansible
- Emergency patching processes must exist for critical zero-day vulnerabilities
- Unpatched systems remain vulnerable even after patches are released — tracking deployment is essential

## Connections

- Parent: [[vulnerability-management]] — patch management is the primary vulnerability remediation method
- See also: [[firmware-updates]]
