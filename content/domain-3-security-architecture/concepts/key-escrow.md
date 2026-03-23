---
title: "Key escrow"
description: "third party holds a copy of the key for recovery; controversial due to trust implications"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Key escrow is a system in which a copy of a cryptographic key is entrusted to a third party (the escrow agent) for safekeeping and potential recovery. If the primary key holder loses access to their key or if legal authorities need access to encrypted data, the escrowed copy can be retrieved. Key escrow is controversial because it creates a concentrated target for attackers and raises concerns about government access to private communications.

## Key Details

- Used for key recovery when users forget passwords or when corporate data must survive employee departure
- Government-mandated key escrow (e.g., Clipper Chip, 1990s) was highly controversial and largely rejected
- Enterprise key escrow within an organization is more widely accepted for business continuity
- The escrow agent becomes a high-value attack target — compromise of the escrow exposes all keys
- Must be secured with strong access controls, multi-person authorization, and audit logging

## Connections

- Parent: [[key-management]] — key escrow is a key management strategy for key recovery
- See also: [[key-splitting-secret-sharing]]
