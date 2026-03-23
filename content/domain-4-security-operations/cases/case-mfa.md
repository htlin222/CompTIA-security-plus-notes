---
title: "Case: The Notification Fatigue Breach — MFA Fatigue Attack Success"
description: "An MFA fatigue attack bombards a senior developer with 47 push notifications at 1 AM until he accidentally approves one. The attacker uses the session to access the CI/CD pipeline and inject a backdoor into the next release build."
draft: false
date: 2026-03-20
tags:
  - domain/4
  - type/case
---

## The Scenario

Proxima Security is a 350-person cybersecurity software company building threat detection and incident response tools. On January 18th at 1:14 AM, a senior architect named Jason Reeves was woken up by his phone vibrating repeatedly. Push notifications kept appearing on his mobile device: "Confirm sign-in: Proxima Security (Microsoft Authenticator)" followed immediately by another notification, then another. By the fifth notification, Jason was annoyed and half-asleep. By the twenty-third notification, he just wanted to make them stop. On the forty-seventh notification, at 1:17 AM, Jason tapped "Approve" without thinking, just to silence the notifications.

What Jason didn't realize was that his Microsoft Authenticator [[push-notifications]] were legitimate—they were actually triggered by an attacker who had compromised his password through a previous LinkedIn data breach. The attacker was attempting to authenticate to Jason's account and had written a script to continuously trigger MFA requests, relying on [[mfa-fatigue-attacks]]—the exhaustion attack where a user finally approves one out of frustration.

Once Jason approved one authentication attempt, the attacker gained access to his account. Jason's account was high-value: he was a senior architect with administrative access to the company's GitHub repositories, the internal CI/CD pipeline (Jenkins), the AWS deployment infrastructure, and the Slack workspace. The attacker, likely part of an Eastern European software supply chain attack group, immediately pivoted to access the GitHub repository containing the source code for Proxima's next major product release scheduled to ship in three weeks.

Using Jason's compromised access, the attacker cloned the repository, analyzed the code, and identified the build pipeline configuration. At 1:35 AM, the attacker pushed a subtle change to the `.github/workflows/build.yml` file—a seemingly innocent line that compiled the project with a custom build parameter. But that parameter instructed the compiler to include a small backdoor: upon installation, the security software would register with an attacker-controlled command-and-control (C2) server and provide remote access to customer systems.

The change was camouflaged among legitimate code commits. The commit message was generic: "Update build optimization settings." The attacker used Jason's account to merge the change directly into the master branch, bypassing the code review process (because Jason had admin privileges that allowed force-pushing). The next morning, the automated CI/CD pipeline picked up the change and compiled the malicious version of the software. By 9:00 AM, the build had completed, and the malicious release was ready for deployment.

The attack was discovered by pure chance. A junior developer, Sarah, noticed that Jason's account had committed a change at 1:35 AM—unusual for Jason, who typically didn't work late nights. She mentioned it to the tech lead in their standup meeting, saying "Did you ask Jason to change the build settings last night?" The tech lead said no. Sarah pulled the commit and reviewed the code change, immediately recognizing it as suspicious. By 9:47 AM, the security team had been alerted and the malicious build was removed before it reached customers.

If Jason had delayed responding to Sarah's email by even two hours, the malicious code would have been deployed to production and distributed to thousands of customers' security infrastructure. The attack would have given the attacker access to networks where Proxima's security software was installed—a devastating supply chain attack.

The investigation revealed multiple security failures:
1. **No [[mfa-fatigue-attacks]] detection**: There was no alerting when 47 authentication attempts arrived in rapid succession on a single user's account.
2. **Weak password reuse prevention**: Jason's password had been compromised in the LinkedIn breach, but he hadn't changed it (LinkedIn breach was months old, but the credentials were only recently leaked on dark web forums).
3. **Overly permissive admin access**: Jason had both administrative GitHub access and could force-push to protected branches without requiring approval.
4. **Missing code review enforcement**: High-risk changes to the build pipeline should have required a security-trained reviewer, not just any developer.
5. **No build artifact signature validation**: The build pipeline didn't verify that the compiler and build tools were unmodified before running them.

## What Went Right

- **Unusual commit timing caught attention**: Sarah's observation about Jason's 1:35 AM commit (unusual for his normal schedule) triggered the discovery.
- **Code review despite bypassed process**: Sarah's instinct to review the suspicious commit prevented the backdoor from reaching production.
- **Rapid incident response**: Once alerted, the security team isolated the compromised account, killed the malicious build, and investigated within hours.
- **Audit logging**: The Git audit logs showed that Jason's account made the changes, allowing the team to identify that Jason's account was compromised (Jason wouldn't have made such changes intentionally).

## What Could Go Wrong

- **No [[mfa-fatigue-attacks]] detection**: If the [[identity-management]] system had detected the 47 rapid-fire authentication requests on a single account, it could have automatically blocked the final attempts before Jason approved one.
- **Weak [[password-attacks]] prevention**: If Jason had used a unique password for his work account (not reused from LinkedIn), the initial compromise wouldn't have occurred.
- **Missing [[privileged-access-management]] enforcement**: Jason shouldn't have had the privilege to force-push to protected branches. Admin access should have required stronger [[mfa]] (hardware token, not just push notifications).
- **No code signing or build artifact validation**: If the build pipeline required code changes to be signed by trusted keys and the compiler to be integrity-verified, the attacker's supply chain attack would have failed.
- **Missing detection rules for suspicious CI/CD access**: If the system monitored for unusual patterns (high-privilege account cloning repositories, modifying build configuration at 1 AM), it would have alerted.

## Key Takeaways

- **[[Mfa-fatigue-attacks]] require detection, not just prevention**: Implement alerts when a single user receives >5 MFA requests within 5 minutes. Automatically lock the account or require a new authentication challenge (FIDO2 hardware key, not push notification) after 3 failed attempts.
- **[[Push-notifications]] for MFA should have built-in friction for late-night approvals**: If an authentication request comes in at an unusual time (outside the user's normal working hours), require additional confirmation (PIN code, or require using a hardware security key instead of push notification).
- **[[Passwordless-authentication]] with hardware keys defeats [[mfa-fatigue-attacks]]**: If Jason had been using a FIDO2 hardware security key for [[something-you-have]] rather than push notifications, the attacker couldn't have remotely triggered an MFA fatigue attack.
- **[[Privileged-access-management]] must restrict force-pushing**: High-privilege Git operations (force-push, branch deletion, protection rule changes) should require additional approval, MFA re-authentication, and possibly a separate admin account with hardware key.
- **Build pipeline changes require code review enforcement**: Commits that modify `.github/workflows/` files or other build configuration should be locked to require explicit security team approval.
- **Supply chain attack resilience requires build artifact verification**: Implement code signing for releases and cryptographic verification of compiler toolchains to prevent subtle backdoor injection.

## Related Cases

- [[case-identity-management]] — Account compromise is often the initial attack vector; identity governance and deprovisioning can detect and contain compromised accounts.
- [[case-sso]] — SSO systems can be configured to require stronger [[something-you-have]] factors (hardware keys) for high-privilege operations.
- [[case-automation-and-scripting]] — CI/CD pipeline security requires the same rigor as other critical infrastructure; malicious automation can affect customers at scale.
