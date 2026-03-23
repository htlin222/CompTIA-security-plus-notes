---
title: "Case: Building Zero Trust After Four Acquisitions — The Messy Reality"
description: "A private equity-backed tech firm acquires three companies in 18 months and ends up with four overlapping VPNs, no consistent identity layer, and no network segmentation. The board mandates zero trust architecture completion within 12 months."
draft: false
date: 2026-03-21
tags:
  - domain/1
  - type/case
---

## The Scenario

InnovateLabs is a Series D enterprise software company backed by a prominent private equity firm. In the 18 months from June 2024 to December 2025, the firm acquired three smaller technology companies: TechFlow (a data integration startup), SecureVault (a threat detection software company), and CloudSmart (a cloud infrastructure optimization company). The acquisitions brought talent and technology but also a chaotic IT infrastructure.

By January 2026, InnovateLabs had:

- 1,200 employees across four offices (San Francisco headquarters, Austin, Denver, Boston)
- Four separate VPN systems (each acquired company had kept its own VPN)
- Three different identity providers (Active Directory, Okta, Auth0)
- Zero network segmentation between business units
- No device management system (employees used whatever devices they wanted)
- No consistent security policies across the merged company

The Chief Information Security Officer, Dr. Lisa Chen, faced a fundamental problem: if an employee from one acquisition logged into the VPN, they had implicit trust and could access systems from any other acquisition. An attacker who compromised a single employee's credentials could laterally move through the entire company.

The incident that forced action came in February 2026. An employee from the Austin office (originally part of TechFlow) had their laptop stolen from a coffee shop. The laptop had cached credentials for the corporate VPN. An attacker tried connecting with those credentials from an IP address in Eastern Europe. The attempt failed—by luck, not by design. MFA on the VPN happened to catch it because the attacker didn't have the employee's phone.

