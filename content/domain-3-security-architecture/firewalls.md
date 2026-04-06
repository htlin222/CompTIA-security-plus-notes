---
title: "Firewalls"
description: "Firewalls filter network traffic based on rules to enforce security boundaries between trusted and untrusted networks."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/high
aliases:
  - "Firewalls"
---

> [!eli5] ELI5: What are Firewalls?
> A firewall is like a bouncer at the door of a club. It checks everyone trying to come in or go out and only lets through the people who are on the list. If someone suspicious shows up, the bouncer turns them away. On a computer network, a firewall checks all the data trying to enter or leave and blocks anything that looks dangerous or breaks the rules.
>
> > [!eli5] ELI5: Firewalls (繁體中文版)
> > 防火牆就像是公司的警衛，它會檢查所有進出的包裹，只允許符合安全規則的包裹通過，把可疑的擋在門外。
> >
> > ```ascii
> > [外部網路] --|防火牆|--> [內部網路]
> > ```

## Overview

A firewall is a network security device or software that monitors and controls incoming and outgoing traffic based on predetermined security rules. Firewalls establish a barrier between trusted internal networks and untrusted external networks. They are the most fundamental network security control and are deployed at network perimeters, between zones, and on individual hosts.

## Key Concepts

- **Firewall types:**
  - **Packet filtering** — inspects headers (source/dest IP, port, protocol); stateless; fast but limited
  - **Stateful inspection** — tracks connection state; allows return traffic for established sessions
  - **Application layer / proxy** — inspects payload content; understands protocols (HTTP, FTP); slower but thorough
  - **Next-Generation Firewall (NGFW)** — combines stateful inspection, deep packet inspection, IPS, and application awareness
  - **Web Application Firewall (WAF)** — specifically protects web applications against attacks like SQLi and XSS
- **[[host-based-vs-network-based|Host-based vs. network-based]]** — host firewalls protect individual systems; network firewalls protect entire segments
- **[[unified-threat-management-utm|Unified Threat Management (UTM)]]** — all-in-one appliance combining firewall, IDS/IPS, antivirus, content filtering, VPN
- **Rule configuration:**
  - Rules processed top-down; first match wins
  - Implicit deny at the bottom (block everything not explicitly allowed)
  - Principle of least privilege in rule design
- **[[access-control-lists-acls|Access Control Lists (ACLs)]]** — ordered lists of permit/deny rules based on traffic attributes
- **[[screened-subnet-dmz|Screened subnet (DMZ)]]** — uses firewalls to create a buffer zone for public-facing services

## Exam Tips

> [!tip] Remember
> NGFW = stateful + DPI + IPS + app awareness. WAF = web apps specifically (Layer 7). Implicit deny = the last rule blocks everything else. Rules are processed top to bottom; order matters.

## Connections

- Core component of [[network-security-architecture]] providing boundary enforcement
- Works alongside [[ids-ips]] which detects and prevents threats that pass through firewall rules
- See also [[network-segmentation]] for how firewalls enforce zone boundaries within the network

## Practice Questions

> [!qbank]- Q-Bank: Firewalls (4 Questions)
>
> **Q1.** A company needs a firewall that can inspect encrypted web traffic, identify applications regardless of port, and block intrusions. Which firewall type BEST meets these requirements?
>
> A. Packet filtering firewall
> B. Stateful inspection firewall
> C. Next-Generation Firewall (NGFW)
> D. Web Application Firewall (WAF)
>
> > [!answer]- Show Answer
> > **C. Next-Generation Firewall (NGFW)**
> >
> > An [[firewalls|NGFW]] combines stateful inspection, deep packet inspection, IPS capabilities, and application awareness, meeting all the stated requirements. A packet filtering firewall (A) only inspects headers and cannot identify applications. A stateful firewall (B) tracks connections but lacks application awareness and IPS. A WAF (D) is specifically designed for web application attacks (SQLi, XSS) and does not provide the full range of capabilities described.
>
> **Q2.** A network administrator creates firewall rules but forgets to add a rule for a new service. Users report they cannot access the service. Which firewall principle explains this behavior?
>
> A. Stateful inspection
> B. Implicit deny
> C. Deep packet inspection
> D. NAT traversal
>
> > [!answer]- Show Answer
> > **B. Implicit deny**
> >
> > [[firewalls|Implicit deny]] is the default rule at the bottom of every firewall rule set — any traffic not explicitly permitted is blocked. Stateful inspection (A) tracks connection states but does not explain the default blocking behavior. Deep packet inspection (C) examines packet payloads but does not block unmatched traffic by default. NAT traversal (D) relates to routing traffic through NAT devices, not default deny behavior.
>
> **Q3.** A web application is experiencing SQL injection attacks despite having a network firewall in place. Which additional firewall should be deployed to address this specific threat?
>
> A. A second packet filtering firewall
> B. A stateful inspection firewall
> C. A Web Application Firewall (WAF)
> D. A host-based firewall on each client
>
> > [!answer]- Show Answer
> > **C. A Web Application Firewall (WAF)**
> >
> > A [[firewalls|WAF]] operates at Layer 7 and specifically protects web applications against attacks like SQL injection and XSS by inspecting HTTP/HTTPS traffic content. A second packet filtering firewall (A) cannot inspect application-layer payloads. A stateful firewall (B) tracks connections but does not analyze web application content. Host-based firewalls on clients (D) protect individual endpoints, not the web application server from injection attacks.
>
> **Q4.** A firewall administrator places a more specific permit rule below a broader deny rule in the rule set. Traffic matching the specific rule is still being blocked. What is the MOST likely cause?
>
> A. The firewall requires a reboot to apply new rules
> B. Firewall rules are processed top-down, and the deny rule matches first
> C. The permit rule uses the wrong encryption protocol
> D. The firewall has exceeded its maximum rule capacity
>
> > [!answer]- Show Answer
> > **B. Firewall rules are processed top-down, and the deny rule matches first**
> >
> > [[firewalls|Firewall rules]] are processed in order from top to bottom, and the first matching rule is applied. Since the broader deny rule is above the permit rule, it matches first and blocks the traffic. Firewalls typically apply rules immediately without rebooting (A). Encryption protocol (C) is unrelated to rule ordering. Rule capacity limits (D) would prevent adding rules, not cause incorrect matching.

## Scenario

> See [[case-firewalls]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [3.2 – Firewall Types](https://www.youtube.com/watch?v=mq1HRM-zGtQ)
