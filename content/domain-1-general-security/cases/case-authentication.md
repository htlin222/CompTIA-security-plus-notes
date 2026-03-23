---
title: "Case: Going Passwordless — The Post-Breach Pivot"
description: "After a credential stuffing attack compromises developer accounts, a Series B fintech company pivots to passwordless authentication. The CTO mandates FIDO2 rollout starting with engineering, forcing the security team to learn passkey management on the fly."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

PayCore is a Series B fintech company based in San Francisco that provides payment processing infrastructure for mid-market SaaS companies. The company has 180 employees, with 35 engineers spread across three teams (backend, frontend, DevOps) and distributed across San Francisco, Austin, and London. In November 2025, the company was hit by a credential stuffing attack that exposed a critical vulnerability in their authentication architecture.

The attack unfolded at 2:15 AM PST on November 17. An automated credential stuffing attack targeting PayCore's engineer login portal (https://git.paycore.dev) used a leaked credential database containing 2.4 billion username/password pairs from a previous breach at an unrelated financial services company. The attackers fired 1.8 million authentication requests at the endpoint over a 45-minute window, using distributed sources to avoid obvious geographic clustering. The login portal had no rate limiting, no CAPTCHA protection, and no alerting configured for brute force patterns.

By 3:02 AM, the attack had successfully compromised three engineering accounts:

- Sarah Kim (senior backend engineer): password was "PayCore2024!\_sarah" (reused from her LinkedIn breach in 2020)
- James Rodriguez (DevOps engineer): password was "dragon2015" (a generic pattern from his Yahoo account compromise)
- Priya Desai (frontend engineer): password was "Password123" (identical to her account at a SaaS tool she used for side projects)

The attackers immediately pivoted after gaining access. They used the compromised accounts to:

1. Clone the main PayCore repository to extract source code
2. Access the AWS management console and enumerate running services
3. Query the production database using stored credentials in GitHub repository secrets
4. Attempt lateral movement to the Kubernetes cluster

The compromise went undetected for 14 hours. At 4:30 PM PST on November 17, Sarah Kim noticed unusual AWS CloudTrail events in her email notification—specifically, a large EC2 instance was spun up in a region she'd never used. She immediately flagged it to the security team. By 5:15 PM, the incident command center was active.

The forensic analysis was sobering. The attackers had accessed the repository, downloaded 18 months of git history, and reviewed the Kubernetes deployment scripts (which contained database credentials for staging environments). They had successfully logged into the staging database and began enumerating customer data. Fortunately, the staging database had only anonymized test data, not real customer financial records. However, the mere fact that attackers had database access while possessing source code credentials was a critical risk.

The CISO, Marcus Johnson, immediately convened the security architecture team. He gave a clear directive: "We are eliminating password-based authentication for engineers by Q1 2026. I want FIDO2 hardware keys deployed to every engineer within 60 days. If we're going to be a fintech company handling other people's money, we cannot depend on passwords that live in password managers and git commits."

The challenge was immediate: FIDO2 (Fast Identity Online 2) is a [[biometric-authentication]] and hardware-based standard that makes phishing and credential theft impossible—when you authenticate with a FIDO2 key, the key verifies the domain you're connecting to before signing the challenge, preventing man-in-the-middle attacks and domain spoofing. But PayCore had never implemented hardware key management at scale. They had no inventory process, no lifecycle management, and no backup authentication method.

Marcus assembled a team:

- Elena Torres (security architect) to design the FIDO2 implementation
- DevOps team to integrate with GitHub, AWS, and internal tooling
- HR to coordinate hardware key procurement and distribution

Week 1: Elena designed the phased rollout:

- Phase 1 (Week 2-4): Pilot with 8 volunteers who would test Yubico YubiKey 5 hardware keys
- Phase 2 (Week 5-8): All 35 engineers would receive YubiKeys; password authentication would be available as fallback
- Phase 3 (Week 9+): Gradual enforcement—passwords would be deprecated in favor of FIDO2-only access

