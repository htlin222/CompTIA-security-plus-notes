---
title: "VPN concentrator"
description: "dedicated device that terminates large numbers of VPN tunnels, centralizing remote access management"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is a VPN concentrator?
> If a VPN is a secret tunnel, a VPN concentrator is the big tunnel station where hundreds of tunnels all meet in one place. It is a dedicated machine built to handle lots of secure connections at the same time.

## Definition

A VPN concentrator is a dedicated network device designed to terminate and manage large numbers of simultaneous VPN connections. Unlike a general-purpose router or firewall that may support VPN as one of many functions, a VPN concentrator is purpose-built for high-throughput VPN termination, providing centralized authentication, encryption, and access policy enforcement for remote users connecting to a corporate network.

## Key Details

- Supports site-to-site and remote-access VPN termination at scale
- Performs encryption/decryption offloading, preserving performance on other network devices
- Integrates with RADIUS, LDAP, or Active Directory for user authentication
- Supports protocols including IPSec, SSL/TLS (SSL VPN), L2TP, and OpenVPN
- Always-on VPN solutions often use concentrators as the central termination point

## Connections

- Parent: [[vpn]] — the VPN concentrator is the infrastructure component that enables scalable VPN deployments
- See also: [[always-on-vpn]], [[ssltls-offloading]]
