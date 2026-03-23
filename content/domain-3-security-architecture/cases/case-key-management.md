---
title: "Case: The Orphaned Backup Keys — HSM Disaster During Failover"
description: "During a disaster recovery drill, the crypto team discovers that HSM backup keys are stored in a safe deposit box at a bank that was acquired and relocated. Nobody has the new access credentials. Key rotation is overdue by 14 months."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/case
---

## The Scenario

GlobalBank is a midsized financial institution with $120B in assets under management. Their encryption infrastructure centers on a Thales SafeNet Luna HSM (Hardware Security Module) that generates and stores the cryptographic keys used to encrypt customer account data, trading positions, and internal communications. The [[hardware-security-module|HSM]] is the crown jewel of their security infrastructure—it lives in a locked cage in the primary data center, protected by guards, cameras, and biometric access controls.

On a Thursday morning in September 2024, the Chief Information Security Officer, Dr. Amara Okafor, scheduled a disaster recovery drill. The scenario: the primary data center loses power, and the organization must failover to a warm standby site 40 miles away. The entire infrastructure—databases, applications, API servers—is replicated to the standby site. But the encryption keys must be manually transferred.

The Head of Cryptography, Samuel Park, opened the [[key-escrow]] procedures document. It outlined the steps:

1. Generate a HSM backup of the master key using a USB token encrypted with an out-of-band passphrase
2. Transport the encrypted backup to the safe deposit box at First National Bank's downtown branch
3. In case of disaster, retrieve the backup from the bank, decrypt it with the out-of-band passphrase, and restore the keys to a HSM at the standby site

Samuel walked to the office of his deputy, Rachel Torres, to start the key recovery test. They would simulate retrieving the backup, validating it, and confirming that keys could be restored without losing any cryptographic state.

Rachel called the bank. The person who answered at First National Bank's downtown branch said: "We don't have a safe deposit box under GlobalBank's name. Are you sure you have the right branch?"

Samuel checked the procedure document. It listed "First National Bank, Downtown Denver Branch, Box 4287." But the bank had been acquired by Wells Fargo three years ago, and the branch had been relocated. The procedure documentation had never been updated.

Rachel tried the new location. The Wells Fargo branch didn't have a record of GlobalBank's box either. After an hour of calls, she reached the historical records department and found that during the acquisition, safe deposit boxes were transferred to a regional facility in Boulder, Colorado, 45 minutes from Denver. GlobalBank's box had been transferred without notifying them.

Samuel got back on the phone with the regional facility. "Yes, we have Box 4287 from the old Denver branch. But you'll need proper authorization and ID to access it."

Samuel had the proper authorization according to the HSM backup procedures—he was on the list of authorized key custodians. But when he arrived at the Boulder facility at 3 PM with a notarized document from GlobalBank's CEO, the facility manager said: "The access credentials for your account were lost in our system migration when we transferred from First National's systems to Wells Fargo's. You'll need to re-enroll in our safe deposit program and re-establish your account credentials. That usually takes 5-7 business days."

Samuel's heart sank. The disaster recovery drill was now a real problem: the HSM backup keys could not be recovered in a timely manner. And there was a bigger issue: **[[key-rotation|key rotation]] was overdue**. According to [[key-management]] policy, all encryption keys must be rotated every 12 months. The current master key had last been rotated 14 months ago.

If the primary data center failed *right now*, GlobalBank would be unable to:
1. Recover the encryption keys needed to access encrypted customer data at the standby site
2. Decrypt any data encrypted with the 14-month-old master key without first rotating it (since the backup was inaccessible)

This meant that a power failure at the primary data center could render terabytes of customer data inaccessible, violating service level agreements and potentially triggering regulatory action.

Samuel escalated to Dr. Okafor, who called an emergency meeting with the Chief Risk Officer, the Head of Compliance, and the Chief Technology Officer. The situation was dire but clear: the [[key-escrow]] system had failed, and the organization needed an immediate remediation plan.

They decided on a multi-phase approach:

