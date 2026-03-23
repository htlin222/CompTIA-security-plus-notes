---
title: "Open design principle"
description: "Security mechanisms should not depend on secrecy of implementation"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is the Open Design Principle?
> A good lock should be safe even if everyone knows exactly how it works. The only secret should be the key itself, not how the lock was built. That's open design -- security that doesn't depend on hiding how it works.

## Definition

The open design principle states that the security of a system should not depend on keeping its design or implementation secret. Security mechanisms should be secure even if an attacker knows exactly how they work—the only secrets should be keys and credentials. This principle was articulated by Kerckhoffs and reaffirmed by Claude Shannon, and it is the foundation of modern cryptographic design.

## Key Details

- **Kerckhoffs's Principle**: "A cryptosystem should be secure even if everything about the system, except the key, is public knowledge."
- **Shannon's Maxim**: "The enemy knows the system"—design assuming the attacker has full knowledge of the mechanism.
- Opposite of **security through obscurity** (which is widely considered insufficient as a sole security measure).
- Practical application: **open-source cryptographic algorithms** (AES, RSA, ECC) are more trusted than proprietary "black box" algorithms because they can be publicly analyzed.
- Why it matters: secret algorithms fail catastrophically when the secret is leaked; well-designed open algorithms fail only if the key is compromised.

## Connections

- Parent: [[security-concepts]] — a foundational security design principle
- See also: [[security-through-obscurity]]
