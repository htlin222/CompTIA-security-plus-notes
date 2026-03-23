---
title: "Case: The Kubernetes Plaintext Discovery — Encrypting 247 Microservices"
description: "A SOC 2 compliance review discovers that internal microservices communicate over unencrypted gRPC within the Kubernetes cluster. While traffic never leaves the network, regulators require encryption in transit everywhere. The team must generate, rotate, and manage certificates for 200+ services."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

TelemetryShift is a San Francisco-based SaaS platform that streams customer behavioral data in real time for analytics. The backend runs on Kubernetes with 247 microservices that process terabytes of telemetry daily. In September 2024, a SOC 2 Type II auditor arrived to conduct the annual compliance review. During the third day, she asked a routine question: "Show me your encryption in transit configuration for all service-to-service communication."

Platform Lead Kenji Tanaka walked her through the architecture. Services communicated via gRPC (Google's RPC framework) over HTTP/2. Every service discovery lookup went through an internal Consul cluster. Database connections to PostgreSQL used SSL/TLS. External API calls used HTTPS. Everything that left the Kubernetes cluster was encrypted.

But everything internal was plaintext.

The auditor raised her eyebrows. "You're claiming SOC 2 compliance, but you're transmitting unencrypted application data between your microservices?"

Kenji's response was: "The traffic never leaves the cluster. It's all on a private network."

The auditor explained the problem: SOC 2 Type II requires that "systems protect information in transit." This doesn't mean "only in transit across the internet." It means data in motion, regardless of whether that motion is internal or external. She elaborated: if an attacker compromises a single pod in the Kubernetes cluster (via a container escape, a vulnerable service, or a node compromise), they could eavesdrop on all plaintext traffic between other services. They could steal API keys, database credentials, customer data, and authentication tokens flowing between services.

The audit finding was stark: **Material Weakness — Lack of Encryption in Transit for Internal Service Communication**. This required remediation before SOC 2 certification could be issued. The deadline: 90 days.

Kenji escalated to Chief Technology Officer Dr. Sarah Okonkwo. The scope was daunting: 247 microservices, 1,400 inter-service communication paths, zero previous TLS configuration for internal traffic. A naive approach would be to patch each service individually—manually generating certificates, distributing keys, configuring gRPC TLS, and rotating credentials. That would take six months and introduce massive operational risk.

Dr. Okonkwo proposed a different approach: use a **service mesh** architecture (specifically Istio, an open-source service mesh for Kubernetes). Istio would:

1. Automatically inject TLS proxies (Envoy) into every pod
2. Automatically generate and rotate certificates using a built-in certificate management system
3. Enforce mTLS (mutual TLS) between all services without code changes
4. Provide encryption policy definition and monitoring

On paper, this was perfect. In practice, the challenges were:

**Challenge 1: [[Key-length]] and [[encryption-modes]] selection** (Week 1-2):
- What [[key-length]] for internal mTLS? The team needed to balance security with performance.
- What [[encryption-modes]]? AES-GCM was the standard, but older services might not support all [[cipher-suite]] options.
- What [[cryptographic-attacks]] needed to be mitigated? The team documented threat models for eavesdropping, man-in-the-middle attacks on internal traffic, and certificate compromise.

**Challenge 2: Certificate generation and rotation** (Week 2-4):
- Istio uses an on-cluster Certificate Authority (CA) to auto-generate certificates for every service
- But the CA private key needed to be protected. They decided to integrate Istio's CA with [[Hardware-Security-Module|HashiCorp Vault]] running in the cluster
- Certificate rotation would happen every 90 days automatically, but the team needed to test renewal procedures

**Challenge 3: Gradual rollout without breaking services** (Week 4-8):
- Enabling mTLS cluster-wide would break every service immediately if any service didn't support the new [[encryption-modes]]
- The team created a [[namespace]]-by-[[namespace]] rollout: enable Istio in one [[namespace]], validate it for one week, then move to the next
- They discovered three legacy services that didn't support the required [[cipher-suite]]. Those services were upgraded in parallel

**Challenge 4: Observability and monitoring** (Week 8-12):
- With [[encryption-modes|encrypted]] traffic, traditional packet inspection became impossible
- Istio provides metrics on encrypted connections, but the team needed to ensure no legitimate traffic was being dropped by overly aggressive TLS policies
- They instrumented application-level metrics to confirm [[hybrid-encryption]] was functioning

By week 12, all 247 services had mTLS enabled. The audit revisited and confirmed: all inter-service traffic was now encrypted using TLS 1.3 with AES-GCM-256. The [[key-length]] was 256-bit with 90-day automatic rotation. Certificate management was automated and auditable.

The audit passed.

But the story doesn't end there. Six months into operation, the team discovered a new challenge: **[[Perfect-forward-secrecy|Perfect Forward Secrecy (PFS)]]. **

A vendor pointed out that while their certificates rotated every 90 days, if a certificate private key was ever compromised, all traffic encrypted with that key could potentially be decrypted retroactively. Some internal data (customer session tokens, personally identifiable information cached in transient services) should have perfect forward secrecy—even if a key is compromised, traffic from the past cannot be decrypted.

The team evaluated [[ephemeral-keys]]. Istio's TLS implementation already used ephemeral session keys via [[PFS]]-enabled cipher suites (ECDHE), so short-term [[cryptographic-attacks]] actually already had [[Perfect-forward-secrecy]]. But longer-lived keys (service-to-service routing credentials) did not.

They eventually implemented a stricter [[key-management]] policy:
- Service certificates: 30-day rotation (reduced from 90)
- Session-level keys: TLS 1.3 with ECDHE (automatic [[Perfect-forward-secrecy]])
- Sensitive service credentials: Vault-managed with 7-day rotation for highest-privilege services

## What Went Right

- **Compliance review caught the gap before an actual breach**: The auditor's questions led to discovery before attackers could exploit the plaintext traffic.
- **Service mesh approach scaled to 247 services**: Rather than patching each service individually, Istio provided infrastructure-level encryption without code changes.
- **Certificate lifecycle was automated**: With automatic rotation and CA management, the team didn't have to manually manage certificates for 247 services.
- **Phased rollout prevented outages**: Deploying [[namespace]] by [[namespace]] allowed validation and issue discovery before full activation.
- **Monitoring remained effective**: Istio's metrics and logging allowed the team to confirm encryption was functioning without breaking observability.

## What Could Go Wrong

- **No encryption would have left the cluster vulnerable**: A pod compromise would allow eavesdropping on all plaintext microservice traffic.
- **Wrong [[encryption-modes]] could weaken security**: If the team had chosen a deprecated cipher suite or weak [[key-length]], the encryption would have provided false confidence.
- **Inadequate key rotation would hinder recovery from compromise**: The original Istio default was 365-day rotation. A leaked key could be valid for nearly a year.
- **All-or-nothing deployment would have broken services**: Enabling mTLS cluster-wide without testing would have caused an outage that would make the project fail.
- **No monitoring of encryption status would hide failures**: If TLS was silently falling back to plaintext due to configuration errors, the team wouldn't know.

## Key Takeaways

- **[[Encryption-modes]] selection is not optional for compliance**: SOC 2, PCI DSS, and HIPAA all require explicit encryption in transit. "It's internal" is not a valid exception.
- **[[Key-length]] and [[cipher-suite]] choices have operational implications**: 256-bit keys use more CPU than 128-bit keys. Some older hardware may not support ECDHE. Document and test these tradeoffs before production rollout.
- **Certificate lifecycle automation is essential at scale**: Managing certificates manually for 247 services is not feasible. Use a service mesh, a certificate manager, or a PKI system that auto-rotates credentials.
- **[[Perfect-forward-secrecy]] requires ephemeral keys**: Static certificates encrypted with AES don't provide PFS. Ensure your [[encryption-modes]] use ECDHE or similar for session-level security.
- **Gradual rollout is safer than big-bang**: Enable encryption one [[namespace]] or one service tier at a time, validate, and then expand. Full cluster encryption on day one will cause failures.
- **Monitoring encrypted traffic requires different tools**: Wireshark and packet analysis can't inspect [[encryption-modes|encrypted]] data. Use application-level metrics, service mesh observability, and certificate chain validation to verify encryption is functioning.

## Related Cases

- [[case-key-management]] — The infrastructure underlying certificate generation, rotation, and lifecycle
- [[case-vpn]] — Similar principles of protecting data in transit, but at the network layer instead of the application layer
- [[case-certificates]] — Understanding X.509 certificates and their role in TLS implementation