**Phase 1: Emergency Key Rotation (Week 1)**
- Generate a new HSM master key (key #2) without using the backup system
- Begin using key #2 for all new encryption
- Maintain key #1 (the 14-month-old key) for decryption of existing data until it could be migrated
- This reduced the window of vulnerability: if the old key became compromised and the backup was inaccessible, only the newest data (encrypted with key #1) would be at risk, not the historical data

**Phase 2: Key Backup Recovery System Overhaul (Week 2-3)**
- Work with Wells Fargo to re-establish account access and retrieve the physical safe deposit box
- Validate that the backup from the safe deposit box was still valid and could be restored to a test HSM
- Create redundant backups at multiple locations (not just one bank)
- Implement automated backup procedures that don't require manual carrier transport

**Phase 3: [[Hardware-security-module|HSM]] Failover Testing (Week 4-5)**
- Deploy a secondary HSM at the standby data center with a copy of the current master key (#2)
- Perform a full failover drill: simulate primary site failure, retrieve keys, activate standby HSM, decrypt data
- Test the end-to-end process without the safe deposit box system (using the new backup procedures)
- Validate that failover could occur within 4 hours

**Phase 4: Key Management Infrastructure Modernization (Ongoing)**
- Moved from manual safe deposit box backup to AWS CloudHSM with geographic replication
- Implemented [[key-splitting-secret-sharing|Shamir's Secret Sharing]] so that key recovery required multiple custodians (no single person could recover keys)
- Set up automated key [[key-rotation|rotation]] every 90 days (reduced from 365 days) to minimize exposure window if a key was compromised
- Integrated [[hardware-security-module|HSM]] with the disaster recovery framework so that failover was automated, not manual

The total cost of the remediation was substantial:

- Professional services from Thales to recover and validate the backup: $45,000
- AWS CloudHSM implementation with redundancy: $180,000 setup, $4,200/month ongoing
- Manual key rotation emergency procedures and training: $30,000
- Downtime and operational impact during failover testing: estimated $200,000

But the alternative—losing access to encrypted customer data during a disaster—would have been far more expensive.

## What Went Right

- **Disaster recovery drill discovered the problem before actual disaster**: If the primary data center had failed without the drill, the key recovery issue would have been discovered in crisis mode with potentially worse outcomes.
- **Proper authorization and documentation existed**: The key custodians had authority to access the backup, and the procedures were documented (even if not updated).
- **Banks keep detailed records**: Wells Fargo was able to locate the safe deposit box through historical records, enabling eventual recovery.
- **Emergency [[key-rotation]] was possible**: The organization could generate a new key without the backup system, allowing continued operations.
- **Regulatory notification wasn't required**: Because this was a test, not an actual data compromise, notification to regulators wasn't necessary.

## What Could Go Wrong

- **If the backup had been lost or destroyed**: The safe deposit box could have been damaged, flooded, or destroyed in a bank accident. That would have meant permanent key loss.
- **If key rotation had been impossible**: If the HSM had been completely unavailable (not just the backup), the organization would have been unable to generate new keys.
- **If key custody wasn't documented**: If the procedures hadn't identified who was authorized to access the backup, recovery would have been blocked by corporate governance.
- **If the [[ephemeral-keys|key material]] had been stored unencrypted**: The safe deposit box encrypted the key material with a passphrase, but if it had been stored in plaintext, access to the box would have compromised the keys.
- **If there were no [[key-escrow]] system at all**: Many organizations don't back up their keys offline, risking permanent loss during a HSM failure.

## Key Takeaways

- **[[Key-escrow]] backup systems must be tested regularly**: Annual [[key-rotation|key rotation]] should include a full backup recovery test. If the backup can't be recovered in a drill, it won't be available in a real disaster.
- **Key backup location and access must be maintained actively**: Banks change, safe deposit boxes are relocated, account credentials are lost. Maintain current contact information and periodically verify that backups are accessible.
- **[[Key-rotation]] deadlines must be non-negotiable**: The 14-month-old key represented a 2-month window of compliance violation. Implement automated enforcement—systems should refuse to use keys older than the rotation period.
- **[[Key-splitting-secret-sharing|Secret sharing]] reduces single-custodian risk**: Shamir's Secret Sharing ensures that no single person can recover keys without at least N other custodians. This prevents both insider threats and single-point-of-failure issues.
- **Failover systems must include key failover**: The standby data center must have its own HSM or secure access to a replicated HSM. Key failover can't be manual if [[disaster-recovery|RTO]] is hours, not days.
- **[[Hardware-security-module|HSM]] management tools should be automated**: Modern HSM solutions like CloudHSM handle geographic replication, automatic backups, and [[key-rotation|rotation]] without manual carrier transport and safe deposit boxes.

## Related Cases

- [[case-encryption]] — How encryption keys are used in data protection
- [[case-certificates]] — Similar key lifecycle and rotation issues for PKI certificates
- [[case-pki]] — Public key infrastructure that depends on reliable key management
- [[case-disaster-recovery]] — How key management fits into the broader disaster recovery architecture

