---
title: "Case: The Container Image Vulnerability Spiral — 73% of Production Images Have Critical CVEs"
description: "A container image vulnerability scan reveals that 73% of production Docker images in the Kubernetes cluster contain critical CVEs, including a known cryptominer payload. The platform team insists that rebuilding will break the CI/CD pipeline. Six months of technical debt has accumulated."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

TechScale is a SaaS platform running 340 microservices in a Kubernetes cluster across AWS. The platform team adopted Docker containers four years ago to enable fast deployment and scaling. Services are built, containerized, and deployed multiple times per day via a CI/CD pipeline.

In March 2024, the security team decided to conduct a comprehensive container image vulnerability scan using Trivy, an open-source container image vulnerability scanner. The results were shocking:

- **Total images in production**: 340 microservices, with an average of 1.2 images per service = ~408 unique images
- **Images with high-severity CVEs**: 298 images (73%)
- **Images with critical-severity CVEs**: 127 images (31%)
- **Common vulnerabilities**: OpenSSL 1.0.2 (deprecated since 2019), curl with DNS rebinding vulnerabilities, Apache with Heartbleed
- **Malware found**: One image (legacy payment processor) contained a known cryptominer binary (Monero miner) that had been baked into the image

The cryptominer was the most concerning. Someone—possibly a third-party developer, possibly an attacker—had added a miner to the image six months ago. It had been running in production for six months, consuming approximately 3.2% of cluster CPU capacity (translating to ~$180/month in AWS compute cost) and mining cryptocurrency for an unknown party.

Chief Information Security Officer Dr. Lisa Park scheduled an emergency meeting with the VP of Platform Engineering, Marcus Lee. The conversation was tense.

Marcus: "We can't rebuild all 340 images. It'll break our CI/CD pipeline. Some of these Dockerfiles are based on old base images that don't exist anymore. Some services are maintained by teams that have left the company. Some are using unpublished private base images."

Dr. Park: "We have critical vulnerabilities in production. One of them is actively mining cryptocurrency. This is unacceptable."

Marcus: "It's not like we can do this overnight. Rebuilding 340 images might take months of engineering work. We need to prioritize."

What emerged from this discussion was a reality many container platforms face: **technical debt**. Over four years of rapid development, the team had accumulated hundreds of images built on outdated base images. Nobody had invested in container image maintenance—no updates to base images, no vulnerability scanning, no systematic patching.

The team analyzed the problem:

**Root Causes:**

1. **Old base images never updated**: Many services used base images from 2018-2019 (e.g., `ubuntu:18.04`, `node:10-alpine`) that were severely out of date. The original developers had left, and nobody maintained them.

2. **Multipart builds not cleaned**: Docker multistage builds often left intermediate layers with dev tools, source code, and build artifacts. Some images were 2GB because of bloat.

3. **No image scanning in CI/CD**: The CI/CD pipeline never scanned images for vulnerabilities. An image could be built with dozens of CVEs and still be deployed.

4. **Base images not maintained**: The team had private base images (with company-specific tools and libraries) that were built once and never updated. When new security patches were released, the private base images never incorporated them.

5. **No image promotion or staging**: Images went directly from build to production with no security scanning, no testing environment, no staged rollout.

6. **Cryptominer not detected**: An obvious malicious binary somehow made it into an image and stayed there for six months. No file integrity checking, no antivirus scanning, no admission controls.

**Remediation Plan:**

The team executed a multi-phased approach:

**Phase 1: Immediate Containment (Week 1)**
- Removed the cryptominer from the compromised image
- Rebuilt just that service and redeployed it
- Stopped the cryptocurrency mining immediately

**Phase 2: Priority Vulnerability Patching (Weeks 2-4)**
- Identified the 127 critical-severity CVEs
- Grouped them by base image (e.g., all OpenSSL vulnerabilities, all curl issues)
- For each group, created an updated base image with patched versions
- Rebuilt all services using those base images
- Tested and deployed the updated images

**Phase 3: Medium Vulnerability Patching (Weeks 5-8)**
- Addressed 171 medium-severity CVEs
- Similar approach: update base images, rebuild services