But Lisa realized: what if the attacker had waited a week and the employee had already re-authenticated with VPN from a different location? Then the VPN would have trusted them. What if the employee had a phone that roamed to an international location? Then the attacker could have used the TOTP app if it was synchronized. What if there was no MFA on some of the other VPN systems? (There wasn't.)

Lisa convened the board. "We need zero trust architecture. Today's situation is indefensible. If an attacker compromises a single credential, they have access to the entire company. We need to change this."

The board gave her a mandate: "Implement zero trust architecture across the entire company by December 31, 2026. Budget: $4M. This is non-negotiable."

**Months 1-2: Assessment and Planning (January-February 2026)**

Lisa's team conducted an inventory of all systems and access patterns:

- Identity systems: three separate systems (AD, Okta, Auth0) managing 1,200 users
- Access patterns: development teams used SSH keys; administrative staff used VPN; contractors used temporary credentials
- Critical systems: 47 databases, 200+ microservices, 15 development platforms, customer-facing SaaS infrastructure
- Network topology: four offices with no segmentation between them; everything was accessible once you were "in the network"

The team defined zero trust principles for InnovateLabs:

1. **Never trust, always verify**: Every access request requires explicit authentication and authorization, regardless of source
2. **Assume breach**: Design defenses assuming an attacker is already inside
3. **Verify every access**: Even if you authenticated yesterday, prove you're allowed to access this resource today
4. **Least privilege by default**: Grant access to the specific resources needed, not broad categories
5. **Device compliance is non-negotiable**: Only managed, compliant devices can access critical systems
6. **Encrypt everything**: All traffic, including internal network traffic, must be encrypted
7. **Observe and validate**: Continuous monitoring of user and device behavior

**Months 3-4: Identity Unification (March-April 2026)**

The most critical first step was consolidating identity management. Lisa's team selected Okta as the central identity provider and began migrating all users from Active Directory and Auth0:

- 600 users from the original InnovateLabs moved to Okta
- 320 users from TechFlow migrated, with their SSH keys rotated
- 180 users from SecureVault migrated from Auth0
- 100 users from CloudSmart migrated, with their contractor accounts normalized
- 47 contractor/vendor accounts were audited and removed (if no longer needed) or re-authorized (if still active)

Each user was required to register a hardware security key during migration. No exceptions—even if it slowed down the migration.

**Months 4-5: Device Management (April-May 2026)**

Lisa deployed Mobile Device Management (MDM) across the company:

- All laptops were enrolled in Mobile Device Management; devices that didn't meet compliance requirements (outdated OS, no disk encryption, compromised) were isolated from the network
- Smartphones were optional for corporate network access, but if used, they had to be managed
- Contractors had to use company-managed laptops; personal devices could no longer access corporate systems

Employees who arrived with laptops that didn't meet compliance (no disk encryption, outdated OS, missing security patches) couldn't access the network until they were remediated. This caused some friction, but Lisa's message was clear: "A compromised device is a breach waiting to happen."

**Months 5-7: Network Access Control (June-July 2026)**

Lisa implemented Network Access Control (NAC). Before a device could access the corporate network, it had to:

1. Prove it was registered in the MDM system
2. Prove it was compliant (current OS, patches applied, encryption enabled)
3. Authenticate the user with MFA
4. Pass a behavioral verification check (is this access from an unusual location?)

If any check failed, the device was placed in a quarantine network where it could only reach the IT helpdesk portal (to troubleshoot compliance issues) and a device remediation service (to update OS, apply patches).

**Months 7-9: Micro-Segmentation (August-September 2026)**

The network was divided into micro-segments:

- Engineering segment: developer workstations and development systems
- Data segment: databases and data processing infrastructure
- SaaS segment: customer-facing application servers
- Admin segment: administrative systems with elevated privileges
- Finance segment: financial and HR systems

Between each segment, security policies controlled traffic:

- Engineering could access the Data segment to query databases but couldn't access Finance
- Finance could access admin segment tools but couldn't access customer data
- SaaS could access Data but was isolated from Admin and Finance

Access was granted based on identity and role:

- A software engineer could access the Engineering and Data segments during business hours
- A contractor could access only specific development repositories, not the entire Engineering segment
- An HR specialist could access Finance and Admin but not Engineering or SaaS

**Months 9-11: Continuous Monitoring (October-November 2026)**

Lisa deployed behavioral analytics and continuous verification:

- Okta logged every access request with context: user, device, location, time, requested resource
- SIEM rules flagged anomalies: an engineer accessing HR systems, finance staff accessing development databases, access from a location 1,000 miles away from yesterday's location
- Continuous re-verification: for sensitive operations (database exports, code deployments, credential access), additional authentication was required

If Sarah worked from the San Francisco office most of the time but suddenly connected to the network from a hotel in Chicago at 3 AM, the system wouldn't automatically trust her. It would require additional verification:

- "You're connecting from an unusual location. Verify with your hardware key."
- Only then would access be granted

**Month 12: Testing and Validation (December 2026)**

Before the zero trust system went fully live, Lisa conducted extensive testing:

**Test 1: Compromised Device**
A security team member brought a laptop infected with malware to simulate a compromise. The MDM system immediately flagged the device as non-compliant (elevated privileges detected). NAC quarantined the device. The device couldn't access any corporate systems, even though the user had valid credentials.

**Test 2: Stolen Credentials**
The team obtained valid credentials of a developer and attempted to access the system from an unusual location. The system detected the anomalous location and locked the account. The legitimate developer received a notification: "Your account was accessed from Russia. If this wasn't you, your account has been compromised." The developer confirmed the unauthorized access and the account was frozen.

**Test 3: Lateral Movement**
A red team member compromised a marketing employee's account (social engineering attack simulated). They tried to move laterally to access the finance database. Network micro-segmentation blocked them. The marketing employee's device was on the "Marketing" segment; the database was on the "Finance" segment; the firewall rules explicitly forbade marketing-to-finance communication.

**Test 4: Privilege Escalation**
A red team member gained access to a development system and tried to escalate privileges. The PAM (Privileged Access Management) system required re-authentication with MFA to elevate privileges. They didn't have the necessary credentials. Privilege escalation failed.

All tests passed. The zero trust architecture was working as designed.

## What Went Right

- **Hardware security keys were mandatory, not optional**: This prevented credential compromise and phishing attacks
- **Device management was enforced at the network level**: Even if a laptop was compromised, it couldn't connect to the network
- **Behavioral analytics caught anomalies**: Unusual access patterns (different location, unusual time, unusual resource) triggered additional verification
- **Network micro-segmentation prevented lateral movement**: Even with compromised credentials, an attacker couldn't move freely between business units
- **Continuous re-verification for sensitive operations**: Accessing sensitive systems wasn't a one-time authentication; it required proving authorization at the time of access
- **PAM prevented privilege escalation**: Even with a valid account, escalating privileges required additional authentication

## What Could Go Wrong

- **Identity systems were fragmented initially**: Having three separate identity providers (AD, Okta, Auth0) meant no unified view of who was accessing what
- **No device management existed initially**: Employees could use any device, compromised devices had no detection or containment
- **Network was completely flat**: No segmentation meant no boundaries between business units and no way to contain a breach
- **SSH keys were the primary authentication for development**: SSH keys don't have MFA; they could be compromised and reused without detection
- **Contractors had the same access as employees**: No way to distinguish between a contractor's legitimate access and an attacker impersonating a contractor
- **No behavioral analytics existed**: Accessing the database from Moscow had no special significance to the system

## Key Takeaways

- **Zero trust is not one product; it's an architecture**: Okta provides identity; MDM provides device compliance; NAC provides network access control; SIEM provides behavioral analytics; PAM provides privilege management. All these must work together.
- **Identity unification is the foundation**: As long as you have multiple identity systems, you can't enforce consistent authentication policies.
- **Device management enables the verify-everything model**: You can't verify that an access request is legitimate if you don't know anything about the device making the request.
- **Micro-segmentation makes lateral movement nearly impossible**: Even if an attacker compromises one user's credentials, network policies prevent them from accessing resources outside that user's business unit.
- **Behavioral analytics separate authorized anomalies from attacks**: An engineer accessing the database at 3 AM from a different country might be legitimate (time zone, travel), but this should trigger additional verification, not automatic denial.
- **Continuous re-verification is essential for sensitive operations**: One-time authentication (login to VPN, then full access) creates unlimited trust windows. Re-verification for each sensitive operation limits that window.
- **Zero trust implementation takes time and budget**: This was a 12-month, $4M effort for 1,200 users. Zero trust is an investment, but the security gains are substantial.

## Related Cases

- [[case-network-segmentation]] — Deep dive into design and implementation of network micro-segmentation
- [[case-mfa]] — Hardware security keys and multi-factor authentication as foundational controls
- [[case-endpoint-security]] — Device management and endpoint detection and response (EDR)
- [[case-network-security-architecture]] — Designing secure network architecture from scratch
