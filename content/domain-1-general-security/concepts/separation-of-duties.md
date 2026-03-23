---
title: "Separation of duties"
description: "Dividing critical tasks among multiple people to prevent fraud and detect errors"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Separation of duties (SoD) is a security principle that divides critical, sensitive, or fraud-prone tasks among multiple individuals so that no single person has complete control over an entire process or transaction. By requiring multiple parties to complete a sensitive action, SoD prevents any one individual from being able to commit fraud, make errors, or abuse their access without detection by others.

## Key Details

- Classic examples: The person who **authorizes** a purchase shouldn't be the one who **processes** it; the person who creates financial records shouldn't be the one who **audits** them.
- In IT: the system administrator who manages backups shouldn't be the only one who verifies their integrity; developers shouldn't be able to push code directly to production.
- **Dual control**: Specific variant requiring two people simultaneously for high-risk actions (e.g., two keys to launch nuclear weapons; two admins to change crypto keys).
- **Two-person integrity**: Similar to dual control—ensures two authorized individuals must be present for sensitive operations.
- Implemented via **role-based access controls**, **workflow systems** requiring approvals, and **audit processes**.

## Connections

- Parent: [[security-concepts]] — a fundamental fraud prevention principle
- See also: [[least-privilege]], [[need-to-know]]
