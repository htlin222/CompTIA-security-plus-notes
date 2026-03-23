---
title: "Security through obscurity"
description: "Relying on secrecy of design rather than robust controls; considered insufficient on its own"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Security through obscurity is the practice of relying on secrecy or concealment of system design, implementation details, or configurations as a security measure. Rather than using robust, proven security mechanisms, security through obscurity assumes that attackers won't discover the system's workings. While it may add a minor layer of difficulty, it is widely considered insufficient as a sole security measure because it fails catastrophically once the secret is discovered.

## Key Details

- Directly contradicted by **Kerckhoffs's Principle** and the **Open Design Principle**—true security must withstand public scrutiny.
- Examples of misplaced obscurity: hiding admin panel at a non-standard URL, changing SSH to a non-standard port (security theater).
- Security through obscurity is **not entirely without value** as a supplementary measure—changing default ports reduces automated scanning hits, for example.
- The problem: once the secret (non-standard URL, custom protocol) is discovered, all security evaporates.
- The alternative: rely on **cryptographically sound algorithms**, **proven protocols**, and **tested security mechanisms** whose security doesn't depend on secrecy.

## Connections

- Parent: [[security-concepts]] — a flawed security approach to understand and avoid
- See also: [[open-design-principle]]
