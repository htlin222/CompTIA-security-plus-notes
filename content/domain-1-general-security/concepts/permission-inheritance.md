---
title: "Permission inheritance"
description: "Child objects inherit permissions from parent containers in access control systems"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Permission inheritance is a mechanism in access control systems where child objects (files, subfolders, subdirectories, child OUs in Active Directory) automatically receive the same permissions as their parent container. This simplifies permission management in hierarchical structures—permissions set at the top level propagate downward—but must be carefully managed to prevent unintended permission grants.

## Key Details

- **Windows NTFS**: Files and folders inherit permissions from parent folders by default—can be disabled for specific objects if needed.
- **Active Directory**: Organizational Units (OUs) inherit Group Policy Objects (GPOs) from parent OUs—managed via precedence rules.
- **Blocking inheritance**: Administrators can explicitly break inheritance on specific objects to assign unique permissions.
- **Explicit permissions** (set directly on an object) take precedence over inherited permissions—important for exceptions.
- Improper inheritance can lead to **over-privileged access**—permissions granted at a high level propagate to all child objects.

## Connections

- Parent: [[authorization]] — inheritance as an access control implementation mechanism
- See also: [[least-privilege]], [[principle-of-least-privilege]]
