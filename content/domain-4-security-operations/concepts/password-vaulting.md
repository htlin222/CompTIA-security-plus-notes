---
title: "Password vaulting"
description: "Storing privileged credentials in an encrypted vault; users check out passwords for time-limited sessions"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
---

## Definition

Password vaulting is a PAM control in which privileged account credentials are stored in a centralized, encrypted vault rather than being known to administrators or stored in scripts. Administrators access systems by checking out credentials from the vault for time-limited sessions, and the vault automatically rotates the credentials after each use, ensuring that no user retains persistent knowledge of privileged passwords.

## Key Details

- Credentials are stored encrypted in the vault — administrators may never see the actual password
- Check-out process: administrator requests access → vault provides temporary credential → session is recorded → vault rotates credential after session ends
- Eliminates shared accounts and passwords stored in scripts, spreadsheets, or post-it notes
- All access is audited: who checked out which credential, when, and for how long
- Major vendors: CyberArk, BeyondTrust, Delinea (formerly Thycotic), HashiCorp Vault

## Connections

- Parent: [[privileged-access-management]] — password vaulting is a core PAM control
- See also: [[credential-rotation]]
