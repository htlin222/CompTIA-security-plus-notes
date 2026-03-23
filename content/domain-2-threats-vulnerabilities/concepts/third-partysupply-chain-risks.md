---
title: "Third-party/supply chain risks"
description: "Vulnerabilities in vendor software, libraries, or dependencies (e.g., Log4Shell)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

Third-party and supply chain risks arise from vulnerabilities in software, components, libraries, or services provided by external vendors and incorporated into an organization's technology stack. Because modern applications often depend on thousands of third-party libraries and components, a single vulnerability in a widely-used dependency can affect millions of systems simultaneously. Supply chain attacks target the build, distribution, or update mechanisms of trusted software.

## Key Details

- **Log4Shell (Log4j, 2021)**: Critical vulnerability in the widely-used Apache Log4j logging library—affected millions of applications globally; CVSS 10.0.
- **SolarWinds (2020)**: Sophisticated supply chain attack compromising the SolarWinds Orion build process—affected ~18,000 customers including US government agencies.
- **XZ Utils (2024)**: Malicious code introduced into a widely-used Linux compression library through a social engineering attack on the maintainer.
- Mitigation: **Software Bill of Materials (SBOM)**—inventory of all components and dependencies; **vulnerability scanning** of dependencies; **vendor risk management** programs.
- **NIST guidelines** and **Executive Order 14028** (US) require SBOM and supply chain security measures for government software vendors.

## Connections

- Parent: [[vulnerability-types]] — a systemic vulnerability from third-party dependencies
- See also: [[misconfigurations]]
