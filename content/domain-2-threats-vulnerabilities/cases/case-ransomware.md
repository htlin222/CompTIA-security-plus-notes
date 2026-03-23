---
title: "Case: The 3:17 AM Encryption — Double-Extortion Ransomware at Precision Manufacturing"
description: "LockBit ransomware encrypts 60% of file shares at a 2,000-employee aerospace components manufacturer. The attacker demands $1.8M and threatens to publish proprietary engineering designs within 72 hours."
draft: false
date: 2026-03-21
tags:
  - domain/2
  - type/case
---

## The Scenario

Precision Manufacturing Inc. (PMI), founded in 1987, manufactures complex aerospace components including landing gear assemblies, fuselage panels, and avionics mounts for commercial aircraft. The company employs 2,000 people across three facilities (California, Ohio, Texas) and generates $680M in annual revenue. PMI's intellectual property—precision manufacturing tooling specifications, CAD designs, proprietary manufacturing processes—is worth hundreds of millions. On March 10, 2026, at 3:17 AM Pacific Time, the on-call incident commander received an alert cascade that would trigger the largest security incident in the company's history.

The attack began on March 8, 2026, at 11:43 PM when an attacker exploited a vulnerability in PMI's Fortinet FortiGate VPN appliance (CVE-2024-47575, a zero-day remote code execution flaw patched in January 2026 but not yet applied to PMI's appliance). The attacker gained unauthenticated remote access to the VPN appliance and from there pivoted to the internal network. The attacker did not immediately encrypt files. Instead, for 27 hours, the attacker conducted reconnaissance, moved [[lateral-movement|laterally]] through the network to the file storage servers, located the most valuable intellectual property (CAD files in `/shares/engineering/designs`, manufacturing specifications in `/shares/proprietary/processes`), and began exfiltrating data. The attacker used SSH to copy 143 GB of data to a cloud storage provider in Eastern Europe.

At 3:14 AM on March 10, the attacker activated the ransomware payload—LockBit 3.0, the most sophisticated ransomware strain in circulation. The malware began encrypting files across all accessible file shares using ChaCha20 encryption. The encryption process was aggressive: files were encrypted in parallel across 8 threads, and the malware prioritized large files and databases (maximum impact). Within 4 hours, 60% of accessible files had been encrypted. File names were appended with `.lockbit` extension. The Windows pagefile, system restore points, and previous file versions were deleted to prevent recovery.

At 3:17 AM, desktop backgrounds across the company changed to a ransom note:

```
===== DATA ENCRYPTED =====
Your files have been encrypted by LockBit.
We have also copied your complete engineering designs and manufacturing specifications.
Payment: 45 Bitcoin ($1.8M at current exchange rate)
Deadline: 72 hours from now
Decryption: https://lockbit[.]dark/decryption
If you do not pay within 72 hours, we will publish your engineering IP on our data leak site.
WARNING: Do not contact law enforcement or your insurance company. Doing so will void your guarantee.
===== END MESSAGE =====
```

The ransom note was accurate: the attackers possessed 143 GB of intellectual property including: (1) CAD designs for the next-generation landing gear assembly (due for aircraft delivery in 18 months), (2) manufacturing process documentation for composite panel fabrication, (3) supplier relationships and pricing agreements worth $14M annually, (4) internal financial projections for the next 3 years, and (5) customer specifications for classified aerospace contracts.

By 4:00 AM, the Chief Information Security Officer, Patricia Chen, had activated the incident response playbook. By 5:30 AM, the incident response team had isolated the affected file servers, disconnected the VPN appliance, and began damage assessment. By 6:00 AM, PMI's CEO and Board of Directors had been notified. By 6:30 AM, external incident response specialists (Mandiant) and legal counsel had been engaged. By 8:00 AM, the FBI Cyber Division and CISA had been notified.

The immediate question was: pay or refuse? The company faced three options with very different risk profiles:

**Option 1 (Pay ransom)**: Transfer 45 Bitcoin to a wallet address provided by the attackers. Risks: (1) no guarantee of decryption or data deletion, (2) 45% of paid ransom goes to money laundering operations funding organized crime, (3) company would be on record as paying ransoms, making it a target for repeat extortion, (4) payment doesn't prevent data publication—the attacker would likely leak the data anyway to extort other competitors with the knowledge of PMI's designs.

**Option 2 (Refuse and recover from backup)**: Restore all encrypted systems from backup tapes. This would require 48–72 hours of restoration but would avoid funding criminals and wouldn't guarantee data publication anyway. However, a full business interruption would halt manufacturing and cost approximately $2.8M per day in lost production.

**Option 3 (Negotiate with attacker)**: Attempt to negotiate a lower ransom or request proof that the data would be deleted. Risks: (1) negotiation takes time, (2) attackers have no incentive to honor deletion promises, (3) negotiation signal indicates willingness to pay, likely resulting in higher demands.

Patricia made the decision at 9:00 AM on March 10: refuse to pay. Restore from backup. Accept the business interruption. The decision was based on: (1) offline backups proved that decryption wasn't necessary, (2) paying ransom doesn't prevent data publication, and (3) refusing to pay discourages future attacks on PMI.

The company initiated the Business Continuity Plan. All manufacturing facilities were notified of the shutdown at 9:30 AM. Major customers were called directly (not email) at 10:00 AM with a revised delivery schedule. The restoration process began immediately, with backup tapes being restored in priority order: (1) critical financial and customer systems (8 hours), (2) engineering design repositories (12 hours), (3) manufacturing systems (16 hours), (4) everything else (24 hours).