The pilot revealed immediate complications. GitHub's FIDO2 support was solid, but AWS required multiple authentication methods (AWS was recommending virtual MFA in addition to FIDO2, which seemed redundant but was their policy). Some internal tools running on Kubernetes didn't support FIDO2 at all; they still required SSH keys. The SSH key management became its own problem: should engineers have both FIDO2 keys and SSH keys? (Answer: yes, because you can't use FIDO2 to unlock an SSH key without additional tooling like ssh-agent and a bridge protocol).

Week 4: The team pivoted to a hybrid approach:

- GitHub: FIDO2 keys become primary; passwords disabled
- AWS: FIDO2 keys + virtual MFA (AWS's requirement)
- SSH (EC2 instances, Kubernetes): FIDO2-backed SSH keys using OpenSSH 8.2+ support for FIDO2 security keys
- Internal tools and dashboards: FIDO2 keys for initial login, with short-lived session tokens for tools that don't support FIDO2

Week 8: All 35 engineers had received and configured their YubiKey 5 hardware keys. Marcus mandated that every engineer also register a backup YubiKey. The Yubico API was integrated into the identity provisioning system so that lost or stolen keys could be revoked instantly.

But the real test came in week 10 when Elena had to handle the first emergency: an engineer traveling to London for a customer meeting had left both their primary and backup YubiKey at home on their desk. They were locked out of GitHub, AWS, and their development environment. The team established an emergency authentication protocol: the engineer could prove their identity through a video call with the security team, and a temporary [[certificate-based-authentication|certificate-based credential]] would be issued for 24 hours. This taught the team a critical lesson: passwordless doesn't mean "completely inflexible." You need break-glass procedures.

By January 2026 (Week 12 of the program), password-based authentication for engineers was completely eliminated. The statistics were compelling:

- Zero credential stuffing attacks on the engineer portal (previously they were occurring every 3-4 weeks)
- Zero successful phishing for engineer accounts (previously they were successful ~1x per quarter)
- Two legitimate emergency credential issues (both handled via the break-glass process in under 2 hours)

The CISO made a public commitment: in 2026, customer-facing authentication would also transition to passwordless options. PayCore began offering customers the option to authenticate using passkeys (a software-based equivalent of FIDO2 using the device's biometric or PIN) alongside their password.

## What Went Right

- **Rapid incident detection**: Sarah Kim's AWS notifications caught the compromise within 14 hours, preventing data exfiltration of production customer data.
- **Phased rollout prevented disruption**: A pilot program with 8 volunteers before full deployment allowed the team to catch integration issues (AWS MFA requirements, SSH key management complications) before affecting 35 engineers.
- **Executive commitment to hardware security**: Marcus's mandate to eliminate passwords wasn't just a security team initiative—it was a company policy backed by the CISO and CTO.
- **Flexible break-glass procedures**: Acknowledging that passwordless authentication could create emergency situations allowed the team to maintain operability while maintaining security.
- **Metrics demonstrated value**: By tracking phishing attempts, credential stuffing attacks, and successful account compromises before and after, the team had clear data showing the value of the investment.

## What Could Go Wrong

- **No rate limiting on authentication endpoints**: The credential stuffing attack succeeded in part because the login endpoint accepted 1.8 million requests in 45 minutes without any throttling.
- **Password reuse across services**: Three engineers had reused passwords from other breaches, making them vulnerable to credential stuffing. There was no breach database monitoring to flag compromised credentials.
- **Credentials stored in version control**: The AWS credentials in GitHub secrets were a secondary vulnerability—engineers shouldn't be storing long-lived credentials in git commits at all.
- **Long detection window**: The 14-hour gap between compromise and detection meant the attackers had time to enumerate systems and download source code.
- **No [[mfa]] on the engineer portal**: Even if password authentication was the primary method, MFA could have prevented the credential stuffing attack from succeeding.
- **No alerting on unusual AWS activity**: The CloudTrail event that Sarah noticed came from her own notification settings, not from a security team alert. The team had no automated detection for "administrator creating a new EC2 instance from a region they've never used."

## Key Takeaways

- **Biometric-authentication and [[certificate-based-authentication]] eliminate credential stuffing and phishing**: FIDO2 keys and passkeys make compromised passwords worthless because they can't be reused.
- **Passwordless authentication requires break-glass procedures**: Emergency authentication methods are essential for business continuity. Establish clear procedures for lost/stolen keys (identity verification + short-lived emergency credentials).
- **Hardware key management is a new operational domain**: Procurement, inventory tracking, revocation, replacement, backup procedures—these are all new operational requirements that require planning and automation.
- **Phased rollout is essential for integration testing**: Different systems (GitHub, AWS, SSH, internal tools) have different FIDO2 support. Pilot with volunteers before full deployment.
- **Credentials in version control are a critical vulnerability**: Implement secrets detection tools, require credential rotation when found in commits, and use short-lived credentials from identity providers instead of long-lived credentials in environment variables.
- **Rate limiting and alerting are table-stakes defense against credential stuffing**: Even with passwords (for systems that still use them), rate limiting, CAPTCHA, and behavioral alerts are essential.

## Related Cases

- [[case-mfa]] — Understanding multi-factor authentication and when passwordless alternatives make sense
- [[case-password-attacks]] — Deep dive into credential stuffing, brute force, and defense mechanisms
- [[case-sso]] — Centralizing authentication across many systems and tools
- [[case-zero-trust]] — Making authentication decisions based on device posture and behavior, not just credential validity
