---
title: "Case: The Subordinate CA Compromise — Emergency Certificate Revocation"
description: "A subordinate certificate authority's private key is compromised at a government agency, affecting 12,000 certificates used for employee smart card authentication and email signing. The root CA must issue a new intermediate CA by morning while maintaining access for 8,000 employees."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

The Department of Defense's Credential Processing Center operates a public key infrastructure (PKI) that issues digital certificates to 3.2 million federal employees and contractors. The system uses a three-level [[chain-of-trust]]:

1. **Root CA** — Offline, stored in an air-gapped facility, used only to sign intermediate CAs
2. **Intermediate CAs** — Four instances (one per agency region), online and used to issue employee certificates
3. **End-entity certificates** — Issued to individual employees, used for email signing and smart card authentication

On a Tuesday morning in October 2024, the backup operator for the Southeast Regional Intermediate CA discovered something alarming in the audit logs. Between October 1-6, the Intermediate CA had issued 47 certificates that nobody remembered requesting. The certificate subjects were:

- `cn=fake-director,ou=accounts,dc=dod,dc=gov`
- `cn=test-user-backdoor,ou=it,dc=dod,dc=gov`
- `cn=admin-override,ou=security,dc=dod,dc=gov`

These weren't legitimate employees. They were test accounts created by an attacker.

The backup operator escalated immediately. The Chief Information Security Officer for the agency, Dr. Margaret Chen, was notified at 8:47 AM. The implication was clear: the Intermediate CA's private key had been compromised. The attacker had access to the CA and could issue certificates for any user or service.

Margaret initiated emergency incident response procedures:

**Step 1: Confirm the Compromise (30 minutes)**
- Forensic team examined the Intermediate CA server's logs
- Found evidence of unauthorized access via a service account that had been compromised six months earlier (undetected until now)
- Confirmed that the attacker had created multiple test certificates over a six-day period
- Assessed risk: 12,000 legitimate certificates issued by this CA could potentially be revoked by the attacker, and 8,000 employees currently used certificates from this CA for daily authentication

**Step 2: Revocation and Containment (1 hour)**
- Immediately revoked the Intermediate CA certificate itself, invalidating all 12,000 certificates it had issued
- Took the compromised Intermediate CA server offline
- Reviewed the [[chain-of-trust]] — if the Intermediate CA was compromised, was the Root CA also at risk?

**Step 3: Root CA Activation (Parallel, 2 hours)**
- The Root CA lives offline in a vault at a secure facility in Arlington, Virginia
- Activation requires physical presence of three key custodians (out of five designated)
- Margaret authorized emergency activation and called the three custodians (one was on vacation, one was at home, one was in the office)
- The in-office custodian retrieved the other two within 45 minutes
- The three entered the vault, activated the offline [[hardware-security-module|HSM]] containing the Root CA private key, and verified its integrity

**Step 4: Issue New Intermediate CA (4 hours)**
- Using the awakened Root CA, the team generated a new certificate signing request (CSR) for a new Southeast Regional Intermediate CA
- The Root CA signed the CSR, creating a new Intermediate CA certificate
- The new Intermediate CA came online at 3:15 PM (6.5 hours after detection)
- Existing systems were redirected to the new CA for any new certificate requests

**Step 5: Massive Reissuance (24+ hours)**
- All 12,000 certificates issued by the compromised CA needed to be replaced
- The team couldn't simply issue new certificates to 8,000 employees—that would overload the new CA and cause delays
- Instead, they implemented a prioritized reissuance:
  - **Priority 1 (4 hours)**: 400 critical accounts (C-suite executives, security officers, system admins) - reissued new certificates
  - **Priority 2 (12 hours)**: 3,600 active daily users - issued new certificates as they logged in the next morning
  - **Priority 3 (48 hours)**: 4,000 less-active users - had new certificates issued gradually
  - **Priority 4 (72 hours)**: Inactive or archived accounts - certificates marked for eventual replacement

