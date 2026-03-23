---
title: "DMZ (Demilitarized Zone)"
description: "screened subnet between the internet and internal network for public-facing services"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
aliases:
  - DMZ
---

> [!eli5] ELI5: What is a DMZ (Demilitarized Zone)?
> Think of it as a lobby in a building. Visitors can enter the lobby and talk to the receptionist, but they cannot go past the locked door into the offices. A DMZ is a network lobby where public services live, keeping the private network safely behind the locked door.

## Definition

A DMZ (Demilitarized Zone), also called a screened subnet, is a network segment that sits between the untrusted internet and the trusted internal network, hosting publicly accessible services (web servers, mail servers, DNS) while isolating them from the internal network. The DMZ provides a controlled buffer zone where public-facing systems can be accessed from the internet without directly exposing the internal network.

## Key Details

- Typically created using two firewalls: one between internet and DMZ, one between DMZ and internal network
- Systems in the DMZ should not be able to initiate connections to internal systems without going through the second firewall
- DMZ traffic: inbound internet → DMZ (allowed); DMZ → internal (restricted); internet → internal (blocked)
- Compromise of a DMZ server does not give direct access to internal systems
- Common DMZ services: web servers, email relays, reverse proxies, DNS servers, VPN concentrators

## Connections

- Parent: [[network-security-architecture]] — DMZ is a fundamental network security architecture element
- See also: [[screened-subnet-dmz]]
