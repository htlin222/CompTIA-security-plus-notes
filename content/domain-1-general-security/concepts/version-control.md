---
title: "Version control"
description: "Tracking changes to configurations, code, and documentation for accountability and rollback"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Version Control?
> It's like saving every draft of your school essay so you can go back to any older version if something goes wrong. You can always see what changed, who changed it, and undo mistakes.

## Definition

Version control is the practice of systematically tracking and managing changes to files, configurations, code, and documentation over time. Every change is recorded with metadata—who made the change, when, and why—creating a complete history that supports auditing, accountability, rollback to previous versions, and collaborative work. In security contexts, version control is essential for configuration management and change management processes.

## Key Details

- **Systems**: Git (distributed), SVN (centralized), Mercurial—most modern environments use Git with platforms like GitHub or GitLab.
- **Security value**: Provides a complete audit trail of changes; enables rollback to last known-good configuration after a problem; detects unauthorized changes.
- **Infrastructure as Code (IaC)**: Storing infrastructure configurations in version-controlled repositories enables reproducible, auditable deployments.
- **Secrets management**: Version control systems must be configured to **never commit credentials, API keys, or passwords**—use secrets managers instead.
- Change management integration: every configuration change should be tracked in version control with a reference to the change request.

## Connections

- Parent: [[change-management]] — version control supports change tracking and rollback
- See also: [[backoutrollback-plan]], [[configuration-management]]
