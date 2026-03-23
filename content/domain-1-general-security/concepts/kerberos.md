---
title: "Kerberos"
description: "Ticket-based authentication protocol used in Active Directory environments; uses port 88"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Kerberos?
> It's like getting a wristband at a fair. You show your ID once at the front gate, they give you a wristband, and then you just flash the wristband at each ride instead of showing your ID every time.

## Definition

Kerberos is a network authentication protocol that uses symmetric key cryptography and a trusted third party—the Key Distribution Center (KDC)—to provide mutual authentication without transmitting passwords over the network. It issues time-limited tickets that prove identity to services, making it the foundation of Windows Active Directory authentication. Kerberos operates on port 88.

## Key Details

- **KDC (Key Distribution Center)**: Consists of the **Authentication Server (AS)** and **Ticket Granting Server (TGS)**—runs on Domain Controllers in Active Directory.
- **TGT (Ticket Granting Ticket)**: Issued after initial authentication—used to request service tickets without re-entering credentials.
- **Service Ticket (TGS)**: Issued for access to a specific service—encrypted with the service account's key.
- **Port 88**: Used by Kerberos; important for firewall rule configuration.
- Key attacks: **Kerberoasting** (service ticket cracking), **Pass-the-Ticket**, **Golden Ticket** (forged TGT using KRBTGT hash), **Silver Ticket** (forged service ticket).

## Connections

- Parent: [[aaa-framework]] — Kerberos implements authentication in the AAA framework
- See also: [[kerberoasting]], [[directory-services]]