**Phase 4: Vulnerability Scanning in CI/CD (Weeks 2-12, parallel)**
- Integrated Trivy vulnerability scanning into the CI/CD pipeline
- Set a threshold: images with critical CVEs cannot be deployed
- Images with high CVEs get a warning but can be deployed if explicitly approved

**Phase 5: Image Maintenance Program (Ongoing)**
- Established a monthly schedule to update base images
- Created a process where all services that use a base image automatically get notified when it's updated
- Set up a quarterly image review: assess what's in production, scan for drift

**Phase 6: Admission Control and Policy Enforcement (Weeks 8-12)**
- Deployed an admission webhook in Kubernetes that inspects all pod deployments
- Policy: pods cannot be created from images with critical vulnerabilities
- This prevents accidental deployment of vulnerable images

**Phase 7: Malware Detection** (Week 1-12, parallel)
- Integrated file integrity checking (using ClamAV and YARA rules) into image scanning
- Scanned all existing images for known malware
- Added malware scanning to the CI/CD pipeline so malicious binaries can't be added in the future

The remediation took 12 weeks (much longer than initial estimates because some services had complex dependencies). By the end:

- **0 critical vulnerabilities** in production
- **14 high-severity vulnerabilities** remaining (dependencies that couldn't be updated without breaking compatibility)
- **127 medium-severity vulnerabilities** remaining (acceptable risk after approval)
- **Cryptominer removed** from all images and infrastructure checked for persistence

## What Went Right

- **Vulnerability scan happened**: A proactive security initiative discovered the problem before an attacker found it.
- **Phased remediation prevented massive disruption**: Rather than rebuilding all 340 images at once, the team prioritized critical issues.
- **CI/CD scanning prevented new vulnerabilities**: Once image scanning was integrated into the pipeline, new vulnerable images couldn't be deployed.
- **Admission control enforced policy**: Even if a vulnerable image somehow made it through the pipeline, the Kubernetes admission webhook would block it.
- **Cryptominer was detected and removed**: The team identified and removed active malicious code rather than discovering it through a breach.

## What Could Go Wrong

- **If vulnerability scanning had never happened**: The cryptominer would still be running, still costing money, still possibly exfiltrating data.
- **If admission control wasn't implemented**: A future developer could accidentally deploy a vulnerable image and breach the security policy.
- **If image scanning in CI/CD wasn't integrated**: New images with vulnerabilities would keep being built and deployed.
- **If the remediation took 12 months instead of 12 weeks**: More critical vulnerabilities might have been exploited.
- **If no maintenance plan was established**: The vulnerability debt would accumulate again within a year.

## Key Takeaways

- **Container images are code and need lifecycle management**: Don't build an image once and forget it. Plan for updates, patches, and maintenance as part of the software lifecycle.
- **Base image updates cascade to all dependent images**: Use immutable base image tags (e.g., `ubuntu:22.04-lts` not `ubuntu:latest`) so you control when dependent images are rebuilt.
- **Scanning must happen in CI/CD, not in production**: Vulnerable images should never make it to production. Fail the build if critical vulnerabilities are detected.
- **Admission control provides a safety net**: Even if an image slips through scanning, an admission webhook can prevent deployment.
- **Vulnerability debt is like technical debt**: It accumulates silently. Six months of unchecked vulnerabilities is normal without systematic scanning and updating.
- **Multistage Docker builds reduce image size**: Use `FROM scratch` or minimal base images and copy only necessary artifacts from builder stages.
- **Private base images must be maintained**: If you have company-specific base images (with libraries, tools, or configurations), they need the same security updates as public base images.
- **Malware detection requires file integrity checking**: Include ClamAV, YARA rules, or other antivirus scanning in your image analysis, not just CVE scanning.

## Related Cases

- [[case-cloud-security]] — Container security as part of cloud infrastructure security
- [[case-infrastructure-as-code]] — Dockerfile as IaC that needs policy enforcement
- [[case-hardening]] — Principles of securing base images and removing unnecessary components

