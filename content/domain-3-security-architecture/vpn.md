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

## Practice Questions

> [!qbank]- Q-Bank: VPN (4 Questions)
>
> **Q1.** A remote employee needs to connect to the corporate network from a hotel that blocks most outbound ports except 80 and 443. Which VPN protocol is MOST likely to work in this situation?
>
> A. IPSec in tunnel mode
> B. SSL/TLS VPN using port 443
> C. L2TP without IPSec
> D. PPTP
>
> > [!answer]- Show Answer
> > **B. SSL/TLS VPN using port 443**
> >
> > [[vpn|SSL/TLS VPNs]] operate over HTTPS (port 443), which is typically allowed through restrictive firewalls and hotel networks. IPSec (A) uses protocols and ports (UDP 500, ESP protocol 50) that are commonly blocked by restrictive firewalls. L2TP without IPSec (C) provides no encryption. PPTP (D) uses port 1723 and GRE protocol, which are commonly blocked and the protocol itself is considered insecure.
>
> **Q2.** A company configures its VPN so that only traffic destined for corporate resources goes through the VPN tunnel, while personal browsing goes directly to the internet. Which VPN configuration is this?
>
> A. Full tunnel
> B. Split tunnel
> C. Always-on VPN
> D. Site-to-site VPN
>
> > [!answer]- Show Answer
> > **B. Split tunnel**
> >
> > [[vpn|Split tunnel]] routes only corporate-destined traffic through the VPN while allowing other traffic to go directly to the internet. Full tunnel (A) routes all traffic through the VPN regardless of destination. Always-on VPN (C) describes automatic connection behavior, not routing policy. Site-to-site VPN (D) connects entire networks together, not individual user routing decisions.
>
> **Q3.** An organization connects two office locations using an IPSec VPN. The entire original IP packet, including headers, is encrypted and encapsulated. Which IPSec mode is being used?
>
> A. Transport mode
> B. Tunnel mode
> C. Aggressive mode
> D. Main mode
>
> > [!answer]- Show Answer
> > **B. Tunnel mode**
> >
> > [[vpn|IPSec tunnel mode]] encrypts the entire original packet including headers and adds new outer headers, which is the standard mode for site-to-site VPNs. Transport mode (A) only encrypts the payload, leaving original headers intact, and is used for host-to-host communication. Aggressive mode (C) and main mode (D) are IKE negotiation phases, not IPSec encapsulation modes.
>
> **Q4.** A security policy requires that all company laptops automatically establish a VPN connection whenever they are powered on, ensuring continuous policy enforcement. Which VPN feature satisfies this requirement?
>
> A. Split tunnel configuration
> B. SSL/TLS VPN with browser-based access
> C. Always-on VPN
> D. VPN concentrator with load balancing
>
> > [!answer]- Show Answer
> > **C. Always-on VPN**
> >
> > [[always-on-vpn|Always-on VPN]] automatically establishes a VPN connection when the device powers on, ensuring that corporate security policies are continuously enforced. Split tunnel (A) is a routing configuration, not an automatic connection feature. Browser-based SSL/TLS VPN (B) requires manual user action to connect. A VPN concentrator (D) terminates VPN connections but does not control whether clients connect automatically.

## Scenario

> See [[case-vpn]] for a practical DevOps scenario applying these concepts.
