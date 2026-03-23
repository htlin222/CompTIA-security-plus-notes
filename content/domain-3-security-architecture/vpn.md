---
title: "VPN"
description: "Virtual Private Networks create encrypted tunnels over public networks to provide secure remote access and site-to-site connectivity."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/high
aliases:
  - "VPN"
---

> [!eli5] ELI5: What is VPN?
> It's like having a secret underground tunnel between your house and your friend's house. Even though cars drive on the regular roads above, your tunnel is hidden and only you two can use it. A VPN creates a private, secret tunnel through the regular internet so that nobody can spy on the information you are sending back and forth. Everything inside the tunnel is scrambled so even if someone found it, they could not read it.

## Overview

A Virtual Private Network (VPN) extends a private network across a public network by creating an encrypted tunnel between endpoints. VPNs provide confidentiality, integrity, and authentication for data in transit. They are used for remote worker access, site-to-site connectivity between offices, and securing communications over untrusted networks.

## Key Concepts

- **VPN types:**
  - **Remote access VPN** — connects individual users to the corporate network (client-to-site)
  - **Site-to-site VPN** — connects entire networks together (office-to-office)
  - **Full tunnel** — all traffic routed through the VPN; more secure
  - **Split tunnel** — only corporate-destined traffic goes through VPN; less secure but better performance
- **VPN protocols:**
  - **IPSec** — operates at Layer 3; uses AH (integrity) and ESP (encryption + integrity); supports tunnel and transport mode
  - **IKE (Internet Key Exchange)** — negotiates IPSec security associations; IKEv2 is current
  - **SSL/TLS VPN** — operates at Layer 4-7; uses HTTPS (port 443); easier through firewalls; browser-based or client
  - **WireGuard** — modern, lightweight VPN protocol with strong cryptography
- **[[always-on-vpn|Always-on VPN]]** — automatically connects when the device is powered on; ensures consistent policy enforcement
- **[[vpn-concentrator|VPN concentrator]]** — dedicated device that terminates multiple VPN connections
- **[[authentication|Authentication]]** — typically uses certificates, MFA, RADIUS, or LDAP for VPN user authentication
- **Tunnel mode vs. transport mode (IPSec):**
  - **Tunnel mode** — encrypts entire original packet including headers; used for site-to-site
  - **Transport mode** — encrypts only the payload; used for host-to-host

## Exam Tips

> [!tip] Remember
> IPSec = Layer 3, uses ESP for encryption. SSL/TLS VPN = Layer 4+, uses port 443, firewall-friendly. Full tunnel = all traffic secured. Split tunnel = only corporate traffic secured. Always-on VPN ensures policy compliance.

## Connections

- Relies on [[encryption]] protocols (IPSec, TLS) to protect data in transit
- Part of the broader [[network-security-architecture]] as a remote access component
- See also [[network-segmentation]] for controlling what VPN users can access once connected

## Scenario

> See [[case-vpn]] for a practical DevOps scenario applying these concepts.
