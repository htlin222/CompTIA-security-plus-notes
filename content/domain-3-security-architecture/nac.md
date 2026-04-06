---
title: "NAC"
description: "Network Access Control restricts network access to devices and users that meet security policy requirements."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/medium
aliases:
  - "NAC"
---

> [!eli5] ELI5: What is NAC?
> It's like a health check before you enter a theme park. Before you get on the rides, someone checks your ticket and makes sure you are tall enough. NAC (Network Access Control) does the same for devices joining a network -- it checks that your computer has the right updates and security software before letting you in. If your device does not pass the check, it gets sent to a waiting area until it is fixed.

## Overview

Network Access Control (NAC) is a security solution that enforces policies on devices attempting to access the network. NAC verifies that endpoints meet security requirements (patching, antivirus, configuration) before granting access. Non-compliant devices can be quarantined, given limited access, or blocked entirely. NAC is critical for managing BYOD environments and IoT devices.

## Key Concepts

- **Pre-admission vs. post-admission:**
  - **Pre-admission** — checks device compliance before allowing network access
  - **Post-admission** — monitors device behavior after access is granted and can revoke access if policy violations are detected
- **Agent-based vs. agentless:**
  - **Agent-based** — software installed on the endpoint performs health checks (persistent or dissolvable agent)
  - **Agentless** — NAC scans the device remotely; less intrusive but less thorough
- **Health checks (posture assessment):**
  - Antivirus up to date
  - OS patches applied
  - Firewall enabled
  - Disk encryption active
  - No prohibited software installed
- **[[8021x|802.1X]]** — IEEE standard for port-based network access control; uses EAP for authentication
  - **Supplicant** — the client device requesting access
  - **Authenticator** — the switch or access point enforcing policy
  - **Authentication server** — RADIUS server that validates credentials
- **[[remediation-network|Remediation network]]** — quarantine VLAN where non-compliant devices are placed to receive updates
- **[[guest-networking|Guest networking]]** — NAC can direct unknown or personal devices to an isolated guest network
- **EAP variants** — EAP-TLS (mutual certificate auth, most secure), PEAP (server certificate + password), EAP-FAST (Cisco, uses PAC), EAP-TTLS (server cert, flexible inner auth)
- **WPA3-Enterprise** — uses 192-bit security mode with EAP-TLS for enterprise wireless NAC

## Exam Tips

> [!tip] Remember
> 802.1X has three components: supplicant (client), authenticator (switch/AP), authentication server (RADIUS). NAC quarantines non-compliant devices rather than outright blocking them, allowing remediation. Agent-based is more thorough than agentless.

## Connections

- Enforces access to segments created by [[network-segmentation]] by controlling which devices enter each zone
- Uses [[firewalls]] and VLAN assignments to quarantine or restrict non-compliant devices
- See also [[network-security-architecture]] for how NAC fits into a zero trust model

## Practice Questions

> [!qbank]- Q-Bank: NAC (4 Questions)
>
> **Q1.** A company implements 802.1X for network access control. A laptop attempts to connect to a switch port. Which component sends the authentication credentials to the RADIUS server?
>
> A. The authentication server
> B. The authenticator (switch)
> C. The supplicant (client)
> D. The DHCP server
>
> > [!answer]- Show Answer
> > **C. The supplicant (client)**
> >
> > In the [[8021x|802.1X]] framework, the supplicant is the client device that provides credentials for authentication. The authenticator/switch (B) relays the credentials but does not originate them. The authentication server/RADIUS (A) validates the credentials but does not send them. The DHCP server (D) assigns IP addresses after authentication and is not part of the 802.1X process.
>
> **Q2.** An employee connects a personal laptop to the corporate network. The NAC system detects that the laptop's antivirus definitions are outdated and its OS is missing critical patches. What should the NAC system do MOST appropriately?
>
> A. Allow full network access and notify the employee to update later
> B. Permanently block the device from all network access
> C. Place the device on a remediation VLAN to receive updates
> D. Disable the network port and require a help desk visit
>
> > [!answer]- Show Answer
> > **C. Place the device on a remediation VLAN to receive updates**
> >
> > A [[remediation-network|remediation VLAN]] quarantines non-compliant devices while providing access to update resources, allowing the device to become compliant. Full access (A) exposes the network to risk from the unpatched device. Permanent blocking (B) is too restrictive when remediation is possible. Disabling the port (D) is unnecessarily disruptive and does not facilitate automatic remediation.
>
> **Q3.** A healthcare organization needs NAC that can assess the security posture of unmanaged contractor devices without installing software. Which NAC approach is MOST appropriate?
>
> A. Agent-based with a persistent agent
> B. Agentless NAC
> C. 802.1X with EAP-TLS
> D. Agent-based with a dissolvable agent
>
> > [!answer]- Show Answer
> > **B. Agentless NAC**
> >
> > [[nac|Agentless NAC]] scans devices remotely without requiring software installation, making it ideal for unmanaged contractor devices where installing agents is impractical. A persistent agent (A) requires permanent software installation on each device. 802.1X with EAP-TLS (C) requires client certificates, which unmanaged devices likely do not have. A dissolvable agent (D) still requires temporary software installation, which may not be permitted on contractor devices.
>
> **Q4.** A NAC system performs a health check before allowing a device onto the network and then continuously monitors the device's compliance status after connection. Which two NAC functions does this represent?
>
> A. Agent-based and agentless assessment
> B. Pre-admission and post-admission control
> C. Physical and logical segmentation
> D. Signature-based and anomaly-based detection
>
> > [!answer]- Show Answer
> > **B. Pre-admission and post-admission control**
> >
> > [[nac|Pre-admission control]] checks device compliance before granting access, while post-admission control monitors compliance after the device is connected and can revoke access if violations occur. Agent-based vs. agentless (A) describes assessment methods, not timing. Physical vs. logical segmentation (C) describes network architecture. Signature vs. anomaly detection (D) applies to IDS/IPS, not NAC.

## Scenario

> See [[case-nac]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [3.2 – Network Appliances](https://www.youtube.com/watch?v=WlOslEy3ztg)
