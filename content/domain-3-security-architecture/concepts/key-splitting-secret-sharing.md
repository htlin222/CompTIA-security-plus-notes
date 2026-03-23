---
title: "Key splitting / secret sharing"
description: "divide a key among multiple custodians; requires a threshold to reconstruct (Shamir's Secret Sharing)"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Key splitting / secret sharing?
> It's like tearing a treasure map into pieces and giving each piece to a different friend. No single friend can find the treasure alone -- they have to get together and combine their pieces to read the full map.

## Definition

Key splitting and secret sharing are cryptographic techniques that divide a secret (such as a cryptographic key) into multiple shares distributed among different custodians, such that the original secret can only be reconstructed when a minimum threshold number of shares are combined. This prevents any single person from having unilateral access to critical keys.

## Key Details

- **Shamir's Secret Sharing**: most common algorithm; divides a key into n shares, any k of which can reconstruct the key (k-of-n threshold scheme)
- Example: a root CA private key split into 5 shares, requiring any 3 to reconstruct (3-of-5 scheme)
- Provides M-of-N dual control: no single custodian can access the key alone
- Used for highly sensitive keys like CA root keys, master encryption keys, and disaster recovery keys
- HSMs often implement m-of-n control for key operations

## Connections

- Parent: [[key-management]] — key splitting is a critical control for protecting the most sensitive keys
- See also: [[key-escrow]]
