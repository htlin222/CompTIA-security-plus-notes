---
title: "Security Policies"
description: "Security policies are formal documents that define an organization's rules, expectations, and requirements for protecting information assets."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/medium
aliases:
  - "Security Policies"
---

> [!eli5] ELI5: What are Security Policies?
> A security policy is like the student handbook your school gives out at the start of the year. It lists the rules everyone needs to follow -- no cheating, be respectful, wear your uniform. For a company, security policies are the official written rules about how to protect computers and data. They cover things like who can access what, how strong your password must be, and what happens if you break a rule. Everyone in the company has to know and follow them.

## Overview

Security policies are high-level, management-approved documents that establish the rules and expectations for how an organization protects its information assets. They serve as the foundation for all security decisions and are enforced through standards, procedures, and guidelines. Policies must be living documents that are regularly reviewed, updated, and communicated to all personnel.

## Key Concepts

- **Policy hierarchy:**
  - **Policies** — mandatory, broad, management-approved ("what" must be done)
  - **Standards** — mandatory, specific technical requirements ("how" it must be done)
  - **Baselines** — minimum security configurations for systems
  - **Guidelines** — recommended but not mandatory best practices
  - **Procedures** — step-by-step instructions for tasks
- **Common security policies:**
  - **Acceptable Use Policy (AUP)** — defines permitted use of organizational resources
  - **Information security policy** — overarching security program direction
  - **Password / credential policy** — complexity, length, rotation, MFA requirements
  - **Data handling / classification policy** — rules for managing data at each classification level
  - **Change management policy** — process for approving and documenting changes
  - **Incident response policy** — defines roles, authority, and procedures for handling incidents
  - **BYOD policy** — rules for personal devices accessing corporate resources
- **[[policy-lifecycle|Policy lifecycle]]** — create, approve, distribute, enforce, review, revise, retire
- **[[exception-process|Exception process]]** — formal mechanism for requesting and approving deviations from policy

## Exam Tips

> [!tip] Remember
> Policies are mandatory and set by management. Guidelines are optional recommendations. Standards define specific requirements. The AUP is the most commonly referenced policy on the exam.

## Connections

- Derived from [[governance]] decisions and organizational risk appetite
- Must align with external [[regulations-and-frameworks]] to ensure compliance
- See also [[security-awareness-training]] for how policies are communicated to employees

## Scenario

> See [[case-security-policies]] for a practical DevOps scenario applying these concepts.