**Step 6: Public Notification (Parallel)**
- Notified affected employees that their certificates would be revoked and reissued
- Provided instructions on obtaining new certificates
- Set up a help desk with extended hours to support employees
- Notified partner agencies about the compromise

**Step 7: Root Cause Investigation (Parallel)**
- The attacker's entry point was a service account used by a monitoring tool
- The account had default credentials that were never changed when the tool was deployed
- The account had administrator privileges on the Intermediate CA
- This single compromised account allowed the attacker to generate certificates

The total impact was manageable because:

1. **The compromise was detected relatively quickly** (6 days of unauthorized activity, but discovery within hours of becoming a significant problem)
2. **The Root CA was offline and secure** — even though the Intermediate CA was compromised, the Root CA couldn't be
3. **Revocation was immediate** — the compromised CA was revoked within 1 hour, making any certificates it issued after revocation invalid
4. **Phased reissuance didn't create a bottleneck** — reissuing 12,000 certificates gradually was better than all at once
5. **Employees had [[certificate-pinning|fallback authentication methods]]** — while certificates were being replaced, employees could use multi-factor authentication or alternate credentials

## What Went Right

- **Audit logs were reviewed regularly**: The unauthorized certificates were discovered within 6 days, not months or years later.
- **Root CA was offline and secure**: Despite the Intermediate CA compromise, the Root CA private key was never at risk.
- **Revocation procedures existed and worked**: The compromised Intermediate CA was immediately revoked, preventing further damage.
- **Root CA activation procedures were tested and functional**: Bringing the Root CA online in 2 hours during an emergency showed the procedures were solid.
- **Phased reissuance was faster than sequential issuance**: Prioritizing critical users allowed operations to recover while background processes handled the long tail.
- **[[Chain-of-trust]] was properly segregated**: The offline Root CA being separate from online Intermediate CAs prevented complete compromise.

## What Could Go Wrong

- **If audit logs hadn't been reviewed**: Unauthorized certificates could have remained unknown for months, allowing attackers persistent access.
- **If the Root CA had been online**: A compromise of the Intermediate CA could have cascaded to compromise the Root CA, requiring complete PKI replacement.
- **If revocation procedures weren't in place**: Revoking 12,000 certificates would have been slow and error-prone, prolonging the vulnerability window.
- **If [[certificate-pinning]] wasn't implemented**: Applications expecting specific root certificates could have failed when certificates were revoked and reissued.
- **If all employees had to be reissued simultaneously**: The CA would have been completely overloaded, causing multi-day delays in employee access.
- **If the service account had been properly secured**: This entire incident might not have happened. Default credentials on administrative accounts are inexcusable.

## Key Takeaways

- **Root CA must be air-gapped and offline**: The Root CA should be activated only for issuing or revoking Intermediate CAs. It should never be online and vulnerable to network attacks.
- **Revocation lists must be maintained and distributed**: Organizations must maintain and periodically update Certificate Revocation Lists (CRLs) or use Online Certificate Status Protocol (OCSP) responders to check certificate validity.
- **[[Chain-of-trust]] segregation prevents cascade**: Multiple layers (Root → Intermediate → End-entity) mean compromise at one level doesn't automatically compromise all levels.
- **Service accounts must be secured like any other credentials**: Default passwords, no rotation, no monitoring, excessive privileges—these are all critical failures.
- **Phased reissuance is better than all-at-once**: Prioritize critical users and let the rest follow gradually to avoid bottlenecks and cascading failures.
- **Incident response procedures must be tested**: The team activated the Root CA, issued a new Intermediate CA, and revoked the old one—all in less than 4 hours—because these procedures had been practiced.
- **[[Certificate-pinning]] provides additional security**: If applications pin the Root CA certificate, an attacker can't use a fake Intermediate CA to impersonate legitimate services.

## Related Cases

- [[case-certificates]] — Specific scenarios involving certificate lifecycle and expiration
- [[case-key-management]] — HSM and key storage that protect the Root CA private key
- [[case-encryption]] — Cryptographic principles underlying PKI

