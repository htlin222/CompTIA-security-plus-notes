---
title: "Case: The Silent Sequence Exposure — Genomics Data on Public S3"
description: "An S3 bucket misconfiguration at a genomics startup leaves 3TB of patient DNA sequencing data world-readable for six days. AWS GuardDuty alerts to an unmonitored email alias while 487 unauthorized requests pull genetic profiles."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

Helix Biosciences is a genomics startup that sequences patient DNA samples for personalized medicine research. They store raw sequencing output—3 terabytes of files containing complete genetic profiles for 14,000 patients—in an S3 bucket named `helix-research-data-v2`. On a Tuesday during sprint planning, junior DevOps engineer Priya Desai was testing a temporary ETL pipeline to process genomic files. She needed to grant a Lambda function read-access to the bucket, and as a quick workaround, she modified the bucket ACL to `public-read` to "unblock testing." She planned to revert it "after lunch" but got pulled into a design review that ran three hours.

By Wednesday morning, AWS GuardDuty had detected the public S3 bucket and generated an alert—a finding marked as "Medium" severity in the security console. The alert was routed to a distribution list called `security-findings@helix-biosciences.com`. That email alias was created during the initial security setup 18 months ago and was supposed to go to the entire security team. However, when the company reorganized six months prior, the alias wasn't updated. It now delivered to a single security contractor who worked part-time and only checked email on Friday afternoons.

Over the next five days, the bucket was discovered and accessed by multiple attackers. Cloud threat intelligence would later show the IP addresses mapped to three different countries and at least two known credential trafficking operations. In total, 487 unauthorized HTTP GET requests pulled down genomic profiles—enough data to identify individuals, understand genetic predispositions, and construct highly targeted phishing campaigns based on disclosed medical information.

The exposure was eventually discovered on Monday morning, not by alerting systems, but because Priya's manager asked why the temporary S3 bucket was still public and why its CloudTrail logs showed unusual access patterns. The incident response team was assembled at 9:15 AM. What they found in the logs was grim:

- 487 GET requests from 23 unique public IP addresses between Wednesday 11 PM and Monday 8 AM
- At least 147 of the requests successfully returned 200 OK with full file contents
- CloudTrail showed no KMS decrypt operations, meaning the [[secrets-management]] keys were not being used—the raw genetic data was stored unencrypted
- The [[shared-responsibility-model]] documentation stated that AWS would handle infrastructure encryption, but the startup had never enabled server-side encryption at the bucket level
- Cross-account access logs were disabled in the [[multitenancy-risks]] protection strategy because the startup assumed single-tenant deployment

Chief Security Officer James Martinez ordered an immediate shutdown of the bucket, extraction of all CloudTrail logs for forensic analysis, and notification to all 14,000 affected patients and their physicians. The company's head of regulatory affairs reviewed the implications: this was a HIPAA violation (genetic information is protected health information), a GDPR violation (genetic data is sensitive biometric data in EU terms), and a state-level privacy law violation across California, New York, and Virginia where patients were located.

The forensic analysis took three weeks. During that time, two patients' genetic profiles were published on a dark web intelligence forum, and at least one group had cross-referenced the data against public genealogy databases and identified five individuals by name. The company spent $2.1 million on breach notification, credit monitoring, identity protection services, and legal settlements.

## What Went Right

- **GuardDuty was enabled**: Despite the alert routing failure, AWS was actively monitoring and caught the public exposure. Organizations without GuardDuty would have zero visibility.
- **CloudTrail logging was comprehensive**: The organization had not disabled logging in [[cloud-deployment-models]] configuration, so detailed access records existed for forensic investigation and breach scope assessment.
- **Immediate remediation**: Once discovered, the bucket was immediately made private, preventing further data leakage.
- **Incident response procedures existed**: Even though discovery was accidental, the company had documented incident response steps that allowed activation of legal, regulatory, and technical teams within 90 minutes.

## What Could Go Wrong

- **Email alias not maintained during organizational change**: The [[shared-responsibility-model]] between cloud provider and organization breaks down if alerts don't reach the right people. Distribution lists and escalation paths must be refreshed during every org restructure.
- **No encryption at rest**: The [[api-security]] and [[data-sovereignty]] would have limited the exposure if data had been encrypted with customer-managed keys. Default AWS encryption uses AWS-managed keys, which provides integrity checking but not confidentiality protection against AWS personnel or law enforcement.
- **ACL-based access control instead of IAM policies**: The [[cloud-deployment-models]] permissions model had degraded to bucket ACLs instead of fine-grained Identity and Access Management. ACLs are a legacy permission system that should be disabled in favor of [[identity-and-access-management]] policies.
- **No monitoring of configuration changes**: There was no alert when the bucket ACL changed from private to public. A configuration detection system (AWS Config) could have triggered automatic remediation.
- **Single [[multitenancy-risks]] layer**: The bucket was shared across multiple data types without isolation. A better [[cloud-deployment-models]] would have separate encryption keys, buckets, or even AWS accounts per customer.
- **No encryption key rotation schedule**: Had the encryption keys been rotated weekly with automatic expiration of old keys, the exposure window would have been limited to the most recent key generation.

## Key Takeaways

- **Email aliases and distribution lists are critical infrastructure**: They must be audited and validated during every organizational change. Failed alerts are silent breaches.
- **Default cloud settings are not secure enough**: [[cloud-deployment-models]] requires explicit security hardening: enable KMS encryption, enable versioning, enable access logging, enable CloudTrail, configure bucket policies to deny public access.
- **ACLs are legacy—use IAM for [[identity-and-access-management]]**: Bucket ACLs allow binary public/private decisions. IAM policies allow role-based, temporary, and context-aware access control that's actually auditable.
- **[[Shared-responsibility-model]] clarity is essential**: AWS protects the infrastructure; you protect the application, data, identity, and configuration. Document what each team owns, and test that documentation quarterly.
- **Temporary workarounds become permanent**: Priya's "unblock testing" ACL change was never reverted because nobody had a system to detect configuration drift. Treat temporary security changes the same as you treat temporary code: they must have expiration times and escalation paths.
- **Breach scope assessment depends on logging**: If CloudTrail had been disabled to "reduce AWS bills," or if access logging had been turned off for "performance," the forensic team would have no way to answer: "How many records were actually accessed?"

## Related Cases

- [[case-serverless-and-containers]] — Container security shares similar patterns of default-insecure configurations
- [[case-data-protection]] — Deep dive into encryption strategies that could have prevented the exposure
- [[case-encryption]] — Understanding key management and customer-managed encryption in cloud environments
- [[case-virtualization-security]] — How resource isolation principles apply to cloud multi-tenancy

