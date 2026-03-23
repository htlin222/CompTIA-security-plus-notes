---
title: "TAXII (Trusted Automated eXchange of Intelligence Information)"
description: "Protocol for exchanging STIX data"
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/sub-topic
aliases:
  - TAXII
---

> [!eli5] ELI5: What is TAXII?
> TAXII is the delivery truck that carries threat information between organizations. While STIX is the language, TAXII is how that information actually gets sent from point A to point B.

## Definition

TAXII (Trusted Automated eXchange of Intelligence Information) is an application protocol for the automated exchange of STIX-formatted threat intelligence between organizations and systems. It defines the transport mechanisms and APIs by which STIX data can be published, subscribed to, and exchanged — enabling automated, machine-speed sharing of threat intelligence without manual intervention.

## Key Details

- TAXII 2.1 is the current version; uses HTTPS as the transport and REST API design
- Two main services: TAXII Collections (a repository) and TAXII Channels (a publish/subscribe model)
- Works together with STIX: STIX defines the threat intelligence FORMAT; TAXII defines how to SHARE it
- Organizations can run TAXII servers to share intelligence or subscribe to external TAXII feeds
- ISACs and threat intelligence platforms (TIPs) commonly use STIX/TAXII for automated intelligence sharing

## Connections

- Parent: [[threat-intelligence]] — TAXII is the transport protocol that makes automated threat intelligence sharing possible
- See also: [[stix-structured-threat-information-expression]]
