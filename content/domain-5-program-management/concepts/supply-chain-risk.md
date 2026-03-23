---
title: "Supply chain risk"
description: "compromised hardware, software, or services introduced through the supply chain (e.g., SolarWinds)"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What is Supply Chain Risk?
> What if someone snuck a rotten ingredient into the factory that makes your favorite cereal? Supply chain risk is the danger that a product or software could be tampered with before it even reaches you, like the SolarWinds attack where bad code was hidden inside a trusted update.

## Definition

Supply chain risk is the risk that malicious actors, hardware tampering, counterfeit components, or compromised software can be introduced into an organization's environment through the supply chain — before the product or service reaches the organization. The SolarWinds attack (2020) is the defining example: attackers compromised the build environment of a legitimate software vendor, inserting malware into signed software updates distributed to thousands of customers. Supply chain attacks are particularly dangerous because they bypass traditional perimeter defenses.

## Key Details

- **Software supply chain**: compromised build pipelines, malicious open-source packages, backdoored software updates (SolarWinds, NotPetya-style attacks)
- **Hardware supply chain**: counterfeit or tampered components (chips, network hardware) introduced during manufacturing or shipping
- **Service supply chain**: compromised managed service providers (MSPs) used as pivot points to attack their customers
- Mitigations: software bill of materials (SBOM), code signing verification, vendor security assessments, NIST SP 800-161 (supply chain risk management)
- Exam tip: supply chain risk is explicitly tested on Security+; know SolarWinds as the canonical example and SBOM as a mitigation tool

## Connections

- Parent: [[third-party-risk]] — supply chain risk is the most complex form of third-party risk
- See also: [[fourth-party-risk]]
- See also: [[vendor-assessment]]