The complete restoration took 48 hours. By 6:00 PM on March 11, critical systems were back online. By 11:00 PM on March 11, manufacturing resumed partial operations. By March 12 at 4:00 PM, full manufacturing capacity had been restored. The total business interruption: 37 hours.

The predicted threat materialized at 8:47 PM on March 11: the attacker published the 143 GB of PMI's intellectual property on the dark web, including design specifications, manufacturing processes, and customer information. The data was released to competitors, demonstrating that the attacker had indeed stolen the information and that payment would not have prevented publication. PMI's initial concern was validated: the ransom demand was extortion rather than a legitimate offer to delete data.

## What Went Right

- **Rapid incident detection and response activation**: The 3:17 AM alert triggered an automated escalation that woke the incident commander and on-call security team within minutes. Fast detection prevented the ransomware from spreading to additional systems and backups.

- **Offline backup strategy prevented catastrophic data loss**: PMI's backup tapes were stored offline in a secure vault, disconnected from the network. Ransomware cannot encrypt offline backups. This single decision proved to be the difference between recovery and potential business extinction.

- **Leadership decision to refuse ransom payment**: Patricia Chen made the right call to refuse ransom despite pressure from the attackers' 72-hour deadline. The decision was based on: (1) backups existed and enabled recovery, (2) data publication cannot be prevented by payment, and (3) refusing to pay discourages future attacks.

- **Complete isolation of affected systems prevented further spread**: The IT team immediately disconnected the VPN appliance and file servers from the network, preventing the ransomware from spreading to other systems (databases, client workstations, backup infrastructure).

- **Business continuity plan enabled measured recovery**: Rather than attempting emergency restoration of everything simultaneously (which would have caused additional failures and extended the outage), the team prioritized systems in order of business criticality, minimizing downstream disruption.

## What Could Go Wrong

- **No offline backup strategy**: Many organizations store backups on network-attached storage or in the cloud, assuming encryption protection. [[encryption-based-ransomware]] can compromise the backup infrastructure and render backups unrecoverable. [[immutable-backups|WORM (write-once-read-many) backups]] stored offline are the only reliable defense.

- **Unpatched VPN appliance created initial access**: CVE-2024-47575 was published on January 15, 2026, and a patch was available immediately. PMI's patch management process took 54 days to deploy the patch. A [[vulnerability-types|27-day patch deployment SLA]] would have prevented this entire incident.

- **No egress filtering allowed data exfiltration**: The attacker copied 143 GB of data to a cloud provider in Eastern Europe without triggering any alerts. Network monitoring for unusual outbound traffic (large data transfers to unfamiliar IP addresses outside business hours) would have detected the data theft within hours rather than 27 hours.

- **No [[edr-xdr|EDR]] monitoring to detect ransomware execution**: PMI relied on traditional antivirus, which didn't detect the ransomware payload. An EDR tool monitoring process execution, file modification patterns, and encrypted file behavior could have detected the ransomware within seconds of activation, enabling containment before 60% of files were encrypted.

- **No network segmentation between production and IT systems**: The attacker moved laterally from the VPN appliance to the file servers without encountering any network barriers. [[network-segmentation|Micro-segmentation]] and [[zero-trust-architecture|zero-trust access control]] would have required additional authentication/authorization for lateral movement, significantly slowing the attack.

- **No immutable snapshots of file systems**: [[file-integrity-monitoring|File snapshots]] (available in NetApp SnapShot, Dell IDPA, Veeam) that are immutable (cannot be modified or deleted, even by root/admin) would have enabled near-instant recovery of pre-attack state. Instead, the attacker deleted all snapshots and forced a slow restoration from tape backups.

## Key Takeaways

- **[[offline-backup|Offline backups]] are non-negotiable for ransomware resilience**: Ransomware cannot encrypt backups that are disconnected from the network. 3–2–1 backup strategy (3 copies, 2 different media types, 1 offsite) is standard for enterprises; at least 1 copy must be offline and immutable.

- **[[immutable-backups|WORM (write-once-read-many) backups]] prevent ransomware from modifying backups**: Even if an attacker compromises backup storage, they cannot encrypt or delete immutable backups. Immutable snapshots and offline vaults should be standard controls.

- **[[double-extortion|Double-extortion ransomware]] (encryption + data theft) cannot be defeated by payment**: Attackers steal data and then threaten publication. Paying ransom doesn't prevent the threat publication; it only enriches criminals. Data protection (preventing exfiltration) is more important than decryption capability.

- **[[lateral-movement|Lateral movement]] should be detected and blocked**: The attacker pivoted from the VPN appliance to file servers undetected. [[network-segmentation]], [[zero-trust-architecture|zero-trust access control]], and [[edr-xdr|EDR]] behavioral monitoring would have detected and blocked lateral movement attempts.

- **Patching timeline is critical**: The 54-day delay in patching CVE-2024-47575 directly enabled this attack. A 7–14-day patch deployment SLA for critical vulnerabilities is standard in organizations that take security seriously.

## Related Cases

- **[[case-incident-response]]** — Ransomware response procedures including triage, containment, eradication, recovery, and lessons learned; understanding the playbook for attack response.

- **[[case-business-continuity]]** — Recovery time objectives (RTO), recovery point objectives (RPO), backup strategy, and disaster recovery testing; understanding how to survive and recover from disruptive incidents.

- **[[case-endpoint-security]]** — [[edr-xdr]] monitoring for ransomware detection; understanding process execution trees, file modification patterns, and behavioral indicators of compromise.

- **[[case-vulnerability-types]]** — Understanding [[misconfigurations|unpatched VPN appliances]], [[default-credentials]], and [[zero-day-vulnerabilities|zero-day exploits]]; the attack surface of network appliances.
