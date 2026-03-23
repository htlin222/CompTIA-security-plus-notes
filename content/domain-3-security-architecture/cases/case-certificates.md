---
title: "Case: The Midnight Expiration — TLS Certificate Crisis at Scale"
description: "A wildcard TLS certificate renewal fails silently, discovered Friday at 4 PM when staging deployments start failing. By Saturday midnight, the entire e-commerce platform is at risk of going dark during peak holiday sales."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

Eventide Logistics operates a multinational e-commerce platform serving 8.5 million customers across North America and Europe. The infrastructure relies on a wildcard TLS certificate for `*.eventide.net` that covers API endpoints, customer-facing web properties, mobile app back-ends, and internal dashboards. On a sunny Friday afternoon in November—the week before Black Friday—engineering manager Derek Liu was reviewing the staging deployment logs when he noticed something alarming: Chrome was throwing certificate validation errors on staging-api.eventide.net.

The certificate, valid for exactly one year, expired at 11:59 PM UTC on Saturday night. Derek checked the automated renewal system: Let's Encrypt ACME renewal had been configured to run every 60 days via a cron job on the legacy certificate server. But that server had been moved to a read-only state five months ago as part of a cloud migration. Nobody had updated the ACME renewal webhook to point at the new cloud infrastructure. The renewal had silently failed—no alerts, no notifications—because the monitoring was still watching the old server.

Derek's hands went cold. It was 4:47 PM Friday. The Certificate Authority wouldn't prioritize an emergency issuance until Monday morning. The entire API fleet was dependent on this single wildcard certificate. Every client—mobile apps, third-party integrations, internal microservices—would hit certificate validation failures within 24 hours. It was 34 hours until complete system failure.

He escalated to the on-call security team and CTO Maria Chen. Maria's first question was practical and terrifying: "When was this certificate last manually tested for renewal?" The answer was never. The [[certificate-lifecycle]] process was documented in a wiki page updated six months ago, but nobody had actually walked through the renewal procedure. The HSM containing the private key was in the primary data center in Virginia. The operations team that normally handled [[certificate-lifecycle]] handoffs was distributed across five time zones—and it was Friday evening.

Maria called an emergency war room. Within 30 minutes, they had assembled security, infrastructure, and engineering leads. They discovered several cascading failures: First, the [[certificate-lifecycle]] renewal process was manual and required five sign-offs from different teams. Second, the [[x509-certificate-fields]] were configured with only Virginia in the Subject Alternative Names list, which meant they couldn't do a quick workaround by issuing a temporary certificate from a different geographic CA. Third, the private key backup stored offline in the HSM had a 12-month key escrow agreement that technically prohibited emergency access without CISO sign-off and a three-hour manual audit trail.

By 9:30 PM Friday, the team had decided to invoke the [[key-escrow]] emergency procedure. The CISO, awakened at home, verbally approved it. Security engineers drove to the primary data center and manually extracted the private key backup from the offline HSM. Meanwhile, Derek worked with the CA account manager via an out-of-band phone call to request a same-day reissuance. At 11:47 PM—exactly 12 minutes before expiration—the new certificate was provisioned and deployed across the fleet via automated push.

The [[certificate-formats]] transition was clean because Derek had standardized on PEM across all services months earlier. But the incident exposed a catastrophic assumption: that automated systems would always work, and that nobody needed to test the manual backup procedures.

## What Went Right

- **Distributed certificate provisioning infrastructure**: Once the new certificate was issued, automated deployment pushed it to all 340 API servers in 4 minutes, preventing customer-facing impact.
- **Emergency key escrow procedures existed**: Despite the bureaucratic requirements, the organization had documented procedures for emergency key recovery that didn't require waiting until Monday.
- **Out-of-band communication channels**: Direct phone contact with the CA account manager allowed expedited reissuance outside normal business hours.
- **Early detection**: Derek noticed the staging error before it affected production, giving the team 34 hours to respond rather than discovering it at 11:45 PM Saturday.

## What Could Go Wrong

- **Monitoring on decommissioned infrastructure**: The ACME renewal cron job and its alerting were never migrated when the legacy certificate server was retired. This is a classic [[certificate-lifecycle]] failure pattern.
- **Single certificate point of failure**: One wildcard covering the entire domain meant a single expiration took down all properties. [[Certificate-pinning]] or geographic distribution could have provided fallback options.
- **No rehearsed renewal procedure**: The team had never walked through an actual renewal, so they didn't discover the configuration drift until crisis time. [[csr-certificate-signing-request]] procedures should be tested quarterly.
- **[[Key-escrow]] friction created delays**: The three-hour audit trail and multiple approvals, while necessary for governance, almost caused the deadline to be missed. Emergency procedures need to be faster or have pre-authorized exception pathways.
- **Interdependent renewal systems**: The cron job failure had no fallback. There should have been a secondary renewal trigger (perhaps a monthly manual audit, or a monitoring system that pre-alerts 90 days before expiration).

## Key Takeaways

- **[[Certificate-lifecycle]] automation must be monitored at every stage**: Not just "cert is valid," but "renewal was attempted," "renewal succeeded," and "new cert was deployed." Each step needs independent alerting.
- **[[Certificate-formats]] and [[x509-certificate-fields]] decisions affect recovery**: A diverse certificate strategy reduces single-point-of-failure risk. Consider geographic distribution and alternative formats.
- **Rehearse [[key-escrow]] and emergency procedures quarterly**: A 12-minute margin is too close. Emergency procedures should be tested under time pressure so teams know what to expect.
- **Retire infrastructure completely**: When decommissioning old systems, audit every dependency—not just application code, but also cron jobs, scheduled tasks, monitoring rules, and certificate renewal pipelines.
- **[[Revocation]] and renewal are different problems**: Plan for both normal [[certificate-lifecycle]] renewal and emergency reissuance. Different tools and procedures may be needed.

## Related Cases

- [[case-key-management]] — Understanding the broader context of key lifecycle and escrow policies that affect certificate renewal
- [[case-pki]] — Deep dive into Public Key Infrastructure and certificate authority hierarchies that constrain renewal options
- [[case-encryption]] — How certificate selection affects encryption strategy and system resilience

